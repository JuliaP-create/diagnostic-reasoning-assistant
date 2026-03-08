# Bronchiectasis

**Overview:** Bronchiectasis is permanent dilation and destruction of the bronchial walls, leading to impaired mucociliary clearance and chronic infection. Causes include post-infectious damage, cystic fibrosis, immune deficiency, and ABPA. It affects the lower respiratory system.

**Typical Presentation:** Chronic productive cough with large volumes of purulent sputum, recurrent respiratory infections, hemoptysis, and progressive dyspnea. Crackles, rhonchi, and squeaks on auscultation. Clubbing may be present in advanced disease.

**Key Distinguishing Features:** Distinguished from chronic bronchitis by larger sputum volumes, hemoptysis, and dilated airways on high-resolution CT (signet ring sign). Distinguished from COPD by productive cough being the dominant feature rather than airflow limitation.

**Severity & Urgency:** Moderate — Chronic progressive condition requiring long-term airway clearance therapy and antibiotics for exacerbations.

**Sources:** [MSD Manual: Bronchiectasis] [PMC5478409]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `J47`
- DDXPlus severity (dataset field): `3`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_45** (B): Have you been coughing up blood?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_77** (B): Do you have a cough that produces colored or more abundant sputum than usual?
- **E_201** (B): Do you have a cough?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_17** (B): Are you of Asian descent?
- **E_18** (B): Do you have cystic fibrosis?
- **E_20** (B): Do you have Rheumatoid Arthritis?
- **E_47** (B): Do you suffer from Crohn’s disease or ulcerative colitis (UC)?
- **E_118** (B): Have you ever had pneumonia?
- **E_123** (B): Do you have a chronic obstructive pulmonary disease (COPD)?
- **E_124** (B): Do you have asthma or have you ever had to use a bronchodilator in the past?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_227** (B): Are you immunosuppressed?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.