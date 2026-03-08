# Pulmonary embolism

**Overview:** Pulmonary embolism (PE) occurs when a blood clot, usually from deep veins of the legs, travels to and blocks a pulmonary artery. It affects the pulmonary vascular system and can impair gas exchange and right heart function. Risk factors include immobility, surgery, cancer, and inherited thrombophilia.

**Typical Presentation:** Sudden-onset dyspnea, pleuritic chest pain, and tachycardia are the hallmark features. Hemoptysis, calf swelling (from concurrent DVT), and hypoxia may also be present. Massive PE causes hypotension and syncope.

**Key Distinguishing Features:** Distinguished from pneumonia by pleuritic pain without productive cough or fever, and from MI by ECG and troponin patterns. A positive D-dimer with high Wells score prompts CT pulmonary angiography.

**Severity & Urgency:** High to Critical — Massive PE with hemodynamic compromise requires emergent thrombolysis or embolectomy.

**Sources:** [NCBI Bookshelf: Pulmonary Embolism, StatPearls] [PMID: 28613592]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `i26`
- DDXPlus severity (dataset field): `2`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_45** (B): Have you been coughing up blood?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_151** (B): Do you have swelling in one or more areas of your body?
- **E_152** (M): Where is the swelling located?
- **E_159** (B): Did you lose consciousness?
- **E_220** (B): Do you have pain that is increased when you breathe in deeply?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_34** (B): Do you have an active cancer?
- **E_100** (B): Do you currently take hormones?
- **E_109** (B): Have you ever had deep vein thrombosis (DVT)?
- **E_110** (B): Have you been unable to move or get up for more than 3 consecutive days within the last 4 weeks?
- **E_196** (B): Have you had surgery within the last month?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.