# HIV (initial infection)

**Overview:** HIV initial (acute) infection occurs 2–4 weeks after exposure to HIV and represents the acute retroviral syndrome. It affects the immune system by targeting CD4+ T cells. It is caused by the human immunodeficiency virus transmitted through sexual contact, blood, or vertical transmission.

**Typical Presentation:** Presents with fever, sore throat, lymphadenopathy, rash, myalgia, and fatigue — resembling mononucleosis. Mucocutaneous ulcers and weight loss may occur. Symptoms are often dismissed as a viral illness.

**Key Distinguishing Features:** Distinguished from EBV mononucleosis by the presence of mucocutaneous ulcers and risk factor history (unprotected sex, IV drug use). A 4th-generation HIV Ag/Ab combo test detects acute infection earlier than antibody-only tests.

**Severity & Urgency:** High — Early detection allows prompt treatment, improving long-term outcomes significantly.

**Sources:** [NCBI Bookshelf: HIV Disease, StatPearls] [PMID: 30480890]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `B20`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_9** (B): Do you have swollen or painful lymph nodes?
- **E_50** (B): Have you had significantly increased sweating?
- **E_51** (B): Have you had diarrhea or an increase in stool frequency?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_88** (B): Do you feel so tired that you are unable to do your usual activities or are you stuck in your bed all day long?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_97** (B): Do you have a sore throat?
- **E_129** (B): Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?
- **E_130** (C): What color is the rash?
- **E_131** (C): Do your lesions peel off?
- **E_132** (C): Is the rash swollen?
- **E_133** (M): Where is the affected region located?
- … (6 more omitted for brevity)

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_27** (B): Have you ever had a sexually transmitted infection?
- **E_61** (B): Are you currently using intravenous drugs?
- **E_115** (B): Have you had unprotected sex with more than one partner in the last 6 months?
- **E_189** (B): Have you had sexual intercourse with an HIV-positive partner in the past 12 months?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.