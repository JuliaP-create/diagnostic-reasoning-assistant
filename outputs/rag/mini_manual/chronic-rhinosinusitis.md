# Chronic rhinosinusitis

**Overview:** Chronic rhinosinusitis (CRS) is persistent inflammation of the paranasal sinuses lasting 12 weeks or more despite treatment. It can occur with or without nasal polyps. Causes include allergies, structural abnormalities, and biofilm-forming bacteria.

**Typical Presentation:** Nasal congestion, facial pain/pressure, purulent nasal discharge, and reduced sense of smell are the cardinal symptoms. Post-nasal drip and chronic cough are common. CT scan shows mucosal thickening or opacification of sinuses.

**Key Distinguishing Features:** Distinguished from acute rhinosinusitis by symptom duration (>12 weeks). Distinguished from allergic rhinitis by prominence of facial pain, purulent discharge, and CT findings.

**Severity & Urgency:** Low to Moderate — Chronic and impacts quality of life, but rarely life-threatening; may require surgery for refractory cases.

**Sources:** [NCBI Bookshelf: Chronic Sinusitis, StatPearls] [PMID: 30855882]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `j32`
- DDXPlus severity (dataset field): `5`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_103** (B): Have you lost your sense of smell?
- **E_181** (B): Do you have nasal congestion or a clear runny nose?
- **E_182** (B): Do you have greenish or yellowish nasal discharge?
- **E_201** (B): Do you have a cough?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_79** (B): Do you smoke cigarettes?
- **E_116** (B): Have you had a cold in the last 2 weeks?
- **E_118** (B): Have you ever had pneumonia?
- **E_120** (B): Do you have polyps in your nose?
- **E_121** (B): Do you have a deviated nasal septum?
- **E_124** (B): Do you have asthma or have you ever had to use a bronchodilator in the past?
- **E_125** (B): Have you ever been diagnosed with gastroesophageal reflux?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_226** (B): Are you more likely to develop common allergies than the general population?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.