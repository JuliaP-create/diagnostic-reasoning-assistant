# Whooping cough

**Overview:** Whooping cough (pertussis) is a highly contagious respiratory infection caused by Bordetella pertussis. It affects the upper and lower respiratory system, with toxin-mediated damage to the ciliated respiratory epithelium. It is vaccine-preventable but still causes outbreaks.

**Typical Presentation:** Three stages: (1) Catarrhal: 1–2 weeks of cold-like symptoms; (2) Paroxysmal: severe paroxysms of coughing followed by inspiratory 'whoop' and post-tussive vomiting, lasting 2–8 weeks; (3) Convalescent: gradual resolution over weeks. Afebrile or low-grade fever.

**Key Distinguishing Features:** Distinguished from other causes of persistent cough by paroxysmal coughing fits with inspiratory whoop, post-tussive vomiting, and absence of fever. Distinguished from croup by absence of barking cough or stridor between paroxysms.

**Severity & Urgency:** Moderate to High — Can be fatal in unvaccinated infants; complications include pneumonia, seizures, and apnea in young infants.

**Sources:** [PMC6859243] [PMC8482022]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `A37`
- DDXPlus severity (dataset field): `4`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_112** (B): Do you wheeze while inhaling or is your breathing noisy after coughing spells?
- **E_166** (B): Did you vomit after coughing?
- **E_203** (B): Do you have intense coughing fits?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_40** (B): Have you been in contact with someone who has had pertussis (whoooping cough)?
- **E_70** (B): Are you significantly overweight compared to people of the same height as you?
- **E_124** (B): Do you have asthma or have you ever had to use a bronchodilator in the past?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?
- **E_209** (B): Are your vaccinations up to date?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.