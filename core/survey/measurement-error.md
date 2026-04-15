---
id: survey-measurement-error
name: "Survey: Measurement error in self-reported variables acknowledged"
methodology:
  - survey
scope:
  - paper
severity: warning
clarity: judgment
tags: [measurement-error, self-report, validity]
author: rdahis
version: 1
---

## What to Check

Self-reported variables — income, health status, hours worked, consumption, attitudes — are subject to measurement error that attenuates OLS estimates toward zero (classical) or introduces correlated bias (non-classical). Papers relying on self-reported key variables must acknowledge this limitation and ideally quantify or bound its impact.

## How to Check

1. Identify the key independent and dependent variables. Which are self-reported?
2. For each self-reported key variable, look for:
   - **Validation against external records**: comparison of reported values to administrative data (tax records, insurance claims, employer records). If available and used, this is strong evidence of measurement quality.
   - **Acknowledgment of attenuation bias**: if the variable is an independent variable with classical measurement error, coefficient estimates are biased toward zero; the paper should note that estimates are lower bounds.
   - **Use of validated scales**: recognized psychometric instruments (PHQ-9 for depression, WHODAS for disability, PANAS for affect) carry their own published reliability evidence.
   - **Anchoring vignettes or list experiments**: for sensitive or socially desirable behaviors, check whether special elicitation techniques were used.
3. Assess whether the paper makes strong causal or precision claims based on a variable known to be heavily mismeasured (e.g., claiming a precise effect size for self-reported income without any mention of measurement error).

## Pass Condition

The paper acknowledges measurement error for key self-reported variables, either by citing validation evidence, noting the direction of expected bias, or referencing the validated instrument used. Papers that use administrative validation data or formally adjust for measurement error receive full marks.

## Failure Examples

1. **No acknowledgment**: Paper estimates the effect of self-reported alcohol consumption on productivity without any mention of underreporting bias. Alcohol consumption is well-known to be substantially under-reported in surveys. Fails.
2. **Precision without qualification**: Paper reports an effect of 0.003 standard deviations and emphasizes precision, when the key variable is self-reported subjective well-being with no validation evidence. The implied precision is not warranted. Fails.
3. **Known low-reliability scale**: Paper uses a single-item self-reported measure of "health" as the primary outcome without acknowledging reliability issues, despite validated multi-item scales being available. Fails.

## References

- Bound, J., Brown, C., & Mathiowetz, N. (2001). Measurement error in survey data. *Handbook of Econometrics*, 5, 3705–3843.
- Meyer, B. D., Mok, W. K., & Sullivan, J. X. (2015). Household surveys in crisis. *Journal of Economic Perspectives*, 29(4), 199–226.
