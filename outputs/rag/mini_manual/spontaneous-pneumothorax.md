# Spontaneous pneumothorax

**Overview:** Spontaneous pneumothorax is the accumulation of air in the pleural space without external trauma. Primary spontaneous pneumothorax (PSP) occurs in patients without known lung disease, typically tall, thin young men. Secondary spontaneous pneumothorax occurs in those with underlying lung disease (COPD, cystic fibrosis).

**Typical Presentation:** Sudden onset of unilateral pleuritic chest pain and dyspnea. Pain may be sharp and steady, often resolving within 24 hours even if pneumothorax persists. Decreased breath sounds, hyper-resonance to percussion, and reduced chest wall movement on the affected side.

**Key Distinguishing Features:** Distinguished from PE by sudden onset with absent rather than reduced breath sounds and hyper-resonant (not normal) percussion. Distinguished from MI by pleuritic character and unilateral lung findings. Chest X-ray or CT confirms the diagnosis.

**Severity & Urgency:** Moderate to High — Small pneumothoraces may resolve with observation, but tension pneumothorax is immediately life-threatening and requires needle decompression.

**Sources:** [PMC2950234] [PMC9487279]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `J93`
- DDXPlus severity (dataset field): `2`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_14** (B): Do you have chest pain even at rest?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_151** (B): Do you have swelling in one or more areas of your body?
- **E_218** (B): Do you have symptoms that are increased with physical exertion but alleviated with rest?
- **E_220** (B): Do you have pain that is increased when you breathe in deeply?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_21** (B): Have you ever had a spontaneous pneumothorax?
- **E_79** (B): Do you smoke cigarettes?
- **E_123** (B): Do you have a chronic obstructive pulmonary disease (COPD)?
- **E_165** (B): Have any of your family members ever had a pneumothorax?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.