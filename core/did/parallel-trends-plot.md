---
id: did-parallel-trends-plot
name: "DiD: Pre-trends visualization shown and plausible"
methodology:
  - did
scope:
  - paper
severity: blocker
clarity: heuristic
tags: [identification, visualization, pre-trends, parallel-trends]
author: rdahis
version: 1
---

## What to Check

A difference-in-differences paper must display a pre-trends plot showing the evolution of the outcome variable for treated and control groups before the treatment date. The parallel trends assumption — that treated and control groups would have followed the same trend absent treatment — is not testable, but visual evidence of pre-period parallel trends is the standard diagnostic and is required by referees at all major journals.

## How to Check

1. Locate the pre-trends or event-study plot. It may appear in the main body or in an appendix. Acceptable formats: (a) raw outcome means by group over time, (b) event-study coefficients with confidence intervals centered at zero in the omitted pre-period.
2. Assess the pre-period: are the pre-treatment trends visually parallel? "Parallel" means no systematic divergence — the gap between treated and control is approximately constant in the pre-period.
3. Check statistical tests: does the paper report a joint F-test or chi-squared test for pre-trends being zero? This is increasingly expected.
4. Check the number of pre-periods shown: at least 3 pre-treatment periods should be visible; fewer makes the parallel trends assumption difficult to assess.

## Pass Condition

A pre-trends or event-study plot is shown with at least 3 pre-treatment periods. Pre-treatment trends are visually parallel (no obvious divergence). A joint test for pre-trends is reported or the absence is noted as a limitation.

## Failure Examples

1. **No pre-trends plot**: Paper runs a standard 2x2 DiD regression and reports coefficients but shows no visual evidence of pre-trends. Referees at any top journal will request this. Fails.
2. **Diverging pre-trends**: Event-study plot shows treated group trending upward and control trending flat for 4 periods before treatment. Paper does not address this. Fails: parallel trends assumption is implausible.
3. **Only one pre-period**: Event-study plot shows t=-1 and t=0 as pre-treatment periods, with t=1, 2, 3 as post. One pre-period is insufficient to assess pre-trends. Fails.

## Notes

- For staggered treatment adoption designs (multiple cohorts), the standard 2x2 event-study is not appropriate. See `did-staggered-heterogeneous-effects` for the relevant check.
- When the outcome is binary or the panel is short, visual parallel trends may be harder to establish. In such cases, a placebo test (shifting treatment date back) can substitute.

## References

- Callaway, B., & Sant'Anna, P. H. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics*, 225(2), 200–230.
- Roth, J. (2022). Pre-test with caution: Event-study estimates after testing for parallel trends. *American Economic Review: Insights*, 4(3), 305–322.
- Sun, L., & Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. *Journal of Econometrics*, 225(2), 175–199.
