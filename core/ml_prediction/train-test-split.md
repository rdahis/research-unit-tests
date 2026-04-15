---
id: ml-prediction-train-test-split
name: "ML: Model performance evaluated on held-out data"
methodology:
  - ml_prediction
scope:
  - paper
severity: blocker
clarity: deterministic
tags: [validation, overfitting, cross-validation]
author: rdahis
version: 1
---

## What to Check

A predictive model evaluated exclusively on the data used to train it will always appear to perform well — this is overfitting, not generalization. Valid performance claims require evaluation on data the model has never seen: a held-out test set, k-fold cross-validation, or (for time series) rolling out-of-sample evaluation.

## How to Check

1. Locate the section reporting model performance (accuracy, AUC, RMSE, etc.).
2. Identify how the evaluation set was constructed:
   - **Random train/test split** (acceptable): e.g., 80% train / 20% test, where test set is untouched during model selection.
   - **k-fold cross-validation** (acceptable): model trained and evaluated on k non-overlapping folds.
   - **Time-series / walk-forward validation** (required for temporal data): evaluation uses only past data to predict future observations.
   - **Same data for training and evaluation** (not acceptable): model fit to entire sample, performance reported on the same sample.
3. Check whether hyperparameter tuning or model selection was done using the test set. If tuning was done on the test set, the reported performance is optimistic (test-set leakage).
4. For deep learning or large models: check for a separate validation set used for early stopping, distinct from the final test set.

## Pass Condition

Performance metrics are reported on a held-out set that was not used during model training or hyperparameter selection. Cross-validation is explicitly described and correctly implemented.

## Failure Examples

1. **In-sample reporting**: Paper trains a random forest on the full dataset and reports R² = 0.92 on the same observations. No holdout described. Fails.
2. **Test-set leakage for selection**: Paper tries 12 model specifications, reports the best-performing one evaluated on the test set. The test set was used implicitly to select the model — performance is inflated. Fails.
3. **Temporal leakage**: Paper predicts GDP growth using features that include variables measured contemporaneously with the outcome. In walk-forward validation, future data should not appear in training. Fails.

## References

- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer. Chapter 7: Model Assessment and Selection.
- Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns*, 4(9).
