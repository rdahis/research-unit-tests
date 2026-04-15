---
id: did-control-group-selection
name: "DiD: Control group selection justified and robust to alternatives"
methodology:
  - did
scope:
  - paper
severity: warning
clarity: judgment
tags: [control-group, identification, sensitivity]
author: rdahis
version: 1
---

## What to Check

The validity of DiD rests on the assumption that treated and control units would have followed parallel trends absent treatment. The choice of which units serve as controls is therefore a core identification assumption, not a data management decision. Papers must justify *why* these particular units are plausible counterfactuals and demonstrate that results are not driven by the specific control group chosen.

## How to Check

1. Identify the control group. Is the choice explained with economic or institutional reasoning? For example: "we use neighboring counties not exposed to the regulation because they share similar industry composition" — this is a justification. "We use all untreated observations" — this is not.
2. Check whether parallel pre-trends hold visually and statistically for the chosen control group (see `did-parallel-trends-plot` and `did-event-study`).
3. Look for robustness checks with alternative control groups:
   - Restricting control units to a more comparable subset (e.g., propensity-score matched controls, geographic neighbors, or units from the same state).
   - Excluding "contaminated" control units (e.g., units that were treated later in a staggered design, or units that anticipate future treatment).
   - Using a "clean comparison" estimator in staggered designs that only compares against never-treated or not-yet-treated units.
4. Assess whether the main result survives across plausible alternative control groups.

## Pass Condition

Control group selection is explicitly justified on economic or institutional grounds. Pre-trends are plausible for the chosen control group. At least one alternative control group specification is presented, either in the main results or in robustness.

## Failure Examples

1. **Default controls**: Paper uses "all other states" as controls for a state-level policy change in 10 states, with no justification for why economically dissimilar states are valid counterfactuals. Fails.
2. **Never-treated confound**: In a staggered design, paper uses late-treated units as controls for early-treated units. Late-treated units may anticipate treatment, violating parallel trends. No sensitivity check. Fails.
3. **Trimming without justification**: Paper drops certain control units without explanation, and including them reverses the sign of the result. No discussion. Fails.

## References

- Callaway, B., & Sant'Anna, P. H. C. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics*, 225(2), 200–230. Section 4 on "clean comparisons."
- Dube, A., Lester, T. W., & Reich, M. (2010). Minimum wage effects across state borders: Estimates using contiguous counties. *Review of Economics and Statistics*, 92(4), 945–964.
