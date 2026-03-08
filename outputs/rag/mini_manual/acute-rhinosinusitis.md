# Acute rhinosinusitis

**Overview:** Acute rhinosinusitis is inflammation of the nasal cavity and paranasal sinuses lasting less than 4 weeks, most commonly caused by viral infection (rhinovirus) and occasionally by secondary bacterial infection. It affects the upper respiratory system.

**Typical Presentation:** Nasal congestion, purulent nasal discharge, facial pain/pressure (especially over maxillary and frontal sinuses), and reduced smell. Bacterial superinfection is suggested by symptoms lasting >10 days, double worsening (improvement then deterioration), or high fever with purulent discharge.

**Key Distinguishing Features:** Distinguished from allergic sinusitis by acute onset, purulent discharge, and facial pain. Distinguished from URTI by prominent facial pain and symptom duration beyond 10 days suggesting bacterial involvement.

**Severity & Urgency:** Low — Mostly viral and self-limiting; bacterial cases respond to antibiotics. Rare complications include orbital cellulitis and intracranial abscess.

**Sources:** [NCBI Bookshelf: Sinusitis, StatPearls] [PMID: 30856035]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `j01`
- DDXPlus severity (dataset field): `4`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
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
- **E_209** (B): Are your vaccinations up to date?
- **E_226** (B): Are you more likely to develop common allergies than the general population?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.