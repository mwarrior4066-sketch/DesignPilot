#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGETS = [
    ('control', ['*.md', '*.json', '*.py'], ['README.md','CHANGELOG.md','PACK_MANIFEST.json','VERSIONING_POLICY.md','MASTER_CHAT_OPERATOR.md','TASK_ROUTER.md','RUNTIME_VALIDATION_LAYER.md','OUTPUT_CONTRACTS_BY_TASK.md','ROUTE_CATALOG.md','PACK_QUALITY_RUBRIC.md','PROJECT_FILE_SYSTEM_PROTOCOL.md','PROJECT_STATE_PROTOCOL.md']),
    ('schemas', ['schemas/*.json'], []),
    ('skills', ['skills/*.md'], []),
    ('templates', ['templates/*.md'], []),
    ('source_docs', ['knowledge-base/source-docs/*'], []),
    ('summaries', ['knowledge-base/summaries/*.md'], []),
    ('runtime_summaries', ['knowledge-base/runtime-summaries/*.md'], []),
    ('runtime', ['runtime/**/*.md','runtime/**/*.json'], []),
    ('indices', ['knowledge-base/indices/*.json'], []),
    ('libraries', ['libraries/*'], []),
    ('projects', ['projects/designpilot/context/*.md','projects/designpilot/problems_and_solutions/*.md'], []),
]
entries = []
for kind, patterns, pinned in TARGETS:
    for rel in pinned:
        p = ROOT / rel
        if p.exists():
            entries.append({'path': rel, 'kind': kind, 'owner': 'pack-maintainer'})
    for pat in patterns:
        for p in sorted(ROOT.glob(pat)):
            if p.is_file():
                rel = p.relative_to(ROOT).as_posix()
                if not any(e['path'] == rel for e in entries):
                    entries.append({'path': rel, 'kind': kind, 'owner': 'pack-maintainer'})
registry = {'registry_version':'1.0.0','pack_version': json.loads((ROOT/'PACK_MANIFEST.json').read_text())['version'], 'entries': entries}
(ROOT/'SOURCE_REFERENCE_REGISTRY.json').write_text(json.dumps(registry, indent=2), encoding='utf-8')
print(f'wrote SOURCE_REFERENCE_REGISTRY.json with {len(entries)} entries')
