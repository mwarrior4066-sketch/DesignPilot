#!/usr/bin/env python3
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from runtime_validator import validate_output
from validate_lightweight_path import validate_lightweight_path

SUITE_PATH = ROOT / 'tests' / 'regression_suite.json'
MANIFEST_PATH = ROOT / 'PACK_MANIFEST.json'


def main():
    suite = json.loads(SUITE_PATH.read_text(encoding='utf-8'))
    manifest = json.loads(MANIFEST_PATH.read_text(encoding='utf-8'))
    failures = 0
    category_totals = Counter()
    category_failures = Counter()
    if suite.get('pack_version') != manifest.get('version'):
        print(f"ERROR regression suite pack_version {suite.get('pack_version')} does not match manifest version {manifest.get('version')}")
        raise SystemExit(1)
    print(f"Regression suite {suite.get('suite_version')} for pack {suite.get('pack_version')}")
    for test in suite['tests']:
        category = test.get('category', 'uncategorized')
        category_totals[category] += 1
        rel = Path(test['golden_output_file'])
        output_path = (ROOT / rel) if (ROOT / rel).exists() else (ROOT / 'tests' / rel)
        output = output_path.read_text(encoding='utf-8')
        report = validate_output(test['validator_task'], test['prompt'], output)
        test_failures = []
        if report['decision'] != test['expected_decision']:
            test_failures.append(f"expected decision {test['expected_decision']} got {report['decision']}")
        issue_ids = {item['id'] for item in report['issues']}
        for issue in test.get('expected_issue_ids', []):
            if issue not in issue_ids:
                test_failures.append(f"expected issue missing: {issue}")
        for issue in test.get('required_issue_absent', []):
            if issue in issue_ids:
                test_failures.append(f"issue should be absent but was present: {issue}")
        if test_failures:
            failures += 1
            category_failures[category] += 1
            print(f"FAIL {test['id']} [{category}] — {test['title']}")
            for failure in test_failures:
                print(f"  ERROR {failure}")
            print(json.dumps(report, indent=2))
        else:
            print(f"PASS {test['id']} [{category}] — {test['title']}")
    print('--- category summary ---')
    for category in sorted(category_totals):
        print(f"{category}: {category_totals[category] - category_failures[category]}/{category_totals[category]} passed")
    lite_report = validate_lightweight_path(ROOT)
    if lite_report['decision'] != 'PASS':
        failures += 1
        print('FAIL lightweight-path validation')
        print(json.dumps(lite_report, indent=2))
    else:
        print('PASS lightweight-path validation')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
