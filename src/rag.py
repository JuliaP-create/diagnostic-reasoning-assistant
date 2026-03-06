from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple, Union

import numpy as np

from . import artifacts
from .inference import predict_topk_from_session_token
from .policy import choose_next_question_info_gain, update_posterior_with_answer
from .types import DiagnosisSession, FeatureSpec, parse_token

try:
    # Optional mini-manual layer (your file has keys matching release_conditions.json)
    from .condition_enrichments import CONDITION_ENRICHMENTS  # type: ignore
except Exception:
    CONDITION_ENRICHMENTS: Dict[str, str] = {}


# -----------------------------
# Paths + loading (repo-friendly)
# -----------------------------
def repo_root() -> Path:
    """Assumes this file is located at <repo>/src/rag.py."""
    return Path(__file__).resolve().parents[1]


def default_data_dir() -> Path:
    return repo_root() / "data"


def default_models_dir() -> Path:
    return repo_root() / "models"


@dataclass
class AssistantResources:
    evidences_map: Dict[str, dict]
    conditions_map: Dict[str, dict]
    condition_enrichments: Dict[str, str]

    model: Any
    preprocessors: Dict[str, Any]
    feature_spec_token: FeatureSpec

    policy_artifacts: Dict[str, Any]


def load_resources(
    *,
    data_dir: Optional[Path] = None,
    models_dir: Optional[Path] = None,
    evidences_filename: str = "release_evidences.json",
    conditions_filename: str = "release_conditions.json",
    preprocessors_name: str = "preprocessors.joblib",
    preprocessors_fallback: str = "preprocessors_token.joblib",
    policy_name: str = "policy_artifacts.joblib",
) -> AssistantResources:
    """Load everything needed for Streamlit / API without retraining."""
    data_dir = default_data_dir() if data_dir is None else Path(data_dir)
    models_dir = default_models_dir() if models_dir is None else Path(models_dir)

    evidences_map = artifacts.load_json(data_dir / evidences_filename)
    conditions_map = artifacts.load_json(data_dir / conditions_filename)

    # Model: prefer calibrated if present (see artifacts.resolve_best_token_model)
    model = artifacts.resolve_best_token_model(models_dir)

    # Preprocessors: prefer preprocessors.joblib (full bundle), fallback to preprocessors_token.joblib
    pp_path = models_dir / preprocessors_name
    if not pp_path.exists():
        pp_path = models_dir / preprocessors_fallback
    preprocessors = artifacts.load_preprocessors(pp_path)

    # Feature spec (token model uses CAT_COLS + NUM_COLS; no age_group in decision map)
    feature_spec_token = FeatureSpec(
        evidence_mode="token",
        cat_cols=list(preprocessors.get("CAT_COLS", ["SEX"])),
        num_cols=list(preprocessors.get("NUM_COLS", ["AGE", "num_bases_effective", "num_items_effective", "extra_multi_values"])),
        age_group_func=None,
    )

    policy_artifacts = artifacts.load_policy_artifacts(models_dir / policy_name)

    return AssistantResources(
        evidences_map=evidences_map,
        conditions_map=conditions_map,
        condition_enrichments=dict(CONDITION_ENRICHMENTS) if CONDITION_ENRICHMENTS else {},
        model=model,
        preprocessors=preprocessors,
        feature_spec_token=feature_spec_token,
        policy_artifacts=policy_artifacts,
    )


# -----------------------------
# Evidence translation utilities
# -----------------------------
def _sort_evidence_codes(codes: Iterable[str]) -> List[str]:
    def _key(x: str) -> Tuple[int, str]:
        m = re.match(r"^E_(\d+)$", x)
        return (int(m.group(1)) if m else 10**9, x)
    return sorted(set(codes), key=_key)


def evidence_question(base: str, evidences_map: Dict[str, dict], *, lang: str = "en") -> str:
    meta = evidences_map.get(base, {})
    if lang == "fr":
        q = meta.get("question_fr") or meta.get("question_en")
    else:
        q = meta.get("question_en") or meta.get("question_fr")
    return (q or base).strip()


def evidence_data_type(base: str, evidences_map: Dict[str, dict]) -> str:
    return str(evidences_map.get(base, {}).get("data_type") or "B")


def evidence_default_value(base: str, evidences_map: Dict[str, dict]) -> Optional[str]:
    dv = evidences_map.get(base, {}).get("default_value", None)
    return None if dv is None else str(dv)


def evidence_is_antecedent(base: str, evidences_map: Dict[str, dict]) -> bool:
    return bool(evidences_map.get(base, {}).get("is_antecedent", False))


def value_to_readable(base: str, val: str, evidences_map: Dict[str, dict], *, lang: str = "en") -> str:
    meta = evidences_map.get(base, {})
    vm = meta.get("value_meaning") or {}
    if isinstance(vm, dict) and val in vm:
        entry = vm[val]
        if isinstance(entry, dict):
            return str(entry.get(lang) or entry.get("en") or entry.get("fr") or val).strip()
    return str(val).strip()


def is_default_value(base: str, val: str, evidences_map: Dict[str, dict]) -> bool:
    dv = evidence_default_value(base, evidences_map)
    return dv is not None and str(val) == str(dv)


def format_evidence_item(token: str, evidences_map: Dict[str, dict]) -> str:
    """Readable one-line representation for a positive evidence token/item."""
    base, val = parse_token(token)
    q = evidence_question(base, evidences_map, lang="en")
    if val is None:
        return q
    readable_val = value_to_readable(base, str(val), evidences_map, lang="en")
    return f"{q} (value: {readable_val})"


def evidence_value_examples(base: str, evidences_map: Dict[str, dict], *, max_n: int = 12) -> str:
    meta = evidences_map.get(base, {})
    poss = meta.get("possible-values") or []
    vm = meta.get("value_meaning") or {}

    if not poss:
        return ""

    ex = []
    for v in poss[:max_n]:
        sv = str(v)
        if isinstance(vm, dict) and sv in vm:
            ex.append(f"{sv}={value_to_readable(base, sv, evidences_map, lang='en')}")
        else:
            ex.append(sv)
    return "; ".join(ex)


# -----------------------------
# Evidence clustering utilities
# -----------------------------
# Cluster names are aligned with what you already use in the notebook.
CLUSTER_ORDER: List[str] = [
    "Pain",
    "Respiratory",
    "GI",
    "Neuro",
    "Skin",
    "GU / Repro",
    "Constitutional",
    "Risk factors / history",
    "Background: Medical history (chronic conditions)",
    "Background: Medications, substances & exposures",
    "Other",
]


def _text_has_any(text: str, needles: Sequence[str]) -> bool:
    t = text.lower()
    return any(n.lower() in t for n in needles)


def classify_evidence_base(base: str, evidences_map: Dict[str, dict]) -> str:
    """Heuristic classifier for evidence bases using question text + antecedent flag."""
    q = evidence_question(base, evidences_map, lang="en")
    is_ant = evidence_is_antecedent(base, evidences_map)

    # Antecedents: split into your 3 “background/history” buckets
    if is_ant:
        meds_kw = [
            "take", "taking", "medication", "drug", "nsaid", "anti-inflammatory",
            "corticosteroid", "antipsychotic", "hormone", "dialysis",
            "coffee", "tea", "energy drink", "intravenous", "stimulant", "smoke",
            "alcohol", "contact", "daycare", "live with", "travel", "exposed", "allergy",
            "infected", "ebola", "viral infection",
        ]
        chronic_kw = [
            "do you have", "have you ever had", "have you been diagnosed",
            "chronic", "copd", "cystic fibrosis", "rheumatoid", "crohn",
            "ulcerative colitis", "parkinson", "cancer", "metastatic",
            "heart valve", "diabetes", "asthma",
        ]

        if _text_has_any(q, meds_kw):
            return "Background: Medications, substances & exposures"
        if _text_has_any(q, chronic_kw):
            return "Background: Medical history (chronic conditions)"
        return "Risk factors / history"

    # Symptoms: keyword-based buckets
    if _text_has_any(q, ["pain", "ache", "hurt", "tender"]):
        return "Pain"
    if _text_has_any(q, ["cough", "breath", "wheeze", "throat", "nasal", "sinus", "sneeze", "sputum", "phlegm", "hoarse"]):
        return "Respiratory"
    if _text_has_any(q, ["nausea", "vomit", "diarrhea", "stool", "abdominal", "abdomen", "stomach", "appetite", "heartburn", "reflux", "jaundice"]):
        return "GI"
    if _text_has_any(q, ["headache", "confused", "dizzy", "weakness", "numb", "tingling", "seiz", "speech", "vision", "tremor"]):
        return "Neuro"
    if _text_has_any(q, ["rash", "skin", "lesion", "itch", "hives", "blister"]):
        return "Skin"
    if _text_has_any(q, ["urine", "urination", "vaginal", "menstru", "pregnan", "testicle", "penis", "vulv", "discharge"]):
        return "GU / Repro"
    if _text_has_any(q, ["fever", "temperature", "chills", "fatigue", "tired", "sweat", "weight loss", "malaise"]):
        return "Constitutional"

    return "Other"


def build_evidence_clusters(evidences_map: Dict[str, dict]) -> Dict[str, List[str]]:
    """Build clusters for all evidence bases."""
    clusters: Dict[str, List[str]] = {k: [] for k in CLUSTER_ORDER}
    for base in evidences_map.keys():
        c = classify_evidence_base(base, evidences_map)
        clusters.setdefault(c, [])
        clusters[c].append(base)

    # Stable order for UI
    for k in list(clusters.keys()):
        clusters[k] = _sort_evidence_codes(clusters[k])

    # Ensure all named clusters exist
    for k in CLUSTER_ORDER:
        clusters.setdefault(k, [])

    return clusters


def split_other_cluster(
    clusters: Dict[str, List[str]],
    evidences_map: Dict[str, dict],
) -> Dict[str, List[str]]:
    """Drop-in helper to refine a pre-defined clusters dict.

    This matches your notebook pattern:
        EVIDENCE_CLUSTERS = split_other_cluster(EVIDENCE_CLUSTERS, evidences_map)
    """
    new_clusters: Dict[str, List[str]] = {k: list(v) for k, v in clusters.items()}
    other = list(new_clusters.get("Other", []))
    new_clusters["Other"] = []

    for base in other:
        c = classify_evidence_base(base, evidences_map)
        new_clusters.setdefault(c, [])
        new_clusters[c].append(base)

    # Re-sort everything deterministically
    for k in list(new_clusters.keys()):
        new_clusters[k] = _sort_evidence_codes(new_clusters[k])

    # Keep cluster order stable (important for UI)
    ordered: Dict[str, List[str]] = {k: new_clusters.get(k, []) for k in CLUSTER_ORDER}
    for k, v in new_clusters.items():
        if k not in ordered:
            ordered[k] = v
    return ordered


# -----------------------------
# Model posterior + policy loop
# -----------------------------
def top_from_proba(proba: np.ndarray, label_encoder, *, k: int = 5) -> List[Tuple[str, float]]:
    idx = np.argsort(proba)[::-1][:k]
    return [(label_encoder.inverse_transform([int(i)])[0], float(proba[int(i)])) for i in idx]


def compute_posterior_with_negatives(
    session: DiagnosisSession,
    proba_model: np.ndarray,
    *,
    p_e_given_d: np.ndarray,
    evidence_index: Dict[str, int],
    beta: float = 0.7,
) -> np.ndarray:
    """Apply policy-table negative updates on top of ML posterior (negatives not in ML features)."""
    post = np.array(proba_model, dtype=float)
    for base in sorted(session.neg_bases):
        post = update_posterior_with_answer(
            post,
            base,
            "no",
            p_e_given_d=p_e_given_d,
            evidence_index=evidence_index,
            beta=beta,
        )
    return post


def assistant_step(
    session: DiagnosisSession,
    res: AssistantResources,
    *,
    k: int = 5,
    beta: float = 0.7,
) -> Dict[str, Any]:
    """One assistant step: ML posterior -> negative-aware posterior -> IG next question."""
    pp = res.preprocessors

    top_ml, proba_ml = predict_topk_from_session_token(
        session,
        res.model,
        mlb_token=pp["mlb_token"],
        ohe=pp["ohe"],
        scaler=pp["scaler"],
        label_encoder=pp["label_encoder"],
        feature_spec=res.feature_spec_token,
        k=k,
    )

    p_e_given_d = res.policy_artifacts["p_e_given_d"]
    # --- Robust evidence_index resolution (backward compatible) ---
    policy_artifacts = res.policy_artifacts

    # Required: p_e_given_d
    p_e_given_d = policy_artifacts.get("p_e_given_d", None)
    if p_e_given_d is None:
        raise KeyError(
            "policy_artifacts is missing 'p_e_given_d'. "
            "Expected models/policy_artifacts.joblib exported from Notebook 02."
        )

    # Preferred: evidence_bases stored alongside p_e_given_d
    evidence_bases = policy_artifacts.get("evidence_bases", None)

    # Fallback: derive evidence_bases from preprocessors' mlb_base (stable in this project)
    if evidence_bases is None:
        mlb_base = res.preprocessors.get("mlb_base") or res.preprocessors.get("mlb")
        if mlb_base is None or not hasattr(mlb_base, "classes_"):
            raise KeyError(
                "Could not derive evidence_bases. "
                "Neither policy_artifacts['evidence_bases'] nor preprocessors['mlb_base'].classes_ is available."
            )
        evidence_bases = list(mlb_base.classes_)

    # Sanity check: must match p_e_given_d columns
    n_evid = int(p_e_given_d.shape[1])
    if len(evidence_bases) != n_evid:
        raise ValueError(
            f"Mismatch: len(evidence_bases)={len(evidence_bases)} but p_e_given_d has {n_evid} evidence columns. "
            "Re-export policy_artifacts.joblib so these are aligned."
        )

    # Preferred: precomputed dict
    evidence_index = policy_artifacts.get("evidence_index", None)

    # Fallback: build it once and cache into the dict
    if evidence_index is None:
        evidence_index = {b: i for i, b in enumerate(evidence_bases)}
        policy_artifacts["evidence_index"] = evidence_index
    # --- end robust evidence_index resolution ---
    evidence_bases = res.policy_artifacts["evidence_bases"]

    posterior = compute_posterior_with_negatives(
        session,
        proba_ml,
        p_e_given_d=p_e_given_d,
        evidence_index=evidence_index,
        beta=beta,
    )

    top = top_from_proba(posterior, pp["label_encoder"], k=k)

    candidates = choose_next_question_info_gain(
        session=session,
        disease_proba=posterior,
        p_e_given_d=p_e_given_d,
        evidence_bases=evidence_bases,
        evidences_map=res.evidences_map,
        top_n=5,
    )

    next_base, ig, p_yes, q_text = candidates[0] if candidates else ("", 0.0, 0.0, "")

    return {
        "top": top,
        "posterior": posterior,
        "top_ml": top_ml,
        "proba_ml": proba_ml,
        "next_base": next_base,
        "next_question_en": q_text or evidence_question(next_base, res.evidences_map, lang="en"),
        "ig": float(ig),
        "p_yes": float(p_yes),
    }


# -----------------------------
# Explanation builders (strings)
# -----------------------------
def explain_topk_diagnoses(
    session: DiagnosisSession,
    top: List[Tuple[str, float]],
    *,
    evidences_map: Dict[str, dict],
    conditions_map: Dict[str, dict],
    condition_enrichments: Optional[Dict[str, str]] = None,
    max_findings: int = 20,
) -> str:
    """Educational explanation string (no medical advice)."""
    condition_enrichments = condition_enrichments or {}

    lines: List[str] = []
    lines.append("Educational explanation (not medical advice).")

    # Positives
    lines.append("What we know so far (positive findings):")
    pos_items = list(session.evidence_tokens_for_ml())
    if not pos_items:
        lines.append("  - (No positive findings recorded yet.)")
    else:
        for it in pos_items[:max_findings]:
            lines.append(f"  - {format_evidence_item(it, evidences_map)}")
        if len(pos_items) > max_findings:
            lines.append(f"  - ... (+{len(pos_items) - max_findings} more)")

    lines.append("")
    lines.append("Why we currently rank these diagnoses near the top (dataset-grounded):")

    pos_bases = session.pos_bases

    for i, (disease, p) in enumerate(top, start=1):
        lines.append(f"{i}) {disease} (estimated likelihood ≈ {p:.3f})")

        # Mini-manual (optional layer)
        mm = condition_enrichments.get(disease)
        if mm:
            # Keep it as provided (already educational + disclaimer in your file)
            lines.append(f"   Mini-manual: {mm}")
        else:
            lines.append("   Mini-manual: (not available in this build)")

        cond = conditions_map.get(disease, {})
        sym = set((cond.get("symptoms") or {}).keys())
        ant = set((cond.get("antecedents") or {}).keys())

        over_sym = _sort_evidence_codes(pos_bases.intersection(sym))
        over_ant = _sort_evidence_codes(pos_bases.intersection(ant))

        if over_sym or over_ant:
            if over_sym:
                lines.append(f"   Dataset grounding: overlaps with listed symptom concepts: {', '.join(over_sym)}.")
            if over_ant:
                lines.append(f"   Dataset grounding: overlaps with listed history/risk concepts: {', '.join(over_ant)}.")
        else:
            lines.append("   Dataset grounding: no direct overlap found with the recorded positives (additional questions may be needed).")

    return "\n".join(lines)


def explain_next_question(
    next_base: str,
    *,
    top: List[Tuple[str, float]],
    p_yes: float,
    ig: float,
    evidences_map: Dict[str, dict],
    label_encoder=None,
    p_e_given_d: Optional[np.ndarray] = None,
    evidence_index: Optional[Dict[str, int]] = None,
) -> str:
    """Educational next-question explanation string (no medical advice)."""
    lines: List[str] = []
    lines.append("Why we ask this next question (educational explanation; not medical advice):")
    q = evidence_question(next_base, evidences_map, lang="en")
    lines.append(f"- Next question: {q}")
    lines.append("- We selected this question because it is expected to be especially helpful for telling the leading options apart.")
    lines.append(f"- In this dataset, the chance of a 'yes' answer (given the current ranking) is ≈ {p_yes:.2f}.")
    lines.append("")
    lines.append("How this question tends to differ across the leading diagnoses (dataset frequencies):")

    if (p_e_given_d is not None) and (evidence_index is not None) and (label_encoder is not None):
        j = evidence_index.get(next_base, None)
        if j is None:
            for disease, _ in top[:3]:
                lines.append(f"- {disease}: (frequency not available)")
        else:
            # Need class index for each disease
            classes = list(label_encoder.classes_)
            disease_to_i = {d: i for i, d in enumerate(classes)}
            for disease, _ in top[:3]:
                di = disease_to_i.get(disease, None)
                if di is None:
                    lines.append(f"- {disease}: (frequency not available)")
                else:
                    lines.append(f"- {disease}: ~{float(p_e_given_d[int(di), int(j)]):.2f} of cases have this as 'yes'")
    else:
        for disease, _ in top[:3]:
            lines.append(f"- {disease}: (frequency not available in this context)")

    lines.append("")
    lines.append("Evidence definition (retrieved from local corpus):")
    meta = evidences_map.get(next_base, {})
    dtype = meta.get("data_type")
    ant = meta.get("is_antecedent")
    dv = meta.get("default_value")
    ex = evidence_value_examples(next_base, evidences_map, max_n=12)

    lines.append(
        f"Evidence base: {next_base} | Question (EN): {q} | Type: {dtype} | Antecedent: {ant} | Default value: {dv}"
        + (f" | Example values: {ex}" if ex else "")
    )
    lines.append("")
    lines.append(f"(Internal usefulness score ≈ {ig:.4f}; higher generally means more expected usefulness.)")
    return "\n".join(lines)