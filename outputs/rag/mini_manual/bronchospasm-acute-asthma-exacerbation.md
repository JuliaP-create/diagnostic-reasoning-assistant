# Bronchospasm / acute asthma exacerbation

**Overview:** An acute asthma exacerbation is a worsening of asthma symptoms caused by airway inflammation, bronchospasm, and mucus production. Triggers include allergens, infections, exercise, and irritants. It affects the lower respiratory system, causing reversible airway obstruction.

**Typical Presentation:** Acute dyspnea, wheezing, chest tightness, and cough. Accessory muscle use and inability to speak in full sentences indicate severity. Peak flow and FEV1 are significantly reduced. Severe cases may have silent chest (no air movement).

**Key Distinguishing Features:** Distinguished from COPD exacerbation by younger age, atopic history, and reversibility with bronchodilators. Distinguished from PE by bilateral wheezing and response to beta-agonists.

**Severity & Urgency:** Moderate to Critical — Status asthmaticus (refractory to bronchodilators) can be fatal without aggressive management including ventilation.

**Sources:** [PMC6780340] [PMC10856115]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `J45`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_201** (B): Do you have a cough?
- **E_214** (B): Have you noticed a wheezing sound when you exhale?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_46** (B): Have you had 2 or more asthma attacks in the past year?
- **E_87** (B): Do you have any family members who have asthma?
- **E_101** (B): Have you been hospitalized for an asthma attack in the past year?
- **E_116** (B): Have you had a cold in the last 2 weeks?
- **E_119** (B): Have you been diagnosed with chronic sinusitis?
- **E_124** (B): Do you have asthma or have you ever had to use a bronchodilator in the past?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_207** (B): Do you live in in a big city?
- **E_222** (B): Are you exposed to secondhand cigarette smoke on a daily basis?
- **E_226** (B): Are you more likely to develop common allergies than the general population?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.