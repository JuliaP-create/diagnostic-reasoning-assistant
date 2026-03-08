# Anaphylaxis

**Overview:** Anaphylaxis is a severe, potentially life-threatening systemic allergic reaction caused by massive IgE-mediated mast cell degranulation. It affects the cardiovascular, respiratory, gastrointestinal, and integumentary systems. Common triggers include foods, insect stings, and medications.

**Typical Presentation:** Rapid onset (minutes to hours) of urticaria, angioedema, wheezing, dyspnea, hypotension, tachycardia, and GI symptoms (nausea, vomiting). Sense of impending doom is characteristic. Biphasic reactions can occur hours after initial resolution.

**Key Distinguishing Features:** Distinguished from panic attack by presence of urticaria, angioedema, and hypotension. Distinguished from scombroid poisoning by absence of recent fish ingestion and by allergen exposure history.

**Severity & Urgency:** Critical — Requires immediate epinephrine; untreated anaphylaxis can cause death within minutes.

**Sources:** [NCBI Bookshelf: Anaphylaxis, StatPearls] [PMID: 29489170]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `T78.0`
- DDXPlus severity (dataset field): `1`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_42** (B): Have you been in contact with or ate something that you have an allergy to?
- **E_51** (B): Have you had diarrhea or an increase in stool frequency?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_82** (B): Do you feel lightheaded and dizzy or do you feel like you are about to faint?
- **E_129** (B): Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?
- **E_130** (C): What color is the rash?
- **E_131** (C): Do your lesions peel off?
- **E_132** (C): Is the rash swollen?
- **E_133** (M): Where is the affected region located?
- **E_134** (C): How intense is the pain caused by the rash?
- **E_135** (C): Is the lesion (or are the lesions) larger than 1cm?
- … (7 more omitted for brevity)

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_12** (B): Do you have a known severe food allergy?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_226** (B): Are you more likely to develop common allergies than the general population?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.