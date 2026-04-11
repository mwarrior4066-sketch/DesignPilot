# Adaptive Explanation Tiered Response Example
Fixture: tests/fixtures/adaptive-explanation-tiered-response.prompt.md
Validation result: tests/evals/adaptive-explanation-tiered-response.eval.json

## Input Prompt
Explain why this admin settings screen should not default to a fully client-rendered implementation. Show how the same answer changes for Functional, Integrative, and Strategic explanation tiers.

## Selected Route and Loaded Skills
- Route: `rt_frontend_architecture`
- Task contract: `frontend_implementation_review`
- Mode: PEER
- Phase: implementation
- Skills: `front-end-architecture-expert.md`, `front-end-handoff-expert.md`, `accessibility-feedback-expert.md`
- Active tiers shown: Functional, Integrative, Strategic

## Final Output
### Architectural framing
The real architectural problem is boundary collapse. A fully client-rendered settings surface feels simple at first, but it pushes rendering, fetching, mutation recovery, and state ownership into one hydrated bundle. That raises bundle and hydration cost and makes the page harder to recover cleanly when a field fails, a request retries, or a section loads slowly.

### Boundary and state model
For all three tiers, the governing decision stays the same: keep a server-first shell, keep account data in server-state, and move only the truly interactive widgets into client islands behind `use client`. That boundary keeps local state local, prevents boolean sprawl from swallowing the whole page, and lets the interface preserve native form semantics. The semantic contract still matters here because WCAG and ARIA expectations do not disappear just because the page is reactive. Native labels, buttons, and form controls remain the safer baseline.

### Rendering and mutation strategy
**Functional:** Keep the layout on the server and move only the few controls that need live interaction into client components. That makes the screen appear faster and reduces hydration tax. Start with a simple boundary map and add loading, error, and retry states to each client island.

**Integrative:** Do not default to CSR for the full surface. A server-first shell plus scoped client islands gives the better tradeoff between perceived speed, state clarity, and maintainability. Use an explicit status union for pending, error, and success behavior instead of stacking flags.

**Strategic:** Server-render the shell. Hydrate only the widgets that earn the cost. Keep mutation handling close to the widget, preserve native form semantics, and do not let a framework default hide the real architecture decision.

### Risks and safer path
The risk is a client-heavy page that feels flexible but hides its recovery logic and performance cost. The safer path is to map boundaries first, preserve semantic host elements, and then verify the result with keyboard and screen-reader checks where behavior depends on those host elements. The tradeoff is slightly more upfront boundary discipline rather than a faster but blurrier implementation. Boundary discipline should win.

## Why This Passed
- It keeps one architectural truth across all tiers and only changes explanation density.
- It uses the required sections of the front-end implementation contract.
- It retains standards-facing semantic language instead of simplifying those constraints away.
- Each tier still ends in a visible next move.

## What Would Have Failed
- Letting the Functional version hide hydration, boundary, or semantic constraints.
- Turning Strategic into a tutorial.
- Changing the actual architectural recommendation across tiers.

## Revision Pass
The weak draft changed tone but not contract shape. The corrected version preserved the route-owning decision, restored the required section headings, and made the standards-facing semantic rule visible.
