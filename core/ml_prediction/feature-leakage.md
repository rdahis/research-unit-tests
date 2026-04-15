---
id: ml-prediction-feature-leakage
name: "ML: No feature leakage from outcome or future data"
methodology:
  - ml_prediction
scope:
  - paper
severity: blocker
clarity: heuristic
tags: [leakage, features, temporal-validity]
author: rdahis
version: 1
---

## What to Check

Feature leakage occurs when predictor variables encode information about the outcome or are measured after the outcome occurs. A model with leakage will show inflated performance that does not replicate in deployment. Two forms are common: (1) **outcome-proxy leakage** — a feature is so close to the outcome that including it is nearly circular; (2) **temporal leakage** — a feature is measured after the outcome, so in a real forecasting context it would be unavailable.

## How to Check

1. List the key predictor variables. For each, ask: *Could this variable be known before the outcome occurs in a real deployment of this model?*
2. Check the timing of each feature relative to the outcome:
   - For a prediction task (predict event at time *t*), all features must be measured strictly before time *t*.
   - Exception: if the purpose is *nowcasting* or *hindcasting*, document which features are contemporaneous and why this is valid.
3. Check for outcome-proxy features: variables that are definitionally or near-definitionally related to the outcome (e.g., using "hospital readmission in the next 30 days" as a feature to predict "hospital readmission in the next 30 days," or using a closely related administrative flag).
4. Check for variables measured during or after data collection that would not be available in the prediction context.

## Pass Condition

All features are causally and temporally prior to the outcome in the intended use case. Any contemporaneous features are explicitly justified. No variable in the feature set is a proxy or transformation of the outcome variable.

## Failure Examples

1. **Temporal leakage**: Predicting loan default using credit bureau scores measured *after* the loan decision. In a real-time model, only pre-application scores would be available. The model learns from the future. Fails.
2. **Outcome proxy**: Predicting hospital mortality using "palliative care referral" as a feature. Palliative care referrals are made precisely for patients expected to die — the feature nearly encodes the outcome. Fails.
3. **Label leakage in text**: Predicting article topic category using word counts that include the category label embedded in the metadata. Fails.

## References

- Kaufman, S., Rosset, S., Perlich, C., & Stitelman, O. (2012). Leakage in data mining: Formulation, detection, and avoidance. *ACM Transactions on Knowledge Discovery from Data*, 6(4), 1–21.
- Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns*, 4(9).
