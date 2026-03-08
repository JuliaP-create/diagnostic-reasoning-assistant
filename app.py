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

# --- Option B: Calm Medical Interface ---
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom, #F8FAFB 0%, #F0F4F8 100%);
}
[data-testid="stAppViewContainer"]::before {
    content: '';
    display: block;
    height: 3px;
    background: linear-gradient(90deg, #06A39B 0%, #648FFF 100%);
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 9999;
}
[data-testid="stSidebar"] {
    background-color: #EEF2F7;
    border-right: 1px solid #DDE7F0;
}
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] .stMarkdown li {
    font-size: 0.8rem;
    line-height: 1.6;
    color: #5F6F7E;
    word-break: break-word;
    white-space: normal;
}
h2 { color: #2C3E50 !important; font-weight: 700 !important; }
h3 {
    color: #2C3E50 !important;
    font-weight: 600 !important;
    margin-top: 1.5rem !important;
    margin-bottom: 0.75rem !important;
    border-bottom: 2px solid #648FFF;
    padding-bottom: 0.5rem;
}
div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #648FFF 0%, #4A7DE8 100%);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    padding: 0.6rem 2rem;
    box-shadow: 0 3px 8px rgba(100,143,255,0.25);
    transition: all 0.2s ease;
}
div.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 12px rgba(100,143,255,0.35);
}
div.stButton > button[kind="secondary"] {
    background-color: white;
    border: 2px solid #648FFF;
    color: #648FFF;
    border-radius: 8px;
    font-weight: 600;
    padding: 0.6rem 2rem;
}
div.stButton > button[kind="secondary"]:hover { background-color: #F0F4FF; }
details {
    background: white;
    border: 1px solid #DDE7F0;
    border-radius: 8px;
    padding: 0.75rem;
    margin-bottom: 0.75rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}
details summary { font-weight: 600; color: #648FFF !important; cursor: pointer; }
hr { border: none; border-top: 1px solid #DDE7F0; margin: 2rem 0; }
.stCaption { color: #6B7C8E !important; font-size: 0.85rem !important; }
div.stFormSubmitButton > button {
    background: linear-gradient(135deg, #06A39B 0%, #648FFF 100%);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    padding: 0.6rem 2rem;
    box-shadow: 0 3px 8px rgba(6,163,155,0.25);
    transition: all 0.2s ease;
}
div.stFormSubmitButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 12px rgba(6,163,155,0.35);
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

clusters = build_evidence_clusters(res.evidences_map)
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
    st.session_state.trace = []
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
    - st.session_state.turn = number of answered questions so far
    - turn_idx = number of the next question (starts at 1)
    Returns: (stop_now, reason_text)
    """
    if turn_idx > max_turns:
        return True, f"Reached the maximum number of questions ({max_turns})."

    topk = step_out.get("topk") or []
    next_base = step_out.get("next_base") or ""
    ig = step_out.get("ig", None)
    candidates = step_out.get("candidates", None)

    if not next_base:
        return True, "No further questions are available."

    if candidates is None:
        score = float(ig) if ig is not None else 0.0
        candidates = [(next_base, score)]

    if turn_idx > min_turns:
        if topk and float(topk[0][1]) >= float(p_stop):
            return True, f"High confidence reached (top diagnosis probability ≈ {float(topk[0][1]):.2f})."
        if candidates:
            best_score = float(candidates[0][1])
            if best_score < float(ig_stop):
                return True, f"Further questions are unlikely to help (usefulness score ≈ {best_score:.4f})."

    return False, ""

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown("""
    <div style="padding: 0.5rem 0 1rem 0;">
        <h2 style="color:#2C3E50; font-size:1.1rem; font-weight:700; margin-bottom:0.25rem;">
            🩺 DDXPlus Assistant
        </h2>
        <p style="font-size:0.8rem; color:#5F6F7E; line-height:1.6;">
            Explore how a machine learning model reasons through symptoms
            to rank possible diagnoses — one question at a time.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    with st.expander("⚠️ Limitations & Disclaimer", expanded=True):
        st.markdown("""
        <ul style="font-size:0.78rem; color:#5F6F7E; line-height:1.8; padding-left:1.1rem;">
            <li>The DDXPlus dataset is <strong>fully synthetic</strong> — generated by medical experts
                but not derived from real patient records</li>
            <li>Results have <strong>no clinical validity</strong> and must never inform any real
                medical decision</li>
            <li>The model reasons only over the <strong>49 conditions</strong> and
                <strong>~223 symptoms</strong> present in the dataset</li>
            <li>Probabilities reflect dataset statistics, <strong>not</strong> true population
                disease prevalence</li>
        </ul>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <p style="font-size:0.76rem; color:#8A9BB0; line-height:1.6;">
        <strong>Dataset:</strong> Fansi Tchango et al.,<br>
        <em>"DDXPlus: A New Dataset for Automatic Medical Diagnosis"</em>,
        NeurIPS 2022.<br><br>
        <strong>Use:</strong> Educational purposes only.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    if st.button("🔄 Reset session", type="secondary"):
        reset_all()


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
# Step 1: Initial evidence input
# -----------------------------
if not st.session_state.started:
    st.subheader("Initial findings (optional)")
    st.caption("This is only for the first input. After starting, the assistant will ask the next best question iteratively.")

    cluster_name = st.selectbox("Pick a category", options=list(clusters.keys()), index=0)
    bases = clusters.get(cluster_name, [])

    def base_label(b: str) -> str:
        return f"{b} — {evidence_question(b, res.evidences_map)}"

    selected_bases = st.multiselect(
        "Select findings you already know are present",
        options=bases,
        format_func=base_label,
        default=[],
    )

    selected_tokens: List[str] = []
    for base in selected_bases:
        dtype = evidence_data_type(base, res.evidences_map)
        dv = evidence_default_value(base, res.evidences_map)

        if dtype == "B":
            selected_tokens.append(base)
            continue

        st.markdown(f"**{base}** — {evidence_question(base, res.evidences_map)}")
        st.caption(f"Default / non-informative value in dataset: {dv}")

        meta = res.evidences_map.get(base, {})
        poss = meta.get("possible-values") or []
        vm = meta.get("value_meaning") or {}

        if poss and all(isinstance(x, (int, float)) for x in poss):
            v = st.slider(f"Value for {base}", min_value=int(min(poss)), max_value=int(max(poss)),
                          value=int(dv) if (dv and dv.isdigit()) else 0)
            if dv is not None and str(v) == str(dv):
                st.info("This equals the dataset default; it will NOT be added as a positive.")
            else:
                selected_tokens.append(f"{base}={v}")
        else:
            opts = [str(x) for x in poss] if poss else list(vm.keys())
            if not opts:
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
# Interactive loop
# -----------------------------
sess: DiagnosisSession = st.session_state.session

st.subheader("Interactive Q&A (policy-driven)")
st.caption("We iteratively rank diagnoses and ask the next most informative question (dataset-grounded).")

step_out = assistant_step(sess, res, k=5, beta=0.7)
top: List[Tuple[str, float]] = step_out["top"]
next_base: str = step_out["next_base"]
next_q: str = step_out["next_question_en"]
ig: float = step_out["ig"]
p_yes: float = step_out["p_yes"]

# Current known positives
with st.expander("Current positive findings (what we know so far)", expanded=False):
    pos = sess.evidence_tokens_for_ml()
    if not pos:
        st.write("(None yet.)")
    else:
        for it in pos:
            st.write(f"- {format_evidence_item(it, res.evidences_map)}")

# --- Top-k diagnoses as styled cards ---
st.markdown("### Top diagnoses (current)")

CARD_COLORS = ["#648FFF", "#06A39B", "#785EF0", "#FE6100", "#DC267F"]
RANK_LABELS = ["1st", "2nd", "3rd", "4th", "5th"]

for i, (d, p) in enumerate(top):
    color = CARD_COLORS[i % len(CARD_COLORS)]
    pct = f"{p * 100:.1f}%"
    bar_width = max(int(p * 100), 4)
    rank = RANK_LABELS[i] if i < 5 else f"{i+1}th"
    st.markdown(f"""
    <div style="background:white; border-left:5px solid {color}; border-radius:8px;
                padding:14px 20px; margin-bottom:10px;
                box-shadow:0 2px 6px rgba(0,0,0,0.07);
                display:flex; justify-content:space-between; align-items:center;">
        <div>
            <span style="font-size:0.72rem; font-weight:700; color:{color};
                         text-transform:uppercase; letter-spacing:0.5px;">{rank}</span><br>
            <span style="font-size:1rem; font-weight:600; color:#2C3E50;">{d}</span>
            <div style="margin-top:8px; height:5px; background:#EEF2F7;
                         border-radius:4px; width:200px;">
                <div style="height:5px; width:{bar_width}%; background:{color};
                             border-radius:4px;"></div>
            </div>
        </div>
        <span style="font-size:1.6rem; font-weight:700; color:{color};">{pct}</span>
    </div>
    """, unsafe_allow_html=True)

# Explanations
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

turn_idx = st.session_state.turn + 1

# --- Stop check ---
stop_now, stop_reason = should_stop_interview(
    {
        "topk": top,
        "next_base": next_base,
        "ig": ig,
        "candidates": step_out.get("candidates", None),
    },
    turn_idx=turn_idx,
    max_turns=20,
    min_turns=3,
    p_stop=0.95,
    ig_stop=0.005,
)

if stop_now:
    st.success(f"✅ Session complete: {stop_reason}")
    st.session_state.stop_reason = stop_reason
    st.stop()

with st.expander(f"📋 More about these conditions (turn {turn_idx})", expanded=False):
    st.text(exp_topk)

with st.expander(f"💡 About the next question (turn {turn_idx})", expanded=False):
    st.text(exp_next)

st.markdown("---")

# --- Next question card ---
st.markdown(f"""
<div style="background:white; border:1px solid #DDE7F0; border-left:5px solid #06A39B;
            border-radius:8px; padding:16px 20px; margin-bottom:20px;
            box-shadow:0 2px 6px rgba(0,0,0,0.06);">
    <span style="font-size:0.72rem; font-weight:700; color:#06A39B;
                 text-transform:uppercase; letter-spacing:0.5px;">
        Next question — Turn {turn_idx}</span><br>
    <span style="font-size:1rem; font-weight:600; color:#2C3E50;">{next_base}</span><br>
    <span style="font-size:0.95rem; color:#5F6F7E; margin-top:4px; display:block;">{next_q}</span>
</div>
""", unsafe_allow_html=True)

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

        if poss and all(isinstance(x, (int, float)) for x in poss):
            value = st.slider("Value", min_value=int(min(poss)), max_value=int(max(poss)),
                              value=int(dv) if (dv and dv.isdigit()) else 0)
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

    st.session_state.trace.append({
        "turn": turn_idx,
        "next_base": next_base,
        "answer_status": status,
        "tokens_added": tokens_added,
        "top": top,
        "ig": ig,
        "p_yes": p_yes,
        "exp_topk": exp_topk,
        "exp_next": exp_next,
    })
    st.session_state.turn += 1
    st.session_state.session = sess
    st.rerun()
