# Bronchitis

**Overview:** Acute bronchitis is inflammation of the bronchial airways, most often caused by viruses (rhinovirus, influenza, RSV). It affects the lower respiratory system. Smoking and air pollution are predisposing factors.

**Typical Presentation:** Persistent cough (lasting 1–3 weeks), often productive with clear or discolored sputum. Low-grade fever, chest discomfort, and wheezing may be present. Absence of consolidation on exam distinguishes it from pneumonia.

**Key Distinguishing Features:** Distinguished from pneumonia by absence of high fever, focal crackles, and chest X-ray infiltrates. Distinguished from asthma by absence of recurrent episodes and reversible airflow obstruction.

**Severity & Urgency:** Low — Self-limiting in most healthy patients; antibiotics are usually not indicated.

**Sources:** [NCBI Bookshelf: Acute Bronchitis, StatPearls] [PMID: 30137776]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `j40`
- DDXPlus severity (dataset field): `4`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_77** (B): Do you have a cough that produces colored or more abundant sputum than usual?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_97** (B): Do you have a sore throat?
- **E_181** (B): Do you have nasal congestion or a clear runny nose?
- **E_201** (B): Do you have a cough?
- **E_214** (B): Have you noticed a wheezing sound when you exhale?
- **E_219** (B): Are your symptoms more prominent at night?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_79** (B): Do you smoke cigarettes?
- **E_123** (B): Do you have a chronic obstructive pulmonary disease (COPD)?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_209** (B): Are your vaccinations up to date?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.