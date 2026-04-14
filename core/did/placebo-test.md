---
id: did-placebo-test
name: "DiD: Placebo/falsification test reported"
methodology:
  - did
scope:
  - paper
severity: warning
clarity: heuristic
tags: [identification, placebo, falsification, robustness]
author: rdahis
version: 1
---

## What to Check

A DiD paper should report at least one falsification or placebo test — an additional check that the estimated effect is not spurious. Standard placebo tests include: (1) shifting the treatment date to a period before actual treatment and verifying the "effect" is zero, (2) applying the treatment indicator to an outcome that should not be affected by the treatment, or (3) assigning treatment to units that were not actually treated.

## How to Check

1. Check whether any placebo or falsification test is reported in the main paper or appendix.
2. Identify which type of placebo is used:
   - **Temporal placebo**: treatment date shifted back by k periods. Estimated effect should be near zero and statistically insignificant in the pre-period.
   - **Outcome placebo**: a second outcome variable that should not respond to treatment is estimated with the same design. Effect should be near zero.
   - **Unit placebo**: treatment assigned to a "donor" group that was never treated. Effect should be near zero.
3. Evaluate the plausibility of the placebo: is the fake treatment date sufficiently far from the real one? Is the placebo outcome genuinely unrelated to treatment?
4. Assess the result: is the placebo estimate small and statistically insignificant? A significant placebo estimate is a red flag for the main identification.

## Pass Condition

At least one credible placebo test is shown. The placebo estimate is small (near zero) and statistically insignificant, or the paper provides a convincing explanation for why a non-zero placebo is not problematic.

## Failure Examples

1. **No placebo test**: Paper runs a DiD and reports parallel trends visually but no falsification check. Fails as `warning` — the test is best practice, not strictly required, but expected at most journals.
2. **Temporal placebo too close to treatment**: Paper shifts the treatment date back by only one period. With one pre-period as placebo, there is little power to detect pre-trends and the test is uninformative. Fails.
3. **Significant placebo, no discussion**: Placebo regression shows a coefficient of −0.18 (p < 0.05) on the fake treatment date. Paper does not acknowledge or explain this. Fails: the main identification is likely compromised.

## Notes

- In staggered DiD designs, the event-study plot itself serves as a partial placebo (pre-period coefficients should be near zero). But a separate placebo with a different fake treatment date or outcome adds independent evidence.
- Severity is `warning` rather than `blocker` because referees will ask for this, but absence alone does not invalidate the paper the way a failed placebo does.
