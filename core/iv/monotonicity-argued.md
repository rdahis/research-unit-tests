---
id: iv-monotonicity-argued
name: "IV: Monotonicity assumption explicitly argued"
methodology:
  - iv
scope:
  - paper
severity: warning
clarity: judgment
tags: [monotonicity, late, compliers, defiers]
author: rdahis
version: 1
---

## What to Check

The LATE (Local Average Treatment Effect) interpretation of IV requires not only instrument relevance and exclusion, but also **monotonicity**: the instrument weakly increases (or weakly decreases) treatment take-up for every unit — no "defiers" (units who take up treatment when the instrument is off and forego it when the instrument is on). Monotonicity is an empirically untestable assumption that requires institutional or economic reasoning.

## How to Check

1. Identify the instrument. Is there any mechanism by which the instrument could *decrease* treatment for some units while *increasing* it for others?
   - Example instrument: distance to college. Monotonicity requires that being close to college never *reduces* college attendance for any individual. This is generally defensible.
   - Example where monotonicity is questionable: a lottery instrument where some units who would have sought treatment voluntarily now rely on the lottery and reduce their effort to obtain treatment independently.
2. Look for an explicit statement of the monotonicity assumption and an argument for why it holds in the specific context. The argument should address potential defiers.
3. Check whether the instrument is binary or continuous:
   - **Binary instrument**: monotonicity means treatment take-up is weakly monotone in Z ∈ {0, 1}.
   - **Continuous instrument**: monotonicity (sometimes called "uniformity") means the same direction of response for all units, which is harder to argue and rarely tested.
4. For papers using multiple instruments, check whether the "unordered monotonicity" assumption (Heckman & Pinto 2018) is discussed when instruments may interact.

## Pass Condition

The monotonicity assumption is stated explicitly. An argument is provided for why no (or negligible) defiers exist in the specific empirical context, based on institutional knowledge or economic reasoning.

## Failure Examples

1. **Omitted**: Paper uses a shift-share (Bartik) instrument. Exclusion restriction is carefully argued. Monotonicity is never mentioned, though the direction of response to local labor demand shocks may plausibly vary by sector. Fails.
2. **Asserted without argument**: Paper states "we assume monotonicity holds" in a footnote with no justification. Fails.
3. **Questionable context**: Paper instruments health insurance take-up with eligibility cutoffs. Argues exclusion restriction but does not address whether some eligible individuals already had private insurance and were crowded out (potential defiers). Fails.

## References

- Imbens, G. W., & Angrist, J. D. (1994). Identification and estimation of local average treatment effects. *Econometrica*, 62(2), 467–475.
- Heckman, J. J., & Pinto, R. (2018). Unordered monotonicity. *Econometrica*, 86(1), 1–35.
- Angrist, J. D., & Pischke, J. S. (2009). *Mostly Harmless Econometrics*. Princeton University Press. Chapter 4.4.
