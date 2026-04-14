#!/usr/bin/env python3
"""Validate all research unit test files against the SPEC."""

import sys
import pathlib
import re

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)

REPO_ROOT = pathlib.Path(__file__).parent.parent

VALID_METHODOLOGY = {
    "universal", "did", "rdd", "iv", "ols", "synth",
    "experiment_lab", "experiment_field", "theory", "ml_prediction", "survey"
}
VALID_SCOPE = {"paper", "proposal", "replication"}
VALID_SEVERITY = {"blocker", "warning", "info"}
VALID_CLARITY = {"deterministic", "heuristic", "judgment"}

REQUIRED_FIELDS = ["id", "name", "methodology", "scope", "severity", "clarity", "author", "version"]
REQUIRED_SECTIONS = ["## What to Check", "## How to Check", "## Pass Condition", "## Failure Examples"]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_file(path):
    text = path.read_text()
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, None, "No YAML frontmatter found"
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return None, None, f"YAML parse error: {e}"
    body = text[m.end():]
    return fm, body, None


def validate_file(path):
    errors = []
    fm, body, parse_err = parse_file(path)
    if parse_err:
        return [parse_err]

    # Required fields
    for field in REQUIRED_FIELDS:
        if field not in fm:
            errors.append(f"Missing required field: {field}")

    # Field types and values
    if "methodology" in fm:
        if not isinstance(fm["methodology"], list):
            errors.append("'methodology' must be a list")
        else:
            invalid = set(fm["methodology"]) - VALID_METHODOLOGY
            if invalid:
                errors.append(f"Invalid methodology values: {invalid}")

    if "scope" in fm:
        if not isinstance(fm["scope"], list):
            errors.append("'scope' must be a list")
        else:
            invalid = set(fm["scope"]) - VALID_SCOPE
            if invalid:
                errors.append(f"Invalid scope values: {invalid}")

    if "severity" in fm and fm["severity"] not in VALID_SEVERITY:
        errors.append(f"Invalid severity: {fm['severity']}. Must be one of {VALID_SEVERITY}")

    if "clarity" in fm and fm["clarity"] not in VALID_CLARITY:
        errors.append(f"Invalid clarity: {fm['clarity']}. Must be one of {VALID_CLARITY}")

    if "id" in fm:
        if not re.match(r"^[a-z0-9-]+$", fm["id"]):
            errors.append(f"'id' must be kebab-case: {fm['id']}")
        # Filename must match either the full id or the id with the methodology
        # prefix stripped. The prefix is derived from the parent directory name
        # (underscores replaced with hyphens). This allows files in core/did/ to
        # use either 'did-parallel-trends-plot.md' or 'parallel-trends-plot.md',
        # and files in core/experiment_lab/ to use 'attrition.md' (stripping
        # 'experiment-lab-' from 'experiment-lab-attrition').
        stem = path.stem
        id_val = fm["id"]
        dir_prefix = path.parent.name.replace("_", "-") + "-"
        if id_val.startswith(dir_prefix):
            short_id = id_val[len(dir_prefix):]
        else:
            short_id = re.sub(r"^[a-z]+-", "", id_val, count=1)
        if stem != id_val and stem != short_id:
            errors.append(
                f"Filename '{path.name}' must match id '{id_val}' "
                f"(as '{id_val}.md' or '{short_id}.md')"
            )

    if "version" in fm and not isinstance(fm["version"], int):
        errors.append("'version' must be an integer")

    if "name" in fm and len(fm["name"]) > 60:
        errors.append(f"'name' exceeds 60 characters ({len(fm['name'])})")

    # Required sections
    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f"Missing required section: {section}")

    return errors


def build_registry_check():
    """Check that all test IDs in registry.yaml match actual files."""
    registry_path = REPO_ROOT / "registry.yaml"
    if not registry_path.exists():
        return ["registry.yaml not found"]

    with open(registry_path) as f:
        registry = yaml.safe_load(f)

    errors = []
    for entry in registry.get("tests", []):
        test_path = REPO_ROOT / entry["path"]
        if not test_path.exists():
            errors.append(f"Registry entry '{entry['id']}' points to missing file: {entry['path']}")
    return errors


def main():
    test_files = list(REPO_ROOT.glob("core/**/*.md")) + list(REPO_ROOT.glob("community/**/*.md"))
    # Exclude non-test markdown files
    test_files = [f for f in test_files if f.name not in {"README.md", "SPEC.md", "CONTRIBUTING.md"}]

    total = 0
    failed = 0

    for path in sorted(test_files):
        rel = path.relative_to(REPO_ROOT)
        errors = validate_file(path)
        total += 1
        if errors:
            failed += 1
            print(f"FAIL  {rel}")
            for e in errors:
                print(f"      - {e}")
        else:
            print(f"OK    {rel}")

    registry_errors = build_registry_check()
    if registry_errors:
        print("\nRegistry errors:")
        for e in registry_errors:
            print(f"  - {e}")
        failed += 1

    print(f"\n{total} tests checked. {failed} file(s) with errors.")
    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
