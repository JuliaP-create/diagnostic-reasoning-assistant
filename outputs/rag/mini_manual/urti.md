# URTI

**Overview:** Upper respiratory tract infection (URTI) is the most common infectious disease, affecting the nose, sinuses, pharynx, and larynx. It is usually caused by viruses (rhinovirus, coronavirus, adenovirus) and is self-limiting. The upper airway mucosa becomes inflamed, causing congestion and discharge.

**Typical Presentation:** Patients present with nasal congestion, rhinorrhea, sore throat, sneezing, mild cough, and low-grade fever. Symptoms typically peak at 2–3 days and resolve within 7–10 days. Fatigue and malaise are common.

**Key Distinguishing Features:** Distinguished from influenza by the absence of high fever, severe myalgia, and prostration. Distinguished from bacterial sinusitis by symptom duration under 10 days and absence of facial pain.

**Severity & Urgency:** Low — Usually self-limiting; complications are rare in otherwise healthy individuals.

**Sources:** [NCBI Bookshelf: Upper Respiratory Tract Infection, StatPearls] [PMID: 30725746]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `j06.9`
- DDXPlus severity (dataset field): `5`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_50** (B): Have you had significantly increased sweating?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_77** (B): Do you have a cough that produces colored or more abundant sputum than usual?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_97** (B): Do you have a sore throat?
- **E_144** (B): Do you have diffuse (widespread) muscle pain?
- **E_181** (B): Do you have nasal congestion or a clear runny nose?
- **E_201** (B): Do you have a cough?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_41** (B): Have you been in contact with a person with similar symptoms in the past 2 weeks?
- **E_48** (B): Do you live with 4 or more people?
- **E_49** (B): Do you attend or work in a daycare?
- **E_79** (B): Do you smoke cigarettes?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_222** (B): Are you exposed to secondhand cigarette smoke on a daily basis?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.