#!/usr/bin/env python3
"""Rebuild manifest.tsv from scratch by reading every corpus file's own front matter.

Used once 2026-08-23 after 4 concurrent Workflow batches produced a messy manifest.tsv (malformed
paths from a category-name typo, duplicate/retry lines, one line with a garbled source field) --
patching ~15 individual bad lines by hand was less reliable than treating the files on disk as
ground truth and regenerating. Safe to re-run any time the manifest is suspected stale/dirty: it
fully overwrites manifest.tsv from the corpus/*.md files that currently exist.

Usage (from corpus/ directory):
    python3 _tooling/regen_manifest.py
"""

import re
from pathlib import Path

CORPUS_ROOT = Path(__file__).resolve().parent.parent

FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
TITLE_RE = re.compile(r'^title:\s*(.+)$', re.MULTILINE)
SOURCES_BLOCK_RE = re.compile(r'^sources:\s*\n((?:\s*-\s*.+\n?)+)', re.MULTILINE)
SOURCES_INLINE_RE = re.compile(r'^sources:\s*\[(.*)\]\s*$', re.MULTILINE)


def extract_title(front_matter: str, fallback: str) -> str:
    m = TITLE_RE.search(front_matter)
    return m.group(1).strip() if m else fallback


def extract_sources(front_matter: str) -> str:
    m = SOURCES_BLOCK_RE.search(front_matter)
    if m:
        urls = re.findall(r'-\s*(\S.*\S|\S)', m.group(1))
        titles = [u.rsplit("/", 1)[-1].replace("_", " ") for u in urls]
        return ",".join(titles) if titles else "unknown"
    m = SOURCES_INLINE_RE.search(front_matter)
    if m:
        urls = [u.strip().strip('"').strip("'") for u in m.group(1).split(",") if u.strip()]
        titles = [u.rsplit("/", 1)[-1].replace("_", " ") for u in urls]
        return ",".join(titles) if titles else "unknown"
    return "unknown"


def main() -> None:
    lines = []
    skipped = []
    md_files = sorted(
        p for p in CORPUS_ROOT.rglob("*.md")
        if "_tooling" not in p.relative_to(CORPUS_ROOT).parts
    )
    for path in md_files:
        text = path.read_text(errors="replace")
        m = FRONT_MATTER_RE.match(text)
        rel = str(path.relative_to(CORPUS_ROOT))
        if not m:
            skipped.append(rel)
            continue
        front_matter = m.group(1)
        title = extract_title(front_matter, path.stem)
        sources = extract_sources(front_matter)
        n_bytes = len(text.encode())
        lines.append(f"{rel}\t{title}\t{n_bytes}\t{sources}\n")

    manifest_path = CORPUS_ROOT / "_tooling" / "manifest.tsv"
    manifest_path.write_text("".join(lines))
    print(f"Wrote {len(lines)} lines to manifest.tsv")
    if skipped:
        print(f"Skipped {len(skipped)} file(s) with no YAML front matter:")
        for s in skipped:
            print(f"  {s}")


if __name__ == "__main__":
    main()
