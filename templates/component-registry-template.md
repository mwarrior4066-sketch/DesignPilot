# Component Registry Entry Template

## Identity
- component name:
- category:
- status: stable / incubating / local-only / deprecated

## Purpose
- what it does:
- when to use:
- when not to use:

## Structure
- anatomy:
- props:
- slots:
- content rules:

## Variants and sizes
- variants:
- sizes:
- responsive rules:

## States
- rest:
- hover:
- focus:
- active:
- selected:
- disabled:
- loading:
- error / success / warning when relevant:

## Accessibility
- keyboard behavior:
- ARIA / semantics:
- target size:
- motion concerns:

## Tokens
- color tokens:
- type tokens:
- spacing tokens:
- motion tokens:

## Implementation
- code availability:
- framework notes:
- testing notes:

## Example output
### Identity
- component name: Exception Severity Badge
- category: status / metadata
- status: stable

### Purpose
- what it does: communicates the severity level of a compliance or policy exception in dashboards, tables, and exports
- when to use: when a record needs a compact severity label that can appear in dense data environments
- when not to use: not for long explanatory alerts or for color-only emphasis without text

### Structure
- anatomy: badge container, severity label text, optional icon, optional tooltip trigger
- props: severity level, icon on/off, compact mode, inverse mode
- slots: label only, or icon + label
- content rules: label text must use canonical severity terms such as Critical, High, Medium, Low

### Variants and sizes
- variants: neutral, severity-coded, inverse for dark surfaces
- sizes: sm, md
- responsive rules: use compact size in dense tables; keep md in standalone summary cards

### States
- rest: stable fill and label pairing
- hover: optional tooltip affordance only when interactive
- focus: visible ring if badge acts as a trigger
- active: only if linked to drill-down interaction
- selected: outline or selected container state if used as filter chip
- disabled: rarely used; if disabled, retain readable label but mute interaction
- loading: skeleton placeholder at list level, not spinning badge itself
- error / success / warning when relevant: handled by severity mapping, not separate ad-hoc styles

### Accessibility
- keyboard behavior: only tabbable when badge opens a detail or filter action
- ARIA / semantics: if static, expose as text; if interactive, use button semantics with label
- target size: 24x24 minimum when interactive, larger preferred in touch contexts
- motion concerns: no pulsing for persistent severity states; motion only for temporary transition moments

### Tokens
- color tokens: status-critical-bg, status-critical-text, status-high-bg, status-high-text
- type tokens: typo.label.sm
- spacing tokens: space-1 horizontal padding, space-0-5 vertical padding
- motion tokens: none for static usage; quick fade for filter selection only

### Implementation
- code availability: available in shared React component library
- framework notes: accepts semantic token props only, no raw hex overrides
- testing notes: validate contrast, label text consistency, filter-chip behavior, and export rendering
