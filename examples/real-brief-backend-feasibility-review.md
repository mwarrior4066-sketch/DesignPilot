# Real Brief Back-End Feasibility Review Example
Fixture: tests/fixtures/real-brief-backend-feasibility-review.prompt.md
Validation result: tests/evals/real-brief-backend-feasibility-review.eval.json

## Input Prompt
A solo product designer is building a client portal for a small brand studio. The first UI pass includes project dashboards, file approvals, invoice status, client comments, and a live activity feed.

The designer wants to know whether this can stay as a polished front-end prototype with lightweight storage, or whether the project needs real back-end planning before the UI is finalized.

Review the back-end feasibility, hidden system dependencies, safer implementation order, and what should be removed from the first release if the goal is a credible portfolio case study rather than a fake production app.

## Selected Route and Loaded Skills
- Route: `rt_backend_feasibility`
- Task contract: `backend_feasibility_review`
- Mode: PEER
- Phase: strategy
- Skills: `back-end-aware-planner.md`, `front-end-handoff-expert.md`

## Final Output
### Requested capability
The surface request is a client portal UI, but the real system is a permissioned workspace with files, approvals, billing visibility, comments, and event history. That is not a lightweight visual layer. It requires ownership rules, storage policy, activity capture, invoice data boundaries, and approval-state behavior before the interface can be honest.

The most important decision is to separate portfolio prototype claims from production claims. A clickable prototype can show the desired experience. A production-like case study must explain the back-end model that would make the experience safe.

### Hidden back-end work
1. Project dashboards need a project, client, member, and permission model.
2. File approvals need upload limits, virus scanning assumptions, file versioning, approval state, and audit history.
3. Invoice status needs either a billing integration or a clearly marked mocked data boundary.
4. Client comments need identity, edit/delete rules, timestamps, and notification behavior.
5. Live activity needs an event model, retention rules, and either polling, server-sent events, or a realtime provider.
6. Every shared object needs object-level authorization, not only a logged-in user check.
7. The project also needs a traceable way to explain what is real, what is simulated, and what remains outside scope.

### Feasibility assessment
The project is feasible as a portfolio piece if the first release is framed as a system design prototype, not a fake shipped SaaS app. The safe version demonstrates the workflow, the state model, and the implementation constraints without pretending to have production billing, secure file infrastructure, or realtime operations fully built.

The obvious alternative is to design the full portal UI first and write the back-end story later. That is faster visually, but it creates weak case-study logic because every screen implies behavior the system cannot support. The tradeoff is visual breadth versus credibility. Credibility should win, because a smaller portal with believable permissions, states, and data boundaries reads stronger than a large portal with invisible back-end assumptions.

### Safer implementation path
1. Start with the project and client membership model.
2. Define roles: studio owner, internal designer, client admin, client reviewer, finance-only viewer.
3. Define object permissions for projects, files, invoices, comments, and approvals.
4. Design approval states before designing approval screens.
5. Mock invoice status with a visible integration boundary rather than implying live billing.
6. Treat activity feed as event history first, then decide whether it needs realtime delivery.
7. Build the first UI pass around three complete flows: file review, comment resolution, and invoice visibility.
8. Defer live activity, bulk file management, and advanced notifications until the underlying events are stable.

### Release boundary
The first credible case-study release should include project overview, file approval, comments, and invoice status as a read-only billing boundary. It should not include full live activity, billing writes, or production file security claims.

This prevents the case study from overclaiming. It also gives the designer a cleaner story: the work is not just a pretty portal, it is a scoped service model with permission, state, and data decisions.

### Verification checkpoints
- Each role has a permission matrix.
- Each file approval state has an allowed next state.
- Each invoice field is marked as mocked, imported, or editable.
- Each comment action has an owner, timestamp, and edit/delete rule.
- Activity feed events come from named system actions, not decorative text.
- The case study labels prototype evidence separately from production assumptions.

## Why This Passed
- It identifies the hidden back-end system behind the UI request.
- It names a concrete release boundary instead of saying everything is feasible.
- It includes a rejected alternative and explains the tradeoff.
- It gives implementation-aware verification checks that a designer could use in a case study.
- It avoids claiming production proof.

## What Would Have Failed
- Calling the portal simple because it looks like a dashboard.
- Treating invoice status, file approval, and live activity as visual-only features.
- Saying the prototype is production-ready without file, billing, permission, and event boundaries.
- Adding every feature to the first release because it makes the project look bigger.

## Revision Pass
The first pass was too close to a feature list. The revision tightened the governing decision: this should be scoped as a credible system design prototype, not a fake production app. The final version adds permission, state, and evidence boundaries so the example shows implementation awareness at the level the pack claims.
