# Project File System Protocol

Project roots are locked and may not drift at the controlled levels.

## Canonical root
```text
projects/<project-slug>/
  README.md
  process/
  finalized/
  problems_and_solutions/
  context/
  handoff/
```

## Required controlled children
### process/
- briefs/
- research/
- strategy/
- structure/
- design/
- specs/
- reviews/
- iterations/
- assets/

### finalized/
- deliverables/
- exports/
- approved_specs/
- release_notes/

### context/
- PROJECT_OVERVIEW.md
- ACTIVE_STATE.md
- TASK_QUEUE.md
- WORKSPACE_MODE.md
- CASE_STUDY_ROADMAP.md

### problems_and_solutions/
- PROBLEM_LOG.md
- DECISION_LOG.md
- PROJECT_SPECIFIC_ERRORS.md

### handoff/
- HANDOFF_NOTES.md
- IMPLEMENTATION_CHECKLIST.md
- OPEN_QUESTIONS.md
- DOWNLOAD_BUNDLE_MANIFEST.md

## Standardized persistence folders
These are not required in every project, but when the project uses them the names are locked:
- `process/research/prompt-packs/` for persisted deep-research prompt packs
- `process/reviews/benchmarks/` for benchmark receipts
- `process/reviews/external_signals/` for reviewer confidence and trust artifacts
- `process/specs/proof/` for proof scorecards and matrices
- `process/structure/case-study/` for narrative and claim mapping
- `finalized/deliverables/proof/` for exported proof summaries

## Research prompt pack naming
Use stable, decision-led names such as:
- `market-gap-prompt-pack-v1.md`
- `user-research-gap-prompt-pack-v1.md`
- `case-study-proof-gap-prompt-pack-v1.md`

## DesignPilot proof extensions
The flagship project maintains the deeper proof folders above and treats them as continuity-critical rather than optional convenience folders.
