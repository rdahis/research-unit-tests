---
id: iv-first-stage-f-stat
name: "IV: First-stage F-statistic reported and sufficient"
methodology:
  - iv
scope:
  - paper
severity: blocker
clarity: deterministic
tags: [identification, weak-instruments, first-stage]
author: rdahis
version: 1
---

## What to Check

Every IV paper must report the first-stage F-statistic for instrument strength. A weak instrument produces biased IV estimates that can be worse than OLS. The conventional threshold of F > 10 (Stock & Yogo, 2005) is widely used, though more recent guidance suggests higher thresholds for inference robustness.

## How to Check

1. Locate the first-stage regression results. They must be shown explicitly — either as a full first-stage table or as a row in the main IV table.
2. Check that the F-statistic for the excluded instrument(s) is reported. "F-statistic" refers to the F-test for joint significance of all excluded instruments in the first stage, not the overall regression F.
3. Evaluate the reported F against thresholds:
   - F < 10: weak instruments; fails unless addressed with weak-IV robust inference (Anderson-Rubin, conditional likelihood ratio test)
   - 10 ≤ F < 20: borderline; flag as `warning`; robust inference recommended
   - F ≥ 20: strong; passes
4. For multiple endogenous variables, check that the Cragg-Donald or Kleibergen-Paap statistic is reported and compared against Stock-Yogo critical values.
5. If inference robust to weak instruments is used (Anderson-Rubin confidence sets, conditional likelihood ratio), the F threshold requirement is relaxed — the paper must state this explicitly.

## Pass Condition

First-stage F-statistic (or equivalent) is reported. F ≥ 10 OR weak-IV robust inference method is used and stated.

## Failure Examples

1. **F not reported**: Table header says "IV estimates" but only the second-stage coefficient is shown. No first-stage table anywhere in paper or appendix. Fails.
2. **F = 6.2, no robust inference**: Paper reports F-statistic of 6.2 and proceeds with standard 2SLS inference. No Anderson-Rubin or other weak-IV robust test. Fails.
3. **F reported but for wrong test**: Paper reports "R² = 0.42 in the first stage" but no F-statistic. R² does not measure instrument strength. Fails.

## Notes

- The F > 10 rule is a rule of thumb from Stock & Yogo (2005) for 10% maximal IV bias relative to OLS with one endogenous variable. Lee et al. (2022) recommend F > 104.7 for valid t-tests at 5% significance. Context matters: use judgment on which threshold is appropriate.
- For just-identified IV (one instrument, one endogenous variable), the F-statistic from the first stage is equivalent to the t-statistic squared.

## References

- Stock, J. H., & Yogo, M. (2005). Testing for weak instruments in linear IV regression. In *Identification and Inference for Econometric Models*. Cambridge University Press.
- Lee, D. S., McCrary, J., Moreira, M. J., & Porter, J. (2022). Valid t-ratio inference for IV. *American Economic Review*, 112(10), 3260–3290.
- Andrews, I., Stock, J. H., & Sun, L. (2019). Weak instruments in instrumental variables regression. *Annual Review of Economics*, 11, 727–753.
