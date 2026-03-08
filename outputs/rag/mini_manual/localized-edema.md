# Localized edema

**Overview:** Localized edema is the accumulation of fluid in a specific body region, as opposed to generalized edema. It can result from venous insufficiency, lymphatic obstruction, infection, inflammation, or allergic reaction. The affected area depends on the underlying cause.

**Typical Presentation:** Presents with unilateral or focal swelling, often in a limb. Pitting edema may be present. Associated warmth and redness suggest infection or inflammation, while painless edema suggests lymphedema or venous insufficiency.

**Key Distinguishing Features:** Distinguished from generalized edema (heart failure, nephrotic syndrome) by its focal distribution. Distinguished from DVT by absence of calf tenderness and negative Doppler ultrasound.

**Severity & Urgency:** Low to Moderate — Depends on cause; uncomplicated cases are low severity, but DVT-associated edema requires urgent evaluation.

**Sources:** [NCBI Bookshelf: Edema, StatPearls] [PMID: 30725761]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `R60.0`
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
- **E_67** (B): Do you have bouts of choking or shortness of breath that wake you up at night?
- **E_96** (B): Have you gained weight recently?
- **E_151** (B): Do you have swelling in one or more areas of your body?
- **E_152** (M): Where is the swelling located?
- **E_217** (B): Are your symptoms worse when lying down and alleviated while sitting up?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_10** (B): Are you currently taking or have you recently taken anti-inflammatory drugs (NSAIDs)?
- **E_22** (B): Do you have a known issue with one of your heart valves?
- **E_44** (B): Do you take corticosteroids?
- **E_106** (B): Do you have heart failure?
- **E_109** (B): Have you ever had deep vein thrombosis (DVT)?
- **E_126** (B): Do you have liver cirrhosis?
- **E_137** (B): Have you ever had surgery to remove lymph nodes?
- **E_149** (B): Do you take a calcium channel blockers (medication)?
- **E_158** (B): Were you diagnosed with endocrine disease or a hormone dysfunction?
- **E_186** (B): Have you ever been diagnosed with obstructive sleep apnea (OSA)?
- **E_197** (B): Do you have a known kidney problem resulting in an inability to retain proteins?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.