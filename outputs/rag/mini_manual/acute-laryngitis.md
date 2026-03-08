# Acute laryngitis

**Overview:** Acute laryngitis is inflammation of the larynx, usually caused by viral upper respiratory infections, vocal strain, or irritant exposure. It affects the voice box and is the most common cause of hoarseness. The vocal cords become edematous and cannot vibrate normally.

**Typical Presentation:** Hoarseness or voice loss (dysphonia) is the hallmark symptom, accompanied by sore throat, dry cough, and throat-clearing sensation. Often follows or accompanies a URTI. Symptoms typically resolve within 1–2 weeks.

**Key Distinguishing Features:** Distinguished from epiglottitis by absence of dysphagia, drooling, and toxic appearance. Distinguished from laryngeal cancer by short duration and association with URTI.

**Severity & Urgency:** Low — Self-limiting; voice rest and hydration are the mainstay of treatment.

**Sources:** [NCBI Bookshelf: Laryngitis, StatPearls] [PMC7342809]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `J04.0`
- DDXPlus severity (dataset field): `4`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_201** (B): Do you have a cough?
- **E_212** (B): Have you noticed that the tone of your voice has become deeper, softer or hoarse?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_48** (B): Do you live with 4 or more people?
- **E_49** (B): Do you attend or work in a daycare?
- **E_79** (B): Do you smoke cigarettes?
- **E_116** (B): Have you had a cold in the last 2 weeks?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.