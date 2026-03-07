from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import streamlit as st

from src.types import DiagnosisSession
from src.rag import (
    AssistantResources,
    assistant_step,
    build_evidence_clusters,
    evidence_data_type,
    evidence_default_value,
    evidence_question,
    format_evidence_item,
    is_default_value,
    load_resources,
    split_other_cluster,
    value_to_readable,
    explain_topk_diagnoses,
    explain_next_question,
)

# -----------------------------
# Streamlit setup
# -----------------------------
st.set_page_config(
    page_title="DDXPlus Diagnostic Reasoning Assistant",
    page_icon="🩺",
    layout="wide",
)

# --- Minimal custom styling ---
st.markdown("""
<style>
/* Soft background */
[data-testid="stAppViewContainer"] {
    background-color: #f8f9fb;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #eef1f7;
}

/* Sidebar text wrap fix */
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] .stMarkdown li {
    font-size: 0.78rem;
    word-break: break-word;
    white-space: normal;
}

/* Top diagnoses — subtle card per row */
div[data-testid="stVerticalBlock"] .stMarkdown h3 {
    color: #2c3e6b;
}

/* Primary button colour */
div.stButton > button[kind="primary"] {
    background-color: #2c3e6b;
    color: white;
    border-radius: 8px;
}

/* Expander header */
details summary {
    font-weight: 600;
    color: #2c3e6b;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("## 🩺 DDXPlus Diagnostic Reasoning Assistant")
st.caption("⚠️ Educational tool only — not medical advice, not for patient care.")
st.markdown("---")



@st.cache_resource
def get_resources() -> AssistantResources:
    return load_resources()


res = get_resources()

# Build clusters for initial input (only used before the first turn)
clusters = build_evidence_clusters(res.evidences_map)
# Optional: if you have an existing EVIDENCE_CLUSTERS dict you prefer, you can refine it like this:
clusters = split_other_cluster(clusters, res.evidences_map)

# -----------------------------
# Session state init
# -----------------------------
if "started" not in st.session_state:
    st.session_state.started = False
if "turn" not in st.session_state:
    st.session_state.turn = 0
if "session" not in st.session_state:
    st.session_state.session = None
if "trace" not in st.session_state:
    st.session_state.trace = []  # list of dict logs
if "stop_reason" not in st.session_state:
    st.session_state.stop_reason = ""



def reset_all() -> None:
    st.session_state.started = False
    st.session_state.turn = 0
    st.session_state.session = None
    st.session_state.trace = []
    st.session_state.stop_reason = ""
    st.rerun()
    


def should_stop_interview(
    step_out: dict,
    *,
    turn_idx: int,
    max_turns: int,
    min_turns: int = 3,
    p_stop: float = 0.95,
    ig_stop: float = 0.005,
) -> tuple[bool, str]:
    """
    Decide whether to stop asking more questions.

    Conventions in this app:
    - `st.session_state.turn` = number of *answered* questions so far
    - `turn_idx` = number of the *next* question we are about to ask (starts at 1)

    We keep this function robust to missing keys in `step_out` so the app does not
    accidentally stop early if `assistant_step()` does not return `candidates`.
    Returns: (stop_now, reason_text)
    """
    # 1) Hard cap (allow asking exactly `max_turns` questions)
    if turn_idx > max_turns:
        return True, f"Reached the maximum number of questions ({max_turns})."

    # Defensive parsing (robust to missing keys)
    topk = step_out.get("topk") or []
    next_base = step_out.get("next_base") or ""
    ig = step_out.get("ig", None)
    candidates = step_out.get("candidates", None)

    # If the policy cannot propose any next question, stop immediately
    if not next_base:
        return True, "No further questions are available."

    # If `assistant_step()` doesn't provide a candidates list, synthesize a minimal one
    # so the stop logic can still use an "informativeness" score.
    if candidates is None:
        score = float(ig) if ig is not None else 0.0
        candidates = [(next_base, score)]

    # 2) Stop criteria that should NOT trigger too early
    # Require that we have already asked at least `min_turns` questions.
    if turn_idx > min_turns:
        # High-confidence stop
        if topk and float(topk[0][1]) >= float(p_stop):
            return True, f"High confidence reached (top diagnosis probability ≈ {float(topk[0][1]):.2f})."

        # Low-usefulness stop (information gain / usefulness score)
        if candidates:
            best_score = float(candidates[0][1])
            if best_score < float(ig_stop):
                return True, f"Further questions are unlikely to help (usefulness score ≈ {best_score:.4f})."

    return False, ""

with st.sidebar:
    st.markdown("### ⚙️ Controls")
    if st.button("🔄 Reset session", type="secondary"):
        reset_all()

    st.markdown("---")
    st.markdown("**Required files:**")
    st.markdown("""
- `data/release_evidences.json`
- `data/release_conditions.json`
- `models/preprocessors_token.joblib`
- `models/logreg_token_calibrated.joblib`
- `models/policy_artifacts.joblib`
""")
    st.markdown("---")
    st.caption("DDXPlus · NeurIPS 2022 · Educational use only")



# -----------------------------
# Step 0: Demographics
# -----------------------------
colA, colB = st.columns(2)
with colA:
    age = st.number_input("Age", min_value=0, max_value=120, value=35, step=1, disabled=st.session_state.started)
with colB:
    sex = st.selectbox("Sex", options=["M", "F"], index=0, disabled=st.session_state.started)

st.markdown("---")


# -----------------------------
# Step 1: Initial evidence input (translation + clustering)
# (Used only BEFORE starting; after start, we use the policy loop)
# -----------------------------
if not st.session_state.started:
    st.subheader("Initial findings (optional)")
    st.caption("This is only for the first input. After starting, the assistant will ask the next best question iteratively.")

    cluster_name = st.selectbox("Pick a category", options=list(clusters.keys()), index=0)
    bases = clusters.get(cluster_name, [])

    # Display label as: "E_53 — Do you have pain somewhere...?"
    def base_label(b: str) -> str:
        return f"{b} — {evidence_question(b, res.evidences_map)}"

    selected_bases = st.multiselect(
        "Select findings you already know are present",
        options=bases,
        format_func=base_label,
        default=[],
    )

    # For value-coded bases, collect the value
    selected_tokens: List[str] = []
    for base in selected_bases:
        dtype = evidence_data_type(base, res.evidences_map)
        dv = evidence_default_value(base, res.evidences_map)

        if dtype == "B":
            # Binary positives: token is just the base
            selected_tokens.append(base)
            continue

        st.markdown(f"**{base}** — {evidence_question(base, res.evidences_map)}")
        st.caption(f"Default / non-informative value in dataset: {dv}")

        meta = res.evidences_map.get(base, {})
        poss = meta.get("possible-values") or []
        vm = meta.get("value_meaning") or {}

        # If numeric scale (common: 0..10), use slider
        if poss and all(isinstance(x, (int, float)) for x in poss):
            v = st.slider(f"Value for {base}", min_value=int(min(poss)), max_value=int(max(poss)), value=int(dv) if (dv and dv.isdigit()) else 0)
            if dv is not None and str(v) == str(dv):
                st.info("This equals the dataset default; it will NOT be added as a positive.")
            else:
                selected_tokens.append(f"{base}={v}")
        else:
            # C or M with V_ codes -> selectbox with readable meanings
            opts = [str(x) for x in poss] if poss else list(vm.keys())
            if not opts:
                # Fallback: free text
                vtxt = st.text_input(f"Value for {base} (free text)", value="")
                if vtxt.strip():
                    if dv is not None and vtxt.strip() == str(dv):
                        st.info("This equals the dataset default; it will NOT be added as a positive.")
                    else:
                        selected_tokens.append(f"{base}={vtxt.strip()}")
            else:
                def opt_label(v: str) -> str:
                    return f"{v} — {value_to_readable(base, v, res.evidences_map)}"

                vsel = st.selectbox(f"Value for {base}", options=opts, format_func=opt_label, index=0)
                if dv is not None and str(vsel) == str(dv):
                    st.info("This equals the dataset default; it will NOT be added as a positive.")
                else:
                    selected_tokens.append(f"{base}={vsel}")

    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("Start session", type="primary"):
            sess = DiagnosisSession(age=float(age), sex=str(sex))
            # Apply tokens (skip defaults by construction above)
            for tok in selected_tokens:
                base, val = tok.split("=", 1) if "=" in tok else (tok, None)
                if val is not None and is_default_value(base, val, res.evidences_map):
                    continue
                sess.add_positive(tok)

            st.session_state.session = sess
            st.session_state.started = True
            st.session_state.turn = 0
            st.session_state.trace = []
            st.rerun()

    with col2:
        if selected_tokens:
            st.markdown("**Initial positives that will be used:**")
            for t in selected_tokens:
                st.write(f"- {format_evidence_item(t, res.evidences_map)}")

    st.stop()


# -----------------------------
# Interactive loop (policy asks next question)
# -----------------------------
sess: DiagnosisSession = st.session_state.session

st.subheader("Interactive Q&A (policy-driven)")
st.caption("We iteratively rank diagnoses and ask the next most informative question (dataset-grounded).")

# Compute current step outputs
step_out = assistant_step(sess, res, k=5, beta=0.7)
top: List[Tuple[str, float]] = step_out["top"]
next_base: str = step_out["next_base"]
next_q: str = step_out["next_question_en"]
ig: float = step_out["ig"]
p_yes: float = step_out["p_yes"]

# Display current known positives
with st.expander("Current positive findings (what we know so far)", expanded=False):
    pos = sess.evidence_tokens_for_ml()
    if not pos:
        st.write("(None yet.)")
    else:
        for it in pos:
            st.write(f"- {format_evidence_item(it, res.evidences_map)}")

# Display Top-k
st.markdown("### Top diagnoses (current)")
for d, p in top:
    st.write(f"- **{d}** — {p:.3f}")

# Build explanations
exp_topk = explain_topk_diagnoses(
    sess,
    top,
    evidences_map=res.evidences_map,
    conditions_map=res.conditions_map,
    condition_enrichments=res.condition_enrichments,
)

exp_next = explain_next_question(
    next_base,
    top=top,
    p_yes=p_yes,
    ig=ig,
    evidences_map=res.evidences_map,
    label_encoder=res.preprocessors["label_encoder"],
    p_e_given_d=res.policy_artifacts["p_e_given_d"],
    evidence_index=res.policy_artifacts["evidence_index"],
)

# Collapsible explanation panels (Streamlit native)
turn_idx = st.session_state.turn + 1

# --- Stop check ---
stop_now, stop_reason = should_stop_interview(
    {
        "topk": top,
        "next_base": next_base,
        "ig": ig,
        # Optional: use candidates if assistant_step exposes them.
        "candidates": step_out.get("candidates", None),
    },
    turn_idx=turn_idx,
    max_turns=20,
    min_turns=3,   # avoid stopping immediately after the first question
    p_stop=0.95,   # require very high confidence before auto-stopping
    ig_stop=0.005, # stop only when questions become near-uninformative
)
if stop_now:
    st.success(f"✅ Session complete: {stop_reason}")
    st.session_state.stop_reason = stop_reason
    st.stop()   # ← stops rendering the form below


with st.expander(f"Turn {turn_idx} — Top‑k explanation", expanded=False):
    st.text(exp_topk)

with st.expander(f"Turn {turn_idx} — Next‑question explanation", expanded=False):
    st.text(exp_next)

st.markdown("---")
st.markdown(f"### Next question: **{next_base}**")
st.write(next_q)

dtype = evidence_data_type(next_base, res.evidences_map)
dv = evidence_default_value(next_base, res.evidences_map)

with st.form(key="answer_form"):
    if dtype == "B":
        ans = st.radio("Answer", options=["yes", "no", "unknown"], horizontal=True)
        value = None
    else:
        st.caption(f"Dataset default value: {dv} (choosing it is treated as a 'no' for base-level policy).")

        meta = res.evidences_map.get(next_base, {})
        poss = meta.get("possible-values") or []
        vm = meta.get("value_meaning") or {}

        ans = "value"
        value = None

        # Numeric scale -> slider
        if poss and all(isinstance(x, (int, float)) for x in poss):
            value = st.slider("Value", min_value=int(min(poss)), max_value=int(max(poss)), value=int(dv) if (dv and dv.isdigit()) else 0)
        else:
            opts = [str(x) for x in poss] if poss else list(vm.keys())
            if opts:
                def opt_label(v: str) -> str:
                    return f"{v} — {value_to_readable(next_base, v, res.evidences_map)}"

                value = st.selectbox("Value", options=opts, format_func=opt_label, index=0)
            else:
                value = st.text_input("Value (free text)", value="")

        unknown_flag = st.checkbox("Mark as unknown / prefer not to answer", value=False)
        if unknown_flag:
            ans = "unknown"

    submitted = st.form_submit_button("Submit answer")

if submitted:
    # Apply answer to session
    if ans == "unknown":
        sess.add_unknown(next_base)
        status = "unknown"
        tokens_added: List[str] = []
    elif dtype == "B":
        if ans == "yes":
            sess.add_positive(next_base)
            status = "positive"
            tokens_added = [next_base]
        else:
            sess.add_negative(next_base)
            status = "negative"
            tokens_added = []
    else:
        # Value-coded: default -> negative, else add token
        vstr = str(value).strip()
        if dv is not None and vstr == str(dv):
            sess.add_negative(next_base)
            status = "negative(default)"
            tokens_added = []
        else:
            tok = f"{next_base}={vstr}"
            sess.add_positive(tok)
            status = "positive"
            tokens_added = [tok]

    # Log turn
    st.session_state.trace.append(
        {
            "turn": turn_idx,
            "next_base": next_base,
            "answer_status": status,
            "tokens_added": tokens_added,
            "top": top,
            "ig": ig,
            "p_yes": p_yes,
            "exp_topk": exp_topk,
            "exp_next": exp_next,
        }
    )
    st.session_state.turn += 1
    st.session_state.session = sess
    st.rerun()
