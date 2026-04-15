#!/usr/bin/env python3
"""
generate_missing_reports.py

Generates missing comparative_report.json and comparative_report.html for batch
runs that have provider summaries but no comparative report. Also generates a
MASTER_SUMMARY.html showing all runs in timeline order with a v3.0 separator.

Usage:
    python3 scripts/generate_missing_reports.py
    python3 scripts/generate_missing_reports.py --run-id batch-20260414-0609
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH_DIR = ROOT / "tests" / "live_outputs" / "batch"
sys.path.insert(0, str(ROOT / "scripts"))

from run_batch_parallel import build_comparative_report, render_html_report

# Runs that predate the v3.0 pack revision (used for the separator in master summary)
PRE_REVISION_RUNS = {
    "batch-20260414-0148",
    "batch-20260414-0203",
    "batch-20260414-0215",
    "batch-20260414-0253",
    "batch-20260414-0319",
    "batch-20260414-0346",
}
REVISION_LABEL = "v3.0 pack deployed"


def load_suite_tests() -> list[dict]:
    suite_path = ROOT / "tests" / "cross_model_regression_suite.json"
    suite = json.loads(suite_path.read_text())
    return suite["tests"]


def load_summaries(run_dir: Path) -> dict[str, dict]:
    summaries = {}
    for pdir in run_dir.iterdir():
        if not pdir.is_dir():
            continue
        sj = pdir / "summary.json"
        if sj.exists():
            summaries[pdir.name] = json.loads(sj.read_text())
    return summaries


def get_tests_for_run(summaries: dict[str, dict], all_tests: list[dict]) -> list[dict]:
    """Return only the tests that were actually run in this batch."""
    test_ids_run: set[str] = set()
    for s in summaries.values():
        for r in s.get("results", []):
            if "error" not in r:
                test_ids_run.add(r["test_id"])
    return [t for t in all_tests if t["id"] in test_ids_run]


def generate_report_for_run(run_dir: Path, all_tests: list[dict]) -> bool:
    cr_path = run_dir / "comparative_report.json"
    html_path = run_dir / "comparative_report.html"

    summaries = load_summaries(run_dir)
    if not summaries:
        print(f"  SKIP {run_dir.name}: no provider summaries found")
        return False

    providers = sorted(summaries.keys())
    tests = get_tests_for_run(summaries, all_tests)

    if not tests:
        print(f"  SKIP {run_dir.name}: no matching tests found in suite")
        return False

    # Determine mode from first summary
    mode = next(iter(summaries.values())).get("mode", "pack")

    report = build_comparative_report(run_dir.name, providers, summaries, tests, mode)
    cr_path.write_text(json.dumps(report, indent=2))
    render_html_report(report, html_path)

    n_providers = len(providers)
    n_tests = len(tests)
    print(f"  GENERATED {run_dir.name}: {n_providers} providers, {n_tests} tests → {html_path.name}")
    return True


def generate_master_summary(all_runs: list[Path], all_tests: list[dict]) -> None:
    """Build MASTER_SUMMARY.html showing all runs in timeline order."""
    out_path = BATCH_DIR.parent.parent / "MASTER_SUMMARY.html"

    run_data = []
    for run_dir in sorted(all_runs):
        cr = run_dir / "comparative_report.json"
        if not cr.exists():
            continue
        report = json.loads(cr.read_text())
        run_data.append((run_dir.name, report))

    if not run_data:
        print("No reports found for master summary")
        return

    # Build provider set across all runs
    all_providers = sorted({
        p for _, r in run_data
        for p in r.get("providers_tested", [])
    })

    PROVIDER_COLORS = {
        "claude": "#d4e9ff", "openai": "#d4f4d4", "gemini": "#fff3d4",
        "xai": "#f4d4f4", "mistral": "#d4f4f4", "deepseek": "#fdd4d4",
    }

    def pct(v):
        return f"{v:.0%}" if v is not None else "—"

    # Header row with provider names
    p_headers = "".join(f'<th style="background:{PROVIDER_COLORS.get(p,"#eee")}">{p}</th>' for p in all_providers)

    rows_html = ""
    prev_was_pre = None
    for run_id, report in run_data:
        is_pre = run_id in PRE_REVISION_RUNS
        # Insert separator between pre and post revision
        if prev_was_pre is True and not is_pre:
            rows_html += (
                f"<tr><td colspan='{2 + len(all_providers)}' class='separator'>"
                f"── {REVISION_LABEL} ──</td></tr>\n"
            )
        prev_was_pre = is_pre

        ranking_by_provider = {r["provider"]: r for r in report.get("ranking", [])}
        era_cls = "pre-rev" if is_pre else "post-rev"
        cells = ""
        for p in all_providers:
            r = ranking_by_provider.get(p)
            if not r:
                cells += "<td class='na'>—</td>"
                continue
            comp = f"{r['avg_composite']:.0f}" if r.get("avg_composite") else "—"
            pr = pct(r.get("pass_rate"))
            gate_ok = r.get("gate_passed", False)
            bg = PROVIDER_COLORS.get(p, "#eee")
            border = "3px solid #2a8a2a" if gate_ok else "3px solid #cc3333"
            cells += (
                f"<td style='background:{bg};border-left:{border}'>"
                f"<strong>{comp}</strong><br><small>{pr}</small></td>"
            )

        report_link = f"batch/{run_id}/comparative_report.html"
        rows_html += (
            f"<tr class='{era_cls}'>"
            f"<td class='run-id'><a href='{report_link}'>{run_id}</a></td>"
            f"<td class='tests-n'>{report.get('tests_run', '—')}</td>"
            f"{cells}"
            f"</tr>\n"
        )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>DesignPilot — All Batch Runs</title>
<style>
  body {{ font-family: system-ui, sans-serif; margin: 2rem auto; max-width: 1200px; font-size: 13px; color: #1a1a1a; }}
  h1 {{ font-size: 1.3rem; margin-bottom: 0.25rem; }}
  .meta {{ color: #777; font-size: 0.82rem; margin-bottom: 1.5rem; }}
  table {{ border-collapse: collapse; width: 100%; }}
  th, td {{ padding: 0.4rem 0.6rem; border: 1px solid #e0e0e0; text-align: center; vertical-align: middle; }}
  th {{ background: #f5f5f5; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.04em; }}
  td.run-id {{ text-align: left; font-family: monospace; font-size: 0.85rem; }}
  td.run-id a {{ color: #1a5faa; text-decoration: none; }}
  td.run-id a:hover {{ text-decoration: underline; }}
  td.tests-n {{ color: #777; font-size: 0.82rem; }}
  td.na {{ color: #ccc; }}
  tr.pre-rev td {{ background-color: #fafafa; }}
  tr.post-rev td {{ background-color: #f0f8ff; }}
  tr.separator td {{
    background: #1a1a1a; color: #fff; font-weight: 700;
    font-size: 0.8rem; letter-spacing: 0.08em; padding: 0.5rem;
    text-align: center; text-transform: uppercase;
  }}
  td strong {{ font-size: 1.05rem; display: block; }}
  td small {{ color: #666; font-size: 0.75rem; }}
  .legend {{ display: flex; gap: 1.5rem; margin-bottom: 1rem; font-size: 0.8rem; }}
  .legend-item {{ display: flex; align-items: center; gap: 0.4rem; }}
  .swatch {{ width: 24px; height: 12px; border-radius: 2px; }}
</style>
</head>
<body>
<h1>DesignPilot — All Batch Runs</h1>
<p class="meta">Scores are composite (60% validator + 40% rubric, 0–100). Cell border: green = gate PASS, red = gate FAIL.</p>
<div class="legend">
  <div class="legend-item"><div class="swatch" style="background:#fafafa;border:1px solid #ddd"></div> Pre-revision runs</div>
  <div class="legend-item"><div class="swatch" style="background:#f0f8ff;border:1px solid #ddd"></div> Post-revision runs</div>
</div>
<table>
  <tr><th>Run</th><th>Tests</th>{p_headers}</tr>
  {rows_html}
</table>
</body>
</html>"""

    out_path.write_text(html, encoding="utf-8")
    print(f"\nMaster summary written: {out_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", help="Generate only for this run ID")
    parser.add_argument("--master-only", action="store_true", help="Only regenerate master summary")
    args = parser.parse_args()

    all_tests = load_suite_tests()
    all_runs = sorted([d for d in BATCH_DIR.iterdir() if d.is_dir()])

    if args.master_only:
        generate_master_summary(all_runs, all_tests)
        return

    if args.run_id:
        target = BATCH_DIR / args.run_id
        if not target.exists():
            raise SystemExit(f"Run not found: {target}")
        generate_report_for_run(target, all_tests)
    else:
        print("Scanning all batch runs for missing reports...\n")
        generated = 0
        for run_dir in all_runs:
            cr = run_dir / "comparative_report.json"
            if not cr.exists():
                if generate_report_for_run(run_dir, all_tests):
                    generated += 1
            else:
                print(f"  EXISTS  {run_dir.name}")
        print(f"\nGenerated {generated} missing reports.")

    generate_master_summary(all_runs, all_tests)


if __name__ == "__main__":
    main()
