# Spontaneous rib fracture

**Overview:** A spontaneous rib fracture occurs without significant trauma, caused by repetitive stress (severe coughing), osteoporosis, pathologic bone weakening (metastases, corticosteroid use), or radiation therapy. It affects the musculoskeletal system, specifically the thoracic cage.

**Typical Presentation:** Localized chest wall pain that worsens with deep breathing, coughing, and movement. Point tenderness over the fracture site is characteristic. May follow a bout of severe coughing (pertussis, chronic bronchitis) or occur in patients with known osteoporosis.

**Key Distinguishing Features:** Distinguished from pleuritic chest pain (PE, pneumonia) by point tenderness reproducible on palpation. Distinguished from costochondritis by location away from costochondral junctions. Imaging (X-ray or CT) confirms the fracture.

**Severity & Urgency:** Low to Moderate — Usually managed conservatively with analgesia; underlying causes (metastases, osteoporosis) require investigation.

**Sources:** [NCBI Bookshelf: Rib Fracture, NBK541020] [PMC4577345]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `S22.9`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_151** (B): Do you have swelling in one or more areas of your body?
- **E_201** (B): Do you have a cough?
- **E_203** (B): Do you have intense coughing fits?
- **E_216** (B): Do you have pain that is increased with movement?
- **E_220** (B): Do you have pain that is increased when you breathe in deeply?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_37** (B): Do you have metastatic cancer?
- **E_78** (B): Do you drink alcohol excessively or do you have an addiction to alcohol?
- **E_153** (B): Are you being treated for osteoporosis?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.