---
id: rdd-covariate-smoothness
name: "RDD: Pre-determined covariates smooth at cutoff"
methodology:
  - rdd
scope:
  - paper
severity: blocker
clarity: heuristic
tags: [identification, covariates, balance, smoothness]
author: rdahis
version: 1
---

## What to Check

Pre-determined covariates (variables determined before treatment assignment) should not jump discontinuously at the RDD cutoff. A discontinuity in a covariate at the cutoff suggests that units on either side differ in ways unrelated to treatment — a violation of local continuity. This is analogous to a covariate balance test in randomized experiments.

## How to Check

1. Identify all pre-determined covariates available in the data (demographic characteristics, baseline outcomes, geographic variables, etc.).
2. Check whether the paper estimates RDD regressions with each covariate as the outcome variable. The coefficient at the cutoff should be near zero and statistically insignificant.
3. Results may appear in a dedicated "covariate smoothness" or "validity checks" table, or in the appendix.
4. Assess the number of covariates tested. Testing 10+ covariates, one will be significant by chance at 5%. Check whether the paper accounts for multiple testing (Bonferroni, Holm, or by noting that the one rejection is a borderline case).
5. Check whether a visual inspection is provided (RDD plots of covariates against the running variable at the cutoff).

## Pass Condition

All major pre-determined covariates are tested. No more than 1–2 show significant discontinuities, and any that do are acknowledged and discussed. Visual checks support smoothness.

## Failure Examples

1. **No covariate smoothness checks**: Paper estimates an RDD on earnings using a test score cutoff but does not check whether demographics (age, gender, prior test scores) are smooth at the cutoff. Fails — sorting could produce demographic discontinuities even if the density test passes.
2. **3 of 8 covariates show significant jumps**: Three pre-determined covariates are discontinuous at the cutoff. Paper states "most covariates are balanced." This understates the problem — 3/8 is far above the false discovery rate expected under the null. Fails.
3. **Only post-treatment covariates tested**: Paper checks smoothness of variables that could be affected by the treatment itself (post-treatment outcomes). These are not valid validity checks. Fails — only pre-determined variables count.

## References

- Imbens, G. W., & Lemieux, T. (2008). Regression discontinuity designs: A guide to practice. *Journal of Econometrics*, 142(2), 615–635.
- Cattaneo, M. D., Idrobo, N., & Titiunik, R. (2020). *A Practical Introduction to Regression Discontinuity Designs*. Cambridge University Press.
