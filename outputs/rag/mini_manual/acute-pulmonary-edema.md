# Acute pulmonary edema

**Overview:** Acute pulmonary edema is the rapid accumulation of fluid in the alveoli, most commonly caused by left ventricular failure (cardiogenic). It can also result from non-cardiogenic causes like ARDS. It affects the respiratory and cardiovascular systems.

**Typical Presentation:** Sudden onset of severe dyspnea, orthopnea, frothy pink sputum, and anxiety. Physical exam reveals bilateral crackles, tachypnea, tachycardia, and often elevated JVP. Chest X-ray shows bilateral alveolar infiltrates (butterfly pattern) and cardiomegaly.

**Key Distinguishing Features:** Distinguished from pneumonia by bilateral symmetric pattern, frothy sputum, and cardiac history. Distinguished from COPD exacerbation by rapid onset, pink sputum, and basal crackles rather than diffuse wheezing.

**Severity & Urgency:** Critical — Medical emergency requiring immediate oxygen, diuretics, vasodilators, and sometimes non-invasive ventilation.

**Sources:** [NCBI Bookshelf: Cardiogenic Pulmonary Edema, NBK544260] [Mayo Clinic: Pulmonary Edema]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `J81.0`
- DDXPlus severity (dataset field): `1`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_50** (B): Have you had significantly increased sweating?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_67** (B): Do you have bouts of choking or shortness of breath that wake you up at night?
- **E_151** (B): Do you have swelling in one or more areas of your body?
- **E_152** (M): Where is the swelling located?
- **E_175** (B): Have you noticed any new fatigue, generalized and vague discomfort, diffuse (widespread) muscle aches or a change in your general well-being related to your consultation today?
- **E_217** (B): Are your symptoms worse when lying down and alleviated while sitting up?
- **E_218** (B): Do you have symptoms that are increased with physical exertion but alleviated with rest?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_5** (B): Have you ever had fluid in your lungs?
- **E_8** (B): Do you currently undergo dialysis?
- **E_104** (B): Do you have high blood pressure or do you take medications to treat high blood pressure?
- **E_105** (B): Have you ever had a heart attack or do you have angina (chest pain)?
- **E_106** (B): Do you have heart failure?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.