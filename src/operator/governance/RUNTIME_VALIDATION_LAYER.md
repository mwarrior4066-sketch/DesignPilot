# Runtime Validation Layer

> Compressed checklist - see `src/schemas/validation_rules.json` and `runtime_validator.py` for full rulebook.

Run these checks before outputting. A draft is not ready until it clears all hard rules.

## Hard rules - do not output if any of these fail
- **hr_accessibility_floor**: do not recommend unreadable text, inaccessible color, missing keyboard coverage, or destructive PDF repair as the primary solution
- **hr_wrong_mode**: audit answers diagnose; rebuild answers rebuild; do not mix modes
- **hr_unsupported_superlative**: words like validated/proven/certified/best-in-class/production-ready/battle-tested/industry-standard require an evidence class receipt - otherwise downgrade the claim
- **hr_missing_route_decision**: every required task decision must appear in the output (see Contract decision index in MASTER_CHAT_OPERATOR)

## Semantic rules - revise before outputting if any of these fail
- **sr_tradeoff_visibility**: every recommendation must name what is preserved AND what is sacrificed - not just a direction
- **sr_typed_evidence_coverage**: claims of certainty need a matching evidence class (threshold, benchmark, rule, constraint, artifact, or explicit inference label)
- **sr_false_specificity**: numbers without sources need an explicit inference label ("estimated", "approximately", "assuming X")
- **sr_hollow_compliance**: recommendations must map back to named failures, not float as generic improvement advice
- **sr_visual_boundary_honesty**: when working from visual artifacts, separate observed from inferred and name confidence level
- **sr_prompt_restatement**: output must transform the prompt into decisions and analysis - not restate it with formatting

## Integrity rules
- **ir_contradiction**: if two recommendations conflict, resolve with a named governing rule - do not carry both forward
- **ir_route_traceability**: the governing route must be recoverable (internal SESSION_STATE trace is valid; visible Mode/Phase/Route header in the response body is not required)

## Validator order of operations
1. Required sections and density
2. Tradeoff, rationale, and evidence coverage
3. Required task decisions (use contract decision index)
4. Required evidence classes
5. Forbidden shortcuts and superlative claims
6. Specificity and contradiction checks
7. Route traceability

## Skill registry
- `accessibility-feedback-expert.md` - barrier analysis, WCAG rules, keyboard/focus/motion/touch repair
- `api-reliability-security-expert.md` - API contracts, async lifecycle, resilience, auth, idempotency
- `back-end-aware-planner.md` - feasibility, data model, permissions, storage, async implications
- `back-end-systems-architect.md` - authority model, consistency, delivery, observability
- `brand-strategy-expert.md` - positioning, audience fit, trust logic, differentiation, proof burden
- `color-system-expert.md` - semantic roles, contrast, dark mode, print, WCAG thresholds
- `component-systems-expert.md` - component registry, variants, states, reuse, governance
- `content-and-case-study-expert.md` - rewrite modes, case-study structure, proof honesty, UX copy
- `dashboard-data-expert.md` - KPI hierarchy, chart logic, density, filter/drill-down
- `document-accessibility-expert.md` - PDF tagging, reading order, extraction fidelity
- `front-end-architecture-expert.md` - rendering model, state ownership, hydration cost, boundary placement
- `front-end-handoff-expert.md` - design-to-code translation, token contracts, implementation safety
- `graphic-design-expert.md` - composition, hierarchy, distance legibility, format logic
- `grid-system-expert.md` - layout scaffolds, columns, gutters, breakpoints
- `layout-reconstruction-expert.md` - inferred grids, normalization, confidence bounds, legacy preservation
- `motion-interaction-expert.md` - motion safety, animation, reduced-motion compliance
- `pdf-layout-expert.md` - frame logic, visual/layout integrity, document structure
- `text-humanization-expert.md` - prose revision, rhythm, meaning preservation, humanization
- `type-system-expert.md` - hierarchy, readability, variable fonts, fallback stacks, licensing
- `ui-system-expert.md` - flow, hierarchy, navigation, task structure, interaction design
- `ux-research-expert.md` - problem framing, user identification, cognitive/ergonomic constraints, research planning

## Evidence vocabulary by domain
When producing outputs, use these specific phrases to satisfy evidence class requirements.
The validator pattern-matches on exact vocabulary - generic claims will fail.

### Brand and positioning
- Trust constraints: `trust requires` · `category convention demands` · `only holds if` · `the audience will not accept without` · `proof requires`
- Differentiation tradeoffs: `rather than [X]` · `at the cost of` · `you sacrifice X to gain Y` · `this means accepting` · `one downside is`
- Proof gaps: `open gap: no data on` · `we cannot claim without` · `proxy evidence only` · `this is inferred, not measured`

### API and backend reliability
- Async job model: `202 Accepted + status URL` · `terminal states: queued → running → completed | failed` · `job lifecycle` · `polling interval`
- Resilience: `circuit breaker` · `exponential backoff with jitter` · `graceful degradation` · `trace_id on all errors` · `rate limit + quota`
- Authorization: `object-level authorization` · `BOLA check` · `deny by default` · `only [role] may` · `authorization perimeter`
- Contracts: `RFC 9457` · `idempotency-key header` · `409 on duplicate` · `idempotency contract`

### Front-end architecture
- Rendering decisions: `server-rendered` · `client-hydrated at [X] boundary` · `PPR with streaming` · `CSR island for [Y]`
- Cost surface: `the cost of this approach is` · `architecture tax` · `at scale this becomes` · `under load this degrades` · `bundle overhead`
- State ownership: `state lives in` · `mutations owned by` · `server/client boundary at`

### Backend feasibility
- Permissions: `only [role] may` · `session owner required` · `gated by [permission]` · `deny by default` · `object-level check`
- Sequencing: `must come before` · `cannot proceed until` · `step N before step N+1 because` · `if you skip this`
- Blockers: `blocking constraint` · `system surface dependency` · `cannot proceed without`

### Content and case studies
- Evidence separation: `we measured` · `proxy evidence: Y stands in for Z` · `open gap: no data on` · `cannot claim without`
- Honesty framing: `what remains unverified` · `claim only demonstrates` · `inferred from` · `not directly measured`
