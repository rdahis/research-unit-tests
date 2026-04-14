# Contributing to Research Unit Tests

Research unit tests improve through community refinement. Anyone can contribute a new test or improve an existing one.

---

## Adding a new test

1. Read [SPEC.md](SPEC.md) fully before writing a test.
2. Choose the right directory:
   - `core/` — proposed for the curated core set (reviewed by maintainers)
   - `community/{your-github-username}/` — your own tests, merged with minimal review
3. Create a file named `{id}.md` where `id` follows the convention `{methodology}-{what-is-checked}`.
4. Fill in all required frontmatter fields and body sections.
5. Run `python scripts/validate.py` and fix all errors.
6. Update `registry.yaml` with your test's entry (or the CI will reject the PR).
7. Open a pull request. Title: `add: {test-id}`.

## Improving an existing test

- Bump the `version` field in frontmatter.
- Describe the change in the PR body.
- Do not change the `id` — IDs are permanent.

## Distilling tests from methodological papers

Econometrics and statistics papers are a source of new unit tests. The workflow:

1. Identify a paper that introduces a new diagnostic, estimator, or check (e.g., a new test for pre-trends, a new validity condition for IV).
2. Read the paper and identify the specific check it recommends.
3. Write a test file that operationalizes that check for agents.
4. Cite the paper in `## References`.

Open an issue titled `paper: {citation}` to flag papers that need to be distilled. Others can claim them.

---

## Test quality standards

A test is accepted if it is:
- **Actionable**: an agent following the "How to Check" instructions would reach the same verdict as a careful human reviewer ≥80% of the time.
- **Scoped**: the test checks one thing, not many.
- **Referenced**: claims about best practices are backed by citations.
- **Calibrated**: the severity level matches the actual cost of failure.

Tests in `core/` face higher scrutiny than `community/`. Core tests are intended to reflect near-consensus best practices.

---

## What not to contribute

- Tests that duplicate existing ones (check the registry first)
- Tests that are purely stylistic preferences without methodological grounding
- Tests that require running code (this repository is declarative only)
