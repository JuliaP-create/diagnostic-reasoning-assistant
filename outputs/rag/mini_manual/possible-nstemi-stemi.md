# Possible NSTEMI / STEMI

**Overview:** NSTEMI and STEMI are forms of acute myocardial infarction caused by coronary artery occlusion. STEMI involves complete occlusion with transmural ischemia, while NSTEMI involves partial or transient occlusion. Both affect the cardiovascular system and require emergent evaluation.

**Typical Presentation:** Substernal chest pain or pressure radiating to the jaw or left arm, with diaphoresis, nausea, and dyspnea. STEMI shows characteristic ST elevation on ECG, while NSTEMI shows ST depression or T-wave changes. Elevated cardiac troponin confirms myocardial injury.

**Key Distinguishing Features:** STEMI is distinguished from NSTEMI by persistent ST-segment elevation on ECG. Both are distinguished from pericarditis by territorial (not diffuse) ECG changes and from PE by elevated troponin with ischemic ECG changes.

**Severity & Urgency:** Critical — STEMI requires emergent reperfusion (PCI within 90 minutes). NSTEMI requires urgent risk stratification and intervention.

**Sources:** [NCBI Bookshelf: STEMI, NBK532281] [PMC9676707]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `I21`
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
- **E_89** (B): Do you constantly feel fatigued or do you have non-restful sleep?
- **E_148** (B): Are you feeling nauseous or do you feel like vomiting?
- **E_161** (B): Have you recently had a loss of appetite or do you get full more quickly then usually?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_2** (B): Are you infected with the human immunodeficiency virus (HIV)?
- **E_69** (B): Do you have diabetes?
- **E_70** (B): Are you significantly overweight compared to people of the same height as you?
- **E_71** (B): Do you have high cholesterol or do you take medications to treat high cholesterol?
- **E_79** (B): Do you smoke cigarettes?
- **E_104** (B): Do you have high blood pressure or do you take medications to treat high blood pressure?
- **E_105** (B): Have you ever had a heart attack or do you have angina (chest pain)?
- **E_108** (B): Do you have a problem with poor circulation?
- **E_191** (B): Are you a former smoker?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_225** (B): Do you have close family members who had a cardiovascular disease problem before the age of 50?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.