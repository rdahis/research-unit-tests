# Research Unit Test — Specification

A **research unit test** is a structured quality check for an academic paper or project. Tests are declarative: they specify *what* to check and *how* an agent should reason about it, but do not execute code against a repository.

---

## File Format

Each test is a single `.md` file with YAML frontmatter followed by Markdown sections.

### Frontmatter (required)

```yaml
---
id: unique-kebab-case-id          # unique across all tests
name: "Human-readable test name"
methodology:                       # list; use "universal" if applies to all
  - universal
  - did
scope:                             # what artifact is being tested
  - paper        # finished or near-finished manuscript
  - proposal     # research proposal / pre-registration
  - replication  # replication package / code
severity: blocker                  # blocker | warning | info
clarity: heuristic                 # deterministic | heuristic | judgment
tags: []                           # optional free-form tags
author: rdahis                     # GitHub username of test author
version: 1                         # increment on breaking changes
---
```

### Frontmatter fields

| Field | Required | Values | Description |
|-------|----------|--------|-------------|
| `id` | yes | kebab-case string | Unique identifier. Never reuse, even after deletion. |
| `name` | yes | string | Short human-readable name (≤60 chars). |
| `methodology` | yes | list | One or more of: `universal`, `did`, `rdd`, `iv`, `ols`, `synth`, `experiment_lab`, `experiment_field`, `theory`, `ml_prediction`, `survey`. |
| `scope` | yes | list | One or more of: `paper`, `proposal`, `replication`. |
| `severity` | yes | enum | `blocker`: paper cannot pass review. `warning`: flag for author attention. `info`: suggestion or best practice. |
| `clarity` | yes | enum | `deterministic`: clear yes/no from inspection. `heuristic`: requires judgment but has objective anchors. `judgment`: requires experience and taste. |
| `tags` | no | list | Free-form. |
| `author` | yes | string | GitHub username. |
| `version` | yes | integer | Start at 1. |

---

## Body Sections

### Required

```markdown
## What to Check
[One paragraph: what property of the paper/project this test verifies and why it matters.]

## How to Check
[Step-by-step agent instructions. Write as if briefing a careful research assistant.
For deterministic tests: enumerate exactly what to look for.
For heuristic tests: provide anchors and examples of pass/fail.
For judgment tests: provide a rubric with explicit criteria.]

## Pass Condition
[Precise statement of what constitutes a pass. Should be unambiguous enough
that two independent agents would agree ≥80% of the time.]

## Failure Examples
[1–3 concrete examples of failure, with brief explanation of why each fails.]
```

### Optional

```markdown
## References
[Papers, textbook chapters, or other tests that motivate or elaborate on this check.]

## Notes
[Caveats, known edge cases, or methodology sub-variants where the test applies differently.]
```

---

## Severity × Clarity Examples

| | Deterministic | Heuristic | Judgment |
|---|---|---|---|
| **Blocker** | Replication package reproduces all tables | SE clustered at correct level | Contribution is new |
| **Warning** | Regression tables include N | Parallel trends plot shown and plausible | Results ordering maximizes impact |
| **Info** | — | Alternative specifications discussed | Paper is feasible within stated timeline |

---

## Naming Conventions

- File: `{id}.md` placed in `core/{methodology}/` or `community/{author}/`
- ID: `{methodology}-{what-is-checked}`, e.g. `did-parallel-trends-plot`, `universal-tables-have-n-obs`
- For universal tests: `universal-{what}` in `core/universal/`

---

## Validation

Run `scripts/validate.py` to check all test files conform to this spec before submitting a PR.
