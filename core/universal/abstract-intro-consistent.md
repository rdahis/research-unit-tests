---
id: universal-abstract-intro-consistent
name: "Abstract, introduction, and results internally consistent"
methodology:
  - universal
scope:
  - paper
severity: blocker
clarity: heuristic
tags: [consistency, abstract, introduction, framing]
author: rdahis
version: 1
---

## What to Check

The abstract, introduction, and results sections must tell the same story. Inconsistencies arise when papers are revised iteratively — a result gets updated but the abstract is not. Inconsistencies mislead readers and signal incomplete revision. Referees catch these and they damage the paper's credibility.

## How to Check

Check consistency along four dimensions:

1. **Quantitative claims**: Numbers stated in the abstract must match the main results tables. Check: the size of the main effect, the sample size, and any specific statistics cited in the abstract (e.g., "a 12% increase in wages").

2. **Direction and significance**: If the abstract says "we find a positive effect," the main coefficient must be positive and statistically significant. If the abstract says "we find no effect," the main result must be statistically insignificant.

3. **Sample and context**: The sample description in the abstract (country, time period, population) must match the data section. Example: abstract says "using data from 2000–2015" but the data section says the main sample is 2005–2015.

4. **Contribution framing**: The contribution stated in the introduction ("this paper is the first to...") must be consistent with the claims in the paper itself. If the intro says "the first causal estimate," the paper must use a credibly causal identification strategy — not OLS with controls.

## Pass Condition

All four dimensions are consistent across abstract, introduction, and results. No quantitative claims in the abstract that do not appear in the tables.

## Failure Examples

1. **Number mismatch**: Abstract states "a 15% increase in earnings." Table 2 column (1) shows a coefficient of 0.11, which the paper interprets as approximately 11%. Fails.
2. **Significance mismatch**: Introduction says "we find strong evidence that X affects Y." Main specification in Table 3 shows p = 0.09. The paper defines significance at 5%. "Strong evidence" in the introduction contradicts a marginally insignificant result. Fails.
3. **Sample period inconsistency**: Abstract says "using 20 years of data." Data section says "our sample runs from 2000 to 2018" (18 years) and notes that 2 years are dropped due to missing data. The abstract overstates the data coverage. Fails.
4. **Causal language without causal design**: Introduction claims "we identify the causal effect of education on earnings." The empirical section uses OLS with individual controls and no instrument, DiD, or RDD. Causal claim in the introduction is inconsistent with the identified design. Fails.
