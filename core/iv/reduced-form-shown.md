---
id: iv-reduced-form-shown
name: "IV: Reduced form reported alongside IV estimates"
methodology:
  - iv
scope:
  - paper
severity: warning
clarity: deterministic
tags: [transparency, reduced-form, iv]
author: rdahis
version: 1
---

## What to Check

The reduced form — the regression of the outcome directly on the instrument, bypassing the endogenous variable — must be reported alongside IV estimates. The reduced form is transparent, requires no assumptions beyond instrument exogeneity, and allows readers to verify that the IV estimate is consistent with the underlying data. An IV estimate without a visible reduced form is opaque.

## How to Check

1. Check whether the paper reports a regression of the primary outcome on the instrument directly (with the same controls and fixed effects as the main specification).
2. Verify that the sign and significance of the reduced form is consistent with the IV estimate. The IV estimate equals the reduced form divided by the first stage, so: if the first stage is positive and the IV is positive, the reduced form must be positive.
3. Confirm the reduced form is not only in the appendix — for any IV paper, it belongs in or near the main results table.

## Pass Condition

Reduced form regression is reported in the main text or an immediately referenced table. Its sign and significance are consistent with the IV estimate and first stage.

## Failure Examples

1. **Reduced form absent**: Paper reports first stage and IV estimates in a three-panel table but omits the reduced form. Readers cannot assess whether the IV result is driven by a plausible signal or by a weak/noisy instrument. Fails.
2. **Inconsistent signs**: First-stage coefficient is positive (instrument increases treatment), IV estimate is positive (treatment increases outcome), but the reduced form coefficient is negative. This is arithmetically impossible and signals a coding error. Fails.
3. **Reduced form in appendix only, dismissed**: Reduced form is buried in appendix with the note "results available upon request." At the time of review it is not available. Fails.

## References

- Angrist, J. D., & Pischke, J.-S. (2009). *Mostly Harmless Econometrics*. Princeton University Press. Section 4.1.
