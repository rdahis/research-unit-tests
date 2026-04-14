---
id: experiment-field-spillovers
name: "Field experiment: Spillover effects addressed"
methodology:
  - experiment_field
scope:
  - paper
severity: blocker
clarity: judgment
tags: [spillovers, sutva, interference, field-experiment]
author: rdahis
version: 1
---

## What to Check

Field experiments — conducted in real-world settings with social interactions — are susceptible to spillover effects: treatment of some units may affect outcomes of untreated units nearby. If spillovers are present and ignored, the estimated ITT or ATE is a biased estimator of the direct treatment effect. Papers must address whether spillovers are plausible and, if so, test for them.

## How to Check

1. Assess whether spillovers are plausible in the study context. Key questions:
   - Do treatment and control units interact (same village, same workplace, same school)?
   - Is the treatment something that can diffuse (information, resources, behavior)?
   - Is the outcome something that can be affected through social interaction?

2. If spillovers are plausible, check whether the paper:
   - Uses a design that enables spillover estimation (two-stage randomization: randomize saturation across clusters, then individuals within clusters).
   - Tests for spillovers by estimating effects on control units as a function of their "exposure" to treated units.
   - Acknowledges the possibility and argues why spillovers are likely small or directionally clear.

3. Evaluate the SUTVA (Stable Unit Treatment Value Assumption) assumption. Does the paper state SUTVA? If SUTVA is assumed, is the assumption credible given the study context?

## Pass Condition

Either: (a) spillovers are demonstrably implausible given the study design and context, stated explicitly, OR (b) spillovers are tested and found negligible, OR (c) spillovers are estimated as part of the design (two-stage randomization or network design).

## Failure Examples

1. **Village-level experiment, spillovers ignored**: Paper randomizes treatment at the household level within villages. Treatment involves sharing information about government services. No discussion of whether treated households share information with control households in the same village. SUTVA is not stated or justified. Fails.
2. **Spillovers acknowledged but not tested**: Paper notes "there may be spillovers" in a footnote but presents no test. If spillovers are plausible, acknowledging them without testing is insufficient. Fails.
3. **SUTVA assumed without justification**: Paper states "we assume SUTVA holds" with no argument for why. In a dense social network, this assumption requires justification. Fails.

## Notes

- Lab and online experiments with no social interaction between subjects generally satisfy SUTVA by design. This test primarily applies to field experiments with naturally occurring social networks.
- Two-stage randomization designs (e.g., Baird et al., 2018) allow estimation of direct, indirect, and total effects — preferred when spillovers are anticipated at the design stage.

## References

- Hudgens, M. G., & Halloran, M. E. (2008). Toward causal inference with interference. *Journal of the American Statistical Association*, 103(482), 832–842.
- Baird, S., Bohren, J. A., McIntosh, C., & Özler, B. (2018). Optimal design of experiments in the presence of interference. *Review of Economics and Statistics*, 100(5), 844–860.
