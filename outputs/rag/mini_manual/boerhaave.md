# Boerhaave

**Overview:** Boerhaave syndrome is a spontaneous (non-iatrogenic) transmural perforation of the esophagus, typically caused by forceful vomiting or retching. It affects the gastrointestinal system and mediastinum. It is the most lethal perforation of the GI tract, with high mortality if untreated.

**Typical Presentation:** Severe retrosternal/epigastric pain following forceful vomiting, often with subcutaneous emphysema. The Mackler triad (vomiting, chest pain, subcutaneous emphysema) is classic but not always complete. Hamman's crunch (mediastinal crackling) may be auscultated.

**Key Distinguishing Features:** Distinguished from MI by history of vomiting preceding pain and subcutaneous emphysema. Distinguished from perforated peptic ulcer by chest rather than abdominal predominance and pneumomediastinum on imaging.

**Severity & Urgency:** Critical — Universally fatal if untreated; requires emergent surgical repair or aggressive conservative management.

**Sources:** [NCBI Bookshelf: Boerhaave Syndrome, NBK430808] [PMC4215748]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `K22.3`
- DDXPlus severity (dataset field): `2`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_148** (B): Are you feeling nauseous or do you feel like vomiting?
- **E_210** (B): Have you recently thrown up blood or something resembling coffee beans?
- **E_211** (B): Have you vomited several times or have you made several efforts to vomit?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_78** (B): Do you drink alcohol excessively or do you have an addiction to alcohol?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.