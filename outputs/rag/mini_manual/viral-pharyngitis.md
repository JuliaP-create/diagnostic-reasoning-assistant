# Viral pharyngitis

**Overview:** Viral pharyngitis is inflammation of the pharynx caused by viruses such as rhinovirus, adenovirus, or Epstein-Barr virus. It is the most common cause of sore throat and affects the upper respiratory system. Transmission is via respiratory droplets or direct contact.

**Typical Presentation:** Presents with sore throat, mild fever, and often accompanies URTI symptoms like cough, rhinorrhea, and conjunctivitis. Absence of tonsillar exudates and anterior cervical lymphadenopathy helps distinguish it from bacterial pharyngitis.

**Key Distinguishing Features:** Unlike Group A Streptococcal pharyngitis, viral pharyngitis typically includes concurrent cough, rhinorrhea, and hoarseness, and lacks tonsillar exudates and high fever.

**Severity & Urgency:** Low — Self-limiting within 5–7 days; antibiotics are not indicated.

**Sources:** [NCBI Bookshelf: Pharyngitis, StatPearls] [PMID: 32310559]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `J02.9`
- DDXPlus severity (dataset field): `4`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_45** (B): Have you been coughing up blood?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_181** (B): Do you have nasal congestion or a clear runny nose?
- **E_201** (B): Do you have a cough?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_41** (B): Have you been in contact with a person with similar symptoms in the past 2 weeks?
- **E_48** (B): Do you live with 4 or more people?
- **E_49** (B): Do you attend or work in a daycare?
- **E_79** (B): Do you smoke cigarettes?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_227** (B): Are you immunosuppressed?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.