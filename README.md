# Diagnostic Reasoning Assistant

An AI-powered clinical decision support tool that assists medical 
professionals in differential diagnosis through iterative questioning, 
ML-driven classification, and RAG-enhanced literature integration.

**Special Focus:** Reducing diagnostic delays for rare and overlooked 
conditions through two-tier architecture and transparent reasoning.

## Project Overview
- **Duration:** 4 weeks (Feb 2026)
- **Type:** Data Science Bootcamp Final Project
- **Approach:** Machine Learning + Generative AI (RAG)
- **Coverage:** 49+ diseases from common to rare conditions

## Key Features
- Ranked differential diagnoses (not unranked lists)
- Iterative questioning to refine predictions
- Two-tier architecture: general classifier → rare disease specialist
- Transparent reasoning with confidence scores
- Literature-backed explanations for rare diagnoses

## Dataset
- DDXPlus: 1.3M synthetic patient cases, 49 pathologies
- Source: [Hugging Face](https://huggingface.co/datasets/aai530-group6/ddxplus)
- NeurIPS 2022, Mila Quebec AI Institute
- Size: 1,292,579 patient cases
- Coverage: 49 pathologies, 223 evidence codes
- Citation: Fansi Tchango et al. (2022)

**Note:** This is a synthetic dataset generated from medical knowledge bases. 
While it doesn't capture all real-world complexity, it provides a robust, 
privacy-compliant foundation for developing and testing diagnostic AI systems.

## Technologies
- Python, scikit-learn, XGBoost
- LangChain, RAG (Retrieval-Augmented Generation)
- Streamlit (web interface)
- Tableau (EDA visualization)

## Motivation
Personal experience with family members' diagnostic odysseys 
(missed/delayed diagnoses) inspired this project to improve 
systematic diagnostic reasoning.

## Status
🚧 In Progress - Week 1: Data Exploration & EDA

---

*Educational tool for medical professionals. Not intended for direct patient use.*

