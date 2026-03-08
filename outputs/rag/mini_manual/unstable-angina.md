# Unstable angina

**Overview:** Unstable angina results from acute obstruction of a coronary artery without complete occlusion and without myocardial necrosis (normal troponin). It is a form of acute coronary syndrome affecting the cardiovascular system. It sits on the spectrum between stable angina and MI.

**Typical Presentation:** New-onset chest pain at rest, or previously stable angina that has become more frequent, severe, or occurs with less exertion. Pain may last >20 minutes and be accompanied by dyspnea, diaphoresis, and nausea. ECG may show ST depression or T-wave inversion.

**Key Distinguishing Features:** Distinguished from NSTEMI by the absence of elevated troponin levels. Distinguished from stable angina by pain at rest, escalating pattern, or new onset.

**Severity & Urgency:** High — Considered a pre-infarction state requiring urgent hospital admission, anticoagulation, and cardiac catheterization.

**Sources:** [Merck Manual: Unstable Angina] [NCBI Bookshelf: NBK442000]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `I20.0`
- DDXPlus severity (dataset field): `2`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_13** (B): Do you find that your symptoms have worsened over the last 2 weeks and that progressively less effort is required to cause the symptoms?
- **E_14** (B): Do you have chest pain even at rest?
- **E_50** (B): Have you had significantly increased sweating?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_89** (B): Do you constantly feel fatigued or do you have non-restful sleep?
- **E_148** (B): Are you feeling nauseous or do you feel like vomiting?
- **E_218** (B): Do you have symptoms that are increased with physical exertion but alleviated with rest?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_69** (B): Do you have diabetes?
- **E_70** (B): Are you significantly overweight compared to people of the same height as you?
- **E_71** (B): Do you have high cholesterol or do you take medications to treat high cholesterol?
- **E_78** (B): Do you drink alcohol excessively or do you have an addiction to alcohol?
- **E_79** (B): Do you smoke cigarettes?
- **E_104** (B): Do you have high blood pressure or do you take medications to treat high blood pressure?
- **E_105** (B): Have you ever had a heart attack or do you have angina (chest pain)?
- **E_143** (B): Do you exercise regularly, 4 times per week or more?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_225** (B): Do you have close family members who had a cardiovascular disease problem before the age of 50?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.