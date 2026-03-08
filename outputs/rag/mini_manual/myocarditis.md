# Myocarditis

**Overview:** Myocarditis is inflammation of the myocardium, most commonly caused by viral infections (Coxsackievirus, parvovirus B19, SARS-CoV-2). It can also result from autoimmune conditions or toxins. It affects the cardiovascular system and can cause ventricular dysfunction.

**Typical Presentation:** Chest pain (85–95% of cases), fever (~65%), and dyspnea in a young patient with a recent viral illness. May mimic acute MI with troponin elevation but normal coronary arteries. Arrhythmias and heart failure can occur. Fulminant myocarditis presents with cardiogenic shock.

**Key Distinguishing Features:** Distinguished from acute MI by younger age, recent viral prodrome, and normal coronary angiography. Distinguished from pericarditis by troponin elevation and ventricular dysfunction on echocardiography. Cardiac MRI (Lake Louise criteria) is the non-invasive gold standard.

**Severity & Urgency:** Moderate to Critical — Many cases are self-limiting, but fulminant myocarditis can be rapidly fatal without mechanical circulatory support.

**Sources:** [PMC11873950] [PMC8439515]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `I51.4`
- DDXPlus severity (dataset field): `2`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_64** (B): Do you feel out of breath with minimal physical effort?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_114** (B): Are you more irritable or has your mood been very unstable recently?
- **E_155** (B): Do you feel your heart is beating fast (racing), irregularly (missing a beat) or do you feel palpitations?
- **E_175** (B): Have you noticed any new fatigue, generalized and vague discomfort, diffuse (widespread) muscle aches or a change in your general well-being related to your consultation today?
- **E_217** (B): Are your symptoms worse when lying down and alleviated while sitting up?
- **E_218** (B): Do you have symptoms that are increased with physical exertion but alleviated with rest?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_0** (B): Have you recently had a viral infection?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.