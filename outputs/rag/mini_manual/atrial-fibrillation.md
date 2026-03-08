# Atrial fibrillation

**Overview:** Atrial fibrillation (AFib) is the most common sustained cardiac arrhythmia, characterized by chaotic, irregular electrical activity in the atria. It results in an irregularly irregular heart rhythm and impaired cardiac output. Major risk factors include hypertension, heart failure, and advancing age.

**Typical Presentation:** Palpitations, dyspnea, fatigue, lightheadedness, and chest discomfort are common. Some patients are asymptomatic and diagnosed incidentally. Physical exam reveals an irregularly irregular pulse, often with a rapid ventricular rate (110–140 bpm).

**Key Distinguishing Features:** Distinguished from other supraventricular tachycardias by the irregularly irregular rhythm and absence of P-waves on ECG. Distinguished from atrial flutter by absence of sawtooth flutter waves.

**Severity & Urgency:** Moderate to High — Major risk of stroke; requires anticoagulation based on CHA2DS2-VASc score and rate or rhythm control.

**Sources:** [NCBI Bookshelf: Atrial Fibrillation, NBK526072] [PMC10684204]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `I48.91`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_76** (B): Do you feel slightly dizzy or lightheaded?
- **E_155** (B): Do you feel your heart is beating fast (racing), irregularly (missing a beat) or do you feel palpitations?
- **E_164** (B): Do you feel your heart is beating very irregularly or in a disorganized pattern?
- **E_218** (B): Do you have symptoms that are increased with physical exertion but alleviated with rest?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_19** (B): Have you been diagnosed with hyperthyroidism?
- **E_22** (B): Do you have a known issue with one of your heart valves?
- **E_31** (B): Do you have severe Chronic Obstructive Pulmonary Disease (COPD)?
- **E_69** (B): Do you have diabetes?
- **E_70** (B): Are you significantly overweight compared to people of the same height as you?
- **E_104** (B): Do you have high blood pressure or do you take medications to treat high blood pressure?
- **E_105** (B): Have you ever had a heart attack or do you have angina (chest pain)?
- **E_139** (B): Do you have a known heart defect?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.