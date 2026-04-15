---
id: did-event-study
name: "DiD: Event study (dynamic effects) reported"
methodology:
  - did
scope:
  - paper
severity: blocker
clarity: deterministic
tags: [parallel-trends, dynamic-effects, anticipation, event-study]
author: rdahis
version: 1
---

## What to Check

A static two-period DiD estimate collapses the entire treatment effect into a single number, hiding the time path of effects and masking pre-treatment trends. An event study plots the coefficients on leads and lags of treatment, serving three purposes: (1) validating parallel pre-trends, (2) detecting anticipation effects (treatment effect starting before treatment), and (3) characterizing whether effects are permanent, temporary, or growing.

This test is distinct from `did-parallel-trends-plot`, which checks only whether any pre-trend visualization exists. This test requires a full event study with both pre- and post-period coefficients.

## How to Check

1. Look for a figure or table presenting event-study (dynamic treatment effect) estimates: coefficients β_{t-k} and β_{t+k} for k = 1, 2, ... periods before and after treatment.
2. Check that pre-treatment coefficients (leads, t−1, t−2, ...) are shown and are statistically indistinguishable from zero. The omitted period (normalized to zero) is typically t−1 or the last pre-treatment period.
3. Check that post-treatment coefficients (lags, t+1, t+2, ...) are shown, allowing the reader to assess treatment effect dynamics.
4. For staggered treatment designs (multiple treatment cohorts): verify that the event study uses a heterogeneity-robust estimator (Callaway & Sant'Anna 2021, de Chaisemartin & D'Haultfœuille 2020, or Borusyak et al. 2024) rather than a two-way fixed effects (TWFE) event study, which is biased under treatment effect heterogeneity.
5. Event study confidence intervals should be reported (usually 95% CIs). A "joint test" of pre-trends (F-test of all pre-period coefficients = 0) is informative but optional.

## Pass Condition

Event study coefficients for both pre- and post-treatment periods are plotted or tabulated. Pre-treatment coefficients are close to zero. The estimator is appropriate for the design (heterogeneity-robust if staggered).

## Failure Examples

1. **Static estimate only**: Paper estimates a two-period DiD and reports a single ATT estimate. No dynamic effects shown. The reader cannot evaluate parallel trends or treatment dynamics. Fails.
2. **Pre-periods only**: Paper shows a pre-trend plot (satisfying `did-parallel-trends-plot`) but reports no post-period dynamics. Fails this test (passes `did-parallel-trends-plot`).
3. **TWFE event study in staggered design**: Paper has staggered rollout across 5 cohorts but runs a standard TWFE event study, which produces "negative weights" artifacts. Fails (see `did-staggered-heterogeneous-effects`).

## References

- Borusyak, K., Jaravel, X., & Spiess, J. (2024). Revisiting event-study designs: Robust and efficient estimation. *Review of Economic Studies*, 91(6), 3253–3285.
- Callaway, B., & Sant'Anna, P. H. C. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics*, 225(2), 200–230.
- Sun, L., & Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. *Journal of Econometrics*, 225(2), 175–199.
