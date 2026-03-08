# Scombroid food poisoning

**Overview:** Scombroid food poisoning is a histamine toxicity caused by eating improperly stored fish (tuna, mackerel, mahi-mahi) that has undergone bacterial histamine production. It is not a true allergy but mimics an allergic reaction. It affects the integumentary, GI, and cardiovascular systems.

**Typical Presentation:** Symptoms begin 10–90 minutes after fish ingestion: facial flushing, urticaria, headache, palpitations, abdominal cramps, nausea, vomiting, and diarrhea. The fish may have tasted peppery or metallic. Symptoms resolve within 3–36 hours.

**Key Distinguishing Features:** Distinguished from anaphylaxis by the temporal relationship to fish consumption and absence of a known allergen sensitivity. Distinguished from ciguatera by prominent flushing and absence of neurologic symptoms (paresthesias, temperature reversal).

**Severity & Urgency:** Low to Moderate — Usually self-limiting; responds rapidly to antihistamines (H1 + H2 blockers). Severe cases can cause hypotension.

**Sources:** [PMC4273511] [PMC3314039]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `T61.1`
- DDXPlus severity (dataset field): `2`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_51** (B): Have you had diarrhea or an increase in stool frequency?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_82** (B): Do you feel lightheaded and dizzy or do you feel like you are about to faint?
- **E_92** (B): Did your cheeks suddenly turn red?
- **E_129** (B): Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?
- **E_130** (C): What color is the rash?
- **E_131** (C): Do your lesions peel off?
- **E_132** (C): Is the rash swollen?
- **E_133** (M): Where is the affected region located?
- **E_134** (C): How intense is the pain caused by the rash?
- **E_135** (C): Is the lesion (or are the lesions) larger than 1cm?
- **E_136** (C): How severe is the itching?
- **E_148** (B): Are you feeling nauseous or do you feel like vomiting?
- **E_155** (B): Do you feel your heart is beating fast (racing), irregularly (missing a beat) or do you feel palpitations?
- **E_214** (B): Have you noticed a wheezing sound when you exhale?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_187** (B): Did you eat dark-fleshed fish (such as tuna) or Swiss cheese before the reaction occurred?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.