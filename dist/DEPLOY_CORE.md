# DEPLOY_CORE

General DesignPilot deployment for critique, planning, audit, rebuild, and cross-domain work.

## Supported use
- full mode: load this profile with `dist/DESIGNPILOT_DEPLOY.md` for compound work inside this domain
- profile-only mode: load just this profile with `dist/SESSION_ZERO.md` for focused single-domain work

## Profile rules
- keep one governing route visible
- do not load another profile unless the task truly spans domains
- switch to the kernel when cross-domain coordination, proof sensitivity, or competing constraints rise

## Included skills

### accessibility-feedback-expert

- Source: `src/skills/accessibility-feedback-expert.md`
- Purpose: Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.

### back-end-aware-planner

- Source: `src/skills/back-end-aware-planner.md`
- Purpose: Use this skill as a strict feasibility control plane between product or design intent and engineering reality. It translates visual or workflow requests into explicit requirements for actors, permissions, data models, APIs, storage, exports, background jobs, observability, and degraded modes. It is the gate, not the deep architecture owner.

### component-systems-expert

- Source: `src/skills/component-systems-expert.md`
- Purpose: Use this skill to decide whether a component should exist, how it should be documented, what variants and states it needs, and how reuse beats drift.

### content-and-case-study-expert

- Source: `src/skills/content-and-case-study-expert.md`
- Purpose: Use this skill to audit, rewrite, expand, or structure UX copy, design rationale, documentation, and case-study writing without losing clarity, mode control, or evidence.

### dashboard-data-expert

- Source: `src/skills/dashboard-data-expert.md`
- Purpose: Use this skill to make production-level decisions about dashboard type, KPI hierarchy, chart choice, density, filters, drill-down, and dense-data readability.

### front-end-handoff-expert

- Source: `src/skills/front-end-handoff-expert.md`
- Purpose: Use this skill as the gateway that translates design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence. It is not the owner of deep front-end architecture decisions.

### layout-reconstruction-expert

- Source: `src/skills/layout-reconstruction-expert.md`
- Purpose: Use this skill to infer, reconstruct, normalize, and extend existing layouts from screenshots, PDFs, and legacy designs.

### text-humanization-expert

- Source: `src/skills/text-humanization-expert.md`
- Purpose: Use this skill to revise prose so it sounds authored, readable, and natural without changing meaning, adding claims, or flattening the writer’s voice.

### ui-system-expert

- Source: `src/skills/ui-system-expert.md`
- Purpose: Use this skill to organize screens, flows, navigation, information architecture, and action hierarchy into a coherent interface system.

### ux-research-expert

- Source: `src/skills/ux-research-expert.md`
- Purpose: Use this skill to frame the problem, identify the user, surface cognitive/ergonomic constraints, and keep work tied to real needs instead of surface styling.

## Supporting source anchors

### Source: `src/operator/project/PROJECT_STATE_PROTOCOL.md`

# Project State Protocol

The continuity layer distinguishes between four proof states and treats continuity as an artifact-backed system rather than a folder-presence ritual.

## Proof families
- **internal operator proof**: routes, contracts, validation, continuity, and failure-prevention behavior
- **comparative proof**: benchmark deltas, controlled baseline comparisons, and scored output differences
- **external confidence proof**: reviewer confidence, user confidence, live artifact reviews, and production-adjacent trust receipts
- **production outcome proof**: measured outcomes from real usage, implementation receipts, or shipped-system impact

## Required continuity files for every project
- `context/CASE_STUDY_ROADMAP.md`
- `context/ACTIVE_STATE.md`
- `problems_and_solutions/PROJECT_SPECIFIC_ERRORS.md`

## Required roadmap sections
Every project roadmap must include:
- `## Project identity`
- `## Proof state`
- `## Done before`
- `## Just added`
- `## Needed next`
- `## Open risks`
- `## Next validation move`
- `## Pending artifacts`
- `## Release readiness`

## Meaningful update threshold
Refresh continuity only when one of these happens:
- a benchmark run is added, removed, or materially rescored
- a new example or regression meaningfully changes the proven surface
- a proof claim changes class or wording strength
- validator, route, or contract behavior changes materially
- a new research prompt pack is stored
- a major project-specific error or decision is logged
- a handoff-ready artifact becomes exportable

Do **not** refresh continuity for tiny copy edits, formatting cleanup, or mirror regeneration by itself.

## Artifact-driven freshness rules
The roadmap and bundle manifest must carry:
- `Last meaningful update`
- `Artifact freshness anchor`
- artifact counts for benchmark runs, external confidence artifacts, and stored prompt packs

The freshness anchor must reflect the newest meaningful artifact in the project proof surface. If artifacts change and the roadmap or bundle manifest still report older counts or an older anchor, the workspace is stale.

## Required proof behavior for the flagship DesignPilot workspace
- keep a fixed prompt set for repeatable comparisons
- keep a claim-to-proof map that separates proof classes cleanly
- keep benchmark artifacts in `process/reviews/benchmarks/`
- keep a structured trust log and at least one external confidence artifact
- store research prompt packs in `process/research/prompt-packs/`
- refresh the roadmap, active state, and bundle manifest when the proof surface changes

## Release-readiness language
Continuity files must state what is:
- proven enough to say directly
- only safe to say comparatively or cautiously
- not allowed to claim yet

That keeps the case-study layer aligned with the real evidence state.

### Source: `src/operator/project/PROJECT_FILE_SYSTEM_PROTOCOL.md`

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

### Source: `src/operator/project/PROJECT_LOGGING_PROTOCOL.md`

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
