---
id: experiment-lab-power-calculation
name: "Experiment: Power calculation reported or MDE stated"
methodology:
  - experiment_lab
  - experiment_field
scope:
  - paper
  - proposal
severity: warning
clarity: heuristic
tags: [power, sample-size, mde, design]
author: rdahis
version: 1
---

## What to Check

Experimental papers should report a power calculation justifying the sample size, or at minimum report the minimum detectable effect (MDE) given the achieved sample. Without this, readers cannot distinguish null results due to lack of power from null results due to genuinely zero effects. For proposals, a power calculation is required to assess whether the experiment is worth running.

## How to Check

1. Check whether the paper reports a power calculation. For proposals, this should use assumed effect sizes and variance from pilot data or prior literature. For completed papers, the calculation may be ex-ante (from the pre-registration) or ex-post (the MDE given the actual sample).
2. Verify the key inputs are stated: assumed effect size (or MDE), standard deviation of the outcome, significance level (α), and power (1−β, typically 80%).
3. For null results specifically: check whether the paper reports the MDE and assesses whether the true effect could plausibly be smaller than the MDE. A null result with a large MDE is uninformative.
4. Check for pre-registration: was the power calculation pre-specified? Post-hoc power calculations can be manipulated.

## Pass Condition

Power calculation or MDE is reported with stated inputs. For null results, the MDE is assessed relative to the effect size the study was designed to detect and relative to effects that would be policy-relevant.

## Failure Examples

1. **No power calculation, null result**: Paper reports no effect of a training program. Sample size is N = 80 per arm. No power calculation. The MDE for this sample at 80% power would be approximately 0.4 standard deviations — a large effect. The paper cannot distinguish "no effect" from "effect smaller than 0.4 SD." Fails as a warning.
2. **Post-hoc power inflation**: Paper reports that "the study was powered to detect a 0.2 SD effect." This is only true if the assumed variance matched the actual outcome variance. If the outcome variance was higher than assumed, the actual MDE was larger. Paper does not check this. Fails.
3. **Proposal with no power calculation**: Research proposal calls for a randomized field experiment with N = 500 households without any power calculation. Fails — it is not possible to assess whether the study is worth running.

## Notes

- Severity is `warning` not `blocker` because the absence of a power calculation does not invalidate reported effects — it only limits the informativeness of null results.
- For pre-registered experiments, the pre-registered power calculation is authoritative. Deviations from pre-registered sample sizes should be explained.

## References

- Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum.
- Duflo, E., Glennerster, R., & Kremer, M. (2007). Using randomization in development economics research: A toolkit. *Handbook of Development Economics*, 4, 3895–3962.
