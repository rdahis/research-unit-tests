---
id: ml-prediction-inference-distinction
name: "ML: Prediction claims not confused with causal inference"
methodology:
  - ml_prediction
scope:
  - paper
severity: blocker
clarity: judgment
tags: [causality, prediction, identification]
author: rdahis
version: 1
---

## What to Check

Predictive accuracy and causal identification are distinct. A model can predict an outcome well using confounded features without identifying the causal effect of any feature. Papers that slide from "our model predicts Y well" to "feature X causes Y" or "policy P will raise Y" commit a prediction-inference conflation. This error appears frequently in papers that use ML for policy recommendation.

## How to Check

1. Identify every causal or policy claim in the paper (look for language such as "increases," "causes," "effect of," "impact of," "intervention will," or "policy recommendation").
2. For each such claim, assess whether the paper uses a method capable of identifying causal effects:
   - **Causal ML methods** (acceptable for causal claims): double/debiased ML (Chernozhukov et al. 2018), causal forests (Wager & Athey 2018), structural models with explicit identification.
   - **Standard predictive ML** (not acceptable for causal claims): LASSO, random forests, neural networks used as black-box predictors without explicit identification strategy.
3. Check whether the paper restricts claims to predictive language ("is associated with," "predicts," "is correlated with") when using predictive methods. If so, assess whether any downstream interpretation or policy recommendation implicitly assumes causation.
4. If the paper uses ML for variable selection (e.g., LASSO to select instruments or controls) and then uses the selected variables in a causal framework, verify that the two-step procedure is valid (e.g., post-selection inference, sample splitting).

## Pass Condition

(a) Paper makes only predictive claims and uses predictive methods, with no causal language; OR (b) paper makes causal claims and uses a method with a valid identification strategy capable of supporting those claims.

## Failure Examples

1. **Implicit causation**: Paper trains a random forest to predict firm productivity and concludes "management practices are the key driver of productivity" based on variable importance scores. Variable importance in a predictive model reflects correlation, not causation. Fails.
2. **Policy extrapolation**: Paper predicts recidivism using ML and recommends using the model to set bail. Prediction under the current distribution does not imply the distribution will remain stable under the policy intervention (Lucas critique). No causal identification. Fails.
3. **Confounded SHAP values**: Paper uses SHAP values to argue that neighborhood income "causes" health disparities. SHAP values are attribution of predictive contribution, not causal attribution. Fails.

## References

- Chernozhukov, V., et al. (2018). Double/debiased machine learning for treatment and structural parameters. *Econometrics Journal*, 21(1), C1–C68.
- Athey, S., & Imbens, G. (2019). Machine learning methods that economists should know about. *Annual Review of Economics*, 11, 685–725.
- Kleinberg, J., Ludwig, J., Mullainathan, S., & Obermeyer, Z. (2015). Prediction policy problems. *American Economic Review: P&P*, 105(5), 491–495.
