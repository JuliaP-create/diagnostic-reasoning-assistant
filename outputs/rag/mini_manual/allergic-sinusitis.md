# Allergic sinusitis

**Overview:** Allergic sinusitis is inflammation of the paranasal sinuses caused by allergic reactions to environmental allergens (dust, pollen, mold). It affects the sinonasal system and often coexists with allergic rhinitis. Chronic mucosal edema impairs sinus drainage.

**Typical Presentation:** Nasal congestion, clear rhinorrhea, sneezing, facial pressure, and post-nasal drip are typical. Symptoms are bilateral and correlate with allergen exposure. Allergic shiners (dark circles under eyes) and pale boggy turbinates may be present.

**Key Distinguishing Features:** Distinguished from acute bacterial sinusitis by clear (not purulent) discharge, bilateral symptoms, and seasonal or exposure-related pattern. Distinguished from URTI by chronicity and allergen correlation.

**Severity & Urgency:** Low — Chronic but manageable with antihistamines, nasal corticosteroids, and allergen avoidance.

**Sources:** [NCBI Bookshelf: Sinusitis, StatPearls] [PMID: 30856035]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `J30`
- DDXPlus severity (dataset field): `4`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_169** (B): Is your nose or the back of your throat itchy?
- **E_170** (B): Do you have severe itching in one or both eyes?
- **E_181** (B): Do you have nasal congestion or a clear runny nose?
- **E_201** (B): Do you have a cough?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_86** (B): Do you have any close family members who suffer from allergies (any type), hay fever or eczema?
- **E_87** (B): Do you have any family members who have asthma?
- **E_124** (B): Do you have asthma or have you ever had to use a bronchodilator in the past?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_207** (B): Do you live in in a big city?
- **E_226** (B): Are you more likely to develop common allergies than the general population?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.