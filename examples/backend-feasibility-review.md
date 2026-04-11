# Back-End Feasibility Review Example
Fixture: tests/fixtures/backend-feasibility-review.prompt.md
Validation result: tests/evals/backend-feasibility-review.eval.json

## Input Prompt
We want to add team sharing, CSV export, approval flows, and a live activity dashboard to a solo-designer project tool. Review the back-end implications before UI work begins.

## Selected Route and Loaded Skills
- Route: `rt_backend_feasibility`
- Task contract: `backend_feasibility_review`
- Mode: PEER
- Phase: strategy
- Skills: `back-end-aware-planner.md`, `front-end-handoff-expert.md`

## Final Output
### Requested capability
The visible ask sounds like four UI features. In practice it is an auth, storage, workflow, and realtime architecture expansion. That changes the proof burden immediately because at least 4 system surfaces now need to agree on ownership, permissions, exports, and event freshness.

### Hidden system requirements
- Team sharing introduces accounts, invitations, access control, and revocation rules.
- CSV export introduces dataset shaping, column governance, permission filtering, and file-generation limits.
- Approval flows introduce state machines, audit history, and notification rules.
- Live activity introduces event capture, retention policy, and either polling or realtime transport.
- Any promised first release needs a clear score for role coverage, because a shared tool with a 0% permission model is still a single-user system wearing collaborative UI.

### Feasibility assessment
This is feasible only if the system moves from single-user assumptions to shared-object ownership. The obvious alternative is to prototype the UI first and “wire the backend later,” but that would hide the real constraints and likely create false promises. The tradeoff is velocity versus correctness. Correctness should win because auth and approval logic become expensive to reverse once exposed.

### Safer implementation path
1. Define tenant and membership model.
2. Define object ownership and permission matrix.
3. Add audit-safe approval states.
4. Add export policy and field-level filters.
5. Add activity feed only after the underlying events are structured.
6. Only then design the UI states around those capabilities.
7. Use one release scorecard so every step is checked against auth coverage, export safety, and event freshness before polish work starts. Set a threshold for permission coverage before the UI can present collaboration as ready.

## Why This Passed
- It reveals hidden architecture clearly.
- It does not pretend the request is only a screen-layout change.
- It names the order of operations.
- It includes a rejected alternative and the reason it fails.

## What Would Have Failed
- “This is only a quick front-end add.”
- Designing dashboard screens before defining event structure.
- Calling exports low-risk without permission filtering.

## Revision Pass
The first draft listed backend impacts but not the dependency order. The revision added the sequencing logic so the plan can guide actual implementation.
