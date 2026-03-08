# Panic attack

**Overview:** A panic attack is an acute episode of intense fear with prominent physical symptoms, occurring without a proportionate external trigger. It is a psychiatric condition but produces striking cardiovascular and respiratory symptoms. It is associated with panic disorder and other anxiety disorders.

**Typical Presentation:** Sudden onset of palpitations, chest pain, dyspnea, diaphoresis, trembling, dizziness, and a sense of impending doom. Peaks within 10 minutes. Paresthesias (tingling) and derealization are common accompanying features.

**Key Distinguishing Features:** Distinguished from acute coronary syndrome by normal ECG and troponin, young age, and recurrent stereotyped episodes. Distinguished from anaphylaxis by absence of urticaria, angioedema, and hypotension.

**Severity & Urgency:** Low — Not life-threatening, but important to rule out cardiac, pulmonary, and endocrine causes of similar symptoms.

**Sources:** [NCBI Bookshelf: Panic Attack, StatPearls] [PMID: 28722900]

**Educational Disclaimer:** "This is an educational summary for a machine learning project. It is not medical advice."

**Educational note:** This mini-manual combines (a) curated clinical summaries (with cited sources) and (b) DDXPlus synthetic metadata mappings. It is not medical advice and is used only to explain model behavior.

## Dataset metadata
- ICD‑10: `f41`
- DDXPlus severity (dataset field): `5`

## Symptoms linked to this condition (DDXPlus mapping)
- **E_16** (B): Do you feel anxious?
- **E_50** (B): Have you had significantly increased sweating?
- **E_53** (B): Do you have pain somewhere, related to your reason for consulting?
- **E_54** (M): Characterize your pain:
- **E_55** (M): Do you feel pain somewhere?
- **E_56** (C): How intense is the pain?
- **E_57** (M): Does the pain radiate to another location?
- **E_58** (C): How precisely is the pain located?
- **E_59** (C): How fast did the pain appear?
- **E_66** (B): Are you experiencing shortness of breath or difficulty breathing in a significant way?
- **E_75** (B): Do you feel like you are (or were) choking or suffocating?
- **E_82** (B): Do you feel lightheaded and dizzy or do you feel like you are about to faint?
- **E_111** (B): Do you feel like you are dying or were you afraid that you were about do die?
- **E_148** (B): Are you feeling nauseous or do you feel like vomiting?
- **E_155** (B): Do you feel your heart is beating fast (racing), irregularly (missing a beat) or do you feel palpitations?
- **E_157** (B): Have you recently had numbness, loss of sensation or tingling, in both arms and legs and around your mouth?
- **E_171** (B): Do you feel like you are detached from your own body or your surroundings?
- **E_177** (B): Do you currently, or did you ever, have numbness, loss of sensitivity or tingling anywhere on your body?

## Antecedents / risk-factor questions linked to this condition (DDXPlus mapping)
- **E_29** (B): Do any members of your immediate family have a psychiatric illness?
- **E_78** (B): Do you drink alcohol excessively or do you have an addiction to alcohol?
- **E_80** (B): Have you ever been diagnosed with depression?
- **E_81** (B): Do you suffer from chronic anxiety?
- **E_99** (B): Have you ever had a migraine or is a member of your family known to have migraines?
- **E_124** (B): Do you have asthma or have you ever had to use a bronchodilator in the past?
- **E_138** (B): Do you suffer from fibromyalgia?
- **E_185** (B): Have you ever had a head trauma?
- **E_204** (C): Have you traveled out of the country in the last 4 weeks?

## Notes for the assistant
- These are **base evidence codes** (question concepts). The predictor still uses token/value encoding.
- The question policy selects among base codes using an expected usefulness score; RAG only provides wording/explanations.