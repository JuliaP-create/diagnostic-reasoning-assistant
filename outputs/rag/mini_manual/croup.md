# Croup

**Overview:** Croup (acute laryngotracheobronchitis) is a common childhood respiratory illness characterized by subglottic airway inflammation. It is usually caused by parainfluenza viruses (types 1 and 3). It primarily affects children aged 6 months to 3 years.

**Typical Presentation:** Preceded by 1–2 days of URTI symptoms, then develops characteristic barking (seal-like) cough, inspiratory stridor, and hoarseness, typically worse at night. Low-grade fever is common. Symptoms are aggravated by crying and agitation.

**Key Distinguishing Features:** Distinguished from epiglottitis by barking cough (absent in epiglottitis), lower fever, and gradual onset. Distinguished from foreign body aspiration by bilateral symptoms and URTI prodrome. Neck X-ray shows 'steeple sign' (subglottic narrowing).

**Severity & Urgency:** Low to Moderate — Most cases are mild and self-limiting; severe croup with stridor at rest requires nebulized epinephrine and systemic corticosteroids.

**Sources:** [Merck Manual: Croup] [PMC7173542]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `J05.0`
- DDXPlus severity (dataset field): `2`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_181** (B): Do you have nasal congestion or a clear runny nose?
- **E_190** (B): Have you noticed that you produce more saliva than usual?
- **E_194** (B): Have you noticed a high pitched sound when breathing in?
- **E_202** (B): Does the person have a whooping cough?
- **E_219** (B): Are your symptoms more prominent at night?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_4** (B): Have you or any member of your family ever had croup?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_209** (B): Are your vaccinations up to date?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.