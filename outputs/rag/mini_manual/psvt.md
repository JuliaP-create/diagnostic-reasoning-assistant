# PSVT

**Overview:** Paroxysmal supraventricular tachycardia (PSVT) is an intermittent rapid heart rhythm originating above the ventricles, most commonly caused by re-entrant circuits (AVNRT or AVRT). It affects the cardiovascular system. It typically occurs in younger, otherwise healthy individuals.

**Typical Presentation:** Sudden-onset palpitations with heart rate 150–250 bpm that start and stop abruptly. Associated with chest discomfort, dyspnea, lightheadedness, and sometimes syncope. Polyuria may follow an episode due to ANP release.

**Key Distinguishing Features:** Distinguished from atrial fibrillation by regular (not irregular) rhythm on ECG. Distinguished from sinus tachycardia by abrupt onset/offset and rate typically >150 bpm. Responsive to vagal maneuvers (Valsalva) and IV adenosine.

**Severity & Urgency:** Low to Moderate — Rarely life-threatening in structurally normal hearts; curative catheter ablation is available.

**Sources:** [PMC7673777] [NCBI Bookshelf: PSVT, NBK507699]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `I47.1`
- DDXPlus severity (dataset field): `2`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_16** (B): Do you feel anxious?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_76** (B): Do you feel slightly dizzy or lightheaded?
- **E_82** (B): Do you feel lightheaded and dizzy or do you feel like you are about to faint?
- **E_155** (B): Do you feel your heart is beating fast (racing), irregularly (missing a beat) or do you feel palpitations?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_35** (B): Do you regularly drink coffee or tea?
- **E_60** (B): Do you consume energy drinks regularly?
- **E_62** (B): Do you regularly take stimulant drugs?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_213** (B): Have you recently taken decongestants or other substances that may have stimulant effects?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.