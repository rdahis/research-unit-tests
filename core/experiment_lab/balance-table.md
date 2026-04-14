---
id: experiment-lab-balance-table
name: "Experiment: Baseline covariate balance table reported"
methodology:
  - experiment_lab
  - experiment_field
scope:
  - paper
severity: blocker
clarity: deterministic
tags: [randomization, balance, baseline, covariate]
author: rdahis
version: 1
---

## What to Check

Randomized experiments must report a balance table showing that pre-treatment (baseline) covariates are similar across treatment and control groups. Balance on observables is the primary empirical check that randomization succeeded. A paper that does not show a balance table gives readers no way to assess whether the randomization was implemented correctly.

## How to Check

1. Locate the balance table. It should show means (and standard deviations or standard errors) of baseline covariates separately for treatment and control groups.
2. Check that the covariates tested are: (a) pre-determined (measured before randomization), and (b) substantively important predictors of the outcome.
3. Check whether the table reports p-values or t-statistics for differences in means. Alternatively, an F-test of joint significance of all covariates in a regression of treatment status on baseline characteristics is acceptable.
4. Assess the balance: are there significant differences on important covariates? One or two marginally significant differences among many tests is expected by chance. Flag systematic imbalance (3+ significant differences, or imbalance on a key outcome predictor).
5. For stratified or blocked randomization, check that the balance test accounts for the stratification (use within-strata comparisons or include strata fixed effects).

## Pass Condition

Balance table present, covers key pre-treatment covariates, reports tests for differences, and shows no systematic imbalance. Any imbalance is acknowledged and controlled for in regression specifications.

## Failure Examples

1. **No balance table**: Paper describes a randomized experiment and proceeds directly to results. No evidence that randomization produced balanced groups. Fails.
2. **Post-treatment covariates included**: Balance table includes variables that could be affected by treatment (e.g., midline outcomes). These are not valid balance checks — only truly pre-determined variables count. Fails.
3. **Systematic imbalance, not addressed**: Treatment group has significantly higher baseline income (p = 0.02) and education (p = 0.04) than control. Paper proceeds without controlling for these. Fails — estimated treatment effect is confounded.

## References

- Bruhn, M., & McKenzie, D. (2009). In pursuit of balance: Randomization in practice in development field experiments. *American Economic Journal: Applied Economics*, 1(4), 200–232.
- Muralidharan, K., & Niehaus, P. (2017). Experimentation at scale. *Journal of Economic Perspectives*, 31(4), 103–124.
