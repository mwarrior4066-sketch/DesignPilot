# Regression Testing Protocol

## Purpose
Keep the pack stable as files change.
Do not trust a new version because it feels better.
The canonical machine-readable suite lives in `tests/regression_suite.json` and is executed by `run_regression_suite.py`.

## Test classes
### Smoke tests
Run after any control-layer change.
Source: `SYSTEM_TEST_CASES.md`

### Pathway regression
Run after edits to routers, skills, or reference mapping.
Check that the same prompt still activates the expected pathway.

### Domain regression
Run after edits to specialist skills, summaries, templates, or libraries.
Check that domain-specific hard fails still trigger.

### Golden-set regression
Run after major pack upgrades.
Use a stable set of 20–40 prompts with known good outputs or known pass/fail expectations.

## Re-test triggers
### Re-test all control-layer regressions after changes to:
- `MASTER_CHAT_OPERATOR.md`
- `SYSTEM_PRECEDENCE.md`
- `MODE_SYSTEM.md`
- `ROADMAP_ROUTER.md`
- `TASK_ROUTER.md`
- `RESPONSE_PROTOCOL.md`
- `RUNTIME_VALIDATION_LAYER.md`

### Re-test pathway and domain regressions after changes to:
- any skill file
- `SKILL_REFERENCE_MAP.md`
- `KNOWLEDGE_LOADING_PROTOCOL.md`
- domain summaries
- output contracts
- domain validators

### Re-test source grounding after changes to:
- source-doc markdown
- summaries
- library entries

## Release gates
A version can ship only if:
- all smoke tests pass
- no P0/P1 regression fails
- weighted score on the golden set does not drop by more than 0.3 average points
- no new contradiction failure appears in unchanged pathways

## Comparison method
Track for each golden case:
- mode
- phase behavior
- pathway
- contract completeness
- hard-gate status
- weighted score
- release decision

## Notes
Do not compare only wording.
Compare decision quality and failure safety.


## Executable harness
Release checks should run the machine-readable suite, not only the prose test docs.
Use the golden outputs folder for stable baseline behavior and update it only when a deliberate contract change has been approved.


## Version-bump tie-in
- failing regressions block any release, regardless of bump size
- a new capability that preserves compatibility is usually a `0.10` change
- a regression or release-metadata fix with no contract change is usually a `0.01` change
- a breaking routing, schema, or release-line reset is a `1.00` change
