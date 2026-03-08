# Tuberculosis

**Overview:** Tuberculosis (TB) is a chronic infectious disease caused by Mycobacterium tuberculosis, primarily affecting the lungs but can involve any organ. It is transmitted via airborne droplets. Active pulmonary TB is a major global health concern.

**Typical Presentation:** Chronic productive cough (>2–3 weeks), hemoptysis, night sweats, low-grade fever, weight loss, and fatigue. Upper lobe cavitary lesions on chest X-ray are classic. Close contacts and immunocompromised individuals are at highest risk.

**Key Distinguishing Features:** Distinguished from pneumonia by chronic course, night sweats, and upper lobe predilection. Distinguished from sarcoidosis by caseating granulomas and positive AFB smear/culture. TB skin test or IGRA supports diagnosis.

**Severity & Urgency:** High — Contagious and can be fatal if untreated; multi-drug resistant TB is a growing global threat.

**Sources:** [NCBI Bookshelf: Tuberculosis, NBK441916] [CDC: TB Diagnosis]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `a15`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_45** (B): Have you been coughing up blood?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_162** (B): Have you had an involuntary weight loss over the last 3 months?
- **E_201** (B): Do you have a cough?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_2** (B): Are you infected with the human immunodeficiency virus (HIV)?
- **E_44** (B): Do you take corticosteroids?
- **E_61** (B): Are you currently using intravenous drugs?
- **E_69** (B): Do you have diabetes?
- **E_78** (B): Do you drink alcohol excessively or do you have an addiction to alcohol?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_208** (B): Is your BMI less than 18.5, or are you underweight?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.