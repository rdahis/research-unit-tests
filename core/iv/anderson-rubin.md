---
id: iv-anderson-rubin
name: "IV: Weak-instrument-robust inference used when F-statistic is borderline"
methodology:
  - iv
scope:
  - paper
severity: warning
clarity: deterministic
tags: [weak-instruments, anderson-rubin, inference, f-statistic]
author: rdahis
version: 1
---

## What to Check

Standard 2SLS confidence intervals are valid only when the instrument is strong. When the first-stage F-statistic falls below the Stock-Yogo (2005) critical values — F < 104.7 for a single instrument at 10% maximal IV size distortion — 2SLS confidence intervals can have actual coverage well below 95%. In these cases, weak-instrument-robust inference (Anderson-Rubin, conditional likelihood ratio, or Montiel Olea-Pflueger effective F) is required.

Note: `iv-first-stage-f-stat` tests whether F > 10 (the conventional minimum). This test is triggered when F is above 10 but below the Stock-Yogo threshold (F ∈ [10, 104.7] for one instrument), or when the paper relies only on the conventional threshold without addressing higher-bar criteria.

## How to Check

1. Identify the first-stage F-statistic. If F < 10, this is already a failure under `iv-first-stage-f-stat`; that test takes precedence.
2. If 10 ≤ F < 104.7 (single instrument): check whether the paper:
   - Reports Anderson-Rubin (1949) confidence intervals (projection-based, valid regardless of instrument strength).
   - Uses the conditional likelihood ratio (CLR) test (Moreira 2003), which is uniformly most powerful among similar tests.
   - Reports the Montiel Olea–Pflueger (2013) effective F-statistic and compares it to their critical values.
   - Uses LIML or k-class estimators as a robustness check (LIML is median-unbiased under weak instruments).
3. For multiple instruments: the Stock-Yogo threshold differs (higher for more instruments). With 5 instruments at 10% maximal size, the threshold is F > 26.9.
4. If F ≥ 104.7 (single instrument): standard 2SLS is valid; this test passes.

## Pass Condition

Either (a) F ≥ 104.7 (single instrument) and standard 2SLS is used; or (b) F < 104.7 but the paper uses weak-instrument-robust inference (Anderson-Rubin CIs, CLR, or Montiel Olea-Pflueger effective F) and clearly reports results under both approaches.

## Failure Examples

1. **F = 11, standard 2SLS only**: Paper reports F = 11.3 and concludes "instruments are strong (F > 10)." Uses 2SLS CIs without further analysis. F = 11.3 is well below the Stock-Yogo threshold of 104.7 for 10% size; 2SLS CIs may be severely distorted. Fails.
2. **Multiple instruments, wrong threshold**: Paper uses 3 instruments, reports F = 18, and cites the single-instrument threshold of 10. The Stock-Yogo threshold for 3 instruments at 10% maximal size is F > 13.91 — barely passed — but the paper uses the wrong reference table. Should be flagged.
3. **Only LIML, no AR CIs**: Paper reports LIML but not Anderson-Rubin confidence intervals. LIML point estimates are more robust but LIML CIs still rely on asymptotic approximations that are unreliable under weak instruments.

## References

- Stock, J. H., & Yogo, M. (2005). Testing for weak instruments in linear IV regression. In D. W. K. Andrews & J. H. Stock (Eds.), *Identification and Inference for Econometric Models*. Cambridge University Press.
- Montiel Olea, J. L., & Pflueger, C. (2013). A robust test for weak instruments. *Journal of Business & Economic Statistics*, 31(3), 358–369.
- Anderson, T. W., & Rubin, H. (1949). Estimation of the parameters of a single equation in a complete system of stochastic equations. *Annals of Mathematical Statistics*, 20(1), 46–63.
- Moreira, M. J. (2003). A conditional likelihood ratio test for structural models. *Econometrica*, 71(4), 1027–1048.
