---
id: ml-prediction-performance-metric
name: "ML: Performance metric appropriate for task and outcome distribution"
methodology:
  - ml_prediction
scope:
  - paper
severity: warning
clarity: heuristic
tags: [evaluation, metrics, imbalance]
author: rdahis
version: 1
---

## What to Check

The choice of performance metric must match the prediction task and the distribution of the outcome variable. The most common error is reporting accuracy for a classification task with an imbalanced outcome — when only 2% of observations are positive, a model that always predicts negative achieves 98% accuracy. Different metrics capture different aspects of performance; a paper should justify its choice.

## How to Check

1. Identify the outcome variable type and its distribution:
   - **Binary outcome**: check the prevalence of the positive class. If < 20% (or > 80%), accuracy alone is insufficient.
   - **Continuous outcome**: RMSE and MAE are standard. Check whether RMSE is appropriate (it weights large errors heavily — suitable if large errors are costly) vs. MAE (appropriate if errors have linear cost).
   - **Rank or ordering tasks**: check for rank-based metrics (NDCG, Spearman rank correlation).
2. For imbalanced binary outcomes, assess whether the paper reports at least one of: AUC-ROC, precision-recall AUC, F1 score, or reports performance at the operating threshold with precision and recall separately.
3. Check whether the metric aligns with the stated use case. For example, if the paper claims the model is useful for targeting interventions, positive predictive value (precision) at the operating threshold matters more than overall AUC.
4. Check for multiple comparisons across metrics: if the paper reports five metrics and highlights the best one, this is selective reporting.

## Pass Condition

The primary performance metric is appropriate for the outcome distribution and the stated use case. For imbalanced binary outcomes, accuracy alone is not accepted as the primary metric without additional metrics. Metric choice is explicitly justified.

## Failure Examples

1. **Accuracy with imbalanced outcome**: Paper predicts fraud (1% of transactions). Reports 99.1% accuracy. A model predicting no fraud achieves 99.0%. The ML model has nearly zero marginal value. Fails if accuracy is the only reported metric.
2. **RMSE for skewed outcomes**: Paper predicts hospital costs. Uses RMSE, which is dominated by rare catastrophic cases. MAE or quantile loss would better capture typical prediction error. Not necessarily a failure, but should be justified.
3. **Metric mismatch with application**: Paper claims model should be used to prioritize patients for intervention but reports only AUC. AUC does not reflect performance at any specific operating point. Precision and recall at the operating threshold are needed. Fails to support the stated application.

## References

- Davis, J., & Goadrich, M. (2006). The relationship between precision-recall and ROC curves. *Proceedings of ICML*.
- Hand, D. J. (2009). Measuring classifier performance: A coherent alternative to the area under the ROC curve. *Machine Learning*, 77(1), 103–123.
