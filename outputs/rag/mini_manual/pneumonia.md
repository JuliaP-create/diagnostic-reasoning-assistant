# Pneumonia

**Overview:** Pneumonia is an infection of the lung parenchyma causing inflammation and consolidation of the alveolar spaces. It can be caused by bacteria (S. pneumoniae most common), viruses, or fungi. It affects the lower respiratory system.

**Typical Presentation:** Presents with productive cough, fever, dyspnea, pleuritic chest pain, and sometimes rigors. On exam, focal crackles, bronchial breath sounds, and dullness to percussion are found. Chest X-ray shows lobar or patchy infiltrates.

**Key Distinguishing Features:** Distinguished from acute bronchitis by focal lung findings on exam and infiltrate on X-ray. Distinguished from PE by productive cough, fever, and consolidation pattern rather than wedge-shaped infarct.

**Severity & Urgency:** Moderate to High — Can be life-threatening in elderly, immunocompromised, or when caused by virulent organisms.

**Sources:** [NCBI Bookshelf: Pneumonia, StatPearls] [PMID: 28722890]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `j17, j18`
- DDXPlus severity (dataset field): `3`

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
- **E_77** (B): Do you have a cough that produces colored or more abundant sputum than usual?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_94** (B): Have you had chills or shivers?
- **E_129** (B): Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?
- **E_130** (C): What color is the rash?
- **E_131** (C): Do your lesions peel off?
- **E_132** (C): Is the rash swollen?
- **E_133** (M): Where is the affected region located?
- **E_134** (C): How intense is the pain caused by the rash?
- … (9 more omitted for brevity)

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_78** (B): Do you drink alcohol excessively or do you have an addiction to alcohol?
- **E_79** (B): Do you smoke cigarettes?
- **E_95** (B): Do you have Parkinson’s disease?
- **E_106** (B): Do you have heart failure?
- **E_107** (B): Have you ever had a stroke?
- **E_118** (B): Have you ever had pneumonia?
- **E_123** (B): Do you have a chronic obstructive pulmonary disease (COPD)?
- **E_124** (B): Do you have asthma or have you ever had to use a bronchodilator in the past?
- **E_196** (B): Have you had surgery within the last month?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_208** (B): Is your BMI less than 18.5, or are you underweight?
- **E_209** (B): Are your vaccinations up to date?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.