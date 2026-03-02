# Diagnostic Reasoning Assistant (Bootcamp Final Project)

An AI-powered *educational* diagnostic reasoning assistant that supports medical students and junior clinicians by:
1) ranking differential diagnoses from structured evidence, and
2) refining them through iterative questioning using an information-gain policy (next).

> **Disclaimer:** Educational tool only. Not intended for direct patient care.

---

## Project status (WIP)
✅ **Week 1: EDA complete**  
✅ **Week 2: Model development complete (baseline + Phase 4 experiments)** *(ML work started Feb 14)*  
✅ **Week 3: Calibration + interactive assistant loop prototype (token model + question policy prototype)**  
🔜 **Next (final week): RAG explanations + deployment + final presentation**

---

## Key results (current best)
### Best model: Logistic Regression with token/value-level evidence encoding
- Evidence representation:
  - **Base encoding:** 223 evidence bases
  - **Token encoding:** 972 value-level tokens (e.g., `E_55=V_29`)
- Full test set performance:
  - **LogReg (base):** Top‑1 ≈ 0.9938, Macro‑F1 ≈ 0.9926
  - **LogReg (token):** Top‑1 ≈ 0.9974, Macro‑F1 ≈ 0.9963  
- Token encoding significantly reduces clinically meaningful confusions, including acute vs chronic rhinosinusitis.

### Calibration (probability quality)
We evaluated probability calibration using:
- multiclass log-loss (lower is better)
- ECE (Expected Calibration Error; 0 is perfect)

All three models are near-diagonal on reliability plots with very low ECE (~0.001–0.002). Token LogReg is best overall (lowest log-loss and ECE).

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
The deployed assistant loads pre-trained artifacts from `models/`:
- Token Logistic Regression model (e.g., `models/logreg_token_multinomial.joblib`)
- Preprocessors bundle (e.g., `models/preprocessors.joblib`) containing:
  - `mlb_token`, `ohe`, `scaler`, `label_encoder`
  - feature metadata (column lists / feature names)
- Calibrated model (or calibrator wrapper), if used in the app (filename depends on your notebook export)

---

## Dataset
**Primary dataset:** DDXPlus (synthetic clinical cases)
- 1,292,579 synthetic patient cases
- 49 pathologies
- 223 evidence bases (+ 972 token/value-level features)
- Differential diagnosis list included but **not used as a predictive input feature**.

**Mapping files**
- `data/release_evidences.json` (evidence code → question text, data type, value meanings)
- `data/release_conditions.json` (condition code → disease metadata)

> Note: DDXPlus is synthetic, privacy-safe data. Results reflect in-dataset performance and may not generalize to real clinical populations.

---

## Technologies
- Python, scikit-learn
- (Planned next) RAG for explanations / question wording
- (Planned next) Streamlit deployment

---

## Repository structure
```text
.
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_model_development.ipynb
├── data/
│   ├── release_evidences.json
│   ├── release_conditions.json
│   └── processed/                 # optional cached artifacts
├── figures/
│   ├── eda/
│   └── ml/
├── outputs/
│   ├── eda/
│   └── ml/
├── models/
├── requirements.txt
└── README.md
```
---
## How to run
1. Create environment and install dependencies:
   - `pip install -r requirements.txt`
2. Download DDXPlus from Hugging Face (not stored in this repo).
3. Run notebooks in order:
   - `01_data_exploration.ipynb`
   - `02_model_development.ipynb`

Outputs:
- Tables saved to `outputs/`
- Figures saved to `figures/`
- Trained models saved to `models/` (joblib)