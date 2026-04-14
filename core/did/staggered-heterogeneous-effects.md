---
id: did-staggered-heterogeneous-effects
name: "DiD: Staggered adoption uses heterogeneity-robust estimator"
methodology:
  - did
scope:
  - paper
severity: blocker
clarity: heuristic
tags: [identification, staggered-did, heterogeneous-effects, two-way-fixed-effects]
author: rdahis
version: 1
---

## What to Check

When treatment is staggered (different units adopt treatment at different times), standard two-way fixed effects (TWFE) regression produces a weighted average of cohort-specific treatment effects where some weights can be negative. This means TWFE can return wrong signs even when all true treatment effects are positive. Papers with staggered adoption must use or address heterogeneity-robust estimators.

## How to Check

1. Determine whether treatment timing is staggered: are there multiple "treatment cohorts" (groups of units that adopt treatment in different periods)?
2. If staggered, check whether the paper uses one of the following heterogeneity-robust methods:
   - Callaway & Sant'Anna (2021) — ATT by cohort × time
   - Sun & Abraham (2021) — interaction-weighted estimator
   - Borusyak, Jaravel & Spiess (2021) — imputation estimator
   - de Chaisemartin & D'Haultfœuille (2020) — DID_M estimator
   - Gardner (2021) — two-stage DiD
3. If TWFE is used as the primary specification, check whether: (a) the paper acknowledges the Goodman-Bacon decomposition problem, (b) robustness checks with a heterogeneity-robust method are provided.
4. Check whether the paper reports heterogeneity in treatment effects across cohorts — even if the average effect is the primary estimand, cohort heterogeneity is informative.

## Pass Condition

Either: (a) the paper uses a heterogeneity-robust estimator as its primary specification, OR (b) the paper uses TWFE but reports robustness to a heterogeneity-robust estimator and discusses the Goodman-Bacon decomposition explicitly.

## Failure Examples

1. **TWFE only, no discussion**: Paper has 50 states adopting a policy between 1990 and 2010. The main tables show TWFE regressions with state and year FE. No discussion of staggered DiD concerns. Published post-2021. Fails.
2. **Goodman-Bacon mentioned but no robust estimator**: Paper cites Goodman-Bacon (2021) in a footnote but reports no alternative estimator. "We acknowledge potential heterogeneity" is not a fix. Fails.
3. **Event-study interpreted as Callaway-Sant'Anna**: Paper reports a binned event-study from TWFE and calls it a test of heterogeneous effects. This is not equivalent. Fails.

## Notes

- Papers written before 2020 and currently under review should be assessed with some tolerance — the literature evolved rapidly. Papers written after 2022 have no excuse.
- For papers with a single treatment date (sharp DiD), this test does not apply. Use `did-parallel-trends-plot` instead.

## References

- Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing. *Journal of Econometrics*, 225(2), 254–277.
- Callaway, B., & Sant'Anna, P. H. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics*, 225(2), 200–230.
- Roth, J., Sant'Anna, P. H., Bilinski, A., & Poe, J. (2023). What's trending in difference-in-differences? A synthesis of the recent econometrics literature. *Journal of Econometrics*, 235(2), 2218–2244.
