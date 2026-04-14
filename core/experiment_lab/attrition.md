---
id: experiment-lab-attrition
name: "Experiment: Attrition and differential attrition tested"
methodology:
  - experiment_lab
  - experiment_field
scope:
  - paper
severity: blocker
clarity: heuristic
tags: [attrition, endline, sample, randomization]
author: rdahis
version: 1
---

## What to Check

Attrition — the loss of subjects between baseline and endline — is a major threat to experimental validity. If attrition is differential (higher in treatment than control, or correlated with baseline characteristics), the endline sample is no longer randomized and the experiment's causal interpretation is compromised. Papers must report attrition rates and test whether attrition is differential.

## How to Check

1. Check whether the paper reports the attrition rate overall and separately by treatment arm.
2. Check whether the paper tests for differential attrition:
   - Regress an indicator for being missing at endline on treatment assignment. The coefficient should be near zero and insignificant.
   - This is sometimes shown in a table or noted in the text.
3. Assess the magnitude of attrition:
   - < 5%: low; likely not a threat even if differential.
   - 5–20%: moderate; differential attrition must be tested and addressed.
   - > 20%: high; even with balance, results may not generalize to the original sample; Lee (2009) bounds or MIPO analysis should be provided.
4. Check whether the paper provides Lee (2009) trimming bounds or Manski-type bounds when attrition is non-trivial. These show how large the effect would need to be to be consistent with a null result under worst-case attrition patterns.

## Pass Condition

Attrition rates reported by arm. Differential attrition tested and not significant, OR attrition is significant but addressed with bounds (Lee 2009 or equivalent). Overall attrition rate is reported.

## Failure Examples

1. **Attrition not reported**: Paper reports endline results without noting how many subjects were lost between baseline and endline. No attrition analysis anywhere. Fails.
2. **Differential attrition ignored**: Treatment group has 18% attrition; control group has 8%. Paper notes the difference but proceeds without bounds or discussion. Fails.
3. **Attrition exceeds 30%, no bounds**: 35% of subjects are missing at endline. Paper argues "attrition is random" without testing it. Fails — without bounds, the main result is uninformative under extreme attrition scenarios.

## References

- Lee, D. S. (2009). Training, wages, and sample selection: Estimating sharp bounds on treatment effects. *Review of Economic Studies*, 76(3), 1071–1102.
- McKenzie, D. (2012). Beyond baseline and follow-up: The case for more T in experiments. *Journal of Development Economics*, 99(2), 210–221.
