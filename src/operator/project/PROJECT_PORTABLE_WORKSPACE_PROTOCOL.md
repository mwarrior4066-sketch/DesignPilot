---
summary_version: 1.1.0
source_reference: internal://designpilot/project-portable-workspace-protocol
last_updated: 2026-04-10
synchronized: true
domain: project-operations
---
# Project Portable Workspace Protocol

## Purpose
Define how the operator should preserve project structure and history when direct filesystem access is unavailable.

## Core rule
Lack of filesystem access is not permission to lose project state.
The operator should maintain a portable workspace model that mirrors the standard project directory layout and can be turned into downloadable files without extra reconstruction.

## Portable workspace model
Maintain this exact logical schema in session state:
- `process/briefs/`
- `process/research/`
- `process/strategy/`
- `process/structure/`
- `process/design/`
- `process/specs/`
- `process/reviews/`
- `process/iterations/`
- `process/assets/`
- `finalized/deliverables/`
- `finalized/exports/`
- `finalized/approved_specs/`
- `finalized/release_notes/`
- `problems_and_solutions/`
- `context/`
- `handoff/`

Treat each important artifact as belonging to one of those canonical locations even before it exists as a physical file.

## What to preserve automatically
Preserve all of these without waiting for the user to ask:
- current brief / problem framing
- major draft artifacts
- major revisions and splits
- meaningful issues and fixes
- meaningful decisions
- finalized outputs
- handoff-ready notes
- active state and next steps

## Bundle readiness rule
A portable workspace should be considered bundle-ready when:
- multiple substantial artifacts exist
- the session has crossed a meaningful milestone
- project continuity would be harmed by losing the current structure
- the user asks for files or a download

## Export behavior
When the bundle is requested or triggered, emit a downloadable workspace that mirrors the exact standard project template with current content written into:
- context files
- process files for in-progress artifacts
- finalized files for stable outputs
- problem and decision logs
- handoff notes and manifest

## Do not do
- do not keep project memory only as scattered chat text
- do not wait until the end of a long session to reconstruct everything from memory
- do not export a flat dump if the project has clear process vs finalized separation
- do not invent portable-only folder names that break the canonical filesystem schema


## Continuity reminder
Portable mode still has to maintain the continuity files owned by `PROJECT_STATE_PROTOCOL.md`.
A bundle is not valid if roadmap or project-specific error files are materially stale after major project changes.
