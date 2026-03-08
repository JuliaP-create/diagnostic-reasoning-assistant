# Acute COPD exacerbation / infection

**Overview:** An acute exacerbation of COPD (AECOPD) is a sustained worsening of respiratory symptoms beyond normal day-to-day variation. Most are triggered by viral or bacterial respiratory infections (2/3 of cases) or air pollution. It affects the lower respiratory system in patients with pre-existing COPD.

**Typical Presentation:** Increased dyspnea, increased sputum volume and purulence, and worsening cough. Wheezing, accessory muscle use, and cyanosis may be present. Severe exacerbations cause hypercapnic respiratory failure with altered mental status.

**Key Distinguishing Features:** Distinguished from acute asthma by older age, smoking history, and incomplete reversibility with bronchodilators. Distinguished from acute pulmonary edema by absence of orthopnea, pink sputum, and bilateral crackles. Requires pre-existing COPD diagnosis.

**Severity & Urgency:** Moderate to High — Leading cause of death in COPD patients; severe exacerbations require hospitalization and may need mechanical ventilation.

**Sources:** [PMC2645331] [PMC7423341]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `j44.1`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_77** (B): Do you have a cough that produces colored or more abundant sputum than usual?
- **E_201** (B): Do you have a cough?
- **E_214** (B): Have you noticed a wheezing sound when you exhale?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_31** (B): Do you have severe Chronic Obstructive Pulmonary Disease (COPD)?
- **E_72** (B): Have you had one or several flare ups of chronic obstructive pulmonary disease (COPD) in the past year?
- **E_79** (B): Do you smoke cigarettes?
- **E_123** (B): Do you have a chronic obstructive pulmonary disease (COPD)?
- **E_125** (B): Have you ever been diagnosed with gastroesophageal reflux?
- **E_198** (B): Do you work in agriculture?
- **E_199** (B): Do you work in construction?
- **E_200** (B): Do you work in the mining sector?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.