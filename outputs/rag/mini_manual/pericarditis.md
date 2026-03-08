# Pericarditis

**Overview:** Pericarditis is inflammation of the pericardium, the double-layered sac surrounding the heart. It is most commonly caused by viral infections (Coxsackievirus, echovirus) but can be autoimmune, post-MI, or idiopathic. It affects the cardiovascular system.

**Typical Presentation:** Sharp, pleuritic chest pain that worsens with inspiration and lying flat, and improves when sitting up and leaning forward. A pericardial friction rub is the pathognomonic physical finding. Diffuse ST elevation and PR depression on ECG are classic.

**Key Distinguishing Features:** Distinguished from STEMI by diffuse (not territorial) ST elevation, PR depression, and pain that changes with position. Distinguished from PE by friction rub and ECG pattern.

**Severity & Urgency:** Moderate — Usually self-limiting with NSAIDs and colchicine, but cardiac tamponade is a rare life-threatening complication.

**Sources:** [NCBI Bookshelf: Pericarditis, StatPearls] [PMID: 28722854]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `I30`
- DDXPlus severity (dataset field): `4`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_155** (B): Do you feel your heart is beating fast (racing), irregularly (missing a beat) or do you feel palpitations?
- **E_217** (B): Are your symptoms worse when lying down and alleviated while sitting up?
- **E_220** (B): Do you have pain that is increased when you breathe in deeply?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_0** (B): Have you recently had a viral infection?
- **E_3** (B): Have you ever had a pericarditis?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.