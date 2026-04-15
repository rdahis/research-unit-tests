---
id: ml-prediction-benchmark-comparison
name: "ML: Performance compared to a simple benchmark"
methodology:
  - ml_prediction
scope:
  - paper
severity: warning
clarity: deterministic
tags: [benchmark, baseline, performance]
author: rdahis
version: 1
---

## What to Check

A reported prediction accuracy of, say, 85% is uninterpretable without context. If always predicting the majority class yields 84%, the model adds almost nothing. Every ML paper must compare model performance to at least one simple baseline that establishes what the task-specific floor of performance is.

## How to Check

1. Identify the reported performance metric (AUC, accuracy, RMSE, F1, etc.).
2. Look for a comparison to at least one of the following benchmarks:
   - **Naive baseline**: always-predict-mean (for regression), always-predict-majority-class (for classification), random prediction, or persistence forecast (for time series).
   - **Simple parametric model**: OLS regression or logistic regression on the same features.
   - **Prior literature model**: the best previously published model for this task/dataset.
3. The benchmark must use the same evaluation set and metric.
4. Check whether the improvement over the benchmark is statistically and economically meaningful. A 0.2 AUC improvement may be statistically significant but economically negligible in a deployment context.

## Pass Condition

At least one benchmark model is reported using the same evaluation set and metric. The gain over the benchmark is quantified.

## Failure Examples

1. **No baseline**: Paper reports RMSE = 0.42 for a neural network prediction of crop yield. No comparison to OLS or climatological mean. The reader cannot assess whether 0.42 is good. Fails.
2. **Benchmark on different data**: Benchmark is from a prior paper using a different sample period. Not directly comparable. Insufficient.
3. **Trivial baseline only**: Paper compares to random prediction for a task where a simple OLS baseline would achieve 90% of the performance. The trivially low bar inflates apparent gains.

## References

- Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2022). M5 accuracy competition: Results, findings, and conclusions. *International Journal of Forecasting*, 38(4), 1346–1364.
- Lipton, Z. C., & Steinhardt, J. (2019). Troubling trends in machine learning scholarship. *Queue*, 17(1), 45–77.
