---
id: universal-standard-errors-clustered
name: "Standard errors clustered at the right level"
methodology:
  - universal
scope:
  - paper
severity: blocker
clarity: heuristic
tags: [inference, clustering, standard-errors]
author: rdahis
version: 1
---

## What to Check

Standard errors must be clustered at the level at which treatment varies, when there is within-cluster correlation in outcomes. Under-clustering (clustering too narrowly) produces standard errors that are too small and inflated t-statistics. Over-clustering (clustering too broadly when no within-cluster correlation exists) is conservative but not invalid.

## How to Check

1. Identify the level at which the main independent variable (treatment or variable of interest) varies. Examples: if treatment is assigned by county, the natural clustering level is county; if by firm, by firm.
2. Check the footnote or header of the main regression table for the stated clustering level.
3. Evaluate whether the stated clustering level matches or is broader than the treatment variation level:
   - **Correct**: treatment varies by county, SEs clustered by county (or by state, which is broader).
   - **Wrong**: treatment varies by county, SEs clustered by individual (narrower than treatment unit).
   - **Wrong**: treatment varies by state but SEs are heteroskedasticity-robust (HC) only — no clustering.
4. Check the number of clusters. With fewer than 20–30 clusters, standard asymptotic cluster-robust SEs are unreliable. Flag if the paper uses few clusters without addressing this (wild cluster bootstrap or other small-cluster corrections).
5. For two-way clustering (e.g. by firm and by year), check that both dimensions are justified and that the `vcovDCL` or equivalent estimator is used.

## Pass Condition

Clustering level matches or is broader than the treatment variation level. Number of clusters is sufficient (≥30) or small-cluster correction is applied. Clustering choice is stated explicitly in the table or notes.

## Failure Examples

1. **Under-clustering**: Treatment is a state-level policy change. Paper clusters SEs at the individual level because "that is where the outcome is measured." Individual-level clustering ignores the within-state correlation induced by the common treatment. Fails.
2. **No clustering for panel data**: Paper estimates a panel regression with firm and year fixed effects. SEs are reported as HC2 heteroskedasticity-robust but not clustered. With repeated observations per firm, within-firm correlation is almost certainly present. Fails unless the panel is very short (T=2) and the paper argues no within-firm serial correlation.
3. **Few clusters without correction**: Paper clusters by state with N=12 states. Standard cluster-robust SEs are unreliable at this cluster count. No wild cluster bootstrap or other correction. Fails.

## References

- Cameron, A. C., & Miller, D. L. (2015). A practitioner's guide to cluster-robust inference. *Journal of Human Resources*, 50(2), 317–372.
- Abadie, A., Athey, S., Imbens, G. W., & Wooldridge, J. M. (2023). When should you adjust standard errors for clustering? *Quarterly Journal of Economics*, 138(1), 1–35.
