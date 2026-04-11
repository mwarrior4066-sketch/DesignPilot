# Front-End Implementation Review Example
Fixture: tests/fixtures/frontend-implementation-review.prompt.md
Validation result: tests/evals/frontend-implementation-review.eval.json

## Input Prompt
Review this front-end implementation plan for a permissions-heavy scheduling dashboard. The current proposal defaults to a large client-rendered page, stores loading and error state in separate booleans, uses custom div buttons in filter chips, and wants optimistic updates for recurring edits. Recommend a safer architecture.

## Selected Route and Loaded Skills
- Route: `rt_frontend_architecture`
- Task contract: `frontend_implementation_review`
- Mode: AUDIT
- Phase: implementation
- Skills: `front-end-architecture-expert.md`, `front-end-handoff-expert.md`, `accessibility-feedback-expert.md`
- Known tensions: server-first performance vs client flexibility, optimistic speed vs rollback safety

## Final Output
### Architectural framing
The visible request sounds like a front-end cleanup, but the real failure is architectural. A permissions-heavy scheduling dashboard should not default to a large CSR surface when much of the shell can be static or server-rendered. The current plan also mixes state responsibilities in a way that will create impossible states and weak recovery behavior.

### Boundary and state model
Use a server-first shell with Server Components for the surrounding dashboard layout, the initial permission-aware dataset, and the static filters metadata. Move `use client` down to the interactive islands that actually need local event handling, such as the recurring-edit form and the live filter controls. That boundary choice reduces hydration cost and keeps permission-sensitive data off the client when it does not need to live there.

State ownership should also change. Local UI toggles can stay local state, but request status should move to an explicit status union or state machine rather than separate `isLoading`, `isError`, and `isSuccess` flags. For recurring edits, use a controlled mutation path with `useActionState` or an equivalent mutation contract so the optimistic path has a rollback rule instead of a visual guess.

The filter chips should not be clickable divs. Use native button semantics or a real toggle host so keyboard behavior, focus, ARIA expectations, and announcement logic are preserved. This is a semantic contract issue, not just styling.

### Rendering and mutation strategy
Choose a mixed rendering model:
- static or server-rendered outer shell for the dashboard frame
- server-state for the permission-scoped schedule data
- client islands for live filter interaction and inline edit entry
- `Suspense` around slower data slices so the rest of the shell can stream safely

For mutations, use a Server Action or another server-owned write boundary for recurring edits. The optimistic UI can still exist, but the tradeoff should be clear: fast perceived response is worth keeping only if rollback, error messaging, and stale-state recovery are explicit. Clarity should win over instant illusion. That means the optimistic state must revert on failure and expose the retry path, not silently drift.

### Risks and safer path
First, split the dashboard into server shell plus client islands and stop the page-wide client rendering default. Then replace boolean-explosion request state with a single status model. After that, swap the filter-chip divs for native button semantics and define keyboard and focus behavior. Finally, add optimistic updates only after the mutation boundary and rollback logic are verified.

The alternative would be to keep the whole page client-heavy for implementation speed, but that preserves hydration tax, boundary blur, and weaker recovery. The safer path is slower up front and more stable later.

## Why This Passed
- It names the rendering model directly instead of giving generic React advice.
- It makes server and client boundaries explicit.
- It names the state model and mutation recovery path.
- It uses semantic and accessibility rules as architectural evidence, not as an afterthought.

## What Would Have Failed
- Saying to convert everything to React components and move on.
- Recommending more hooks without fixing ownership and rollback logic.
- Calling the plan production-ready without naming hydration and bundle costs.

## Revision Pass
The weak draft only said to split the page into smaller components. The corrected version made the governing decisions visible: rendering, boundary placement, state ownership, semantic host selection, and rollback-safe mutation behavior.
