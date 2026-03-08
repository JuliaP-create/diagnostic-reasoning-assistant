# Influenza

**Overview:** Influenza is an acute respiratory illness caused by influenza A or B viruses. It affects the upper and lower respiratory tract and has significant systemic effects. It spreads via respiratory droplets and has seasonal epidemic patterns.

**Typical Presentation:** Abrupt onset of high fever, severe myalgia, headache, dry cough, sore throat, and profound fatigue. Unlike common cold (URTI), systemic symptoms dominate over nasal symptoms. Duration is typically 5–7 days.

**Key Distinguishing Features:** Distinguished from URTI by sudden onset, high fever (>38.5°C), severe body aches, and prostration. Rapid influenza diagnostic tests or PCR confirm the diagnosis during flu season.

**Severity & Urgency:** Moderate — Most healthy adults recover, but high risk of complications (pneumonia, death) in elderly, immunocompromised, and young children.

**Sources:** [NCBI Bookshelf: Influenza, StatPearls] [PMID: 29763133]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `j11.1`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_50** (B): Have you had significantly increased sweating?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_88** (B): Do you feel so tired that you are unable to do your usual activities or are you stuck in your bed all day long?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_94** (B): Have you had chills or shivers?
- **E_97** (B): Do you have a sore throat?
- **E_129** (B): Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?
- **E_130** (C): What color is the rash?
- **E_131** (C): Do your lesions peel off?
- **E_132** (C): Is the rash swollen?
- **E_133** (M): Where is the affected region located?
- **E_134** (C): How intense is the pain caused by the rash?
- … (6 more omitted for brevity)

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_79** (B): Do you smoke cigarettes?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_227** (B): Are you immunosuppressed?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.