---
summary_version: 1.2.0
source_reference: internal://designpilot/project-logging-protocol
last_updated: 2026-04-10
synchronized: true
domain: project-operations
---
# Project Logging Protocol

## Purpose
Standardize project logging so problem history, decisions, and release readiness survive across sessions and are specific enough to teach the pack what went wrong.

This protocol applies in both:
- **filesystem mode** using real files
- **portable workspace mode** using an export-ready in-memory workspace until files are requested or automatically bundled

## Required logs
- `problems_and_solutions/PROBLEM_LOG.md`
- `problems_and_solutions/DECISION_LOG.md`
- `problems_and_solutions/PROJECT_SPECIFIC_ERRORS.md`
- `context/ACTIVE_STATE.md`
- `handoff/DOWNLOAD_BUNDLE_MANIFEST.md`

Roadmap freshness is owned by `PROJECT_STATE_PROTOCOL.md`. This file governs **how** logs are written.

## Classification taxonomy
Use one primary classification per entry:
- `routing_error`
- `evidence_error`
- `continuity_error`
- `validation_error`
- `implementation_realism_error`
- `overclaim_error`
- `template_misuse`
- `project_specific_constraint_miss`

## PROBLEM_LOG entry format
```md
## YYYY-MM-DD HH:MM — <short issue title>
- Error ID:
- Classification:
- Context:
- Artifact(s):
- Severity:
- Surfaced by:
- What went wrong:
- Why it happened:
- Missing or violated rule:
- Fix applied:
- Prevention rule:
- Pack-level or project-level:
- Status:
```

## DECISION_LOG entry format
```md
## YYYY-MM-DD HH:MM — <decision title>
- Decision ID:
- Classification:
- Context:
- Options considered:
- Decision:
- Why:
- Files affected:
- Validation impact:
- Follow-up:
```

## PROJECT_SPECIFIC_ERRORS entry format
```md
## <error title>
- Error ID:
- Classification:
- Context:
- What went wrong:
- Why it happened:
- Missing or violated rule:
- Fix applied:
- Prevention rule:
- Pack-level or project-level:
- Status:
```

## ACTIVE_STATE contents
Keep this short and current:
- project goal
- active phase
- active task
- workspace mode
- files being worked on
- continuity status
- blockers
- next action

## DOWNLOAD_BUNDLE_MANIFEST contents
Track what should be included when a downloadable workspace is created:
- project slug
- workspace mode
- current milestone
- populated files by folder
- finalized artifacts ready for export
- open work still in process
- continuity freshness anchor
- last bundle-ready timestamp

## Logging threshold
Create a problem log entry only for meaningful problems, not tiny copy edits. Log when the issue changes structure, quality, direction, proof honesty, or deliverable reliability.

Create a decision log entry whenever the operator:
- changes architecture or structure
- changes theme or system logic
- splits or merges deliverables
- changes a route, phase, or implementation path
- adds a new release gate or continuity rule
- adopts a new rule to avoid repeated failure

## Portable mode behavior
If filesystem access is unavailable:
- continue maintaining log entries as if the files existed
- keep the current contents export-ready
- update the bundle manifest as progress accumulates
- preserve the same field structure so the project can be written to disk later without translation
