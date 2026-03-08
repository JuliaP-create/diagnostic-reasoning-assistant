# Stable angina

**Overview:** Stable angina is predictable chest discomfort caused by myocardial ischemia during physical exertion or emotional stress, due to fixed atherosclerotic coronary artery narrowing. It affects the cardiovascular system. It is a manifestation of chronic coronary syndrome.

**Typical Presentation:** Chest pressure or tightness brought on by exertion and relieved within minutes by rest or sublingual nitroglycerin. Pain may radiate to the jaw, arm, or back. Symptoms are predictable and consistent in character over weeks to months.

**Key Distinguishing Features:** Distinguished from unstable angina by its predictable, exertion-related pattern and relief with rest. Distinguished from GERD by exertional trigger and ECG changes during stress testing.

**Severity & Urgency:** Moderate — Not immediately life-threatening but indicates significant coronary artery disease requiring risk factor management and possible revascularization.

**Sources:** [NCBI Bookshelf: Stable Angina, NBK559016] [PMC11980508]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `I20.9`
- DDXPlus severity (dataset field): `2`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_89** (B): Do you constantly feel fatigued or do you have non-restful sleep?
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