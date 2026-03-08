# Anemia

**Overview:** Anemia is a condition where hemoglobin or red blood cell count is below normal, reducing oxygen delivery to tissues. Causes include iron deficiency, chronic disease, vitamin B12/folate deficiency, and blood loss. It affects the hematologic system with downstream effects on multiple organs.

**Typical Presentation:** Patients report fatigue, pallor, weakness, dyspnea on exertion, and dizziness. Tachycardia and systolic flow murmurs may be found on exam. Severe anemia can cause chest pain or syncope.

**Key Distinguishing Features:** Distinguished from heart failure by normal BNP levels and from hypothyroidism by normal thyroid function. Low hemoglobin on CBC confirms the diagnosis; further workup determines the subtype.

**Severity & Urgency:** Low to High — Mild anemia is low severity; severe anemia (Hb < 7 g/dL) can cause cardiac decompensation and is high severity.

**Sources:** [NCBI Bookshelf: Anemia, StatPearls] [PMID: 33085726]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `D64.9`
- DDXPlus severity (dataset field): `4`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_76** (B): Do you feel slightly dizzy or lightheaded?
- **E_82** (B): Do you feel lightheaded and dizzy or do you feel like you are about to faint?
- **E_88** (B): Do you feel so tired that you are unable to do your usual activities or are you stuck in your bed all day long?
- **E_89** (B): Do you constantly feel fatigued or do you have non-restful sleep?
- **E_140** (B): Have you recently had stools that were black (like coal)?
- **E_145** (B): Do you have very abundant or very long menstruation periods?
- **E_154** (B): Is your skin much paler than usual?
- **E_179** (B): Have you noticed light red blood or blood clots in your stool?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_7** (B): Do you have a poor diet?
- **E_24** (B): Have you ever had a diagnosis of anemia?
- **E_26** (B): Do you have any family members who have been diagnosed with anemia?
- **E_113** (B): Do you have chronic kidney failure?
- **E_146** (B): Are you taking any new oral anticoagulants ((NOACs)?
- **E_167** (B): Do you think you are pregnant or are you currently pregnant?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_208** (B): Is your BMI less than 18.5, or are you underweight?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.