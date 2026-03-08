# Guillain-Barré syndrome

**Overview:** Guillain-Barré syndrome (GBS) is an acute autoimmune disorder in which the immune system attacks the peripheral nerves. It is usually triggered by a preceding infection (Campylobacter jejuni, EBV, influenza). It affects the peripheral nervous system, causing rapidly progressive weakness.

**Typical Presentation:** Ascending, symmetric muscle weakness starting in the legs and progressing upward over days. Deep tendon reflexes are diminished or absent. Paresthesias, back pain, and autonomic dysfunction (blood pressure instability, tachycardia) may accompany weakness.

**Key Distinguishing Features:** Distinguished from transverse myelitis by absent reflexes (rather than hyperreflexia) and from myasthenia gravis by ascending pattern and areflexia. CSF shows elevated protein with normal cell count (albuminocytologic dissociation).

**Severity & Urgency:** High — Up to 25% of patients require mechanical ventilation; early treatment with IVIG or plasmapheresis improves outcomes.

**Sources:** [PMC4809704] [PMC11235944]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `G61.0`
- DDXPlus severity (dataset field): `2`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_83** (B): Have you noticed weakness in your facial muscles and/or eyes?
- **E_84** (B): Do you feel weakness in both arms and/or both legs?
- **E_93** (B): Do you have numbness, loss of sensation or tingling in the feet?
- **E_156** (B): Have you had weakness or paralysis on one side of the face, which may still be present or completely resolved?
- **E_157** (B): Have you recently had numbness, loss of sensation or tingling, in both arms and legs and around your mouth?
- **E_176** (B): Did you previously, or do you currently, have any weakness/paralysis in one or more of your limbs or in your face?
- **E_177** (B): Do you currently, or did you ever, have numbness, loss of sensitivity or tingling anywhere on your body?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_0** (B): Have you recently had a viral infection?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.