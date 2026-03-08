# Inguinal hernia

**Overview:** An inguinal hernia is a protrusion of abdominal contents through the inguinal canal. It can be indirect (through the internal ring, congenital) or direct (through the floor of the canal, acquired). It affects the abdominal wall and groin region, predominantly in males.

**Typical Presentation:** A visible or palpable bulge in the groin that increases with standing, coughing, or straining, and often reduces when lying down. Aching discomfort in the groin is common. Pain worsens with activity and improves with rest.

**Key Distinguishing Features:** Distinguished from femoral hernia by location above the inguinal ligament (femoral is below). Distinguished from lymphadenopathy by a positive cough impulse and reducibility. Strangulation causes acute, severe pain with nausea and requires emergent surgery.

**Severity & Urgency:** Low to High — Uncomplicated hernias are low severity; strangulated hernias are surgical emergencies.

**Sources:** [PMC2223000] [AAFP: Inguinal Hernias, 2020]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `K40`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_30** (B): Do you feel your abdomen is bloated or distended (swollen due to pressure from inside)?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_129** (B): Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?
- **E_130** (C): What color is the rash?
- **E_131** (C): Do your lesions peel off?
- **E_132** (C): Is the rash swollen?
- **E_133** (M): Where is the affected region located?
- **E_134** (C): How intense is the pain caused by the rash?
- **E_135** (C): Is the lesion (or are the lesions) larger than 1cm?
- **E_136** (C): How severe is the itching?
- **E_150** (B): Have you been able to pass stools or gas since your symptoms increased?
- **E_203** (B): Do you have intense coughing fits?
- … (1 more omitted for brevity)

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_70** (B): Are you significantly overweight compared to people of the same height as you?
- **E_160** (B): Were you born prematurely or did you suffer any complication at birth?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.