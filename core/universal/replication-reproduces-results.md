---
id: universal-replication-reproduces-results
name: "Replication package reproduces all main results"
methodology:
  - universal
scope:
  - replication
severity: blocker
clarity: deterministic
tags: [replication, transparency, code]
author: rdahis
version: 1
---

## What to Check

The replication package must, when run from scratch in a clean environment, reproduce all tables and figures reported as main results in the paper. This is the most fundamental test of research integrity and credibility.

## How to Check

1. Locate the master script (often `main.do`, `run_all.R`, `main.py`, or similar). If no master script exists, that is itself a failure.
2. Run the master script in a clean environment (fresh R/Stata/Python session, no pre-loaded objects, no pre-existing output files).
3. Compare all output files (tables in `.tex`/`.csv`, figures as `.pdf`/`.png`) to the paper:
   - Coefficients must match to at least 2 significant figures.
   - Standard errors must match to at least 2 significant figures.
   - N values must match exactly.
   - Stars/significance indicators must match.
4. If the package requires proprietary or restricted data, check that: (a) the package clearly documents what data are needed, (b) synthetic or publicly available data are provided where possible, and (c) the code is otherwise complete and runnable.

## Pass Condition

All main tables and figures in the paper are reproduced exactly (within floating-point tolerance) by running the replication package from scratch. Minor formatting differences (font, color) are acceptable; numerical differences are not.

## Failure Examples

1. **No master script**: Package contains many individual scripts with no documented execution order. A reviewer cannot determine which scripts produce which outputs. Fails.
2. **Hard-coded paths**: Script begins with `setwd("/Users/author/Desktop/project")`. Fails to run in any other environment without manual editing.
3. **Numerical mismatch**: Table 2 column (3) reports a coefficient of 0.142 in the paper, but running the code produces 0.089. No explanation provided. Fails.
4. **Missing scripts**: The code produces Tables 1–4 and Figures 1–2, but the paper also reports Table A.1 in the appendix. No code for the appendix table exists in the package. Fails.

## References

- Vilhuber, L. (2020). Report by the AEA Data Editor. *AEA Papers and Proceedings*, 110, 764–775.
- Chang, A. C., & Li, P. (2015). Is economics research replicable? Sixty published papers from thirteen journals say "usually not." Finance and Economics Discussion Series 2015-083.
