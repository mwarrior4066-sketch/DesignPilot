# Domain Validators

This file defines what the validation layer must check by specialist domain.
Do not duplicate full skill logic here.
Use this file to point validation toward the canonical owner.

## Accessibility and feedback
Owner: `skills/accessibility-feedback-expert.md`
Check:
- required states present when interactive
- visible focus preserved
- touch targets not undersized
- reduced-motion or flash safety respected
Hard fail:
- hidden focus
- inaccessible target size as the default solution
- unsafe motion or flashing behavior

## Color
Owner: `skills/color-system-expert.md`
Check:
- role map exists
- contrast logic exists
- brand color is not overriding accessibility
- dark mode logic exists when needed
Hard fail:
- inaccessible primary text/color pairing
- color-only meaning in critical states without fallback cues

## Typography
Owner: `skills/type-system-expert.md`
Check:
- readable size / measure / hierarchy logic
- no shrink-to-fit anti-pattern
- fallback and implementation note when needed
Hard fail:
- unreadable body text as the primary solution
- collapsed hierarchy used to solve space problems

## Grid / layout reconstruction
Owners:
- `skills/grid-system-expert.md`
- `skills/layout-reconstruction-expert.md`
Check:
- correct distinction between new layout and inferred layout
- stable alignment logic
- no invented grid when source layout should be inferred
Hard fail:
- source layout ignored when clearly available

## Dashboard / data-vis
Owner: `skills/dashboard-data-expert.md`
Check:
- dashboard type declared
- chart choice justified
- density handled
- filter/drill-down or empty-state logic included when relevant
Hard fail:
- overloaded single-view recommendation with no mitigation
- obviously wrong chart type passed as acceptable

## PDF / document accessibility
Owners:
- `skills/pdf-layout-expert.md`
- `skills/document-accessibility-expert.md`
Check:
- layout/frame logic
- tagging/reading-order/extraction concerns when relevant
- OCR or artifact handling when relevant
Hard fail:
- document turned into a screenshot answer when document behavior matters

## Front-end handoff
Owner: `skills/front-end-handoff-expert.md`
Check:
- implementation boundary is clear
- tokens/states/accessibility implications are named
- no fake code certainty
Hard fail:
- implementation guidance that ignores required state/accessibility logic

## Back-end aware planning
Owner: `skills/back-end-aware-planner.md`
Check:
- feasibility verdict exists
- backend implication map exists
- auth/data/export/realtime implications are surfaced when relevant
Hard fail:
- backend-heavy request treated as purely visual

## Brand strategy
Owner: `skills/brand-strategy-expert.md`
Check:
- audience fit logic
- frame of reference or positioning logic
- trust burden or proof logic
Hard fail:
- unsupported hard claims passed through as final recommendations

## Content and case study
Owner: `skills/content-and-case-study-expert.md`
Check:
- correct writing mode
- problem/process/solution/outcome visibility when relevant
- rationale/evidence present
Hard fail:
- wrong writing mode for the user’s request

## Graphic design
Owner: `skills/graphic-design-expert.md`
Check:
- format logic declared
- hierarchy/composition logic present
- distance/time constraints handled when relevant
Hard fail:
- deck/poster/editorial logic clearly misapplied
