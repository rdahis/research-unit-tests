---
id: synth-donor-pool-selection
name: "Synth: Donor pool selection justified"
methodology:
  - synth
scope:
  - paper
severity: blocker
clarity: judgment
tags: [identification, donor-pool, synthetic-control]
author: rdahis
version: 1
---

## What to Check

The synthetic control method constructs a counterfactual by weighting untreated units (the donor pool). The choice of which units to include in the donor pool is a researcher degree of freedom that can substantially affect results. The paper must justify which units are included and excluded.

## How to Check

1. Identify which units comprise the donor pool. Is this stated explicitly?
2. Evaluate the inclusion criteria. Acceptable justifications:
   - All untreated units in the same geographic/institutional context (e.g., all US states except the treated one).
   - Units restricted by economic or institutional comparability (e.g., excluding units with structural breaks, or units that received a related treatment).
   - Pre-specified inclusion rules (e.g., units with at least N years of data).
3. Check for exclusion of units that might make the treated unit look bad (cherry-picking the donor pool to improve fit). Red flag: donor pool excludes plausible comparators without stated reason.
4. Check pre-treatment fit: does the synthetic control closely match the treated unit's pre-treatment outcome path? Report the pre-treatment MSPE (mean squared prediction error) or visual fit.

## Pass Condition

Donor pool inclusion/exclusion criteria are stated explicitly and justified on economic or institutional grounds, not on post-hoc fit considerations. Pre-treatment fit is shown visually and/or via MSPE.

## Failure Examples

1. **Undisclosed exclusions**: Paper uses US state-level data but excludes several large states from the donor pool. No reason given. Fails — donor pool may have been chosen to improve synthetic fit.
2. **No pre-treatment fit shown**: Paper reports the synthetic control result but does not show how closely the pre-treatment path was matched. Fails.
3. **Fit-based donor pool**: Paper reports "we selected the 10 best-fitting donor units." Optimizing the donor pool on fit is a form of overfitting that inflates confidence in the post-treatment result. Fails unless the paper uses the Synthetic Difference-in-Differences or another method robust to this.

## References

- Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for comparative case studies. *Journal of the American Statistical Association*, 105(490), 493–505.
- Abadie, A. (2021). Using synthetic controls: Feasibility, data requirements, and methodological aspects. *Journal of Economic Literature*, 59(2), 391–425.
