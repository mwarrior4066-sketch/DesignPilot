# Component Spec Example
Fixture: tests/fixtures/component-spec.prompt.md
Validation result: tests/evals/component-spec.eval.json

## Input Prompt
Write a reusable component spec for a bulk-action toolbar used in a table with selection, disabled rows, async processing, and partial permissions.

## Selected Route and Loaded Skills
- Route: `rt_component_spec`
- Task contract: `component_spec`
- Mode: REBUILD
- Phase: specs
- Skills: `component-systems-expert.md`, `front-end-handoff-expert.md`

## Final Output
### Purpose and scope
The bulk-action toolbar appears only when one or more eligible rows are selected. It exists to expose batch actions without permanently consuming table chrome. It does not own row selection itself, and it should inherit selection state rather than redefine it.

### Anatomy
- container
- selection count label
- primary bulk action slot
- overflow menu for secondary actions
- permission warning banner
- async progress inline status
- dismiss control

### State matrix
- hidden: zero rows selected
- active: at least one eligible row selected
- mixed eligibility: selected rows include disabled or unauthorized items
- processing: action submitted, toolbar locks destructive controls and shows progress
- partial success: action completed for some rows and returns a structured error summary
- error: request failed and preserves selection for retry

### Accessibility and implementation notes
Keyboard focus moves into the toolbar only after selection changes. The toolbar must announce selection count changes to assistive tech, expose the count through an aria-live pattern, and keep the primary action disabled when the current permission set blocks execution. Screen reader messaging should explain whether the action is blocked by permissions or by zero eligible rows. The alternative would be to silently hide unavailable actions, but that weakens trust because users cannot tell whether the limitation comes from permissions or missing selection. Preserve explicit messaging and flex visual compactness first.

## Why This Passed
- The boundary between table and toolbar is explicit.
- States include real conflict cases instead of only happy-path states.
- Accessibility and permission logic are implementation-ready.
- It includes one rejected alternative with rationale.

## What Would Have Failed
- Listing anatomy only, with state behavior deferred to a later undocumented pass.
- Treating unauthorized rows as a generic error instead of a permission state.
- Deferring accessibility to engineering later.

## Revision Pass
The earlier draft named the visible parts but not the ownership boundary. The revision added the scope rule and the mixed-eligibility state so the component can survive real handoff.
