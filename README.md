# Diagnostic Reasoning Assistant (Bootcamp Final Project)

An AI-powered *educational* diagnostic reasoning assistant that aims to support
medical students and junior clinicians by generating ranked differential diagnoses
and (later) refining them through iterative questioning.

> **Disclaimer:** Educational tool only. Not intended for direct patient care.

---

## Project status (Week 1)
✅ **Week 1: Data Exploration & EDA (in progress / mostly complete)**

Current work focuses on:
- Loading the DDXPlus dataset (train/validate/test splits)
- Parsing evidence and differential diagnosis fields into usable Python structures
- Data quality checks (missingness, duplicates)
- Exploratory visualizations and dataset understanding
- Preparing the ground for feature engineering and modeling in Week 2

---

## Dataset
**Primary dataset:** DDXPlus (synthetic clinical cases)
- DDXPlus: 1,292,579 synthetic patient cases, 49 pathologies, 223 evidence codes
- Source: [Hugging Face](https://huggingface.co/datasets/aai530-group6/ddxplus)
- NeurIPS 2022, Mila Quebec AI Institute
- Citation: Fansi Tchango et al. (2022)

**The dataset contains:**
- Demographics (e.g., age, sex)
- Evidence codes (symptoms/findings; some are binary, categorical, or multi-choice)
- Ground truth pathology (diagnosis)
- Differential diagnosis list

**Mapping files used in EDA:**
- `data/release_evidences.json` (evidence code → question text, type, value meanings)
- `data/release_conditions.json` (condition code → disease info)

> Note: DDXPlus is synthetic, privacy-safe data. Results will reflect in-dataset performance
> and may not generalize to real clinical populations without further validation.

---
## Technologies
- Python, scikit-learn, XGBoost
- LangChain, RAG (Retrieval-Augmented Generation)
- Streamlit (web interface)
- Tableau (EDA visualization)

## Repository structure (current)
```text
.
├── notebooks/
│   └── 01_data_exploration.ipynb
├── data/
│   ├── release_evidences.json
│   ├── release_conditions.json
│   └── processed/                 # created by notebooks (optional outputs)
├── figures/                       # created by notebooks (plots)
├── outputs/                       # created by notebooks (tables/summaries)
├── requirements.txt               # (optional; add as you lock dependencies)
└── README.md

