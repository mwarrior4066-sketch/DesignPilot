# Lightweight Response Protocol

The full routed stack is not required for every small ask.
This protocol decides when a lighter execution path is safer and faster.

## Task weights
- `lightweight`
- `standard`
- `compound`

## Lightweight criteria
Use `lightweight` only when all are true:
- the ask is bounded and narrow
- the answer does not require deep cross-domain coordination
- proof sensitivity is low to medium
- no architecture, remediation, or project-state update is required

Typical lightweight asks:
- short rewrites
- one focused critique callout
- a compact comparison
- a quick recommendation with one clear tradeoff

## Lightweight execution
May skip:
- full designer response filter
- text humanization pass unless the ask is itself humanization
- long visible trace
- full silent critic loop repetition

Must still keep:
- correct route choice
- honest claim boundaries
- accessibility and semantic floors
- at least one real rationale or evidence cue when the task needs it

## Compound criteria
Use `compound` when any are true:
- architecture or API behavior is central
- PDF or document semantics are at risk
- multiple constraints compete and must be ranked
- proof language or validation credibility is central
- the answer changes release readiness or project operating state
