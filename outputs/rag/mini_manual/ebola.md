# Ebola

**Overview:** Ebola virus disease (EVD) is a severe, often fatal hemorrhagic fever caused by Ebola virus (Filoviridae family). It is transmitted through direct contact with infected blood and body fluids. It affects multiple organ systems with high mortality (25–90% depending on strain and setting).

**Typical Presentation:** Abrupt onset of fever, fatigue, myalgia, and headache ('dry' symptoms) after 8–10 day incubation. By days 4–5, severe watery diarrhea, vomiting, and abdominal pain ('wet' symptoms) develop. Hemorrhagic manifestations (petechiae, mucosal bleeding) occur in ~40% of patients, typically later in the course.

**Key Distinguishing Features:** Distinguished from malaria and typhoid fever by epidemiologic context (endemic area, contact with EVD patient) and hemorrhagic features. Distinguished from other viral hemorrhagic fevers by RT-PCR testing. Biosafety level 4 containment required.

**Severity & Urgency:** Critical — Case fatality rate is very high; no specific antiviral treatment, though supportive care and experimental therapies improve survival.

**Sources:** [WHO: Ebola Disease Fact Sheet] [PMC5175058]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `a98.4`
- DDXPlus severity (dataset field): `1`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_39** (B): Have you felt confused or disorientated lately?
- **E_51** (B): Have you had diarrhea or an increase in stool frequency?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_89** (B): Do you constantly feel fatigued or do you have non-restful sleep?
- **E_91** (B): Do you have a fever (either felt or measured with a thermometer)?
- **E_97** (B): Do you have a sore throat?
- **E_144** (B): Do you have diffuse (widespread) muscle pain?
- **E_148** (B): Are you feeling nauseous or do you feel like vomiting?
- **E_178** (B): Have you noticed any unusual bleeding or bruising related to your consultation today?
- **E_201** (B): Do you have a cough?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_41** (B): Have you been in contact with a person with similar symptoms in the past 2 weeks?
- **E_73** (B): In the last month, have you been in contact with anyone infected with the Ebola virus?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.