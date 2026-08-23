#!/usr/bin/env python3
"""Assemble the `args` payload for batch-write-category.js from a work-item JSON file.

The Workflow tool's scripts have no filesystem access (see the script's own header comment), so
everything it needs -- item list, inlined style rules, absolute paths -- must be pre-loaded into
`args` by the caller. This script does that assembly and prints ready-to-paste JSON.

Usage:
    python3 _tooling/build_workflow_args.py _tooling/workitems/02-realm-and-succession.json
"""

import json
import sys
from pathlib import Path

TOOLING_DIR = Path(__file__).resolve().parent
CORPUS_ROOT = TOOLING_DIR.parent
FETCHER_DIR = CORPUS_ROOT.parent / "fetcher"


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 _tooling/build_workflow_args.py <workitems-file.json>", file=sys.stderr)
        raise SystemExit(1)

    workitems_path = Path(sys.argv[1])
    items = json.loads(workitems_path.read_text())
    # Drop items already marked DONE in their notes -- no point re-batching them.
    items = [i for i in items if "DONE" not in i.get("notes", "")]

    category_dir = workitems_path.stem  # e.g. "02-realm-and-succession"
    cheatsheet = (TOOLING_DIR / "style-cheatsheet.md").read_text()

    payload = {
        "items": items,
        "styleCheatsheet": cheatsheet,
        "categoryDir": category_dir,
        "fetcherDir": str(FETCHER_DIR),
        "batchSize": 6,
        "model": "claude-haiku-4-5-20251001",
    }
    print(json.dumps(payload, indent=2))
    print(f"\n{len(items)} items ready (after dropping DONE ones) for category {category_dir!r}", file=sys.stderr)


if __name__ == "__main__":
    main()
