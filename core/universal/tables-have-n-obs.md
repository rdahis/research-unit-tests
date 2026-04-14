---
id: universal-tables-have-n-obs
name: "Regression tables report number of observations"
methodology:
  - universal
scope:
  - paper
severity: blocker
clarity: deterministic
tags: [tables, transparency, replication]
author: rdahis
version: 1
---

## What to Check

Every regression table must report the number of observations (N) for each column. N is the most basic check on whether the estimation sample matches the described sample. Missing N forces readers to guess; it also prevents catching errors in sample selection.

## How to Check

1. Identify all tables in the paper that report regression coefficients (OLS, IV, DiD, RDD, probit, etc.).
2. For each such table, check whether each column (specification) reports N.
3. N may appear as a row labeled "Observations", "N", "Obs.", or similar — all are acceptable.
4. Check that N values are plausible given the described sample: if the paper says the sample covers 500 municipalities over 10 years, a balanced panel would have N ≈ 5,000. Deviations should be explained (unbalanced panel, missing data, subsample).

## Pass Condition

Every regression column in every regression table reports N, and the reported N values are consistent with the sample description in the data section.

## Failure Examples

1. **Missing N row**: A table with five columns showing coefficients, standard errors, and fixed effects indicators, but no row for observations. Fails: reader cannot verify sample.
2. **N present but implausible**: Paper describes a sample of 1,200 firms, but Table 3 shows N = 40,000. No footnote explains the discrepancy. Fails: inconsistency suggests a sample selection error or mislabeled table.
3. **N only in the last column**: Columns 1–4 are blank in the observations row; N is reported only in column 5. Fails: each specification may use a different sample; each column needs its own N.

## References

- Christensen, G., & Miguel, E. (2018). Transparency, reproducibility, and the credibility of economics research. *Journal of Economic Literature*, 56(3), 920–980.
