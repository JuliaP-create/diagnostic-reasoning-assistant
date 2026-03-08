# GERD

**Overview:** Gastroesophageal reflux disease (GERD) is a chronic condition where stomach acid frequently flows back into the esophagus, causing mucosal irritation. It affects the gastrointestinal system. It results from lower esophageal sphincter dysfunction.

**Typical Presentation:** Heartburn (retrosternal burning) and acid regurgitation are the cardinal symptoms, typically worsened by lying down or after meals. Atypical presentations include chronic cough, hoarseness, and chest pain mimicking cardiac disease.

**Key Distinguishing Features:** Distinguished from cardiac chest pain by its relationship to meals, relief with antacids, and absence of exertional triggers or ECG changes. Distinguished from esophageal cancer by endoscopic evaluation.

**Severity & Urgency:** Low to Moderate — Usually manageable with lifestyle changes and medication, but chronic untreated GERD can lead to Barrett esophagus.

**Sources:** [NCBI Bookshelf: Gastroesophageal Reflux Disease, StatPearls] [PMID: 30247884]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `K21`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_140** (B): Have you recently had stools that were black (like coal)?
- **E_173** (B): Do you have a burning sensation that starts in your stomach then goes up into your throat, and can be associated with a bitter taste in your mouth?
- **E_201** (B): Do you have a cough?
- **E_210** (B): Have you recently thrown up blood or something resembling coffee beans?
- **E_215** (B): Do you have symptoms that get worse after eating?
- **E_217** (B): Are your symptoms worse when lying down and alleviated while sitting up?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_70** (B): Are you significantly overweight compared to people of the same height as you?
- **E_78** (B): Do you drink alcohol excessively or do you have an addiction to alcohol?
- **E_79** (B): Do you smoke cigarettes?
- **E_98** (B): Do you have a hiatal hernia?
- **E_124** (B): Do you have asthma or have you ever had to use a bronchodilator in the past?
- **E_167** (B): Do you think you are pregnant or are you currently pregnant?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.