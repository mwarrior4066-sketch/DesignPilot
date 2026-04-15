#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

SEVERITY_ORDER = {
    'BLOCKER': 4,
    'ERROR': 3,
    'WARN': 2,
    'INFO': 1,
}
FAIL_SEVERITIES = {'BLOCKER', 'ERROR'}


def issue(severity: str, message: str, *, code: Optional[str] = None, source: Optional[str] = None, details: Any = None) -> Dict[str, Any]:
    sev = severity.upper().strip()
    if sev not in SEVERITY_ORDER:
        raise ValueError(f'Unsupported severity: {severity}')
    record: Dict[str, Any] = {'severity': sev, 'message': message}
    if code:
        record['code'] = code
    if source:
        record['source'] = source
    if details is not None:
        record['details'] = details
    return record


def issues_from_legacy(*, blockers: Optional[Iterable[str]] = None, errors: Optional[Iterable[str]] = None, warnings: Optional[Iterable[str]] = None, infos: Optional[Iterable[str]] = None, source: Optional[str] = None) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for sev, values in [('BLOCKER', blockers), ('ERROR', errors), ('WARN', warnings), ('INFO', infos)]:
        for value in values or []:
            out.append(issue(sev, str(value), source=source))
    return out


def decision_for(issues: Iterable[Dict[str, Any]], *, warn_only: bool = False) -> str:
    if warn_only:
        return 'PASS'
    for item in issues:
        if item.get('severity') in FAIL_SEVERITIES:
            return 'FAIL'
    return 'PASS'


def metrics_dict(**kwargs: Any) -> Dict[str, Any]:
    return {k: v for k, v in kwargs.items()}


def build_report(name: str, issues: List[Dict[str, Any]], *, metrics: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, Any]] = None, warn_only: bool = False) -> Dict[str, Any]:
    metrics = metrics or {}
    metadata = metadata or {}
    decision = decision_for(issues, warn_only=warn_only)
    counts = {sev: 0 for sev in SEVERITY_ORDER}
    for item in issues:
        counts[item['severity']] = counts.get(item['severity'], 0) + 1
    report = {
        'validator': name,
        'decision': decision,
        'warn_only': warn_only,
        'issue_counts': counts,
        'issues': sorted(issues, key=lambda x: SEVERITY_ORDER.get(x['severity'], 0), reverse=True),
        'metrics': metrics,
        'metadata': metadata,
    }
    return report


def write_report(path: Path, report: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2), encoding='utf-8')


def print_report(report: Dict[str, Any]) -> None:
    print(json.dumps(report, indent=2))


def exit_code_for(report: Dict[str, Any]) -> int:
    return 1 if report.get('decision') == 'FAIL' else 0


def aggregate_reports(name: str, reports: List[Dict[str, Any]], *, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    issues: List[Dict[str, Any]] = []
    metrics: Dict[str, Any] = {'validators': len(reports)}
    for report in reports:
        issues.extend(report.get('issues', []))
        metrics[report.get('validator', f'validator_{len(metrics)}')] = report.get('decision')
    return build_report(name, issues, metrics=metrics, metadata=metadata or {'validators': [r.get('validator') for r in reports]})
