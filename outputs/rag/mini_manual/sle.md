# SLE

**Overview:** Systemic lupus erythematosus (SLE) is a chronic autoimmune disease causing widespread inflammation affecting multiple organ systems. It is characterized by autoantibodies (especially anti-dsDNA and anti-Smith) and immune complex deposition. It predominantly affects women of reproductive age.

**Typical Presentation:** Fatigue, joint pain, malar (butterfly) rash, photosensitivity, oral ulcers, and hair loss are common. Renal involvement (lupus nephritis), serositis (pleuritis, pericarditis), and hematologic cytopenias may occur. Symptoms wax and wane in flares and remissions.

**Key Distinguishing Features:** Distinguished from rheumatoid arthritis by malar rash, multi-organ involvement, and positive ANA/anti-dsDNA antibodies. Distinguished from fibromyalgia by objective laboratory and organ findings rather than just pain and fatigue.

**Severity & Urgency:** Moderate to High — Variable course; lupus nephritis and CNS lupus can be life-threatening. Requires long-term immunosuppressive therapy.

**Sources:** [NCBI Bookshelf: SLE, NBK535405] [PMC3391953]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `M34`
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
- **E_89** (B): Do you constantly feel fatigued or do you have non-restful sleep?
- **E_129** (B): Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?
- **E_130** (C): What color is the rash?
- **E_131** (C): Do your lesions peel off?
- **E_132** (C): Is the rash swollen?
- **E_133** (M): Where is the affected region located?
- **E_135** (C): Is the lesion (or are the lesions) larger than 1cm?
- **E_136** (C): How severe is the itching?
- **E_151** (B): Do you have swelling in one or more areas of your body?
- **E_206** (B): Do you have painful mouth ulcers or sores?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_3** (B): Have you ever had a pericarditis?
- **E_11** (B): Have you breastfed one of your children for more than 9 months?
- **E_79** (B): Do you smoke cigarettes?
- **E_102** (B): Are you consulting because you have high blood pressure?
- **E_141** (B): Did you have your first menstrual period before the age of 12?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.