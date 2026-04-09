#!/usr/bin/env python3
"""
Design Expert Pack — Staleness Linter
======================================
Scans skills/ and knowledge-base/summaries/ for frontmatter compliance.

Usage:
    python3 lint_pack.py [pack_root] [--max-age-days N] [--strict]

    pack_root      Path to the pack directory (default: current directory)
    --max-age-days How many days before last_updated triggers a warning (default: 90)
    --strict       Exit with code 1 if any warnings exist, not just errors

Exit codes:
    0  All files pass
    1  One or more files have errors or (with --strict) warnings
"""

import os
import sys
import argparse
from datetime import date, datetime

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False


# ── Config ────────────────────────────────────────────────────────────────────

SKILL_REQUIRED_FIELDS = [
    "skill_version",
    "source_reference",
    "last_updated",
    "synchronized",
    "canonical_owner",
    "domain",
]

SUMMARY_REQUIRED_FIELDS = [
    "summary_version",
    "source_reference",
    "last_updated",
    "synchronized",
    "domain",
]

SCAN_TARGETS = [
    ("skills", SKILL_REQUIRED_FIELDS, "skill"),
    ("knowledge-base/summaries", SUMMARY_REQUIRED_FIELDS, "summary"),
]


# ── Colours ───────────────────────────────────────────────────────────────────

USE_COLOR = sys.stdout.isatty()

def red(s):    return f"\033[31m{s}\033[0m" if USE_COLOR else s
def yellow(s): return f"\033[33m{s}\033[0m" if USE_COLOR else s
def green(s):  return f"\033[32m{s}\033[0m" if USE_COLOR else s
def bold(s):   return f"\033[1m{s}\033[0m"  if USE_COLOR else s
def dim(s):    return f"\033[2m{s}\033[0m"  if USE_COLOR else s


# ── Frontmatter parser ────────────────────────────────────────────────────────

def extract_frontmatter(text):
    """Return (dict_or_None, errors_list)."""
    if not text.startswith("---"):
        return None, ["no frontmatter block found (file must start with ---)"]

    end = text.find("\n---", 3)
    if end == -1:
        return None, ["frontmatter block opened but never closed"]

    raw = text[3:end].strip()

    if YAML_AVAILABLE:
        try:
            data = yaml.safe_load(raw)
            return data if isinstance(data, dict) else {}, []
        except yaml.YAMLError as e:
            return None, [f"YAML parse error: {e}"]
    else:
        # Minimal line-by-line parser (no PyYAML dependency)
        data = {}
        current_list_key = None
        for line in raw.splitlines():
            if line.startswith("  - ") and current_list_key:
                data[current_list_key].append(line[4:].strip())
            elif ": " in line and not line.startswith(" "):
                k, _, v = line.partition(": ")
                k = k.strip()
                v = v.strip()
                if v == "":
                    data[k] = []
                    current_list_key = k
                else:
                    current_list_key = None
                    if v.lower() == "true":
                        data[k] = True
                    elif v.lower() == "false":
                        data[k] = False
                    else:
                        data[k] = v
            elif line.endswith(":") and not line.startswith(" "):
                k = line.rstrip(":")
                data[k] = []
                current_list_key = k
        return data, []


# ── Single-file check ─────────────────────────────────────────────────────────

def check_file(path, required_fields, max_age_days):
    errors = []
    warnings = []

    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        return [f"cannot read file: {e}"], []

    fm, parse_errors = extract_frontmatter(text)
    if parse_errors:
        return parse_errors, []
    if fm is None:
        return ["frontmatter missing or unparseable"], []

    # Required field presence
    for field in required_fields:
        if field not in fm:
            errors.append(f"missing required field: {field}")

    # synchronized: false is an explicit staleness flag
    if fm.get("synchronized") is False:
        errors.append("synchronized: false — file is marked stale")

    # source_reference must be a non-empty list
    sr = fm.get("source_reference")
    if sr is not None:
        if not isinstance(sr, list) or len(sr) == 0:
            errors.append("source_reference must be a non-empty list")

    # last_updated age check
    lu = fm.get("last_updated")
    if lu is not None:
        try:
            if isinstance(lu, str):
                lu_date = datetime.strptime(lu, "%Y-%m-%d").date()
            elif isinstance(lu, date):
                lu_date = lu
            else:
                raise ValueError("unexpected type")
            age = (date.today() - lu_date).days
            if age > max_age_days:
                warnings.append(
                    f"last_updated is {age} days ago "
                    f"(threshold: {max_age_days} days) — consider re-syncing"
                )
        except ValueError:
            errors.append(f"last_updated '{lu}' is not a valid YYYY-MM-DD date")

    return errors, warnings


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Lint frontmatter compliance for Design Expert pack files."
    )
    parser.add_argument(
        "pack_root",
        nargs="?",
        default=".",
        help="Path to the pack root directory (default: current directory)",
    )
    parser.add_argument(
        "--max-age-days",
        type=int,
        default=90,
        help="Days before last_updated triggers a warning (default: 90)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if any warnings exist, not just errors",
    )
    args = parser.parse_args()

    pack_root = os.path.abspath(args.pack_root)
    if not os.path.isdir(pack_root):
        print(red(f"Error: pack_root '{pack_root}' is not a directory."))
        sys.exit(1)

    total_files = 0
    total_errors = 0
    total_warnings = 0
    results = []  # (rel_path, errors, warnings)

    for subdir, required_fields, _ in SCAN_TARGETS:
        scan_dir = os.path.join(pack_root, subdir)
        if not os.path.isdir(scan_dir):
            print(yellow(f"Warning: directory not found, skipping: {subdir}"))
            continue

        for fname in sorted(os.listdir(scan_dir)):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(scan_dir, fname)
            rel = os.path.relpath(fpath, pack_root)
            errors, warnings = check_file(fpath, required_fields, args.max_age_days)
            total_files += 1
            total_errors += len(errors)
            total_warnings += len(warnings)
            results.append((rel, errors, warnings))

    # ── Output ────────────────────────────────────────────────────────────────

    print()
    print(bold("Design Expert Pack — Staleness Linter"))
    print(dim(f"Pack root : {pack_root}"))
    print(dim(f"Scanned   : {total_files} files"))
    print(dim(f"Max age   : {args.max_age_days} days"))
    print(dim(f"PyYAML    : {'available' if YAML_AVAILABLE else 'not installed, using built-in parser'}"))
    print()

    any_issue = False
    for rel, errors, warnings in results:
        if not errors and not warnings:
            print(green("  PASS") + f"  {rel}")
        else:
            any_issue = True
            if errors:
                print(red("  FAIL") + f"  {bold(rel)}")
                for e in errors:
                    print(f"        {red('ERROR')}  {e}")
            if warnings:
                if not errors:
                    print(yellow("  WARN") + f"  {bold(rel)}")
                for w in warnings:
                    print(f"        {yellow('WARN ')}  {w}")

    print()

    # ── Summary ───────────────────────────────────────────────────────────────

    status_parts = []
    if total_errors == 0 and total_warnings == 0:
        status_parts.append(green("All files pass."))
    else:
        if total_errors > 0:
            status_parts.append(red(f"{total_errors} error(s)"))
        if total_warnings > 0:
            status_parts.append(yellow(f"{total_warnings} warning(s)"))

    print("  ".join(status_parts) + f"  {dim(f'({total_files} files checked)')}")
    print()

    if total_errors > 0:
        sys.exit(1)
    if args.strict and total_warnings > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
