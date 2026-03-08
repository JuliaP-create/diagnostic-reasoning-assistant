# Pulmonary neoplasm

**Overview:** Pulmonary neoplasm (lung cancer) refers to malignant tumors arising from the lung parenchyma or airways. The two main types are non-small cell lung cancer (NSCLC, ~85%) and small cell lung cancer (SCLC, ~15%). Smoking is the primary risk factor, accounting for ~80% of cases.

**Typical Presentation:** Persistent cough, hemoptysis, dyspnea, chest pain, and unintentional weight loss. Hoarseness (recurrent laryngeal nerve involvement) and superior vena cava syndrome may occur. Many early-stage tumors are asymptomatic and found incidentally on imaging.

**Key Distinguishing Features:** Distinguished from pneumonia by non-resolving or recurrent infiltrate on X-ray and constitutional symptoms. Distinguished from TB by mass lesion rather than cavitary disease and absence of AFB. Biopsy is required for definitive diagnosis.

**Severity & Urgency:** High — Overall 5-year survival is approximately 20%; early detection through low-dose CT screening improves outcomes.

**Sources:** [AAFP: Lung Cancer 2022] [Mayo Clinic: Lung Cancer]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `c34`
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
- **E_89** (B): Do you constantly feel fatigued or do you have non-restful sleep?
- **E_161** (B): Have you recently had a loss of appetite or do you get full more quickly then usually?
- **E_162** (B): Have you had an involuntary weight loss over the last 3 months?
- **E_201** (B): Do you have a cough?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_79** (B): Do you smoke cigarettes?
- **E_191** (B): Are you a former smoker?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_222** (B): Are you exposed to secondhand cigarette smoke on a daily basis?
- **E_224** (B): Do you have family members who have had lung cancer?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.