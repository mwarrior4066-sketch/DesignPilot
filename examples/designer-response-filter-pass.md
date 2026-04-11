# Designer Response Filter Example
Fixture: tests/fixtures/designer-response-filter-pass.prompt.md
Validation result: tests/evals/designer-response-filter-pass.eval.json

## Input Prompt
Take this backend architecture advice and transform it into a designer-readable answer for an Integrative-tier user without removing the hard constraints.

## Selected Route and Loaded Skills
- Route: `rt_backend_systems_architecture`
- Task contract: `backend_architecture_spec`
- Mode: PEER
- Phase: implementation
- Skills: `back-end-systems-architect.md`, `back-end-aware-planner.md`
- Response layer: `DESIGNER_RESPONSE_FILTER_PROTOCOL.md`
- Active tier: Integrative

## Final Output
### System framing
The dashboard can look simple on the surface, but the system under it cannot be treated like a flat CRUD app. Access, freshness, and export behavior have to be designed as system rules because the interface is promising actions across actors, resources, and permissions, not just showing a table.

### Core model and authority boundaries
Start with an actor, resource, and action model: who can view, edit, export, or share which resource, under what relationship. The source-of-truth boundary also has to be explicit. If the dashboard shows derived views, alerts, and exports, the pack should still name which record is canonical and which surfaces are projections. Roles alone are not enough here because object-level permission and tenant membership still govern the real authority boundary.

### Data, consistency, and delivery design
For a designer, the consequence is that a “live” table or a share flow silently requires a consistency stance. Some views may need read-your-writes or bounded staleness, while others can tolerate a slower update path. Delivery patterns also matter: cursor pagination is safer than pretending page numbers will stay stable, and any webhook or export path should be treated as an async event or outbox-backed flow instead of a hand-waved background task. That delivery choice also changes what the UI can honestly promise about timing, retries, and completion states.

### Observability and failure posture
The system also needs an operational tax note. If you add live updates, sharing, and export behavior, you inherit trace_id propagation, queue lag monitoring, logs, and metrics for failed delivery or stale views. The filter keeps those constraints visible, but it translates them into design consequences: do not finalize live-update or export UI until the authority model, consistency posture, and operational visibility are named.

### Translation note
The filter preserved the authority, consistency, and delivery burden, but it shifted them into designer-facing consequences and sequencing.

### Actionable next steps
1. Write the actor, resource, and action matrix.
2. Decide which dashboard states need stronger freshness and which can tolerate bounded staleness.
3. Only then finalize sharing, export, and live-update UI behaviors.

## Why This Passed
- It translates backend architecture into designer-facing consequences instead of dumbing it down.
- It keeps the authority, consistency, delivery, and observability constraints visible.
- It ends with an ordered next-step path appropriate for an Integrative explanation tier.

## What Would Have Failed
- Replacing the system constraints with generic “talk to engineering” advice.
- Removing source-of-truth and consistency language to make the answer feel easier.
- Ending without a usable next move.

## Revision Pass
The weak draft was technically correct but read like a backend memo. The corrected version preserved the hard constraints and rewrote them as design-facing consequences, sequencing, and operational dependencies.
