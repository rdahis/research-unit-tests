---
id: synth-placebo-tests
name: "Synth: In-space and/or in-time placebo tests reported"
methodology:
  - synth
scope:
  - paper
severity: blocker
clarity: heuristic
tags: [identification, placebo, falsification, synthetic-control]
author: rdahis
version: 1
---

## What to Check

Synthetic control papers must report placebo tests to assess whether the estimated effect is unusually large relative to what would be obtained by chance. Standard placebo approaches are: (1) in-space placebos (apply the same method to each donor unit as if it were treated), and (2) in-time placebos (shift the treatment date to a pre-treatment period and check for a spurious effect).

## How to Check

1. **In-space placebos**: Check whether the paper iterates the synthetic control over all donor units, treating each as if it had received the treatment. The resulting distribution of placebo effects is compared to the treated unit's effect. The treated unit's post-treatment MSPE ratio should be large relative to the distribution.
   - A common visual: a "spaghetti plot" showing the treated unit's path alongside all placebo paths.
   - A common statistic: the ratio of post-treatment MSPE to pre-treatment MSPE for the treated unit, compared to the same ratio for all donor units. A p-value is the rank of the treated unit in this distribution.

2. **In-time placebos**: Check whether the paper applies the synthetic control with a fake treatment date in the pre-period. The synthetic control should closely track the treated unit before the fake treatment date, and the estimated "effect" should be near zero.

3. Assess the result: Is the treated unit's effect large relative to the placebo distribution? Is the in-time placebo near zero?

## Pass Condition

At least one placebo test (in-space or in-time) is reported. For in-space: the treated unit ranks near the top of the MSPE ratio distribution (informally p < 0.10). For in-time: the placebo effect is near zero.

## Failure Examples

1. **No placebo tests**: Paper reports synthetic control estimates and a pre-treatment fit plot but no placebo analysis. Fails — inference requires the placebo distribution.
2. **Poor pre-treatment fit excluded from donor pool**: Several donor units have very poor pre-treatment fit (high pre-MSPE) and are excluded from the in-space placebo. This inflates the p-value. Fails if exclusions are not justified and disclosed.
3. **In-time placebo shows large pre-period effect**: The fake treatment date 3 years before actual treatment produces an effect of comparable magnitude to the main result. Fails — the main estimate is not distinguishable from noise.

## References

- Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for comparative case studies. *Journal of the American Statistical Association*, 105(490), 493–505.
- Cavallo, E., Galiani, S., Noy, I., & Pantano, J. (2013). Catastrophic natural disasters and economic growth. *Review of Economics and Statistics*, 95(5), 1549–1561.
