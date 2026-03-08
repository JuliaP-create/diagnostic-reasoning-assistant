# Larygospasm

**Overview:** Laryngospasm is an involuntary spasm of the laryngeal muscles causing partial or complete closure of the vocal cords, resulting in acute airway obstruction. Common triggers include gastroesophageal reflux, airway irritation, post-extubation, and aspiration. It affects the upper airway.

**Typical Presentation:** Sudden inability to breathe or speak, inspiratory stridor, and a sensation of choking or suffocation. Episodes are typically brief (seconds to a minute) but terrifying. Post-operative laryngospasm occurs after extubation, especially in children with URTI symptoms.

**Key Distinguishing Features:** Distinguished from asthma by acute upper airway obstruction (inspiratory stridor) rather than lower airway obstruction (expiratory wheezing). Distinguished from anaphylaxis by absence of urticaria and angioedema. Episodes are self-limiting but can be life-threatening.

**Severity & Urgency:** Moderate to High — Usually resolves spontaneously in seconds, but prolonged laryngospasm can cause hypoxia, loss of consciousness, and death if not managed emergently.

**Sources:** [PMC10363359] [PMC7361892]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `J38.5`
- DDXPlus severity (dataset field): `1`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_194** (B): Have you noticed a high pitched sound when breathing in?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_79** (B): Do you smoke cigarettes?
- **E_116** (B): Have you had a cold in the last 2 weeks?
- **E_124** (B): Do you have asthma or have you ever had to use a bronchodilator in the past?
- **E_125** (B): Have you ever been diagnosed with gastroesophageal reflux?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_222** (B): Are you exposed to secondhand cigarette smoke on a daily basis?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.