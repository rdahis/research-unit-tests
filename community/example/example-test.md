---
id: example-your-test-id
name: "Short descriptive name for the test (≤ 80 chars)"
methodology:
  - universal          # replace with the applicable methodology key(s)
scope:
  - paper              # paper | proposal | replication
severity: warning      # blocker | warning | info
clarity: heuristic     # deterministic | heuristic | judgment
tags: [example, template]
author: your-github-handle
version: 1
---

## What to Check

One paragraph explaining the methodological principle behind this test. Why does this matter? What goes wrong when it is violated?

Keep this to 3–5 sentences. Cite a well-known reference if one exists.

## How to Check

Step-by-step instructions for a reviewer (human or AI agent) to evaluate this test:

1. First, look for X in the paper.
2. Then, check whether Y holds.
3. If the paper contains Z, assess whether it meets standard W.

Be specific about where to look (table headers, footnotes, appendix sections) and what constitutes a pass at each step.

## Pass Condition

State explicitly what the paper must do to pass this test. One or two sentences. This is the single criterion the reviewer uses to decide PASS vs. FAIL.

## Failure Examples

1. **Failure type 1**: Describe a concrete example of a paper that would fail. Include the specific pattern that triggers the failure. Fails.
2. **Failure type 2**: Another failure mode, ideally from a different cause. Fails.

## References

- Author, A., & Author, B. (Year). Title of paper. *Journal Name*, Volume(Issue), Pages.
- Include at least one peer-reviewed reference. Textbooks are acceptable. Working papers are acceptable if widely cited.
