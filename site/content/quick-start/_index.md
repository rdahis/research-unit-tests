---
title: "Quick Start"
---

Research unit tests are designed to slot into a [Claude Code](https://claude.ai/code) workflow with minimal setup. This page describes three levels of integration.

---

## Level 1 — Reference from your project's CLAUDE.md

The simplest approach. Point your project's `CLAUDE.md` at this repository's rules so any Claude Code agent you run automatically has access to the tests.

Add to your project's `CLAUDE.md` (or create one if it doesn't exist):

```markdown
## Research quality

Before considering any paper or proposal complete, run research unit tests.
Rules: https://github.com/rdahis/research-unit-tests/tree/main/.claude/rules
Tests: https://github.com/rdahis/research-unit-tests/tree/main/core
Registry: https://github.com/rdahis/research-unit-tests/blob/main/registry.yaml
```

Then ask Claude to review your paper:

```
Review this paper using research unit tests.
Methodology: did
Scope: paper
[paste abstract + key sections, or attach PDF]
```

---

## Level 2 — Clone the repo into your project

For full local access (offline, customizable):

```bash
# From your project root
git clone https://github.com/rdahis/research-unit-tests .research-unit-tests
```

Then add to your project's `CLAUDE.md`:

```markdown
## Research quality

Run research unit tests before finalizing any paper or proposal.
Load rules from: .research-unit-tests/.claude/rules/research-test-runner.md
Load registry from: .research-unit-tests/registry.yaml
```

This gives Claude Code direct file access — no network calls required.

---

## Level 3 — Add your own local tests

Clone the repo (Level 2), then add tests to a `community/` subdirectory named after your GitHub username:

```
.research-unit-tests/
└── community/
    └── your-username/
        ├── my-custom-test.md
        └── another-test.md
```

Each test follows [the same spec](https://github.com/rdahis/research-unit-tests/blob/main/SPEC.md). Your tests are loaded automatically by the agent runner alongside core tests.

To validate your tests:

```bash
cd .research-unit-tests
python scripts/validate.py
```

To share them with the community, open a pull request.

---

## Running a review

Once set up, ask Claude to run a review in plain English:

```
Review my paper using research unit tests.
Methodology: did
Scope: paper
```

Or provide detail:

```
Run research unit tests on this proposal.
Methodology: iv, ols
Scope: proposal
Focus on blockers only — skip warnings.
```

The agent will:
1. Load all applicable tests (universal + methodology-specific)
2. Run each test in severity order
3. Report PASS / FAIL / WARN / SKIP per test with specific evidence
4. Return a verdict: PASS only if all blockers pass

---

## Understanding the output

```
[PASS] universal-tables-have-n-obs
  All regression tables report N. Table 2 shows N=4,312 per column.

[FAIL] did-staggered-heterogeneous-effects
  Paper uses TWFE with staggered adoption (47 cohorts, 1990–2018) but does
  not use a heterogeneity-robust estimator. No Callaway-Sant'Anna or
  Sun-Abraham robustness check anywhere.

[WARN] universal-robustness-section
  Only one robustness check shown (column 4 of Table 3). Standard is ≥3
  substantively distinct checks.

## Verdict: FAIL
1 blocker failed. Address did-staggered-heterogeneous-effects before submission.
```

A paper **passes** only if zero blockers fail. Warnings are flagged for author attention but do not block.

---

## Keeping tests up to date

```bash
cd .research-unit-tests
git pull
```

New tests added to core are immediately available after pulling.
