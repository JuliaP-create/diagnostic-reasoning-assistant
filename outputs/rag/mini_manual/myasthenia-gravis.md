# Myasthenia gravis

**Overview:** Myasthenia gravis (MG) is an autoimmune disorder in which antibodies (usually anti-AChR) attack the neuromuscular junction, impairing signal transmission. It affects the neuromuscular system. It can occur at any age but has bimodal peaks (young women, older men).

**Typical Presentation:** Fluctuating, fatigable muscle weakness that worsens with use and improves with rest. Ocular symptoms (ptosis, diplopia) are the most common initial presentation (~80%). Bulbar weakness (dysphagia, dysarthria) and limb weakness may follow. Myasthenic crisis causes respiratory failure.

**Key Distinguishing Features:** Distinguished from Lambert-Eaton syndrome by weakness that worsens (not improves) with activity. Distinguished from GBS by chronic fluctuating course rather than acute monophasic progression. Anti-AChR antibodies are positive in ~85% of generalized MG.

**Severity & Urgency:** Moderate to High — Manageable with treatment (pyridostigmine, immunosuppressants), but myasthenic crisis is a medical emergency.

**Sources:** [PMC2211463] [PMC8196750]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `G70.0`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_38** (B): Do you have pain or weakness in your jaw?
- **E_52** (B): Do you have the perception of seeing two images of a single object seen overlapping or adjacent to each other (double vision)?
- **E_63** (B): Do you have difficulty articulating words/speaking?
- **E_65** (B): Do you have difficulty swallowing, or have a feeling of discomfort/blockage when swallowing?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_84** (B): Do you feel weakness in both arms and/or both legs?
- **E_90** (B): Do your symptoms of muscle weakness increase with fatigue and/or stress?
- **E_172** (B): Do you have a hard time opening/raising one or both eyelids?
- **E_176** (B): Did you previously, or do you currently, have any weakness/paralysis in one or more of your limbs or in your face?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_28** (B): Are there any members of your family who have been diagnosed myasthenia gravis?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.