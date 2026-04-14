---
id: rdd-bandwidth-sensitivity
name: "RDD: Estimates robust to bandwidth choice"
methodology:
  - rdd
scope:
  - paper
severity: blocker
clarity: heuristic
tags: [identification, bandwidth, robustness, local-linear]
author: rdahis
version: 1
---

## What to Check

RDD estimates are sensitive to bandwidth choice. The paper must show that results are not driven by the specific bandwidth selected — whether chosen by MSE-optimal selector (Imbens & Kalyanaraman, 2012; Calonico, Cattaneo & Titiunik, 2014) or manually. Sensitivity to bandwidth is one of the most common sources of fragility in RDD papers.

## How to Check

1. Identify the main bandwidth used. Is it data-driven (CCT, IK) or manually selected? Data-driven is preferred; manual requires justification.
2. Check whether a bandwidth sensitivity plot or table is shown. Standard practice: report estimates at 50%, 75%, 100%, 125%, and 150% of the main bandwidth, or show a plot of the point estimate and CI as a function of bandwidth.
3. Assess stability: do the estimates change sign or lose significance across the bandwidth range? Estimates that hold sign and approximate magnitude are robust.
4. Check the polynomial order: local linear (order 1) is the current standard. Higher-order polynomials are susceptible to overfitting near the boundary and are discouraged by recent literature (Gelman & Imbens, 2019).

## Pass Condition

Estimates are shown across multiple bandwidths (at minimum 3 values). Point estimates hold sign and approximate magnitude across bandwidth range. Local linear (order 1) is used or higher-order use is explicitly justified.

## Failure Examples

1. **Single bandwidth, no sensitivity**: Paper uses CCT-optimal bandwidth and shows only those results. No evidence that estimates are stable. Fails.
2. **Sign flip at narrower bandwidth**: Bandwidth sensitivity plot shows positive estimate at optimal bandwidth but negative at 75% of optimal. Paper proceeds without discussion. Fails.
3. **High-order polynomial without justification**: Paper uses 4th-order polynomial in the running variable. No reference to Gelman & Imbens (2019) or justification. Fails as a warning.

## Notes

- Donut-hole robustness (excluding observations very close to the cutoff) is an additional useful check for sorting/manipulation, but is separate from bandwidth sensitivity.
- For fuzzy RDD, bandwidth sensitivity applies to both the first stage and the reduced form separately.

## References

- Calonico, S., Cattaneo, M. D., & Titiunik, R. (2014). Robust nonparametric confidence intervals for regression-discontinuity designs. *Econometrica*, 82(6), 2295–2326.
- Gelman, A., & Imbens, G. (2019). Why high-order polynomials should not be used in regression discontinuity designs. *Journal of Business & Economic Statistics*, 37(3), 447–456.
- Imbens, G., & Kalyanaraman, K. (2012). Optimal bandwidth choice for the regression discontinuity estimator. *Review of Economic Studies*, 79(3), 933–959.
