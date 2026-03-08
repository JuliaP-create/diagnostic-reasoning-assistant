# Acute otitis media

**Overview:** Acute otitis media (AOM) is a middle ear infection most common in children aged 6–24 months. It is caused by bacteria (Streptococcus pneumoniae, Haemophilus influenzae) or viruses following URTI. It affects the middle ear space behind the tympanic membrane.

**Typical Presentation:** Ear pain (otalgia), fever, irritability (in infants), and hearing difficulty are typical. Otoscopy reveals a bulging, erythematous tympanic membrane, often with effusion. In children, ear tugging may be the only sign.

**Key Distinguishing Features:** Distinguished from otitis externa (swimmer's ear) by pain with tympanic membrane changes rather than canal tenderness. Distinguished from otitis media with effusion by presence of acute symptoms (pain, fever).

**Severity & Urgency:** Low to Moderate — Usually self-limiting or responsive to antibiotics; rare complications include mastoiditis.

**Sources:** [NCBI Bookshelf: Acute Otitis Media, StatPearls] [PMID: 29262176]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `H66.90`
- DDXPlus severity (dataset field): `4`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_114** (B): Are you more irritable or has your mood been very unstable recently?
- **E_181** (B): Do you have nasal congestion or a clear runny nose?
- **E_201** (B): Do you have a cough?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_1** (B): Are you currently being treated or have you recently been treated with an oral antibiotic for an ear infection?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_209** (B): Are your vaccinations up to date?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.