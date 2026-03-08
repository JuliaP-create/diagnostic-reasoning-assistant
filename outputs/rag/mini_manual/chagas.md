# Chagas

**Overview:** Chagas disease is a tropical parasitic infection caused by Trypanosoma cruzi, transmitted primarily by triatomine bugs ('kissing bugs'). It is endemic in Latin America. It affects the cardiovascular and gastrointestinal systems in its chronic phase.

**Typical Presentation:** Acute phase: fever, malaise, facial swelling (Romaña sign — unilateral periorbital edema), lymphadenopathy, and a skin lesion (chagoma) at the bite site. Chronic phase (years later): cardiomyopathy (heart failure, arrhythmias, sudden death) and megaesophagus/megacolon.

**Key Distinguishing Features:** Distinguished from other causes of dilated cardiomyopathy by epidemiologic exposure (Latin America), right bundle branch block and left anterior fascicular block on ECG, and positive T. cruzi serology. Romaña sign is pathognomonic for acute infection.

**Severity & Urgency:** Moderate to High — Acute phase is usually mild, but chronic Chagas cardiomyopathy is a major cause of heart failure and sudden death in endemic regions.

**Sources:** [PMC8716970] [WHO: Chagas Disease Fact Sheet]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `B57`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_9** (B): Do you have swollen or painful lymph nodes?
- **E_51** (B): Have you had diarrhea or an increase in stool frequency?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_148** (B): Are you feeling nauseous or do you feel like vomiting?
- **E_151** (B): Do you have swelling in one or more areas of your body?
- **E_152** (M): Where is the swelling located?
- **E_174** (B): Have you been unintentionally losing weight or have you lost your appetite?
- **E_175** (B): Have you noticed any new fatigue, generalized and vague discomfort, diffuse (widespread) muscle aches or a change in your general well-being related to your consultation today?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.