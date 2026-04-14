---
id: synth-single-treated-unit
name: "Synth: Single-unit design limitations acknowledged"
methodology:
  - synth
scope:
  - paper
severity: warning
clarity: heuristic
tags: [identification, inference, synthetic-control, external-validity]
author: rdahis
version: 1
---

## What to Check

The synthetic control method was designed for comparative case studies with a single (or small number of) treated unit(s). This creates specific limitations: (1) classical inference is not applicable, (2) external validity is limited to the treated unit's context, and (3) the method cannot recover an average treatment effect across many units. Papers must acknowledge these limitations and not overstate what the design can establish.

## How to Check

1. Check whether the paper uses standard p-values or confidence intervals from classical statistics for the synthetic control estimate. These are not valid — inference relies on the permutation/placebo distribution. Flag if the paper reports t-statistics or conventional p-values for the main SCM estimate.
2. Check whether the paper acknowledges that results apply to the specific treated unit and context, not necessarily more broadly.
3. If the paper has multiple treated units, check whether it uses an appropriate aggregation method (e.g., averaged synthetic controls, Synthetic DiD, or the Abadie & L'Hour 2021 penalized SCM).

## Pass Condition

Paper does not use classical t-tests or p-values for SCM inference. Permutation-based p-values are used. Single-unit limitations are acknowledged at least briefly.

## Failure Examples

1. **Classical p-values reported**: Paper reports "the effect is −0.14 (p = 0.03)" using a standard t-test on the SCM estimate. Classical inference is invalid for SCM. Fails.
2. **Overstatement of external validity**: Paper uses a single-country SCM and concludes "this shows that policy X is effective across developing countries." SCM identifies the effect for the one treated country only. Fails.

## References

- Abadie, A. (2021). Using synthetic controls: Feasibility, data requirements, and methodological aspects. *Journal of Economic Literature*, 59(2), 391–425.
- Abadie, A., & L'Hour, J. (2021). A penalized synthetic control estimator for disaggregated data. *Journal of the American Statistical Association*, 116(536), 1817–1834.
