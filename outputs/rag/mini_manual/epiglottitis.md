# Epiglottitis

**Overview:** Epiglottitis is a rapidly progressive infection/inflammation of the epiglottis and surrounding supraglottic structures, which can cause life-threatening airway obstruction. In children, H. influenzae type b was the classic cause (now reduced by vaccination); in adults, various bacteria and viruses are causative.

**Typical Presentation:** Acute onset of severe sore throat (out of proportion to exam findings), high fever, drooling, dysphagia, and muffled ('hot potato') voice. Patients may adopt the tripod position (sitting upright, leaning forward). Stridor indicates impending airway obstruction.

**Key Distinguishing Features:** Distinguished from croup by absence of barking cough, older age, and more toxic appearance. Distinguished from acute laryngitis by severity and presence of drooling/dysphagia. Lateral neck X-ray shows 'thumbprint sign.'

**Severity & Urgency:** Critical — Medical emergency requiring immediate airway management; epiglottic abscess has 30% mortality.

**Sources:** [PMC7342809] [PMC3498669]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `J05.1`
- DDXPlus severity (dataset field): `2`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_33** (B): Do you have pain that improves when you lean forward?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_65** (B): Do you have difficulty swallowing, or have a feeling of discomfort/blockage when swallowing?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_190** (B): Have you noticed that you produce more saliva than usual?
- **E_194** (B): Have you noticed a high pitched sound when breathing in?
- **E_212** (B): Have you noticed that the tone of your voice has become deeper, softer or hoarse?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_62** (B): Do you regularly take stimulant drugs?
- **E_69** (B): Do you have diabetes?
- **E_78** (B): Do you drink alcohol excessively or do you have an addiction to alcohol?
- **E_104** (B): Do you have high blood pressure or do you take medications to treat high blood pressure?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_209** (B): Are your vaccinations up to date?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.