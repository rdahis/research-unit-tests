---
id: survey-response-rate
name: "Survey: Response rate reported and non-response bias addressed"
methodology:
  - survey
scope:
  - paper
severity: blocker
clarity: heuristic
tags: [non-response, external-validity, attrition]
author: rdahis
version: 1
---

## What to Check

The response rate determines who is observed. A low response rate does not automatically invalidate a survey study, but it requires explicit non-response analysis. Failure to report or address non-response leaves the reader unable to assess the representativeness of the sample.

## How to Check

1. Locate the data section. Is the overall response rate (or contact, cooperation, and refusal rates following AAPOR standards) reported?
2. Assess the response rate level:
   - Response rate ≥ 70%: minimal non-response concern; noting the rate is sufficient.
   - Response rate 40–70%: non-response analysis required. Look for comparison of respondents vs. non-respondents on characteristics available from sampling frame or administrative data.
   - Response rate < 40%: strong non-response analysis required. Look for follow-up surveys of non-respondents, bounding analysis (Manski bounds), or inverse probability weighting.
3. For panel surveys: check attrition rates over waves and whether differential attrition is analyzed (see also `experiment-lab-attrition`).
4. Check whether the paper makes population-level claims. If yes, the non-response analysis must be proportionally thorough.

## Pass Condition

Response rate is stated explicitly. If response rate < 70%, the paper includes non-response analysis comparing respondents to non-respondents on at least one external variable (from sampling frame, administrative data, or demographic census). Claims are appropriately scoped to the responding sample when non-response is high.

## Failure Examples

1. **Rate not reported**: Paper analyzes 1,200 survey respondents with no mention of how many were contacted or refused. Fails.
2. **Low rate, no analysis**: Paper reports 31% response rate and makes population-level claims without non-response analysis or qualification. Fails.
3. **Only total sample size**: Paper says "n = 800 respondents" but does not disclose the sampling frame size or approach rate, making the response rate impossible to calculate. Fails.

## References

- American Association for Public Opinion Research (AAPOR). (2023). *Standard Definitions: Final Dispositions of Case Codes and Outcome Rates for Surveys* (10th ed.).
- Groves, R. M., & Peytcheva, E. (2008). The impact of nonresponse rates on nonresponse bias. *Public Opinion Quarterly*, 72(2), 167–189.
