---
id: universal-contribution-is-new
name: "Contribution is new relative to existing literature"
methodology:
  - universal
scope:
  - paper
  - proposal
severity: warning
clarity: judgment
tags: [contribution, literature, novelty]
author: rdahis
version: 1
---

## What to Check

The paper's main contribution must be genuinely new: it should answer a question, establish a fact, or provide a tool that does not already exist in the published or working-paper literature. "New" does not mean orthogonal to all prior work — it means the specific claim being made has not already been established.

## How to Check

1. Identify the paper's stated contribution(s). These should appear in the introduction, typically in a bulleted list or a paragraph beginning "This paper contributes..."
2. For each contribution, search Google Scholar, SSRN, NBER, and EconLit for papers making the same or closely related claim. Use the key outcome variable, the setting, and the methodology as search terms.
3. Evaluate whether the claimed novelty holds along (1) the question, (2) the setting/context, or (3) the method:
   - **Novelty of question**: Is the causal or descriptive question new? Or has it been answered for the same or a very similar context?
   - **Novelty of setting**: Is the contribution primarily that it answers an existing question in a new country, time period, or population? This is weaker novelty.
   - **Novelty of method**: Does the paper develop a new identification strategy, estimator, or data source that enables answering a previously unanswerable question? This is strong novelty.
4. Check whether the literature review in the paper itself identifies the closest prior work and explains precisely what is new relative to it.

## Pass Condition

The paper makes at least one contribution that is clearly new along the question, setting, or method dimension, and the introduction explicitly identifies the closest prior work and explains the gap. Setting-only novelty ("same question, new country") is acceptable but weak; flag as `warning` that the contribution may not clear top-journal bars.

## Failure Examples

1. **Already answered**: The paper estimates the effect of minimum wage on employment in Brazil. A 2021 paper in the *Journal of Development Economics* estimates the same effect using the same identification strategy and the same data source. The new paper adds two more years of data but no new variation. Fails: the marginal contribution is too small.
2. **No literature comparison**: The introduction lists four related papers but does not explain what is new relative to any of them. The reader cannot determine whether the contribution is new without doing the literature search themselves. Fails: novelty is not established, even if it exists.
3. **Novelty claimed but not delivered**: Paper claims to use "a novel IV strategy" but the IV is identical to one used in a well-known 2018 paper. The literature review does not cite that paper. Fails.

## Notes

- For proposals and early-stage projects, a full novelty check against working papers is expected; published papers only is insufficient.
- Novelty is necessary but not sufficient for a good contribution. See also: `universal-contribution-is-interesting`.

## References

- Hamermesh, D. S. (2013). Six decades of top economics publishing: Who and how? *Journal of Economic Literature*, 51(1), 162–172.
