#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ('control', ['README.md','CHANGELOG.md','QUICKSTART.md','PACK_MANIFEST.json','src/operator/**/*.md','src/operator/**/*.json','scripts/*.py'], []),
    ('schemas', ['src/schemas/*.json'], []),
    ('skills', ['src/skills/*.md'], []),
    ('templates', ['src/templates/*.md'], []),
    ('source_docs', ['src/knowledge-base/source-docs/*'], []),
    ('summaries', ['src/knowledge-base/summaries/*.md'], []),
    ('runtime_summaries', ['src/knowledge-base/summaries/*.md'], []),
    ('runtime', ['src/runtime/**/*.md','src/runtime/**/*.json'], []),
    ('indices', ['src/knowledge-base/indices/*.json'], []),
    ('libraries', ['src/libraries/*'], []),
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
(ROOT/'src'/'operator'/'reference'/'SOURCE_REFERENCE_REGISTRY.json').write_text(json.dumps(registry, indent=2), encoding='utf-8')
print(f'wrote src/operator/reference/SOURCE_REFERENCE_REGISTRY.json with {len(entries)} entries')
