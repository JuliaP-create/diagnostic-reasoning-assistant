# Pancreatic neoplasm

**Overview:** Pancreatic neoplasm refers to tumors of the pancreas, with pancreatic ductal adenocarcinoma (PDAC) being the most common and lethal type (>90% of cases). It affects the gastrointestinal and hepatobiliary systems. Risk factors include smoking, chronic pancreatitis, diabetes, and family history.

**Typical Presentation:** Insidious onset of painless jaundice (head tumors), weight loss, and new-onset diabetes. Epigastric pain radiating to the back is common with body/tail tumors. Courvoisier sign (painless, palpable gallbladder) may be present.

**Key Distinguishing Features:** Distinguished from choledocholithiasis by painless jaundice and mass on imaging. Distinguished from chronic pancreatitis by progressive weight loss and CA 19-9 elevation. The 5-year survival rate is only 5–15%.

**Severity & Urgency:** High — Most cases are diagnosed at an advanced stage; only ~20% are surgically resectable at diagnosis.

**Sources:** [NCBI Bookshelf: Pancreatic Cancer, NBK518996] [PMC9827589]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `c25`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_51** (B): Have you had diarrhea or an increase in stool frequency?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_89** (B): Do you constantly feel fatigued or do you have non-restful sleep?
- **E_129** (B): Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?
- **E_130** (C): What color is the rash?
- **E_131** (C): Do your lesions peel off?
- **E_132** (C): Is the rash swollen?
- **E_133** (M): Where is the affected region located?
- **E_134** (C): How intense is the pain caused by the rash?
- **E_135** (C): Is the lesion (or are the lesions) larger than 1cm?
- **E_136** (C): How severe is the itching?
- **E_148** (B): Are you feeling nauseous or do you feel like vomiting?
- … (3 more omitted for brevity)

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_6** (B): Do you have chronic pancreatitis?
- **E_69** (B): Do you have diabetes?
- **E_70** (B): Are you significantly overweight compared to people of the same height as you?
- **E_79** (B): Do you smoke cigarettes?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_223** (B): Are there members of your family who have been diagnosed with pancreatic cancer?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.