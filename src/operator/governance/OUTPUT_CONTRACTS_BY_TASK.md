# Output Contracts by Task

> Generated from `src/schemas/task_contracts.json`, stored evals, and `tests/regression_suite.json`. Add contract changes in the schema first, then regenerate.

This is the human-readable contract catalog for the pack. Each contract entry shows the required sections, the named decisions the task must make, the evidence classes that must appear, the shortcut/overclaim patterns that should fail, and the example / regression artifacts that currently prove the route.

## UI Structure Critique

- Task ID: `ui_structure_critique`
- Task group: audit
- Allowed modes: AUDIT, PEER
- Allowed phases: structure, ui
- Required skills: ui-system-expert.md, grid-system-expert.md
- Data owner: ui-system-expert
- Risk tier: medium
- SLA freshness: same release cycle as routing changes

### Why this contract exists
`ui_structure_critique` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Problem framing | 25 words | Sets the user-task and failure frame. |
| Findings | 45 words | Surface real structural failures instead of taste comments. |
| Recommendations | 45 words | Convert critique into concrete structural action. |
| Tradeoffs | 20 words | Show what is preserved and what can flex first. |

### Required decisions
- {'id': 'structural_failure', 'description': 'Names the actual structural failure, not just taste discomfort.', 'any_of': ['failing because', 'failure', 'problem is', 'competes', 'crowded', 'buried', 'diluted', 'slow first parse', 'confusion', 'hierarchy']}
- {'id': 'hierarchy_winner', 'description': 'Names what should win the first scan or primary action hierarchy.', 'any_of': ['primary', 'dominant', 'winner', 'should win', 'first scan', 'unambiguous', 'priority', 'legible', 'clarity should win']}
- {'id': 'intervention_order', 'description': 'Shows the order of interventions or ranked rebuild sequence.', 'any_of': ['first', 'then', 'before', 'after', 'rebuild order', 'move', 'reduce', 'demote', 'collapse']}
- {'id': 'tradeoff_resolution', 'description': 'Resolves clarity against another goal instead of keeping all goals equal.', 'any_of': ['tradeoff', 'rather than', 'instead of', 'preserve', 'sacrifice', 'flex first', 'clarity should win']}
- {'id': 'visual_confidence_boundary', 'description': 'Names what is directly observed vs inferred when visual input is part of the task.', 'any_of': ['confidence', 'observed', 'inferred', 'unverified', 'appears', 'visible evidence']}

### Required evidence classes
- {'class_id': 'state_or_behavior_rule', 'description': 'Uses a hierarchy, flow, scan, or behavior rule.'}
- {'class_id': 'implementation_constraint', 'description': 'Uses a real layout or density constraint.'}
- {'class_id': 'comparison_artifact', 'description': 'Names a rejected alternative or competing pattern.'}
- {'class_id': 'visual_structure_rule', 'description': 'Uses a visual-structure rule when the critique is grounded in screenshots or visible layout evidence.'}

### Example coverage
- ui-structure-critique

### Regression references
- pass-01 (smoke)
- fail-23 (fail-hollow-compliance)

### Forbidden shortcuts
- `cosmetic_cleanup_only` — Cosmetic cleanup cannot stand in for structure.
  - signal: make it prettier
  - signal: just add whitespace
  - signal: looks great as-is
  - signal: visual polish only
- `generic_hierarchy_advice` — Generic hierarchy language cannot pass without naming a winner.
  - signal: improve hierarchy
  - signal: make the cta stronger
  - signal: more emphasis everywhere

### Overclaim rules
- `no_fake_validation` — Do not imply validation or proof without receipts.
  - blocked terms: validated, proven, confirmed
  - evidence escape hatch: benchmark, threshold, [file:, test, evidence
- `no_claimed_user_testing` — Do not imply user evidence that is not actually present.
  - blocked terms: user-tested, users proved, research proved
  - evidence escape hatch: interview, survey, benchmark, [file:

### Legacy fail patterns
- hard fail: looks great as-is
- hard fail: just make it prettier
- hard fail: finalize the UI now
- soft fail: could maybe
- soft fail: might want to consider

## Component Specification

- Task ID: `component_spec`
- Task group: spec
- Allowed modes: REBUILD, PEER
- Allowed phases: specs, ui
- Required skills: component-systems-expert.md, front-end-handoff-expert.md
- Data owner: component-systems-expert
- Risk tier: medium
- SLA freshness: same release cycle as component state changes

### Why this contract exists
`component_spec` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Purpose and scope | 20 words | Defines when the component exists and where it stops. |
| Anatomy | 25 words | Names the governed parts. |
| State matrix | 35 words | Shows interaction and edge states. |
| Accessibility and implementation notes | 35 words | Prevents front-end drift. |

### Required decisions
- {'id': 'component_boundary', 'description': 'Defines what the component owns and what remains outside it.', 'any_of': ['scope', 'owns', 'does not own', 'boundary', 'outside', 'purpose']}
- {'id': 'state_coverage', 'description': 'Makes state coverage explicit rather than implied.', 'any_of': ['state', 'default', 'hover', 'focus', 'disabled', 'error', 'loading', 'selected']}
- {'id': 'accessibility_behavior', 'description': 'Names keyboard, focus, aria, or announcement behavior.', 'any_of': ['keyboard', 'focus', 'aria', 'screen reader', 'announce', 'tab order']}
- {'id': 'implementation_boundary', 'description': 'Shows a token, prop, or implementation constraint.', 'any_of': ['token', 'prop', 'variant', 'implementation', 'boundary', 'do not hardcode']}

### Required evidence classes
- {'class_id': 'state_or_behavior_rule', 'description': 'Uses explicit state or behavior rules.'}
- {'class_id': 'implementation_constraint', 'description': 'Uses component, token, or boundary constraints.'}
- {'class_id': 'standards_reference', 'description': 'Uses aria, keyboard, or accessibility guidance when behavior depends on it.'}

### Example coverage
- component-spec

### Regression references
- pass-02 (smoke)

### Forbidden shortcuts
- `state_tbd` — State logic cannot be deferred.
  - signal: states tbd
  - signal: state later
  - signal: states later
- `accessibility_later` — Accessibility cannot be postponed.
  - signal: accessibility later
  - signal: keyboard later
  - signal: aria later

### Overclaim rules
- `no_unearned_reusability` — Do not call the component reusable without state-safe boundaries.
  - blocked terms: fully reusable, production-ready
  - evidence escape hatch: state matrix, variant, prop, token

### Legacy fail patterns
- hard fail: states TBD
- hard fail: accessibility later
- soft fail: basic component
- soft fail: simple usage

## Dashboard Audit

- Task ID: `dashboard_audit`
- Task group: audit
- Allowed modes: AUDIT, PEER
- Allowed phases: strategy, structure, ui
- Required skills: dashboard-data-expert.md, ui-system-expert.md
- Data owner: dashboard-data-expert
- Risk tier: high
- SLA freshness: same release cycle as KPI or data-source changes

### Why this contract exists
`dashboard_audit` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Dashboard role | 20 words | Classifies the view correctly. |
| Key failures | 45 words | Names priority issues in hierarchy, density, and interpretation. |
| Evidence and rationale | 35 words | Links recommendations to signal quality, KPI logic, or usage risk. |
| Recommended rebuild path | 35 words | Shows the order of correction. |

### Required decisions
- {'id': 'dashboard_type', 'description': 'Classifies the dashboard role or user context.', 'any_of': ['operational', 'executive', 'monitoring', 'analytical', 'dashboard role', 'overview']}
- {'id': 'kpi_priority', 'description': 'Names the KPI or first-scan hierarchy winner.', 'any_of': ['kpi', 'metric', 'first', 'priority', 'above the fold', 'scan time', 'overview']}
- {'id': 'density_strategy', 'description': 'Explains what should be compressed, grouped, or deferred.', 'any_of': ['density', 'group', 'defer', 'scan time', 'cluster', 'progressive disclosure']}
- {'id': 'drilldown_or_filter_logic', 'description': 'Names filter, drill-down, or chart-choice logic.', 'any_of': ['filter', 'drill-down', 'chart', 'table', 'trend', 'compare']}
- {'id': 'visual_confidence_boundary', 'description': 'Names what is directly observed vs inferred when visual input is part of the task.', 'any_of': ['confidence', 'observed', 'inferred', 'unverified', 'appears', 'visible evidence']}

### Required evidence classes
- {'class_id': 'state_or_behavior_rule', 'description': 'Uses scan, interaction, or behavioral rules.'}
- {'class_id': 'measurable_threshold', 'description': 'Uses KPI, threshold, or metric logic.'}
- {'class_id': 'comparison_artifact', 'description': 'Compares chart or layout alternatives.'}
- {'class_id': 'visual_structure_rule', 'description': 'Uses a visual-structure rule when the critique is grounded in screenshots or visible layout evidence.'}

### Example coverage
- dashboard-audit

### Regression references
- pass-03 (smoke)
- fail-01 (fail-depth)

### Forbidden shortcuts
- `more_charts` — Adding more charts is not a hierarchy strategy.
  - signal: add more charts
  - signal: show everything above the fold
- `visual_cleanup_only` — Visual cleanup cannot replace KPI logic.
  - signal: clean up visually
  - signal: make it look modern

### Overclaim rules
- `no_fake_performance_claims` — Do not claim efficiency gains without real metric logic.
  - blocked terms: validated dashboard, proven dashboard
  - evidence escape hatch: metric, benchmark, threshold, [file:

### Legacy fail patterns
- hard fail: add more charts
- hard fail: show everything above the fold
- soft fail: clean up visually

## Back-End Feasibility Review

- Task ID: `backend_feasibility_review`
- Task group: strategy
- Allowed modes: AUDIT, PEER, STRUCTURE
- Allowed phases: strategy, specs
- Required skills: back-end-aware-planner.md, front-end-handoff-expert.md
- Data owner: back-end-aware-planner
- Risk tier: high
- SLA freshness: same release cycle as auth or storage changes

### Why this contract exists
`backend_feasibility_review` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Requested capability | 20 words | States the visible ask and hidden system implications. |
| Hidden system requirements | 45 words | Maps UI ask to auth, storage, exports, or APIs. |
| Feasibility assessment | 35 words | Calls out blockers, assumptions, and sequencing. |
| Safer implementation path | 35 words | Shows a realistic build order. |

### Required decisions
- {'id': 'data_dependency', 'description': 'Names data model, schema, ownership, or retention implications.', 'any_of': ['data model', 'schema', 'ownership', 'record', 'field', 'tenant', 'membership', 'retention', 'object']}
- {'id': 'permissions_dependency', 'description': 'Names auth, role, or access control implications.', 'any_of': ['auth', 'permission', 'role', 'access', 'invite', 'revocation', 'approval']}
- {'id': 'system_surface_dependency', 'description': 'Names storage, export, api, event, or realtime implications.', 'any_of': ['storage', 'export', 'api', 'event', 'realtime', 'polling', 'webhook', 'queue']}
- {'id': 'blocking_constraint', 'description': 'Names what blocks naive implementation or what must come first.', 'any_of': ['only if', 'cannot', 'blocked', 'constraint', 'before', 'first', 'expensive to reverse', 'safer path']}

### Required evidence classes
- {'class_id': 'permission_rule', 'description': 'Uses a permission, auth, or ownership rule.'}
- {'class_id': 'data_model_dependency', 'description': 'Uses schema, ownership, or data dependency logic.'}
- {'class_id': 'implementation_constraint', 'description': 'Uses integration, sequencing, or system constraints.'}

### Example coverage
- backend-feasibility-review

### Regression references
- pass-04 (smoke)

### Forbidden shortcuts
- `visual_only_reframe` — The task cannot be reframed as visual-only.
  - signal: purely visual change
  - signal: no backend impact
  - signal: front-end only
- `handwave_feasibility` — Feasibility cannot be waved through.
  - signal: should be straightforward
  - signal: easy backend task

### Overclaim rules
- `no_security_overclaim` — Do not imply safety or scalability without actual constraints.
  - blocked terms: secure by default, scales automatically
  - evidence escape hatch: permission, audit, retention, queue, limit, [file:

### Legacy fail patterns
- hard fail: purely visual change
- hard fail: no backend impact
- soft fail: should be straightforward

## PDF Remediation Plan

- Task ID: `pdf_remediation_plan`
- Task group: rebuild
- Allowed modes: AUDIT, REBUILD, PEER
- Allowed phases: structure, specs, implementation
- Required skills: document-accessibility-expert.md, pdf-layout-expert.md
- Data owner: document-accessibility-expert
- Risk tier: high
- SLA freshness: same release cycle as remediation tooling or standards changes

### Why this contract exists
`pdf_remediation_plan` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Current failure state | 25 words | Names the real accessibility/document integrity problem. |
| Remediation sequence | 45 words | Orders the steps so semantics are preserved. |
| Verification checks | 35 words | Shows how success is confirmed. |
| Risk controls | 25 words | Prevents destructive edits and copy-paste damage. |

### Required decisions
- {'id': 'semantic_failure', 'description': 'Names structure, tagging, or semantic failure state.', 'any_of': ['semantically broken', 'structure tree', 'tag', 'artifact', 'header association', 'semantic']}
- {'id': 'reading_order_or_extraction', 'description': 'Names reading-order or extraction fidelity concerns.', 'any_of': ['reading order', 'sequence', 'copy-paste', 'extraction', 'unicode', 'ligature', 'text layer']}
- {'id': 'verification_method', 'description': 'Defines how remediation success is checked.', 'any_of': ['verify', 'verification', 'check', 'screen reader', 'extract', 'copy-paste', 'inspect']}
- {'id': 'destructive_shortcut_rejected', 'description': 'Rejects flattening, rasterizing, or OCR-first shortcuts.', 'any_of': ['do not flatten', 'rasterize', 'ocr', 'destructive', 'preserve']}

### Required evidence classes
- {'class_id': 'standards_reference', 'description': 'Uses tagging, accessibility, or document standards references.'}
- {'class_id': 'verification_method', 'description': 'Uses explicit verification checks.'}
- {'class_id': 'implementation_constraint', 'description': 'Uses preservation and sequencing constraints.'}

### Example coverage
- pdf-remediation-plan

### Regression references
- pass-05 (compound)

### Forbidden shortcuts
- `destructive_repair` — Destructive repair cannot be the main fix.
  - signal: flatten the pdf
  - signal: rasterize the page
  - signal: just use ocr only
- `semantic_blur` — The plan cannot blur semantics into visual cleanup.
  - signal: make it accessible somehow
  - signal: looks correct visually so it is fine

### Overclaim rules
- `no_compliance_overclaim` — Do not call the file compliant or accessible without verification.
  - blocked terms: compliant, accessible, pdf/ua ready
  - evidence escape hatch: verification, check, screen reader, extract, [file:

### Legacy fail patterns
- hard fail: flatten the pdf
- hard fail: rasterize the page
- hard fail: just use OCR only
- soft fail: make it accessible somehow

## Brand Positioning Pass

- Task ID: `brand_positioning_pass`
- Task group: strategy
- Allowed modes: AUDIT, REBUILD, PEER
- Allowed phases: strategy, communication
- Required skills: brand-strategy-expert.md, content-and-case-study-expert.md
- Data owner: brand-strategy-expert
- Risk tier: medium
- SLA freshness: same release cycle as audience or market evidence changes

### Why this contract exists
`brand_positioning_pass` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Audience and problem | 25 words | Anchors brand to a real segment and pain. |
| Positioning frame | 35 words | Shows category, alternative, and wedge. |
| Trust and proof burden | 30 words | Prevents adjective-only branding. |
| Messaging consequences | 25 words | Translates strategy into language behavior. |

### Required decisions
- {'id': 'audience_frame', 'description': 'Names the segment and the problem or perception gap.', 'any_of': ['audience', 'segment', 'for', 'buyer', 'customer', 'problem', 'perception gap']}
- {'id': 'differentiation_frame', 'description': 'Names what alternative the brand is being positioned against.', 'any_of': ['against', 'alternative', 'category', 'differentiate', 'frame of reference', 'not just']}
- {'id': 'trust_logic', 'description': 'Names the trust signal or proof burden.', 'any_of': ['trust', 'proof', 'credibility', 'signal', 'receipt', 'evidence']}
- {'id': 'messaging_consequence', 'description': 'Translates the strategy into message or tone behavior.', 'any_of': ['message', 'messaging', 'tone', 'language', 'should sound', 'consequence']}

### Required evidence classes
- {'class_id': 'comparison_artifact', 'description': 'Uses alternative, category, or competitor comparison logic.'}
- {'class_id': 'file_backed_receipt', 'description': 'Uses a proof artifact, signal, or file-backed receipt when available.'}
- {'class_id': 'implementation_constraint', 'description': 'Uses a real constraint such as trust, usability, or category convention.'}

### Example coverage
- brand-positioning-pass

### Regression references
- pass-06 (smoke)
- fail-02 (fail-depth)

### Forbidden shortcuts
- `adjective_stack` — Adjective stacks cannot stand in for positioning.
  - signal: best-in-class brand
  - signal: premium modern innovative
  - signal: strong brand presence
- `tone_without_audience` — Tone advice cannot float without audience logic.
  - signal: cool tone
  - signal: make it feel premium

### Overclaim rules
- `no_market_superiority` — Do not imply superiority without real proof.
  - blocked terms: best, leading, category-defining
  - evidence escape hatch: segment, evidence, benchmark, [file:

### Legacy fail patterns
- hard fail: best-in-class brand
- hard fail: premium modern innovative
- soft fail: strong brand presence

## Case Study Rewrite

- Task ID: `case_study_rewrite`
- Task group: rebuild
- Allowed modes: REBUILD, STRUCTURE, PEER
- Allowed phases: communication, case-study
- Required skills: content-and-case-study-expert.md
- Data owner: content-and-case-study-expert
- Risk tier: medium
- SLA freshness: same release cycle as new proof artifacts

### Why this contract exists
`case_study_rewrite` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Problem | 25 words | Names the original problem and stakes. |
| Process | 35 words | Shows what was actually done, not generic steps. |
| Solution | 35 words | Explains the rebuilt logic or artifact. |
| Outcome and proof | 35 words | Links claims to evidence and open gaps. |

### Required decisions
- {'id': 'claim_vs_proof_boundary', 'description': 'Separates the project claim from the available proof.', 'any_of': ['claim', 'proof', 'evidence', 'what remains open', 'not yet', 'gap']}
- {'id': 'proxy_vs_measured', 'description': 'Distinguishes proxy or internal proof from measured or external proof.', 'any_of': ['proxy', 'measured', 'benchmark', 'internal', 'external', 'confidence artifact']}
- {'id': 'narrative_order', 'description': 'Explains the structural order or why it changed.', 'any_of': ['lead with', 'then', 'order', 'structure', 'rebuild', 'moved']}
- {'id': 'honesty_tradeoff', 'description': 'Resolves narrative smoothness against evidentiary honesty.', 'any_of': ['tradeoff', 'honesty', 'smoothness', 'rather than', 'instead of', 'wins']}

### Required evidence classes
- {'class_id': 'comparison_artifact', 'description': 'Uses benchmark, before/after, or alternative comparison logic.'}
- {'class_id': 'narrative_proof_boundary', 'description': 'Uses explicit claim-to-proof boundary language.'}
- {'class_id': 'file_backed_receipt', 'description': 'Uses benchmark files, maps, or proof artifacts when available.'}

### Example coverage
- case-study-rewrite

### Regression references
- pass-07 (compound)
- fail-03 (fail-proof)

### Forbidden shortcuts
- `storytelling_only` — Storytelling cannot replace proof calibration.
  - signal: storytelling only
  - signal: portfolio polish only
  - signal: this shows my passion
- `findings_without_rebuild` — A findings-only rewrite does not satisfy the task.
  - signal: findings only
  - signal: just summarize

### Overclaim rules
- `no_external_validation_claim` — Do not imply external validation without external artifacts.
  - blocked terms: validated, proven in production, externally validated
  - evidence escape hatch: external, reviewer, benchmark, confidence artifact, [file:

### Legacy fail patterns
- hard fail: findings only
- hard fail: this case study shows my passion
- soft fail: storytelling only

## Accessibility Feedback Audit

- Task ID: `accessibility_feedback_audit`
- Task group: audit
- Allowed modes: AUDIT, PEER
- Allowed phases: accessibility, ui
- Required skills: accessibility-feedback-expert.md, ui-system-expert.md
- Data owner: accessibility-feedback-expert
- Risk tier: high
- SLA freshness: same release cycle as interaction pattern changes

### Why this contract exists
`accessibility_feedback_audit` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Access failure framing | 25 words | Name the blocked user action or assistive-tech failure. |
| Barrier inventory | 45 words | List concrete barriers, not generic usability discomfort. |
| Repair priorities | 45 words | Turn findings into an ordered fix plan. |
| Verification method | 25 words | Show how the fix will be verified. |

### Required decisions
- {'id': 'blocked_user_action', 'description': 'Names the blocked or degraded user action.', 'any_of': ['blocked', 'cannot', 'fails when', 'focus', 'keyboard', 'screen reader', 'announcement', 'trap', 'skip']}
- {'id': 'priority_order', 'description': 'Shows what should be fixed first.', 'any_of': ['first', 'then', 'priority', 'highest-risk', 'before', 'repair order']}
- {'id': 'behavior_rule', 'description': 'Names the behavior rule, not only the visual preference.', 'any_of': ['tab order', 'focus', 'aria', 'announcement', 'label', 'error state', 'keyboard', 'screen reader']}
- {'id': 'verification_step', 'description': 'Explains how to verify the repair.', 'any_of': ['verify', 'test', 'check', 'screen reader', 'keyboard only', 'inspect', 'axe', 'copy of state']}

### Required evidence classes
- {'class_id': 'standards_reference', 'description': 'Uses WCAG, APCA, ARIA, or accessibility semantics.'}
- {'class_id': 'state_or_behavior_rule', 'description': 'Uses focus, keyboard, or state behavior rules.'}
- {'class_id': 'verification_method', 'description': 'Names how the repair will be tested.'}

### Example coverage
- accessibility-feedback-pass

### Regression references
- pass-08 (smoke)
- fail-04 (fail-accessibility)

### Forbidden shortcuts
- `defer_accessibility` — Accessibility cannot be postponed until later.
  - signal: accessibility later
  - signal: screen reader later
  - signal: keyboard later
- `paint_only_fix` — Color-only fixes cannot stand in for semantic repair.
  - signal: just make focus blue
  - signal: increase contrast only
  - signal: change the color and it is fixed

### Overclaim rules
- `no_claimed_compliance` — Do not claim compliance without a standard or test receipt.
  - blocked terms: wcag compliant, accessible, fully accessible, validated
  - evidence escape hatch: wcag, apca, test, verify, screen reader, benchmark, [file:

### Legacy fail patterns
- hard fail: accessibility later
- hard fail: screen reader later
- hard fail: just make focus blue
- soft fail: probably accessible
- soft fail: seems fine

## Color System Specification

- Task ID: `color_system_spec`
- Task group: spec
- Allowed modes: REBUILD, PEER
- Allowed phases: tokens, ui
- Required skills: color-system-expert.md, accessibility-feedback-expert.md
- Data owner: color-system-expert
- Risk tier: medium
- SLA freshness: same release cycle as theme or semantic-role changes

### Why this contract exists
`color_system_spec` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Role model | 25 words | Defines semantic color roles instead of a loose palette. |
| Token map | 40 words | Maps roles to tokens, aliases, or state usage. |
| Contrast and state rules | 35 words | Prevents color-only semantics and contrast drift. |
| Migration notes | 25 words | Shows how to move from the current palette safely. |

### Required decisions
- {'id': 'semantic_roles', 'description': 'Defines role ownership such as surface, text, status, action, or chart roles.', 'any_of': ['role', 'surface', 'text', 'action', 'status', 'chart', 'semantic', 'alias']}
- {'id': 'state_mapping', 'description': 'Maps roles to states or interaction use.', 'any_of': ['hover', 'focus', 'disabled', 'error', 'warning', 'success', 'selected', 'state']}
- {'id': 'contrast_boundary', 'description': 'Names contrast or non-color fallback requirements.', 'any_of': ['contrast', '4.5:1', 'apca', 'non-color', 'icon and label', 'pairing']}
- {'id': 'migration_strategy', 'description': 'Shows how existing colors migrate into the new role model.', 'any_of': ['migrate', 'alias', 'deprecate', 'replace', 'token map', 'phase out']}

### Required evidence classes
- {'class_id': 'implementation_constraint', 'description': 'Uses token, alias, or theme-boundary constraints.'}
- {'class_id': 'measurable_threshold', 'description': 'Uses contrast thresholds or measurable limits.'}
- {'class_id': 'comparison_artifact', 'description': 'Names a rejected palette-only alternative or previous state.'}

### Example coverage
- color-system-pass

### Regression references
- pass-09 (smoke)
- fail-05 (fail-color)

### Forbidden shortcuts
- `palette_without_roles` — A color list without semantic roles cannot pass.
  - signal: pick nicer colors
  - signal: palette only
  - signal: brand color everywhere
- `color_only_state` — Status meaning cannot rely on color alone.
  - signal: use red and green only
  - signal: the color itself explains it

### Overclaim rules
- `no_fake_accessibility` — Do not call the color system accessible without thresholds or fallback rules.
  - blocked terms: accessible palette, wcag compliant, validated color system
  - evidence escape hatch: 4.5:1, apca, contrast, non-color, test, [file:

### Legacy fail patterns
- hard fail: pick nicer colors
- hard fail: brand color everywhere
- hard fail: palette only
- soft fail: could feel fresher
- soft fail: more vibrant maybe

## Graphic Critique

- Task ID: `graphic_critique`
- Task group: audit
- Allowed modes: AUDIT, PEER
- Allowed phases: brand, communication
- Required skills: graphic-design-expert.md, type-system-expert.md
- Data owner: graphic-design-expert
- Risk tier: medium
- SLA freshness: same release cycle as campaign or editorial artifact changes

### Why this contract exists
`graphic_critique` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Communication goal | 20 words | Defines what the artifact needs to communicate first. |
| Composition failures | 45 words | Names focal, hierarchy, or distance-legibility failures. |
| Rebuild moves | 45 words | Turns critique into compositional action. |
| Distance and emphasis tradeoff | 20 words | Shows what should dominate and what can recede. |

### Required decisions
- {'id': 'focal_winner', 'description': 'Names what should dominate the first read.', 'any_of': ['focal', 'dominant', 'first read', 'headline wins', 'should lead', 'primary image']}
- {'id': 'distance_legibility', 'description': 'Names distance or scan-legibility implications.', 'any_of': ['distance', 'legibility', 'scan', 'thumbnail', 'poster distance', 'headline/body ratio']}
- {'id': 'composition_rule', 'description': 'Uses alignment, grouping, rhythm, or proportion language.', 'any_of': ['alignment', 'grouping', 'rhythm', 'composition', 'balance', 'scale', 'crop', 'proportion']}
- {'id': 'emphasis_tradeoff', 'description': 'Resolves what can recede so the focal message survives.', 'any_of': ['tradeoff', 'recede', 'demote', 'rather than', 'instead of', 'secondary']}

### Required evidence classes
- {'class_id': 'visual_structure_rule', 'description': 'Uses composition, focal, rhythm, or legibility rules.'}
- {'class_id': 'comparison_artifact', 'description': 'Names the rejected alternative or competing focal path.'}
- {'class_id': 'implementation_constraint', 'description': 'Uses size, crop, or production-boundary constraints.'}

### Example coverage
- graphic-critique-pass

### Regression references
- pass-10 (smoke)
- fail-06 (fail-graphic)

### Forbidden shortcuts
- `taste_only` — Taste commentary cannot replace communication diagnosis.
  - signal: looks cool
  - signal: make it pop
  - signal: be more bold
- `style_without_goal` — Style comments without a communication goal cannot pass.
  - signal: nicer font
  - signal: better colors only
  - signal: more modern style

### Overclaim rules
- `no_claimed_readability` — Do not claim readability gains without a legibility rule or testable reason.
  - blocked terms: readable now, fixed readability, validated hierarchy
  - evidence escape hatch: distance, scan, legibility, test, threshold, [file:

### Legacy fail patterns
- hard fail: make it pop
- hard fail: looks cool
- hard fail: be more bold
- soft fail: could be cleaner
- soft fail: feels off

## Layout Reconstruction Plan

- Task ID: `layout_reconstruction_plan`
- Task group: rebuild
- Allowed modes: REBUILD, PEER
- Allowed phases: implementation, structure
- Required skills: layout-reconstruction-expert.md, grid-system-expert.md
- Data owner: layout-reconstruction-expert
- Risk tier: high
- SLA freshness: same release cycle as source-artifact updates

### Why this contract exists
`layout_reconstruction_plan` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Source constraints | 25 words | Defines what must be preserved from the source artifact. |
| Reconstruction assumptions | 35 words | Makes inferred structure explicit instead of pretending certainty. |
| Rebuild sequence | 45 words | Shows the ordered reconstruction plan. |
| Verification checkpoints | 25 words | Protects against drift and silent geometry errors. |

### Required decisions
- {'id': 'preserved_elements', 'description': 'Names what geometry or content must remain stable.', 'any_of': ['preserve', 'must remain', 'source truth', 'locked', 'do not move', 'existing artifact']}
- {'id': 'inference_boundary', 'description': 'Labels inferred structure as assumption or proxy.', 'any_of': ['assumption', 'inference', 'estimated', 'proxy', 'likely grid', 'inferred']}
- {'id': 'reconstruction_order', 'description': 'Shows the ordered reconstruction sequence.', 'any_of': ['first', 'then', 'before', 'after', 'sequence', 'checkpoint']}
- {'id': 'verification_method', 'description': 'Names how the reconstruction will be checked.', 'any_of': ['verify', 'overlay', 'measurement', 'extract', 'compare', 'check']}
- {'id': 'visual_confidence_boundary', 'description': 'Names what is directly observed vs inferred when visual input is part of the task.', 'any_of': ['confidence', 'observed', 'inferred', 'unverified', 'appears', 'visible evidence']}

### Required evidence classes
- {'class_id': 'implementation_constraint', 'description': 'Uses geometry, grid, or preservation constraints.'}
- {'class_id': 'comparison_artifact', 'description': 'Compares the rebuilt artifact back to the source.'}
- {'class_id': 'verification_method', 'description': 'Uses overlays, measurements, or extraction checks.'}
- {'class_id': 'visual_structure_rule', 'description': 'Uses a visual-structure rule when the critique is grounded in screenshots or visible layout evidence.'}

### Example coverage
- layout-reconstruction-pass

### Regression references
- pass-11 (compound)
- fail-07 (fail-layout)
- fail-24 (fail-visual-boundary)

### Forbidden shortcuts
- `redraw_without_boundary` — Redrawing from scratch ignores the reconstruction brief.
  - signal: redraw it from scratch
  - signal: reimagine the layout
  - signal: just clean it up
- `eyeballed_geometry` — Eyeballed spacing cannot stand in for structure.
  - signal: eyeball the spacing
  - signal: approximate it
  - signal: close enough

### Overclaim rules
- `no_exactness_without_receipt` — Do not claim exact preservation without measured comparison or explicit inference labeling.
  - blocked terms: exact match, identical, mathematically identical
  - evidence escape hatch: overlay, measurement, compare, estimate, inference, [file:

### Legacy fail patterns
- hard fail: redraw it from scratch
- hard fail: eyeball the spacing
- hard fail: just clean it up
- soft fail: approximate it
- soft fail: close enough

## Type System Recommendation

- Task ID: `type_system_recommendation`
- Task group: spec
- Allowed modes: REBUILD, PEER
- Allowed phases: tokens, communication, ui
- Required skills: type-system-expert.md, accessibility-feedback-expert.md
- Data owner: type-system-expert
- Risk tier: medium
- SLA freshness: same release cycle as type scale or readability rules

### Why this contract exists
`type_system_recommendation` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Reading context | 20 words | Defines where the type system will be read and at what density. |
| Scale and role map | 40 words | Maps text roles to scale, weight, and hierarchy rules. |
| Readability rules | 35 words | Names line length, contrast, spacing, or emphasis boundaries. |
| Adoption guidance | 25 words | Shows how to phase the new type system into the artifact. |

### Required decisions
- {'id': 'reading_context', 'description': 'Defines the reading context and density constraint.', 'any_of': ['reading context', 'dense table', 'long-form', 'mobile', 'dashboard', 'distance', 'scan']}
- {'id': 'role_hierarchy', 'description': 'Maps roles such as display, heading, body, label, or meta text.', 'any_of': ['display', 'heading', 'body', 'label', 'meta', 'role map', 'hierarchy']}
- {'id': 'readability_boundary', 'description': 'Uses a readability rule or threshold.', 'any_of': ['line length', 'line-height', 'contrast', 'tracking', 'readability', '16px', '45-75', 'chars']}
- {'id': 'adoption_sequence', 'description': 'Shows what changes first and what stays stable.', 'any_of': ['phase', 'adopt', 'migrate', 'first', 'then', 'keep existing']}

### Required evidence classes
- {'class_id': 'visual_structure_rule', 'description': 'Uses legibility, hierarchy, or reading-flow rules.'}
- {'class_id': 'measurable_threshold', 'description': 'Uses measurable type or readability thresholds.'}
- {'class_id': 'implementation_constraint', 'description': 'Uses token, density, or platform-boundary constraints.'}

### Example coverage
- type-system-pass

### Regression references
- pass-12 (smoke)
- fail-08 (fail-specificity)

### Forbidden shortcuts
- `font_swap_only` — A font swap is not a type system.
  - signal: pick a nicer font
  - signal: just tighten tracking
  - signal: use inter at 12px
- `taste_only_type` — Taste language cannot replace readability rules.
  - signal: more elegant font
  - signal: sharper type only

### Overclaim rules
- `no_fake_readability_proof` — Do not claim readability is solved without measurable rules or context.
  - blocked terms: readability fixed, perfectly readable, validated type scale
  - evidence escape hatch: line length, threshold, contrast, density, test, [file:

### Legacy fail patterns
- hard fail: use inter at 12px
- hard fail: just tighten tracking
- hard fail: pick a nicer font
- soft fail: feels too loose
- soft fail: could be sharper

## UX Research Gap Map

- Task ID: `ux_research_gap_map`
- Task group: strategy
- Allowed modes: PEER, AUDIT
- Allowed phases: research, strategy
- Required skills: ux-research-expert.md, content-and-case-study-expert.md
- Data owner: ux-research-expert
- Risk tier: medium
- SLA freshness: same release cycle as the product scope or audience assumptions

### Why this contract exists
`ux_research_gap_map` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Known evidence | 25 words | Separates what is already known from assumption. |
| Critical gaps | 45 words | Names the highest-risk unknowns that block good decisions. |
| Research plan | 45 words | Maps each gap to a method, sample, and output. |
| Decision impact | 25 words | Shows what product or narrative decision each study unlocks. |

### Required decisions
- {'id': 'known_vs_unknown', 'description': 'Separates known evidence from assumption.', 'any_of': ['known', 'unknown', 'assumption', 'evidence already', 'not yet known', 'gap']}
- {'id': 'gap_priority', 'description': 'Ranks which research gaps matter first.', 'any_of': ['highest-risk', 'priority', 'first', 'before launch', 'critical gap', 'blocker']}
- {'id': 'method_mapping', 'description': 'Maps gaps to concrete research methods.', 'any_of': ['interview', 'survey', 'usability test', 'diary', 'field study', 'method', 'sample']}
- {'id': 'decision_linkage', 'description': 'Connects the study back to a product or communication decision.', 'any_of': ['this unlocks', 'decision', 'changes whether', 'affects', 'if true then']}

### Required evidence classes
- {'class_id': 'research_artifact', 'description': 'Uses research methods, participants, or artifacts.'}
- {'class_id': 'comparison_artifact', 'description': 'Compares current evidence to missing evidence or alternative methods.'}
- {'class_id': 'narrative_proof_boundary', 'description': 'Distinguishes assumption, proxy evidence, and measured proof.'}

### Example coverage
- ux-research-pass

### Regression references
- pass-13 (smoke)
- fail-09 (fail-research)

### Forbidden shortcuts
- `generic_research_advice` — Generic 'do interviews' advice cannot pass.
  - signal: just do some interviews
  - signal: talk to users
  - signal: research later
- `no_gap_priority` — Unranked wish lists are not research plans.
  - signal: collect more data
  - signal: do more research

### Overclaim rules
- `no_fake_user_evidence` — Do not imply user evidence that has not been collected.
  - blocked terms: users proved, research proved, validated by users
  - evidence escape hatch: interview, survey, usability test, artifact, [file:

### Legacy fail patterns
- hard fail: just do some interviews
- hard fail: research later
- hard fail: talk to users
- soft fail: probably enough
- soft fail: might learn something

## Front-End Implementation Review

- Task ID: `frontend_implementation_review`
- Task group: implementation
- Allowed modes: AUDIT, PEER, STRUCTURE
- Allowed phases: implementation, ui, specs
- Required skills: front-end-architecture-expert.md, front-end-handoff-expert.md, accessibility-feedback-expert.md
- Data owner: front-end-architecture-expert
- Risk tier: high
- SLA freshness: same release cycle as rendering, state, or interaction architecture changes

### Why this contract exists
`frontend_implementation_review` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Architectural framing | 25 words | Name the real front-end architectural problem and its user-facing consequence. |
| Boundary and state model | 45 words | Make server/client and state ownership explicit. |
| Rendering and mutation strategy | 45 words | Choose rendering, fetching, and mutation handling instead of generic implementation advice. |
| Risks and safer path | 30 words | Expose the cost surface and safer implementation order. |

### Required decisions
- {'id': 'rendering_model', 'description': 'Chooses the rendering strategy instead of implying it.', 'any_of': ['static', 'dynamic', 'ppr', 'csr', 'server component', 'client component', 'suspense', 'streaming']}
- {'id': 'state_ownership', 'description': 'Names where state lives and how transitions are handled.', 'any_of': ['local state', 'server-state', 'shared state', 'state machine', 'status union', 'useactionstate', 'useformstatus', 'useoptimistic']}
- {'id': 'boundary_placement', 'description': 'Makes the server/client boundary or mutation boundary explicit.', 'any_of': ['use client', 'server action', 'boundary', 'hydrate', 'hydration', 'server component', 'client component']}
- {'id': 'semantic_contract', 'description': 'Names the semantic or native-element contract.', 'any_of': ['native', 'button', 'form', 'dialog', 'table', 'grid', 'role is a promise', 'semantic']}
- {'id': 'cost_or_degraded_path', 'description': 'Names the cost surface or degraded path.', 'any_of': ['bundle', 'hydration', 'fallback', 'degraded', 'retry', 'lazy', 'performance cost', 'rollback']}

### Required evidence classes
- {'class_id': 'rendering_boundary_rule', 'description': 'Uses rendering or boundary-specific evidence.'}
- {'class_id': 'state_or_behavior_rule', 'description': 'Uses explicit state or interaction behavior rules.'}
- {'class_id': 'implementation_constraint', 'description': 'Uses real implementation constraints rather than generic framework advice.'}
- {'class_id': 'standards_reference', 'description': 'Uses semantic or accessibility standards when behavior depends on them.'}

### Example coverage
- adaptive-explanation-tiered-response
- frontend-implementation-review

### Regression references
- pass-14 (smoke)
- fail-10 (fail-frontend-architecture)
- pass-17 (comprehension)
- fail-17 (tier-boundary)
- fail-22 (filter-bloat)

### Forbidden shortcuts
- `framework_swap_only` — A framework swap cannot stand in for an architectural decision.
  - signal: just convert it to react
  - signal: rewrite in next
  - signal: move it into components
- `hook_sprawl` — More hooks is not an architectural answer.
  - signal: use more hooks
  - signal: add a useeffect
  - signal: componentize it later

### Overclaim rules
- `no_production_ready_without_costs` — Do not call the implementation production-ready without boundary, state, and cost logic.
  - blocked terms: production-ready, scalable, performant
  - evidence escape hatch: hydration, bundle, boundary, state machine, rollback, benchmark, test

### Legacy fail patterns
- hard fail: just convert it to react
- hard fail: componentize it later
- hard fail: use more hooks
- soft fail: should be simple
- soft fail: probably fine

## Back-End Architecture Spec

- Task ID: `backend_architecture_spec`
- Task group: spec
- Allowed modes: STRUCTURE, PEER, REBUILD
- Allowed phases: strategy, specs, implementation
- Required skills: back-end-systems-architect.md, back-end-aware-planner.md, api-reliability-security-expert.md
- Data owner: back-end-systems-architect
- Risk tier: high
- SLA freshness: same release cycle as authority, consistency, or delivery-model changes

### Why this contract exists
`backend_architecture_spec` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| System framing | 25 words | Names the system, actors, resources, and why architecture is needed. |
| Core model and authority boundaries | 45 words | Defines ownership, authorization, and source-of-truth. |
| Data, consistency, and delivery design | 50 words | Chooses consistency, pagination, events, async, or webhook patterns. |
| Observability and failure posture | 30 words | Shows how the system will be monitored and where it can safely degrade. |

### Required decisions
- {'id': 'actor_resource_action', 'description': 'Names actors, resources, and actions.', 'any_of': ['actor', 'resource', 'action', 'owner', 'viewer', 'editor', 'admin', 'relationship']}
- {'id': 'source_of_truth', 'description': 'Names the source-of-truth or ownership model.', 'any_of': ['source-of-truth', 'canonical', 'ownership', 'writer', 'record owner', 'authority']}
- {'id': 'authorization_model', 'description': 'Names the authorization posture.', 'any_of': ['rbac', 'abac', 'rebac', 'object-level', 'property-level', 'tenant', 'membership', 'permission']}
- {'id': 'consistency_stance', 'description': 'Names the freshness or consistency model.', 'any_of': ['linearizable', 'bounded staleness', 'read-your-writes', 'revision token', 'consistency token', 'stale', 'freshness']}
- {'id': 'delivery_pattern', 'description': 'Names pagination, async, event, or webhook design.', 'any_of': ['cursor', 'keyset', 'offset', 'webhook', 'outbox', 'queue', 'async', 'micro-batch', 'event']}
- {'id': 'observability_tax', 'description': 'Names metrics, tracing, or operational tax.', 'any_of': ['trace', 'trace_id', 'metrics', 'logs', 'queue lag', 'saturation', 'tax', 'operational']}

### Required evidence classes
- {'class_id': 'data_model_dependency', 'description': 'Uses data-model or ownership evidence.'}
- {'class_id': 'permission_rule', 'description': 'Uses authorization or policy evidence.'}
- {'class_id': 'consistency_model', 'description': 'Uses explicit consistency or delivery-model evidence.'}
- {'class_id': 'implementation_constraint', 'description': 'Names operational or scalability constraints.'}

### Example coverage
- backend-architecture-spec
- designer-response-filter-pass

### Regression references
- pass-15 (smoke)
- fail-11 (fail-backend-architecture)
- pass-18 (comprehension)
- fail-18 (tier-boundary)
- fail-19 (actionability)

### Forbidden shortcuts
- `endpoint_theater` — Endpoint count is not architecture.
  - signal: just add an endpoint
  - signal: just add a table
  - signal: just add redis
- `security_by_identifier` — Identifiers do not replace authorization.
  - signal: use uuid and it is secure
  - signal: security by obscurity
  - signal: unguessable ids solve it

### Overclaim rules
- `no_scalability_without_tax` — Do not call the system scalable or enterprise-ready without naming the architecture tax and authority model.
  - blocked terms: scalable, enterprise-ready, globally distributed
  - evidence escape hatch: tenant, outbox, cursor, trace, consistency, rebac, observability

### Legacy fail patterns
- hard fail: just add an endpoint
- hard fail: make it realtime
- hard fail: use uuid and it is secure
- soft fail: should scale fine
- soft fail: probably okay

## API Reliability and Security Review

- Task ID: `api_reliability_security_review`
- Task group: audit
- Allowed modes: AUDIT, PEER, STRUCTURE
- Allowed phases: implementation, specs, strategy
- Required skills: api-reliability-security-expert.md, back-end-systems-architect.md, back-end-aware-planner.md
- Data owner: api-reliability-security-expert
- Risk tier: high
- SLA freshness: same release cycle as API contract, auth, or background-job changes

### Why this contract exists
`api_reliability_security_review` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Failure semantics | 30 words | Defines the error envelope and what the client can reason about. |
| Authorization and resource protection | 45 words | Names BOLA/BFLA style boundaries and resource controls. |
| Idempotency and async lifecycle | 45 words | Makes retry safety and long-running job behavior explicit. |
| Resilience and observability | 35 words | Names resilience, quotas, degradation, and telemetry posture. |

### Required decisions
- {'id': 'problem_details_contract', 'description': 'Names RFC 9457 style failure semantics.', 'any_of': ['rfc 9457', 'problem details', 'application/problem+json', 'type', 'title', 'status', 'detail', 'instance']}
- {'id': 'authorization_perimeter', 'description': 'Names the authorization boundary and relevant API risk.', 'any_of': ['bola', 'bfla', 'bopla', 'object-level', 'function-level', 'property-level', 'deny by default', 'tenant']}
- {'id': 'idempotency_contract', 'description': 'Names idempotency-key behavior.', 'any_of': ['idempotency-key', 'fingerprint', '409 conflict', '422 unprocessable', '400 bad request', 'ttl', 'client-generated']}
- {'id': 'async_job_model', 'description': 'Names the async job lifecycle when work is long-running.', 'any_of': ['202 accepted', 'status url', 'queued', 'running', 'terminal success', 'terminal failure', 'webhook']}
- {'id': 'resilience_strategy', 'description': 'Names resilience or protection rules.', 'any_of': ['circuit breaker', 'backoff', 'jitter', 'load shedding', 'graceful degradation', 'quota', 'trace_id', 'observability']}

### Required evidence classes
- {'class_id': 'failure_semantics_rule', 'description': 'Uses structured failure-semantic evidence.'}
- {'class_id': 'permission_rule', 'description': 'Uses authorization or access-control evidence.'}
- {'class_id': 'async_lifecycle_rule', 'description': 'Uses idempotency or async lifecycle evidence.'}
- {'class_id': 'resilience_rule', 'description': 'Uses resilience, quota, or observability evidence.'}

### Example coverage
- api-reliability-security-review

### Regression references
- pass-16 (smoke)
- fail-12 (fail-api-reliability)

### Forbidden shortcuts
- `retry_theater` — Retries without idempotency are not safe.
  - signal: just retry it
  - signal: retry until it works
  - signal: rate limit later
- `success_envelope_failure` — Failure cannot hide inside a success envelope.
  - signal: return 200 with an error field
  - signal: always 200
  - signal: uuid makes it secure

### Overclaim rules
- `no_security_or_reliability_theater` — Do not call the API secure or reliable without explicit contracts.
  - blocked terms: secure, reliable, production-ready, compliant
  - evidence escape hatch: rfc 9457, object-level, idempotency-key, 202 accepted, trace_id, quota, test, verify

### Legacy fail patterns
- hard fail: just retry it
- hard fail: rate limit later
- hard fail: return 200 with an error field
- hard fail: uuid makes it secure
- soft fail: should be reliable
- soft fail: probably secure

## Text Humanization Revision

- Task ID: `text_humanization_revision`
- Task group: writing-quality
- Allowed modes: REBUILD, PEER, STRUCTURE
- Allowed phases: communication, case-study, implementation
- Required skills: text-humanization-expert.md, content-and-case-study-expert.md
- Data owner: text-humanization-expert
- Risk tier: medium
- SLA freshness: same session as source revision requests

### Why this contract exists
`text_humanization_revision` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.

### Required sections
| Section | Minimum substance | Why it exists |
|---|---:|---|
| Job of the piece | 18 words | Identifies what the text must still do after revision. |
| Pattern scan | 22 words | Shows what felt machine-shaped or repetitive. |
| Meaning-preservation guard | 22 words | Protects against semantic drift or tone replacement. |
| Revised passage | 35 words | Shows the rewritten prose. |
| Why this reads more human | 22 words | Explains the revision logic instead of asserting it. |

### Required decisions
- {'id': 'job_of_piece', 'description': 'Names what the text is trying to do.', 'any_of': ['job of the piece', 'the text is trying to', 'must still do', 'purpose']}
- {'id': 'pattern_scan', 'description': 'Names repeated or machine-shaped patterns.', 'any_of': ['pattern', 'repeated', 'formulaic', 'nominalization', 'transition load', 'flat rhythm']}
- {'id': 'meaning_guard', 'description': 'Names what must remain stable.', 'any_of': ['meaning-preservation', 'meaning guard', 'claims preserved', 'argument preserved', 'drift risk']}
- {'id': 'revision_sequence', 'description': 'Makes revision logic visible.', 'any_of': ['repair', 'rebalance', 'prune', 'revise', 'realism pass', 'voice']}
- {'id': 'voice_guard', 'description': "Protects the writer's tone from generic polish.", 'any_of': ['voice', 'tone', 'kept', 'not replaced', 'authored texture']}

### Required evidence classes
- {'class_id': 'meaning_preservation_guard', 'description': 'Uses explicit meaning-preservation language.'}
- {'class_id': 'prose_quality_signal', 'description': 'Uses concrete prose-quality evidence like repetition, rhythm, or verb logic.'}
- {'class_id': 'comparison_artifact', 'description': 'Uses before/after or explicit revision comparison logic.'}

### Example coverage
- text-humanization-pass

### Regression references
- pass-19 (comprehension)
- fail-20 (humanization)
- fail-21 (humanization)

### Forbidden shortcuts
- `difference_only` — The rewrite cannot exist only to look different.
  - signal: rewrite for difference only
  - signal: just change the wording
  - signal: make it sound human somehow
- `casualize_default` — Casualization cannot stand in for humanization.
  - signal: casualize it more
  - signal: make it more casual by default

### Overclaim rules
- `no_humanized_claim_without_guard` — Do not claim the revision is more human without naming meaning guard and revision logic.
  - blocked terms: humanized, more human, natural now
  - evidence escape hatch: meaning-preservation, pattern, voice, drift risk, revised passage

### Legacy fail patterns
- hard fail: rewrite for difference only
- hard fail: casualize it more
- hard fail: make it sound human somehow
- soft fail: a bit more natural
- soft fail: less robotic
