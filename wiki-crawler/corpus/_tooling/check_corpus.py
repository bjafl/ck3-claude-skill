#!/usr/bin/env python3
"""Corpus hygiene check: broken relative cross-links + duplicate/malformed manifest lines.

See HANDOFF.md §6: "Manifest and cross-link hygiene needs an explicit pass, not just hoping
agents get it right." Run this at the end of every category batch, not just once at the end of
the whole build.

Usage (from the corpus/ directory, or pass --root):
    python3 _tooling/check_corpus.py
"""

import argparse
import re
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def find_broken_links(root: Path) -> list[tuple[Path, str]]:
    broken = []
    for md_file in root.rglob("*.md"):
        if "_tooling" in md_file.parts:
            continue
        text = md_file.read_text(errors="replace")
        for m in LINK_RE.finditer(text):
            target = m.group(1)
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target_path = (md_file.parent / target).resolve()
            if not target_path.exists():
                broken.append((md_file.relative_to(root), target))
    return broken


def check_manifest(root: Path) -> tuple[list[str], list[str]]:
    manifest_path = root / "_tooling" / "manifest.tsv"
    if not manifest_path.exists():
        return [], []
    lines = manifest_path.read_text().splitlines()
    seen_paths: dict[str, int] = {}
    duplicates = []
    malformed = []
    missing_files = []
    for i, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) != 4:
            malformed.append(f"line {i}: expected 4 tab-separated fields, got {len(parts)}: {line!r}")
            continue
        relpath = parts[0]
        if relpath in seen_paths:
            duplicates.append(f"{relpath} (lines {seen_paths[relpath]} and {i})")
        else:
            seen_paths[relpath] = i
        if not (root / relpath).exists():
            missing_files.append(f"line {i}: manifest references {relpath!r} but the file doesn't exist")
    return duplicates + malformed + missing_files, list(seen_paths.keys())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Path to the corpus/ root (default: cwd)")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    broken = find_broken_links(root)
    manifest_issues, manifest_files = check_manifest(root)

    md_files = [p for p in root.rglob("*.md") if "_tooling" not in p.parts]
    manifest_set = set(manifest_files)
    unmanifested = sorted(
        str(p.relative_to(root)) for p in md_files
        if str(p.relative_to(root)) not in manifest_set and p.name != "_index.md" and p.name != "README.md" and p.name != "INDEX.md"
    )

    print(f"Scanned {len(md_files)} corpus files.\n")

    if broken:
        print(f"BROKEN LINKS ({len(broken)}):")
        for src, target in broken:
            print(f"  {src} -> {target}")
        print()
    else:
        print("No broken relative links found.\n")

    if manifest_issues:
        print(f"MANIFEST ISSUES ({len(manifest_issues)}):")
        for issue in manifest_issues:
            print(f"  {issue}")
        print()
    else:
        print("manifest.tsv: no duplicates, no malformed lines, all referenced files exist.\n")

    if unmanifested:
        print(f"FILES NOT IN MANIFEST ({len(unmanifested)}) -- may be forgotten manifest-append steps:")
        for f in unmanifested:
            print(f"  {f}")
    else:
        print("Every corpus file is accounted for in manifest.tsv.")


if __name__ == "__main__":
    main()
