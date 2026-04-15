# Community Tests

This directory contains research unit tests contributed by the community. Anyone can contribute a test; core maintainers review and merge.

## How to contribute

1. Copy `example/example-test.md` to a new file: `community/<your-handle>/<test-id>.md`
2. Fill in all required frontmatter fields (see spec below).
3. Run `python scripts/validate.py` — all fields must pass.
4. Open a pull request. Use the "New Test Proposal" issue template if you want feedback before writing a full test.

## Test file spec

```yaml
---
id: <unique-kebab-case-id>        # required; must be globally unique
name: "<Short descriptive name>"  # required; ≤ 80 chars
methodology:                       # required; one or more from the list below
  - universal | did | rdd | iv | synth | experiment_lab | experiment_field
  - theory | ml_prediction | survey
scope:                             # required; one or more
  - paper | proposal | replication
severity: blocker | warning | info # required
clarity: deterministic | heuristic | judgment  # required
tags: [tag1, tag2]                 # optional but encouraged
author: <your-github-handle>       # required
version: 1                         # required; start at 1
---

## What to Check
## How to Check
## Pass Condition
## Failure Examples
## References
```

## Severity definitions

| Level | Meaning |
|-------|---------|
| `blocker` | Failure means the paper has a fundamental validity problem. A paper should not be published or delivered while this test fails. |
| `warning` | Failure indicates a significant methodological gap. The paper may still be publishable but the issue warrants attention. |
| `info` | Best practice. Failure is not disqualifying but is noted. |

## Clarity definitions

| Level | Meaning |
|-------|---------|
| `deterministic` | Pass/fail can be determined by inspection with a binary answer. |
| `heuristic` | Requires interpretation of context; experienced reviewer should agree on result. |
| `judgment` | Requires expertise and taste; reviewers may disagree. Agent should report reasoning. |

## Quality bar for community tests

- **Specific**: the test must check one well-defined thing, not a bundle of issues.
- **Actionable**: a failing paper must know exactly what to do to pass.
- **Sourced**: the "How to Check" section must cite at least one peer-reviewed reference or methodological standard.
- **Not redundant**: check the [test registry](../registry.yaml) before submitting; do not duplicate an existing core or community test.
