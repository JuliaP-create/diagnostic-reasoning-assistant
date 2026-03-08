# Bronchiolitis

**Overview:** Bronchiolitis is an acute viral lower respiratory infection of the small airways (bronchioles) predominantly affecting infants under 2 years of age. Respiratory syncytial virus (RSV) is the most common cause. It is the leading cause of hospitalization in infants.

**Typical Presentation:** Begins with URTI symptoms (rhinorrhea, cough), then progresses to tachypnea, wheezing, crackles, nasal flaring, and intercostal retractions over 3–5 days. Poor feeding and irritability are common. Apnea can occur in premature infants.

**Key Distinguishing Features:** Distinguished from asthma by age (<2 years), first episode of wheezing, and viral prodrome. Distinguished from pneumonia by diffuse rather than focal findings. Diagnosis is clinical; routine imaging and lab tests are not recommended.

**Severity & Urgency:** Low to Moderate — Most cases are mild and self-limiting with supportive care; premature infants and those with underlying cardiopulmonary disease are at risk for severe disease.

**Sources:** [PMC4235450] [PMC7152281]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `j21`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_23** (B): Do you ever temporarily stop breathing while you’re asleep?
- **E_32** (B): Do you have a decrease in appetite?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_181** (B): Do you have nasal congestion or a clear runny nose?
- **E_201** (B): Do you have a cough?
- **E_214** (B): Have you noticed a wheezing sound when you exhale?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_48** (B): Do you live with 4 or more people?
- **E_142** (B): Does your mother suffer from asthma?
- **E_183** (B): Do you live in a rural area?
- **E_195** (B): Do you live in the suburbs?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_209** (B): Are your vaccinations up to date?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.