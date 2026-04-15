#!/usr/bin/env python3
"""
archive_batch_runs.py

Tiered storage for batch run outputs. Keeps the most recent run untouched,
compresses older ones progressively.

Tier 1 (newest run): full data — all .md outputs, all JSON, HTML reports
Tier 2 (runs 2-4):   compressed — .md outputs gzipped into raw_outputs.tar.gz
Tier 3 (runs 5+):    minimal — .md files deleted, only JSON/HTML reports kept

Usage:
    python3 scripts/archive_batch_runs.py           # apply archiving
    python3 scripts/archive_batch_runs.py --dry-run # preview without changes
    python3 scripts/archive_batch_runs.py --status  # show current tier of each run
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH_DIR = ROOT / "tests" / "live_outputs" / "batch"

TIER1_COUNT = 1   # keep full
TIER2_COUNT = 3   # compress .md → tar.gz
# everything older = Tier 3 (delete .md)

ARCHIVE_README = """# Archived Batch Run

This run has been archived to save space (Tier 3 storage).

## What was removed
- All raw model output files (*.md) have been deleted.

## What is preserved
- comparative_report.json — full scoring data for all providers and tests
- comparative_report.html — visual report
- [provider]/summary.json — per-provider summary with all scores and issue lists

## Archived on
{date}

## Run metadata
{metadata}
"""


def get_runs() -> list[Path]:
    """Return all batch run dirs sorted newest-first."""
    return sorted(
        [d for d in BATCH_DIR.iterdir() if d.is_dir() and d.name.startswith("batch-")],
        reverse=True,
    )


def tier_of(run_dir: Path, runs: list[Path]) -> int:
    idx = runs.index(run_dir)
    if idx < TIER1_COUNT:
        return 1
    if idx < TIER1_COUNT + TIER2_COUNT:
        return 2
    return 3


def md_files(run_dir: Path) -> list[Path]:
    return list(run_dir.glob("**/*.md"))


def is_tier2_archived(run_dir: Path) -> bool:
    return (run_dir / "raw_outputs.tar.gz").exists()


def is_tier3_archived(run_dir: Path) -> bool:
    return (run_dir / "README_ARCHIVED.md").exists()


def current_tier(run_dir: Path) -> int:
    if is_tier3_archived(run_dir):
        return 3
    if is_tier2_archived(run_dir):
        return 2
    return 1


def size_kb(paths: list[Path]) -> int:
    return sum(p.stat().st_size for p in paths if p.exists()) // 1024


def apply_tier2(run_dir: Path, dry_run: bool) -> int:
    """Gzip all .md files into raw_outputs.tar.gz. Returns bytes saved."""
    mds = md_files(run_dir)
    if not mds:
        return 0
    saved = size_kb(mds)
    if dry_run:
        print(f"    [DRY] would gzip {len(mds)} .md files (~{saved}KB)")
        return saved * 1024

    tar_path = run_dir / "raw_outputs.tar.gz"
    with tarfile.open(tar_path, "w:gz") as tar:
        for md in mds:
            tar.add(md, arcname=md.relative_to(run_dir))
    for md in mds:
        md.unlink()
    print(f"    Gzipped {len(mds)} .md files → raw_outputs.tar.gz (~{saved}KB saved)")
    return saved * 1024


def apply_tier3(run_dir: Path, dry_run: bool) -> int:
    """Delete all .md files and write README_ARCHIVED.md."""
    mds = md_files(run_dir)
    # Also remove tar.gz if present (we're going fully minimal)
    tar = run_dir / "raw_outputs.tar.gz"
    saved = size_kb(mds) + (tar.stat().st_size // 1024 if tar.exists() else 0)

    # Collect metadata
    cr = run_dir / "comparative_report.json"
    metadata = "No comparative report"
    if cr.exists():
        try:
            report = json.loads(cr.read_text())
            ranking = report.get("ranking", [])
            lines = [f"  {r['provider']}: {r.get('pass_rate',0):.0%} composite={r.get('avg_composite','—')}"
                     for r in ranking]
            metadata = "\n".join(lines)
        except Exception:
            pass

    if dry_run:
        print(f"    [DRY] would delete {len(mds)} .md files + tar (~{saved}KB), write README_ARCHIVED.md")
        return saved * 1024

    for md in mds:
        md.unlink()
    if tar.exists():
        tar.unlink()

    import datetime
    readme = ARCHIVE_README.format(
        date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        metadata=metadata,
    )
    (run_dir / "README_ARCHIVED.md").write_text(readme)
    print(f"    Archived: deleted {len(mds)} .md files, wrote README_ARCHIVED.md (~{saved}KB saved)")
    return saved * 1024


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="Preview without making changes")
    parser.add_argument("--status", action="store_true", help="Show current tier of each run")
    args = parser.parse_args()

    runs = get_runs()
    if not runs:
        print("No batch runs found.")
        return

    if args.status:
        print(f"{'Run':35} {'Current tier':15} {'MD files':10} {'Size KB':10}")
        print("-" * 75)
        for run in runs:
            target_tier = tier_of(run, runs)
            cur_tier = current_tier(run)
            mds = md_files(run)
            kb = size_kb(mds)
            needs = " (needs archiving)" if cur_tier > target_tier else ""
            print(f"  {run.name:33} Tier {cur_tier} → {target_tier}  {len(mds):8}  {kb:8}{needs}")
        return

    print(f"Batch archive — {len(runs)} runs found")
    print(f"Policy: Tier 1 (keep full): newest {TIER1_COUNT}, "
          f"Tier 2 (compress): next {TIER2_COUNT}, Tier 3 (minimal): rest\n")

    total_saved = 0
    for run in runs:
        target = tier_of(run, runs)
        cur = current_tier(run)

        if cur >= target:
            print(f"  {run.name}  Tier {cur} ✓")
            continue

        print(f"  {run.name}  Tier {cur} → Tier {target}")
        if target == 2:
            total_saved += apply_tier2(run, args.dry_run)
        elif target == 3:
            total_saved += apply_tier3(run, args.dry_run)

    label = "[DRY RUN] Would save" if args.dry_run else "Total saved"
    print(f"\n{label}: ~{total_saved // 1024}KB")


if __name__ == "__main__":
    main()
