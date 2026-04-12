# Style Guide Template

## 1. Foundations
- brand role:
- audience fit:
- archetype:
- voice:
- what the system should feel like:
- what it must never feel like:

## 2. Grid
- medium:
- columns:
- gutters:
- margins:
- baseline:
- breakpoint logic:
- allowed span patterns:

## 3. Type
- display family:
- body family:
- hierarchy:
- body size:
- leading:
- fallback stack:
- variable font or optical sizing notes:

## 4. Color
- foundation neutrals:
- action colors:
- status colors:
- accent usage rule:
- APCA or WCAG notes:
- Pantone notes:

## 5. Components and states
- button states:
- form states:
- focus rules:
- disabled rules:
- error and success rules:
- motion rules:

## 6. Tokens
- primitives:
- semantic aliases:
- component tokens:
- naming rule:
- what should never be hard-coded:

## Example output
### 1. Foundations
- brand role: enterprise asset-governance platform for cloud operations and compliance teams
- audience fit: technical admins, compliance reviewers, operations managers
- archetype: competent steward with restrained operator energy
- voice: direct, clear, evidence-first, never theatrical
- what the system should feel like: controlled, readable, trustworthy, high-signal
- what it must never feel like: playful, chaotic, luxury-fashion, over-animated

### 2. Grid
- medium: responsive web app + supporting dashboards
- columns: 12 desktop / 8 tablet / 4 mobile
- gutters: 24px desktop, 24px tablet, 16px mobile
- margins: 32px desktop default, 24px tablet, 16px mobile
- baseline: 8px rhythm with 24px body-text cadence where reading-heavy
- breakpoint logic: mobile-first contraction from 12 -> 8 -> 4 with no custom one-off grids
- allowed span patterns: 12, 8/4, 6/6, 4/4/4, 3/3/3/3, full-width cards on mobile

### 3. Type
- display family: Mona Sans
- body family: Inter
- hierarchy: display / section / label / body / caption / mono data
- body size: 16px default, 14px only for secondary metadata
- leading: 1.5 body, 1.2 display, 1.35 support text
- fallback stack: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif
- variable font or optical sizing notes: use variable fonts where available; keep optical sizing automatic for large display moments

### 4. Color
- foundation neutrals: neutral-0, 25, 75, 200, 700, 900, 950
- action colors: blue primary, teal secondary highlight only
- status colors: green success, amber warning, red error, sky info
- accent usage rule: accents are reserved for action and high-signal emphasis, not decorative fill
- APCA or WCAG notes: body text targets APCA Lc 75+ and WCAG AA minimums at all times
- Pantone notes: Pantone only applies to identity-critical print surfaces, not routine UI components

### 5. Components and states
- button states: every button must define rest, hover, focus-visible, pressed, disabled, loading
- form states: default, focus, filled, error, success, disabled must be explicit
- focus rules: visible 3:1 non-text contrast minimum, never removed for aesthetics
- disabled rules: cannot rely on low opacity alone; must remain understandable as inactive
- error and success rules: never color-only; pair with label/icon or summary text
- motion rules: subtle, under 200ms for UI transitions; obey reduced-motion preferences

### 6. Tokens
- primitives: raw neutral, blue, teal, red, amber, green scales + spacing/radius/shadow primitives
- semantic aliases: text-primary, text-secondary, surface-default, border-muted, action-primary, status-error
- component tokens: button-primary-bg, input-border-default, card-padding-md, focus-ring-color
- naming rule: category-role-variant-state; no value names in semantic or component tokens
- what should never be hard-coded: status colors, spacing steps, focus colors, shadows, type sizes
