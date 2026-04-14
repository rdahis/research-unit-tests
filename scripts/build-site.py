#!/usr/bin/env python3
"""Prepare Hugo site content from test files and registry."""

import pathlib
import re
import shutil
import sys

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)

REPO_ROOT = pathlib.Path(__file__).parent.parent
SITE_ROOT = REPO_ROOT / "site"
CONTENT_TESTS = SITE_ROOT / "content" / "tests"
SITE_DATA = SITE_ROOT / "data"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def main():
    # Recreate content/tests/
    if CONTENT_TESTS.exists():
        shutil.rmtree(CONTENT_TESTS)
    CONTENT_TESTS.mkdir(parents=True)
    SITE_DATA.mkdir(parents=True, exist_ok=True)

    # Copy registry
    shutil.copy(REPO_ROOT / "registry.yaml", SITE_DATA / "registry.yaml")

    # Process test files
    test_files = (
        list(REPO_ROOT.glob("core/**/*.md"))
        + list(REPO_ROOT.glob("community/**/*.md"))
    )
    count = 0
    for path in sorted(test_files):
        if path.name in {"README.md", "SPEC.md", "CONTRIBUTING.md"}:
            continue
        text = path.read_text()
        m = FRONTMATTER_RE.match(text)
        if not m:
            print(f"  SKIP (no frontmatter): {path.relative_to(REPO_ROOT)}")
            continue
        fm = yaml.safe_load(m.group(1))
        body = text[m.end():]

        # Add Hugo-required title and path (for GitHub link in template)
        fm["title"] = fm.get("name", path.stem)
        fm["source_path"] = str(path.relative_to(REPO_ROOT))

        out_path = CONTENT_TESTS / f"{fm['id']}.md"
        with open(out_path, "w") as f:
            f.write("---\n")
            yaml.dump(fm, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
            f.write("---\n")
            f.write(body)
        count += 1

    # Generate contributing page from CONTRIBUTING.md
    contrib_src = REPO_ROOT / "CONTRIBUTING.md"
    contrib_dir = SITE_ROOT / "content" / "contributing"
    contrib_dir.mkdir(exist_ok=True)
    contrib_out = contrib_dir / "_index.md"
    with open(contrib_out, "w") as f:
        f.write('---\ntitle: "Contributing"\n---\n\n')
        f.write(contrib_src.read_text())

    print(f"Site content built: {count} test pages + contributing page.")
    print(f"Registry copied to site/data/registry.yaml.")


if __name__ == "__main__":
    main()
