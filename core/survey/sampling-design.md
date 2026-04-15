---
id: survey-sampling-design
name: "Survey: Complex sampling design accounted for in standard errors"
methodology:
  - survey
scope:
  - paper
severity: blocker
clarity: deterministic
tags: [sampling, standard-errors, weights, stratification]
author: rdahis
version: 1
---

## What to Check

Surveys that use stratified sampling, cluster sampling, or multi-stage probability sampling have a complex design that inflates or deflates the variance of estimators relative to a simple random sample. Ignoring the design produces incorrect standard errors and potentially wrong inference. If the survey provides sampling weights, these must be used to obtain population-representative estimates.

## How to Check

1. Identify the survey's sampling design. Look for terms like: stratified sample, cluster sample, probability-proportional-to-size (PPS) sampling, multi-stage sampling. If the survey is a well-known dataset (NHANES, DHS, ACS, PNAD), note its complex design.
2. Check whether the analysis uses:
   - **Survey-weighted estimators**: `svy` prefix in Stata, `svydesign`/`survey` package in R, `svy*` commands. Weights must match the survey design (stratum, PSU, and weight variables specified).
   - **Design-based standard errors**: not just HC-robust or cluster-robust SEs, but SEs that account for the sampling design structure.
3. If the paper uses no weights and no design adjustment, verify whether this is defensible: some surveys are self-weighting (equal probability sampling within a stratum) and within-stratum analysis may not require weights.
4. Check whether weights are normalized appropriately (sampling weights vs. analytic weights vs. probability weights — these differ in how they affect SEs).

## Pass Condition

If the survey uses a complex sampling design (stratification, clustering, or sampling weights provided), the analysis uses design-appropriate estimators and standard errors. The stratum and PSU (primary sampling unit) variables are specified or the justification for simple random sample analysis is stated.

## Failure Examples

1. **Ignoring cluster structure**: Analysis of a nationally representative household survey (clustered by village) uses OLS with HC-robust SEs. Within-village correlation is ignored. SEs are too small. Fails.
2. **Weights ignored for representative estimates**: Paper makes national prevalence claims using an oversample of minority groups without applying sampling weights. Estimates are biased toward minority group. Fails.
3. **Wrong weight type**: Paper specifies frequency weights instead of probability weights in Stata (`fweight` vs. `pweight`). `fweight` inflates sample size, producing spuriously small SEs. Fails.

## References

- Lumley, T. (2010). *Complex Surveys: A Guide to Analysis Using R*. Wiley.
- Kish, L. (1965). *Survey Sampling*. Wiley. Chapter 4: Stratified Sampling.
- StataCorp. (2023). *Stata Survey Data Reference Manual*. Stata Press.
