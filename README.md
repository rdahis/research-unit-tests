# Research Unit Tests

A library of structured quality checks for academic research papers — analogous to unit tests in software engineering.

---

## What is a research unit test?

A research unit test specifies a single quality criterion, how to check it, and what constitutes a pass. Tests range from deterministic (does the replication package run?) to judgment-based (is the contribution interesting?). They are organized by methodology and severity.

Tests are declarative: each is a Markdown file an agent can read and follow. No code execution required.

---

## Test taxonomy

| Dimension | Values |
|-----------|--------|
| **Methodology** | `universal`, `did`, `rdd`, `iv`, `ols`, `synth`, `experiment_lab`, `experiment_field`, `theory`, `ml_prediction`, `survey` |
| **Scope** | `paper`, `proposal`, `replication` |
| **Severity** | `blocker` (paper cannot pass), `warning` (flag for author), `info` (suggestion) |
| **Clarity** | `deterministic` (clear yes/no), `heuristic` (objective anchors), `judgment` (requires experience) |

---

## Current tests

| ID | Name | Method | Severity | Clarity |
|----|------|--------|----------|---------|
| `universal-tables-have-n-obs` | Regression tables report N | universal | blocker | deterministic |
| `universal-replication-reproduces-results` | Replication package reproduces results | universal | blocker | deterministic |
| `universal-contribution-is-new` | Contribution is new | universal | blocker | judgment |
| `universal-contribution-is-interesting` | Contribution is interesting | universal | blocker | judgment |
| `did-parallel-trends-plot` | Pre-trends visualization shown | did | blocker | heuristic |
| `did-staggered-heterogeneous-effects` | Staggered adoption uses robust estimator | did | blocker | heuristic |
| `iv-first-stage-f-stat` | First-stage F-statistic sufficient | iv | blocker | deterministic |
| `rdd-bandwidth-sensitivity` | Estimates robust to bandwidth choice | rdd | blocker | heuristic |

---

## Using with Claude Code

Add this repository's `.claude/` directory to your project, or reference it in your `CLAUDE.md`. Then:

```
Review this paper using research unit tests: [paper.pdf or description]
Methodology: did
Scope: paper
```

The agent will load applicable tests from the registry, run each check, and produce a structured pass/fail report.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New tests go in `community/{your-username}/`. Propose to core via PR.

---

## License

MIT. Tests in `community/` are owned by their respective authors under the same license unless otherwise stated.
