---
id: universal-robustness-section
name: "Main results accompanied by robustness checks"
methodology:
  - universal
scope:
  - paper
severity: warning
clarity: heuristic
tags: [robustness, sensitivity, specification]
author: rdahis
version: 1
---

## What to Check

Every empirical paper should demonstrate that its main findings are not driven by a specific modeling choice, sample restriction, or outlier. A robustness section (or robustness tables in the appendix) shows that results hold across reasonable alternatives. Without robustness checks, a reader cannot distinguish a stable finding from one that depends on a particular specification.

## How to Check

1. Check whether the paper includes a robustness section or table. It may appear in the main text or appendix.
2. Evaluate the quality and relevance of the robustness checks:
   - **Alternative specifications**: different control sets, different functional forms, different fixed effects structures.
   - **Alternative samples**: dropping outliers, restricting to a more homogeneous sub-sample, using a different time period.
   - **Alternative outcome definitions**: if the main outcome is an index, show results for component outcomes; if it is log-transformed, show levels.
   - **Alternative identification choices**: different bandwidth (RDD), different clustering level, different instrument.
3. Assess whether the robustness checks address the most important threats to the main specification — not just easy variations that are unlikely to change results.
4. Check whether results change meaningfully across the robustness checks. If they do, the paper must discuss which specification is most credible and why.

## Pass Condition

At least three substantively distinct robustness checks are reported. Main results hold (same sign, similar magnitude, significant at conventional levels) across the majority of checks. Any exceptions are discussed.

## Failure Examples

1. **No robustness checks**: Paper reports one main specification and concludes. No alternative specifications in main text or appendix. Fails.
2. **Trivial robustness only**: Robustness table shows the main result with and without a single control variable. This is not a meaningful test of stability. Fails.
3. **Sign flip in robustness, unexplained**: One robustness specification reverses the sign of the main coefficient. Paper acknowledges this in a footnote as "sensitive to this specification" and proceeds to emphasize the main result. Fails — the instability requires explanation and adjudication.

## Notes

- Severity is `warning` not `blocker` because a paper without robustness checks can still present a valid estimate — it is just less convincing. Referees will request robustness checks; the paper should include them proactively.
- Specification curves (Simonsohn et al., 2020) are the state-of-the-art for comprehensive robustness. Not required but recommended for papers where specification choices are numerous.

## References

- Simonsohn, U., Simmons, J. P., & Nelson, L. D. (2020). Specification curve analysis. *Nature Human Behaviour*, 4(11), 1208–1214.
- Lu, X., & White, H. (2014). Robustness checks and robustness tests in applied economics. *Journal of Econometrics*, 178, 194–206.
