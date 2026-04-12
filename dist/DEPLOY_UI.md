# DEPLOY_UI

UI-heavy deployment for interface systems, components, grids, accessibility, and implementation realism.

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

### api-reliability-security-expert

- Source: `src/skills/api-reliability-security-expert.md`
- Purpose: Use this skill when the answer depends on structured failures, authorization perimeters, retry safety, async job lifecycles, resilience patterns, quotas, or telemetry across API and tool boundaries.

### back-end-aware-planner

- Source: `src/skills/back-end-aware-planner.md`
- Purpose: Use this skill as a strict feasibility control plane between product or design intent and engineering reality. It translates visual or workflow requests into explicit requirements for actors, permissions, data models, APIs, storage, exports, background jobs, observability, and degraded modes. It is the gate, not the deep architecture owner.

### back-end-systems-architect

- Source: `src/skills/back-end-systems-architect.md`
- Purpose: Use this skill for deeper system-architecture work beyond feasibility: authority boundaries, authorization model, consistency stance, pagination, async events, webhooks, multi-tenancy, and observability.

### color-system-expert

- Source: `src/skills/color-system-expert.md`
- Purpose: Use this skill to build or evaluate palettes by semantic role, domain fit, contrast, dark-mode behavior, state logic, data-vis safety, and print awareness.

### component-systems-expert

- Source: `src/skills/component-systems-expert.md`
- Purpose: Use this skill to decide whether a component should exist, how it should be documented, what variants and states it needs, and how reuse beats drift.

### dashboard-data-expert

- Source: `src/skills/dashboard-data-expert.md`
- Purpose: Use this skill to make production-level decisions about dashboard type, KPI hierarchy, chart choice, density, filters, drill-down, and dense-data readability.

### document-accessibility-expert

- Source: `src/skills/document-accessibility-expert.md`
- Purpose: Use this skill to preserve or restore document accessibility: tagging, reading order, artifacts, Unicode mapping, OCR remediation, and extraction fidelity.

### front-end-architecture-expert

- Source: `src/skills/front-end-architecture-expert.md`
- Purpose: Use this skill for production-level front-end architecture decisions: rendering model, server and client boundaries, state ownership, mutation strategy, semantic structure, accessibility behavior at the system layer, and performance cost.

### front-end-handoff-expert

- Source: `src/skills/front-end-handoff-expert.md`
- Purpose: Use this skill as the gateway that translates design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence. It is not the owner of deep front-end architecture decisions.

### grid-system-expert

- Source: `src/skills/grid-system-expert.md`
- Purpose: Use this skill to choose new grid systems by medium and content type: web, app, slide, editorial, dashboard, and document layouts.

### layout-reconstruction-expert

- Source: `src/skills/layout-reconstruction-expert.md`
- Purpose: Use this skill to infer, reconstruct, normalize, and extend existing layouts from screenshots, PDFs, and legacy designs.

### pdf-layout-expert

- Source: `src/skills/pdf-layout-expert.md`
- Purpose: Use this skill to edit, repair, or rebuild PDFs while preserving frame logic, baseline rhythm, visual hierarchy, and layout integrity.

### type-system-expert

- Source: `src/skills/type-system-expert.md`
- Purpose: Use this skill to choose, compare, pair, substitute, and deploy typefaces intelligently across UI, editorial, brand, dashboards, presentations, print, accessibility-sensitive, and multilingual systems.

### ui-system-expert

- Source: `src/skills/ui-system-expert.md`
- Purpose: Use this skill to organize screens, flows, navigation, information architecture, and action hierarchy into a coherent interface system.

## Supporting source anchors

### Source: `src/operator/reference/DESIGN_TOKEN_ARCHITECTURE.md`

# Design Token Architecture

Use this file to keep design decisions translatable to code.

## Token layers
1. Primitive tokens — raw values
2. Semantic tokens — role-based aliases
3. Component tokens — component-specific applications

## Naming rule
Use:
`{category}-{role}-{variant}-{state}`

Examples:
- `color-text-primary`
- `color-border-negative`
- `space-layout-page-x`
- `radius-control-sm`
- `motion-feedback-fast`
- `button-bg-primary-hover`

## Non-negotiables
- primitives must not be used directly in component code unless no semantic alias exists yet
- names must not encode raw values like `16px` or `blue`
- stateful components must have state tokens or state rules
- dark mode must swap through semantic aliases, not one-off overrides
- token output should stay flat and human-readable

## Default stack
- color
- typography
- spacing
- radius
- border
- shadow
- motion
- z-index / layering
- component aliases

## Validation checks
- max 3 alias layers
- avoid more than 5 name segments
- reject raw-value naming
- prefer semantic and component aliases over ad hoc literals

### Source: `src/operator/protocols/VISUAL_INPUT_PROTOCOL.md`

# Visual Input Protocol

Use this protocol when the task includes screenshots, mockups, page images, or image-based PDFs.
This is a pre-pass, not a standalone deliverable route.

## Purpose
Visual inputs are evidence-bearing, but they are incomplete.
The operator must separate what is visible from what is inferred.

## Required extraction fields
- artifact type
- layout type
- visible components
- hierarchy cues
- probable grid structure
- approximate type scale
- density and grouping cues
- visible state cues if present
- mismatch between user description and visible evidence
- confidence level

## Evidence classes
Mark observations as one of:
- observed
- inferred
- unverified

## Confidence scale
- high: directly visible and stable from the artifact
- medium: strongly suggested by spacing, grouping, or repeated structure
- low: plausible but not confirmable from the artifact alone

## Rules
- do not claim unseen interaction behavior from static pixels alone
- do not claim source-file semantics, accessibility tree logic, or document tags from screenshots alone
- do not treat image-based PDFs as semantically trustworthy documents
- surface user-description mismatches explicitly
- keep inferred grid and type claims bounded by confidence language

## Routing handoff
After the visual pre-pass:
- UI/hierarchy failures -> `rt_ui_structure_critique`
- KPI order and dense-data failures -> `rt_dashboard_audit`
- artifact recovery or extension -> `rt_layout_reconstruction_plan`
- document semantics or extraction risk -> `rt_pdf_remediation`
