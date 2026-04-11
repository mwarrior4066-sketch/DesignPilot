#!/usr/bin/env python3
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / 'projects'
REQ_ROOT_DIRS = ['process', 'finalized', 'problems_and_solutions', 'context', 'handoff']
REQ_ROOT_FILES = ['README.md']
REQ_CONTEXT = ['PROJECT_OVERVIEW.md', 'ACTIVE_STATE.md', 'TASK_QUEUE.md', 'WORKSPACE_MODE.md', 'CASE_STUDY_ROADMAP.md']
REQ_PROBLEMS = ['PROBLEM_LOG.md', 'DECISION_LOG.md', 'PROJECT_SPECIFIC_ERRORS.md']
REQ_HANDOFF = ['HANDOFF_NOTES.md', 'IMPLEMENTATION_CHECKLIST.md', 'OPEN_QUESTIONS.md', 'DOWNLOAD_BUNDLE_MANIFEST.md']
REQ_PROCESS = ['briefs', 'research', 'strategy', 'structure', 'design', 'specs', 'reviews', 'iterations', 'assets']
REQ_FINALIZED = ['deliverables', 'exports', 'approved_specs', 'release_notes']
FLAGSHIP_PROOF = [
    'process/research/proof/FIXED_PROMPT_SET.md',
    'process/specs/proof/COMPARATIVE_SCORECARD.md',
    'process/structure/case-study/CLAIM_TO_PROOF_MAP.md',
    'process/reviews/benchmarks/benchmark-run-001.json',
    'process/reviews/external_signals/TRUST_SIGNAL_LOG.md',
    'finalized/deliverables/proof/PROOF_STACK_SUMMARY.md'
]
ROADMAP_SECTIONS = [
    '## Project identity',
    '## Proof state',
    '## Done before',
    '## Just added',
    '## Needed next',
    '## Open risks',
    '## Next validation move',
    '## Pending artifacts',
    '## Release readiness'
]
ACTIVE_REQUIRED = [
    '- Project goal:',
    '- Active phase:',
    '- Active task:',
    '- Workspace mode:',
    '- Files being worked on:',
    '- Blockers:',
    '- Next action:'
]
ACTIVE_STATUS_BLOCK = [
    '- Current release:',
    '- Manifest status:',
    '- Continuity sync:',
    '- Proof sync:',
    '- Runtime sync:',
    '- Last refresh:'
]
BUNDLE_REQUIRED = [
    '- Project slug:',
    '- Workspace mode:',
    '- Current milestone:',
    '- Populated files by folder:',
    '- Finalized artifacts ready for export:',
    '- Open work still in process:',
    '- Continuity freshness anchor:',
    '- Last bundle-ready timestamp:'
]
PROBLEM_FIELDS = [
    'Error ID', 'Classification', 'Context', 'Artifact(s)', 'Severity', 'Surfaced by',
    'What went wrong', 'Why it happened', 'Missing or violated rule', 'Fix applied',
    'Prevention rule', 'Pack-level or project-level', 'Status'
]
DECISION_FIELDS = [
    'Decision ID', 'Classification', 'Context', 'Options considered', 'Decision', 'Why',
    'Files affected', 'Validation impact', 'Follow-up'
]
PROJECT_ERROR_FIELDS = [
    'Error ID', 'Classification', 'Context', 'What went wrong', 'Why it happened',
    'Missing or violated rule', 'Fix applied', 'Prevention rule', 'Pack-level or project-level', 'Status'
]


def noncanonical(path: Path, allowed):
    return sorted([p.name for p in path.iterdir() if p.name not in allowed])


def parse_bullet(text: str, label: str):
    m = re.search(rf"^- {re.escape(label)}:\s*(.+)$", text, flags=re.MULTILINE)
    return m.group(1).strip() if m else None


def parse_int_bullet(text: str, label: str):
    value = parse_bullet(text, label)
    if value is None:
        return None
    try:
        return int(re.search(r'\d+', value).group())
    except Exception:
        return None


def read(path: Path):
    return path.read_text(encoding='utf-8')


def ensure_sections(text: str, sections, errors, path_label):
    for sec in sections:
        if sec not in text:
            errors.append(f'missing {path_label} section {sec}')


def split_entries(text: str):
    return [chunk.strip() for chunk in re.split(r'(?=^## )', text, flags=re.MULTILINE) if chunk.strip().startswith('## ')]

def ensure_entry_fields(text: str, fields, errors, file_label):
    entries = split_entries(text)
    if not entries:
        errors.append(f'no structured entries found in {file_label}')
        return
    for idx, entry in enumerate(entries, start=1):
        for field in fields:
            if f'- {field}:' not in entry:
                errors.append(f'missing field "{field}" in {file_label} entry {idx}')


def newest_date(paths):
    candidates = [p for p in paths if p.exists()]
    if not candidates:
        return None
    latest = max(candidates, key=lambda p: p.stat().st_mtime).stat().st_mtime
    return datetime.fromtimestamp(latest, tz=timezone.utc)


def check_project(project_dir: Path):
    errors = []
    for name in REQ_ROOT_FILES:
        if not (project_dir / name).is_file():
            errors.append(f'missing {name}')
    for name in REQ_ROOT_DIRS:
        if not (project_dir / name).is_dir():
            errors.append(f'missing {name}/')
    if errors:
        return errors
    allowed_root = set(REQ_ROOT_FILES + REQ_ROOT_DIRS)
    extra_root = noncanonical(project_dir, allowed_root)
    if extra_root:
        errors.append('noncanonical project root children: ' + ', '.join(extra_root))
    for name in REQ_CONTEXT:
        if not (project_dir / 'context' / name).is_file():
            errors.append(f'missing context/{name}')
    for name in REQ_PROBLEMS:
        if not (project_dir / 'problems_and_solutions' / name).is_file():
            errors.append(f'missing problems_and_solutions/{name}')
    for name in REQ_HANDOFF:
        if not (project_dir / 'handoff' / name).is_file():
            errors.append(f'missing handoff/{name}')
    for name in REQ_PROCESS:
        if not (project_dir / 'process' / name).is_dir():
            errors.append(f'missing process/{name}/')
    for name in REQ_FINALIZED:
        if not (project_dir / 'finalized' / name).is_dir():
            errors.append(f'missing finalized/{name}/')

    # Generic structured-file checks
    roadmap_path = project_dir / 'context' / 'CASE_STUDY_ROADMAP.md'
    active_path = project_dir / 'context' / 'ACTIVE_STATE.md'
    bundle_path = project_dir / 'handoff' / 'DOWNLOAD_BUNDLE_MANIFEST.md'
    problem_path = project_dir / 'problems_and_solutions' / 'PROBLEM_LOG.md'
    decision_path = project_dir / 'problems_and_solutions' / 'DECISION_LOG.md'
    project_error_path = project_dir / 'problems_and_solutions' / 'PROJECT_SPECIFIC_ERRORS.md'

    if roadmap_path.exists():
        roadmap_text = read(roadmap_path)
        ensure_sections(roadmap_text, ROADMAP_SECTIONS, errors, 'roadmap')
    if active_path.exists():
        active_text = read(active_path)
        for marker in ACTIVE_REQUIRED:
            if marker not in active_text:
                errors.append(f'missing ACTIVE_STATE field {marker}')
        if '- Continuity status:' in active_text:
            pass
        else:
            for marker in ACTIVE_STATUS_BLOCK:
                if marker not in active_text:
                    errors.append(f'missing ACTIVE_STATE status block field {marker}')
    if bundle_path.exists():
        bundle_text = read(bundle_path)
        for marker in BUNDLE_REQUIRED:
            if marker not in bundle_text:
                errors.append(f'missing DOWNLOAD_BUNDLE_MANIFEST field {marker}')
    if problem_path.exists():
        ensure_entry_fields(read(problem_path), PROBLEM_FIELDS, errors, 'PROBLEM_LOG.md')
    if decision_path.exists():
        ensure_entry_fields(read(decision_path), DECISION_FIELDS, errors, 'DECISION_LOG.md')
    if project_error_path.exists():
        project_error_text = read(project_error_path)
        # only enforce entry structure if there are actual project errors recorded
        if '## ' in project_error_text:
            ensure_entry_fields(project_error_text, PROJECT_ERROR_FIELDS, errors, 'PROJECT_SPECIFIC_ERRORS.md')

    if project_dir.name == 'designpilot':
        for rel in FLAGSHIP_PROOF:
            if not (project_dir / rel).exists():
                errors.append(f'missing flagship proof artifact {rel}')
        prompt_dir = project_dir / 'process' / 'research' / 'prompt-packs'
        if not prompt_dir.is_dir():
            errors.append('missing process/research/prompt-packs/')
        else:
            prompt_count = len(list(prompt_dir.glob('*.md')))
            if prompt_count == 0:
                errors.append('no stored research prompt packs found')

        roadmap_text = read(roadmap_path)
        bundle_text = read(bundle_path)

        benchmark_count = len(list((project_dir / 'process' / 'reviews' / 'benchmarks').glob('*.json')))
        external_count = len([p for p in (project_dir / 'process' / 'reviews' / 'external_signals').glob('*.md') if p.name != 'TRUST_SIGNAL_LOG.md'])
        prompt_count = len(list((project_dir / 'process' / 'research' / 'prompt-packs').glob('*.md')))

        reported_benchmark = parse_int_bullet(roadmap_text, 'Benchmark artifact count')
        reported_external = parse_int_bullet(roadmap_text, 'External confidence artifact count')
        reported_prompt = parse_int_bullet(roadmap_text, 'Research prompt packs stored')
        if reported_benchmark != benchmark_count:
            errors.append(f'roadmap benchmark count mismatch: {reported_benchmark} != {benchmark_count}')
        if reported_external != external_count:
            errors.append(f'roadmap external confidence count mismatch: {reported_external} != {external_count}')
        if reported_prompt != prompt_count:
            errors.append(f'roadmap prompt-pack count mismatch: {reported_prompt} != {prompt_count}')

        artifact_paths = (
            list((project_dir / 'process' / 'reviews' / 'benchmarks').glob('*')) +
            list((project_dir / 'process' / 'reviews' / 'external_signals').glob('*')) +
            list((project_dir / 'process' / 'research' / 'prompt-packs').glob('*')) +
            [project_dir / 'process' / 'structure' / 'case-study' / 'CLAIM_TO_PROOF_MAP.md',
             project_dir / 'finalized' / 'deliverables' / 'proof' / 'PROOF_STACK_SUMMARY.md']
        )
        newest = newest_date(artifact_paths)
        if newest is not None:
            expected_anchor = newest.strftime('%Y-%m-%dT%H:%M:%SZ')
            roadmap_anchor = parse_bullet(roadmap_text, 'Artifact freshness anchor')
            bundle_anchor = parse_bullet(bundle_text, 'Continuity freshness anchor')
            if roadmap_anchor != expected_anchor:
                errors.append(f'roadmap freshness anchor mismatch: {roadmap_anchor} != {expected_anchor}')
            if bundle_anchor != expected_anchor:
                errors.append(f'bundle freshness anchor mismatch: {bundle_anchor} != {expected_anchor}')
            if roadmap_path.stat().st_mtime + 1 < newest.timestamp():
                errors.append('roadmap appears older than newest proof artifact')
            if bundle_path.stat().st_mtime + 1 < newest.timestamp():
                errors.append('bundle manifest appears older than newest proof artifact')

        proof_summary = read(project_dir / 'finalized' / 'deliverables' / 'proof' / 'PROOF_STACK_SUMMARY.md')
        if 'Production outcome proof is still open' not in proof_summary:
            errors.append('proof summary missing production outcome proof boundary')
        if 'production outcome proof open' not in roadmap_text.lower():
            errors.append('roadmap missing production outcome proof boundary')

    return errors


def main():
    failures = 0
    for project_dir in sorted(PROJECTS.iterdir()):
        if not project_dir.is_dir() or project_dir.name.startswith('_'):
            continue
        errors = check_project(project_dir)
        if errors:
            failures += 1
            print(f'FAIL {project_dir.name}')
            for error in errors:
                print(f'  ERROR {error}')
        else:
            print(f'PASS {project_dir.name}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
