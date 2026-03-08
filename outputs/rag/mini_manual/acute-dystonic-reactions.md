# Acute dystonic reactions

**Overview:** Acute dystonic reactions are involuntary sustained muscle contractions causing abnormal postures. They are most commonly caused by dopamine-blocking medications (antipsychotics, metoclopramide). They affect the nervous system, particularly the extrapyramidal pathways.

**Typical Presentation:** Sudden onset of neck twisting (torticollis), jaw clenching (trismus), tongue protrusion, oculogyric crisis (eyes rolling upward), or opisthotonus. Onset is typically within hours to days of starting or increasing an offending medication.

**Key Distinguishing Features:** Distinguished from seizures by preserved consciousness and from tetanus by recent medication exposure. Rapid resolution with IV diphenhydramine or benztropine is both diagnostic and therapeutic.

**Severity & Urgency:** Moderate — Rarely life-threatening but very distressing; laryngeal dystonia can compromise the airway.

**Sources:** [NCBI Bookshelf: Acute Dystonic Reactions, StatPearls] [PMID: 29630260]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `G24.02`
- DDXPlus severity (dataset field): `2`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_128** (B): Have you ever felt like you were suffocating for a very short time associated with inability to breathe or speak?
- **E_168** (B): Do you have trouble keeping your tongue in your mouth?
- **E_172** (B): Do you have a hard time opening/raising one or both eyelids?
- **E_180** (B): Are you unable to control the direction of your eyes?
- **E_192** (B): Do you feel that muscle spasms or soreness in your neck are keeping you from turning your head to one side?
- **E_193** (B): Do you have annoying muscle spasms in your face, neck or any other part of your body?
- **E_205** (B): Do you suddenly have difficulty or an inability to open your mouth or have jaw pain when opening it?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_15** (B): Have you started or taken any antipsychotic medication within the last 7 days?
- **E_62** (B): Do you regularly take stimulant drugs?
- **E_147** (B): Have you been treated in hospital recently for nausea, agitation, intoxication or aggressive behavior and received medication via an intravenous or intramuscular route?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.