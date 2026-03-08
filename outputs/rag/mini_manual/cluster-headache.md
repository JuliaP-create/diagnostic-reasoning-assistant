# Cluster headache

**Overview:** Cluster headache is a primary headache disorder involving severe unilateral pain, typically periorbital or temporal, occurring in clusters (bouts) lasting weeks to months. It is caused by dysfunction of the trigeminovascular system and hypothalamus. It affects the nervous system.

**Typical Presentation:** Excruciating unilateral headache lasting 15–180 minutes, occurring up to 8 times daily, often at the same time each day. Accompanied by ipsilateral cranial autonomic features: tearing, conjunctival injection, nasal congestion, ptosis, and miosis. Patients are characteristically restless and agitated.

**Key Distinguishing Features:** Distinguished from migraine by shorter duration, extreme restlessness (migraine patients prefer stillness), and prominent unilateral autonomic features. Distinguished from paroxysmal hemicrania by longer attack duration and response to oxygen/triptans.

**Severity & Urgency:** Moderate — Intensely painful but not life-threatening; described as one of the most severe pain conditions known.

**Sources:** [PMC5909131] [PMC10957682]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `g44.009`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_127** (B): Do you feel that your eyes produce excessive tears?
- **E_176** (B): Did you previously, or do you currently, have any weakness/paralysis in one or more of your limbs or in your face?
- **E_181** (B): Do you have nasal congestion or a clear runny nose?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_25** (B): Have any of your family members been diagnosed with cluster headaches?
- **E_78** (B): Do you drink alcohol excessively or do you have an addiction to alcohol?
- **E_184** (B): Do you take medication that dilates your blood vessels?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.