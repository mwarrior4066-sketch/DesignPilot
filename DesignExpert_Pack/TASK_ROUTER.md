# Task Router

Route automatically.
Do not ask the user which skill to use.

## Routing model
Classify every task by:
- trigger
- pathway
- modules
- evidence artifact
- risk flag

Use the smallest correct pathway.
Do not load a specialist skill if the ask does not need it.

## Primary pathways

### 1. Strategy pathway
Use when the request is about:
- market gap
- audience
- psychographics
- positioning
- brand fit
- product rationale

Load:
- `skills/ux-research-expert.md`
- `skills/brand-strategy-expert.md`

Read first:
- `knowledge-base/summaries/ux-roadmap-summary.md`
- `knowledge-base/summaries/audience-and-industry-summary.md`
- `knowledge-base/summaries/brand-and-archetype-summary.md`

Evidence:
- audience logic
- problem statement
- positioning frame
- decision criteria

### 2. UI structure pathway
Use when the request is about:
- screens
- flows
- IA
- hierarchy
- navigation
- action placement

Load:
- `skills/ui-system-expert.md`
- `skills/grid-system-expert.md` when layout is structural
- `skills/type-system-expert.md` when hierarchy or readability matters

Evidence:
- primary action
- hierarchy map
- navigation logic
- layout logic

### 3. Accessibility and feedback pathway
Use when the request is about:
- focus
- keyboard behavior
- hover/focus content
- touch targets
- motion safety
- interaction feedback
- state visibility

Load:
- `skills/accessibility-feedback-expert.md`
- `skills/color-system-expert.md` when contrast or state color matters
- `skills/front-end-handoff-expert.md` when implementation detail is needed

Evidence:
- state matrix
- focus/keyboard rule
- contrast threshold
- motion or target-size rule

### 4. Dashboard and data-vis pathway
Use when the request is about:
- dashboards
- KPI hierarchy
- chart choice
- data density
- filters
- drill-downs
- empty states

Load:
- `skills/dashboard-data-expert.md`
- `skills/ui-system-expert.md`
- `skills/color-system-expert.md`
- `skills/accessibility-feedback-expert.md` when chart readability or interaction matters

Evidence:
- dashboard type
- KPI hierarchy
- chart-selection rule
- density rule
- filter/drill-down logic

### 5. Typography pathway
Use when the request is about:
- font choice
- pairing
- hierarchy
- leading
- measure
- variable fonts
- opsz
- fallback stacks
- licensing-aware substitutions

Load:
- `skills/type-system-expert.md`
- `libraries/FONT_LIBRARY.json`, `libraries/FONT_LIBRARY.md`

Evidence:
- role assignment
- body/display defaults
- measure target
- leading ratio
- fallback stack

### 6. Color pathway
Use when the request is about:
- palette
- contrast
- APCA
- WCAG
- dark mode
- Pantone
- semantic color roles
- state color logic

Load:
- `skills/color-system-expert.md`
- `knowledge-base/summaries/pantone-production-summary.md` when print-aware
- `skills/accessibility-feedback-expert.md` when state behavior matters
- `libraries/PANTONE_LIBRARY.json`, `libraries/PANTONE_LIBRARY.md` when print-aware

Evidence:
- role map
- WCAG threshold
- APCA threshold when relevant
- dark-mode rule
- fallback logic

### 7. New-layout grid pathway
Use when the request is about:
- columns
- spacing systems
- breakpoints
- modular layout
- editorial grids
- slide grids
- app grids

Load:
- `skills/grid-system-expert.md`
- `skills/type-system-expert.md` when baseline or measure matters

Evidence:
- medium
- margins
- columns
- gutters
- baseline or breakpoint rule

### 8. Layout reconstruction pathway
Use when the request is about:
- extending an existing layout
- inferring a grid from screenshots/PDFs
- normalizing inconsistent legacy layouts
- preserving an established structure while adding new content

Load:
- `skills/layout-reconstruction-expert.md`
- `skills/grid-system-expert.md`
- `skills/type-system-expert.md` when text measure or baseline fit matters

Evidence:
- inferred grid or manuscript model
- tolerance / normalization rule
- legacy-preservation rule
- confidence / fallback note

### 9. PDF and document pathway
Use when the request is about:
- PDFs
- spreads
- footers
- text frames
- extraction
- tagging
- reading order
- artifacts
- OCR repair

Load:
- `skills/pdf-layout-expert.md`
- `skills/document-accessibility-expert.md`
- `skills/layout-reconstruction-expert.md` when legacy structure must be inferred
- `skills/color-system-expert.md` when print or contrast matters

Evidence:
- frame logic
- tag/artifact rule
- reading-order rule
- extraction rule
- baseline or OCR fallback rule

### 10. Component systems pathway
Use when the request is about:
- component inventory
- variants
- sizes
- state coverage
- component reuse
- governance
- “should this be a new component?”

Load:
- `skills/component-systems-expert.md`
- `skills/accessibility-feedback-expert.md`
- `skills/front-end-handoff-expert.md` when implementation detail is needed

Evidence:
- component purpose
- when-to-use / when-not-to-use
- required states
- reuse vs new-component decision

### 11. Build and handoff pathway
Use when the request is about:
- React
- Next.js
- Tailwind
- tokens
- implementation
- design handoff
- component build
- motion implementation
- webfont loading

Load:
- `skills/front-end-handoff-expert.md`
- `skills/component-systems-expert.md`
- `skills/accessibility-feedback-expert.md`
- `skills/color-system-expert.md` when contrast or state logic matters
- `skills/type-system-expert.md` when font loading or fallback matters
- `skills/back-end-aware-planner.md` when data/auth/export risk appears

Evidence:
- component boundary
- token usage
- state matrix
- keyboard/focus behavior
- font loading / fallback logic
- implementation constraint

### 12. Communication pathway
Use when the request is about:
- portfolio
- case study
- rewrite
- simplification
- UX copy
- rationale
- design writing

Load:
- `skills/content-and-case-study-expert.md`
- `skills/ux-research-expert.md` when reasoning must tie back to research
- `skills/brand-strategy-expert.md` when tone or audience fit matters

Evidence:
- audience
- clarity pass
- structure choice
- rewrite logic

## Risk triggers
Automatically add `skills/back-end-aware-planner.md` when the request implies non-trivial technical risk.
Automatically add `skills/document-accessibility-expert.md` when a PDF must remain accessible.
Automatically add `skills/accessibility-feedback-expert.md` when interactivity, motion, or target size matters.
