# Diagnostic Reasoning Assistant (Bootcamp Final Project)

An AI-powered **educational** diagnostic reasoning assistant built on the **DDXPlus** dataset.

It demonstrates an end-to-end offline workflow:
1) predict a ranked differential diagnosis from structured evidence (token Logistic Regression), and  
2) iteratively refine the differential by asking the next best evidence question (information-gain policy),  
3) provide **grounded, user-facing explanations** using **local TF‑IDF retrieval** over a curated corpus (DDXPlus definitions + mini‑manuals).

> **Safety disclaimer:** This repository is for education and demonstration only. It is **not medical advice** and is **not intended for direct patient care**.

---

## Project status (current)
✅ **Week 1:** EDA complete  
✅ **Week 2:** Model development complete (baseline + Phase 4 experiments)  
✅ **Week 3:** Calibration + interactive assistant loop prototype (token model + question policy)  
✅ **Week 4:** **Notebook 03 complete — offline TF‑IDF RAG explanations + multi‑turn demo traces saved**

**Next (remaining work):**
- Refactor Notebook 03 helpers into `src/rag.py`
- Streamlit demo app (symptom input → iterative Q&A → ranked diagnoses + explanations)
- Final presentation prep

---

## Key results (current best)
### Best model: Logistic Regression with token/value-level evidence encoding
- Evidence representation:
  - **Base encoding:** 223 evidence bases
  - **Token encoding:** 972 value-level tokens (e.g., `E_55=V_29`)
- Full test set performance:
  - **LogReg (base):** Top‑1 ≈ 0.9938, Macro‑F1 ≈ 0.9926
  - **LogReg (token):** Top‑1 ≈ 0.9974, Macro‑F1 ≈ 0.9963  
- Token encoding significantly reduces clinically meaningful confusions (e.g., acute vs chronic rhinosinusitis).

### Calibration (probability quality)
We evaluate probability calibration using:
- multiclass log-loss (lower is better)
- ECE (Expected Calibration Error; 0 is perfect)

All three models are near-diagonal on reliability plots with very low ECE (~0.001–0.002). Token LogReg is best overall (lowest log-loss and ECE).

---

## Notebook 03 (RAG explanations) — what is now implemented
Notebook 03 connects the predictive assistant loop to an explanation layer that stays **fully offline**:

- **Canonical TF‑IDF retriever:** `outputs/rag/tfidf_retriever.joblib` (321 local documents)
- **Mini‑manuals (49 conditions):** saved to `outputs/rag/mini_manual/` and loaded back into memory for explanations
- **Clinical enrichment source:** `src/condition_enrichments.py` (`CONDITION_ENRICHMENTS` dict; keys match `data/release_conditions.json`)
- **Multi‑turn demos + logs (for validation / presentation):**
  - `outputs/rag/demo_trace_log.json`
  - `outputs/rag/ambiguous_seed_demo_log.json`

All user-facing explanation text is framed as educational and includes a safety disclaimer.

---

## Selected figures
### Interactive setting: Accuracy vs evidence budget
Top‑1 accuracy vs number of known positive evidences (m):  
![Top‑1 accuracy vs evidences](figures/ml/12_budget_curve_top1.png)

### Token encoding improvement (headline metrics)
![Base vs Token metrics](figures/ml/15_base_vs_token_headline_metrics.png)

### Error analysis: biggest confusion reductions
![Top confusion reductions](figures/ml/20_top5_confusion_reductions_base_vs_token.png)

### Calibration (reliability diagram)
![Calibration reliability](figures/ml/21_calibration_reliability_3models.png)

### Calibration vs known evidences — ECE
![ECE vs evidence](figures/ml/22_calibration_vs_m_ece.png)

---

## Deployment artifacts (no retraining required)
The assistant runs from **saved artifacts** (joblib) — no retraining is required.

### Models (`models/`)
- Token Logistic Regression:
  - `models/logreg_token_multinomial.joblib`
  - `models/logreg_token_calibrated.joblib` (preferred when available)
- Question policy artifacts:
  - `models/policy_artifacts.joblib` (includes `p_e_given_d`, evidence base list, etc.)
- Preprocessors (bundle preferred; legacy fallbacks supported):
  - `models/preprocessors.joblib` *(preferred; contains `mlb_base`, `mlb_token`, encoders, and feature specs)*
  - `models/preprocessors_token.joblib` *(legacy)*
  - `models/preprocessors_base.joblib` *(legacy)*

### RAG (`outputs/rag/`)
- `outputs/rag/tfidf_retriever.joblib`
- `outputs/rag/mini_manual/index.json`
- `outputs/rag/mini_manual/*.md` (49 files)
- `outputs/rag/mini_manual_summary.csv`
- `outputs/rag/demo_trace_log.json`
- `outputs/rag/ambiguous_seed_demo_log.json`

---

## Dataset
**Primary dataset:** DDXPlus (synthetic clinical cases)
- ~1.29M synthetic patient cases
- 49 pathologies
- 223 evidence bases (+ 972 token/value-level features)
- Differential diagnosis list included but **not used as a predictive input feature**.

**Mapping files (tracked in repo)**
- `data/release_evidences.json` (evidence code → question text, data type, value meanings)
- `data/release_conditions.json` (condition name → disease metadata)

> Note: DDXPlus is synthetic, privacy-safe data. Results reflect in-dataset performance and may not generalize to real clinical populations.

---

## Technologies
- Python, scikit-learn
- Offline TF‑IDF retrieval (RAG baseline)
- (Next) Streamlit deployment

---

## Repository structure
```text
.
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_development.ipynb
│   └── 03_rag_explanations_ddxplus.ipynb
├── src/
│   ├── artifacts.py
│   ├── encoding.py
│   ├── inference.py
│   ├── policy.py
│   ├── types.py
│   └── condition_enrichments.py
├── data/
│   ├── release_evidences.json
│   ├── release_conditions.json
│   └── processed/                 # optional cached artifacts
├── figures/
│   ├── eda/
│   ├── ml/
│   └── rag/
├── outputs/
│   ├── eda/
│   ├── ml/
│   └── rag/
├── models/
├── scripts/
├── requirements.txt
└── README.md
```

---

## How to run
### 1) Set up the environment
```bash
pip install -r requirements.txt
```

### 2) Data availability
The full DDXPlus case dataset is typically downloaded separately (not stored in this repo).  
However, **Notebook 03** does **not** require the full case dataset if the `models/` artifacts are already present.

### 3) Run notebooks (recommended order)
1. `notebooks/01_data_exploration.ipynb`  
2. `notebooks/02_model_development.ipynb`  
   - saves `models/` artifacts (model, calibrator, policy table, preprocessors)
3. `notebooks/03_rag_explanations_ddxplus.ipynb`  
   - builds the TF‑IDF retriever
   - runs demo traces with explanations
   - saves RAG artifacts + logs to `outputs/rag/`

### 4) Known environment note (joblib + scikit-learn)
If you see an `InconsistentVersionWarning` when loading artifacts, pin scikit‑learn to the version used when the models were saved.

---

## What we intentionally did not do (for the bootcamp deadline)
- No dense embeddings / vector database
- No external PubMed retrieval at runtime
- No LLM API calls (offline-only requirement)

---

## License / attribution
DDXPlus is a published synthetic benchmark dataset; please follow the dataset’s license and terms for any redistribution.
