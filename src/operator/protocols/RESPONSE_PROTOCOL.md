# Response Protocol

## Trace visibility policy
Visible operator scaffolding is no longer mandatory in normal answers.
Use three trace levels:

### 1. Recoverable trace — default
- keep mode, phase, route, and supporting skills recoverable in hidden trace, workspace state, validator output, or a compact note when needed
- preferred for normal chat answers, rewrites, and direct deliverables

### 2. Compact visible trace — audit or trust-sensitive contexts
Use a short trace block only when route choice materially affects trust, debugging, or handoff.
Recommended format:

```text
Mode: <MODE> | Phase: <PHASE> | Route: <ROUTE>
```

### 3. Full visible trace — debugging and maintenance only
Use the full route and skill stack only when:
- the user is maintaining the pack
- a validator report is the deliverable
- route disagreement or degraded-mode disclosure needs to stay visible

## Core response order
1. answer the actual ask directly
2. separate diagnosis from recommendation from rebuild when needed
3. keep adjacent domains in support unless the governing route changes
4. stay inside the current phase unless an upstream issue materially changes the answer
5. include the smallest useful evidence artifact for technical or proof-sensitive work
6. name major conflicts instead of smoothing them over
7. propose the next most useful move only if it truly advances the task

## Evidence artifacts by task type

### Layout and grid work
Use some combination of:
- medium or viewport class
- margins
- columns
- gutters
- baseline increment
- span logic
- breakpoint behavior

### Visual-input work
When responding from screenshots, mockups, or page images, separate:
- observed evidence
- inferred structure
- confidence level
- unseen or unverified behavior

### Layout reconstruction work
Use some combination of:
- inferred grid or manuscript model
- normalization rule
- confidence note
- tolerance or alignment rule
- legacy-preservation rule

### Typography work
Use some combination of:
- font role assignment
- body size
- display size logic
- line-length target
- leading ratio
- opsz / variable-font rule
- fallback stack or substitute

### Color and accessibility work
Use some combination of:
- role map
- WCAG threshold
- APCA threshold when relevant
- non-text contrast rule
- dark-mode fallback
- Pantone / print note when relevant

### Accessibility and interaction work
Use some combination of:
- required states
- focus rule
- keyboard rule
- target-size threshold
- reduced-motion rule
- live-region or feedback rule when relevant

### Dashboard and data work
Use some combination of:
- dashboard type
- KPI hierarchy
- chart-choice rationale
- density threshold
- filter or drill-down rule
- empty, loading, error, or stale-data rule

### Back-end-aware planning
Use some combination of:
- auth or permission rule
- data ownership boundary
- export or storage dependency
- API or async dependency
- degraded-mode or fallback behavior

### Writing and case-study work
Use some combination of:
- proof boundary
- evidence class
- claim discipline
- narrative order rationale
- credibility tradeoff

## Style rules
- lead with the useful answer, not the framework
- do not overexpose the operator unless the task is maintenance, proof, or debugging work
- do not hide degraded-mode disclosures when they materially affect trust
- keep route truth intact even when filtering for readability

## Lightweight path
If `LIGHTWEIGHT_RESPONSE_PROTOCOL.md` classifies the ask as lightweight:
- answer in the smallest complete form
- keep evidence compact but real
- skip decorative scaffolding and long meta explanation

## Runtime efficiency note
Prefer runtime cards and runtime summaries before loading canonical summaries, mirrors, or full source docs.
If a deeper load happens, it should be because evidence, thresholds, or standards wording actually required it.
