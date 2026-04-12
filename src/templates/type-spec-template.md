# Type Spec Template

Use this template when the task needs a concrete type system instead of loose font suggestions.

## Roles
- Primary UI / body family:
- Secondary / support family:
- Display / headline family:
- Monospace family:
- Accessibility-first substitute:
- Cross-platform fallback stack:

## Why these choices
- medium:
- audience:
- tone:
- readability need:
- density need:
- licensing / deployment note:

## Technical rules
- variable font available:
- axes to use:
- body size:
- body leading:
- display leading:
- target measure:
- figures needed: tabular / lining / oldstyle:
- optical sizing rule:

## Fallback logic
- missing premium font substitute:
- system-safe substitute:
- multilingual substitute:
- dark-mode or contrast note:

## Token mapping
- `typo.body.family`:
- `typo.body.size`:
- `typo.body.line-height`:
- `typo.display.family`:
- `typo.display.weight`:
- `typo.mono.family`:

## Example output
### Roles
- Primary UI / body family: Inter Variable
- Secondary / support family: Inter Variable
- Display / headline family: Mona Sans Variable
- Monospace family: IBM Plex Mono
- Accessibility-first substitute: Atkinson Hyperlegible Next
- Cross-platform fallback stack: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif

### Why these choices
- medium: enterprise SaaS web app with PDF exports and sales decks
- audience: technical admins, operations managers, compliance reviewers
- tone: competent, modern, restrained
- readability need: high, especially in dense settings and forms
- density need: medium-high without collapsing legibility
- licensing / deployment note: open-source primary stack keeps implementation and procurement simple

### Technical rules
- variable font available: yes
- axes to use: wght and slnt for UI, opsz when supported for display sizing
- body size: 16px default, 14px only for secondary metadata
- body leading: 1.5
- display leading: 1.15–1.25 depending on size
- target measure: 60–75 CPL for reading surfaces; cap explanations near 65ch
- figures needed: tabular + lining for dashboards, oldstyle optional for editorial notes
- optical sizing rule: font-optical-sizing: auto; increase weight slightly for small labels if opsz unavailable

### Fallback logic
- missing premium font substitute: replace premium grotesk with Inter or Public Sans before using arbitrary generic sans
- system-safe substitute: system-ui stack for constrained environments
- multilingual substitute: Noto Sans / Noto Serif where broad script coverage is required
- dark-mode or contrast note: keep weights slightly stronger in dark mode for small UI text

### Token mapping
- `typo.body.family`: Inter
- `typo.body.size`: 16px
- `typo.body.line-height`: 1.5
- `typo.display.family`: Mona Sans
- `typo.display.weight`: 650
- `typo.mono.family`: IBM Plex Mono
