---
id: universal-ols-omitted-variable-discussed
name: "OLS/correlational papers address omitted variable bias"
methodology:
  - universal
  - ols
scope:
  - paper
severity: blocker
clarity: judgment
tags: [identification, omitted-variable-bias, endogeneity, ols]
author: rdahis
version: 1
---

## What to Check

Any paper that interprets OLS coefficients causally — or that does not explicitly disclaim causal interpretation — must discuss the omitted variable bias problem. Specifically, it must identify the most plausible confounders, assess the likely direction of bias, and either argue the bias is small or explain why the association is still informative.

Papers that present purely descriptive or predictive regressions and make no causal claims are exempt — but the lack of causal interpretation must be stated explicitly.

## How to Check

1. Determine whether the paper interprets its OLS estimates causally. Look for language like "X increases Y by…", "the effect of X on Y is…", or "X causes Y." If causal language is used, proceed to step 2. If the paper explicitly says "these are descriptive/correlational," check only that the disclaimer is clear and not contradicted elsewhere.
2. Identify the main endogeneity concern: what omitted variable is most likely correlated with both X and Y? The paper must name it.
3. Assess the paper's response. Acceptable responses:
   - Fixed effects strategy that absorbs the confounder (argue why FE is sufficient).
   - Sensitivity analysis: Oster (2019) bounds, Cinelli & Hazlett (2020) sensitivity, or similar — quantifying how strong the omitted variable would need to be to overturn the result.
   - Argument from theory or institutional knowledge that the confounder is absent or of negligible magnitude.
4. Check for the Altonji-Elder-Taber test or equivalent: does selection on observables predict selection on unobservables? This is best practice for OLS papers making causal claims.

## Pass Condition

The paper either: (a) makes no causal claims and states this explicitly, OR (b) makes causal claims and provides a credible argument or sensitivity analysis addressing the most plausible omitted variable bias.

## Failure Examples

1. **Causal language, no discussion**: Paper regresses wages on education with individual controls and states "an additional year of education increases wages by 8%." No discussion of ability bias, family background, or other confounders. Fails.
2. **Disclaimer buried**: Paper has a single footnote saying "we cannot establish causality" but the introduction, results, and conclusion all use causal language ("the policy reduces crime by 12%"). The disclaimer is cosmetic. Fails.
3. **Fixed effects assumed sufficient without argument**: Paper adds firm fixed effects and claims "selection on unobservables within firm is unlikely." No argument for why time-varying within-firm confounders are absent. Fails — FE only controls for time-invariant unobserved heterogeneity.

## Notes

- This test applies to OLS papers claiming causal effects. It also applies to papers using DiD, IV, or RDD when the main specification includes OLS controls whose endogeneity might affect the estimate.
- Papers in the descriptive tradition (national accounts, measurement papers, index construction) are exempt if they make no causal claims anywhere.

## References

- Oster, E. (2019). Unobservable selection and coefficient stability: Theory and evidence. *Journal of Business & Economic Statistics*, 37(2), 187–204.
- Cinelli, C., & Hazlett, C. (2020). Making sense of sensitivity: Extending omitted variable bias. *Journal of the Royal Statistical Society: Series B*, 82(1), 39–67.
