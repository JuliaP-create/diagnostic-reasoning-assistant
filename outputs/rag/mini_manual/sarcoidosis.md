# Sarcoidosis

**Overview:** Sarcoidosis is a systemic granulomatous disease of unknown cause characterized by noncaseating granulomas, most commonly affecting the lungs and lymph nodes. It can also involve the skin, eyes, liver, and nervous system. It predominantly affects adults aged 25–40.

**Typical Presentation:** Bilateral hilar lymphadenopathy, dry cough, dyspnea, and fatigue are the most common presentations. Skin findings include erythema nodosum and lupus pernio. Many patients are asymptomatic and discovered incidentally on chest X-ray.

**Key Distinguishing Features:** Distinguished from lymphoma by bilateral symmetrical hilar lymphadenopathy and noncaseating granulomas on biopsy. Distinguished from tuberculosis by negative AFB stains and cultures.

**Severity & Urgency:** Moderate — Often self-remitting (especially stage I), but progressive pulmonary or cardiac sarcoidosis can be severe.

**Sources:** [PMC8066110] [PMC6713839]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `d86`
- DDXPlus severity (dataset field): `4`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_9** (B): Do you have swollen or painful lymph nodes?
- **E_43** (B): Have you lost consciousness associated with violent and sustained muscle contractions or had an absence episode?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_74** (B): Have you noticed a diffuse (widespread) redness in one or both eyes?
- **E_129** (B): Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?
- **E_130** (C): What color is the rash?
- **E_131** (C): Do your lesions peel off?
- **E_132** (C): Is the rash swollen?
- **E_133** (M): Where is the affected region located?
- **E_134** (C): How intense is the pain caused by the rash?
- **E_135** (C): Is the lesion (or are the lesions) larger than 1cm?
- … (2 more omitted for brevity)

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_70** (B): Are you significantly overweight compared to people of the same height as you?
- **E_198** (B): Do you work in agriculture?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.