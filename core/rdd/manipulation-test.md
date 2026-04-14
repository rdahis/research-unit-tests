---
id: rdd-manipulation-test
name: "RDD: No manipulation of running variable (density test)"
methodology:
  - rdd
scope:
  - paper
severity: blocker
clarity: heuristic
tags: [identification, manipulation, density, sorting, mccrary]
author: rdahis
version: 1
---

## What to Check

The RDD identification assumption requires that units cannot precisely manipulate their value of the running variable to sort across the cutoff. If manipulation is present, units just above and below the cutoff are systematically different (sorted), and the local continuity assumption fails. The standard diagnostic is a density test showing no discontinuity in the density of the running variable at the cutoff.

## How to Check

1. Check whether the paper reports a density test. Accepted methods:
   - McCrary (2008) test — widely used, acceptable
   - Cattaneo, Jansson & Ma (2020) `rddensity` test — preferred by current literature
2. Check the result: the null hypothesis is continuity of the density at the cutoff. A rejection (p < 0.05) is evidence of manipulation.
3. Check the visual: a histogram or density plot of the running variable is expected. Look for bunching (excess mass) just above or below the cutoff.
4. If the density test rejects, check how the paper handles it:
   - Acceptable responses: donut-hole robustness (dropping observations within ε of cutoff), subsample analysis, or a theoretical argument for why sorting does not threaten identification.
   - Unacceptable: ignoring the rejection.

## Pass Condition

A density test is reported and does not reject continuity at conventional significance levels (p > 0.05), OR a rejection is acknowledged and addressed via donut-hole or theoretical argument.

## Failure Examples

1. **No density test**: Paper uses an RDD design based on a vote share cutoff in elections but shows no density test. In electoral settings, manipulation of vote margins is a known concern. Fails.
2. **Test rejects, paper ignores it**: McCrary test produces p = 0.012. Paper footnotes it as "the density test is not significant at the 1% level" (technically true) and proceeds without further discussion. This is misleading and inadequate. Fails.
3. **Bunching visible but not tested**: Histogram shows a clear spike in observations just above the cutoff. No formal test reported. Fails.

## Notes

- In settings where manipulation is implausible by design (e.g. exact birthdate cutoffs for school entry, discontinuities in administrative formulas), the density test can be replaced by a theoretical argument. The argument must be explicit.
- The Cattaneo et al. (2020) `rddensity` test is preferred over McCrary because it uses local polynomial methods consistent with the main RDD estimation.

## References

- McCrary, J. (2008). Manipulation of the running variable in the regression discontinuity design: A density test. *Journal of Econometrics*, 142(2), 698–714.
- Cattaneo, M. D., Jansson, M., & Ma, X. (2020). Simple local polynomial density estimators. *Journal of the American Statistical Association*, 115(531), 1449–1455.
