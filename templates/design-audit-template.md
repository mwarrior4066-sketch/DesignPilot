# Design Audit Template

Use this when the task is diagnostic. This is not a rebuild template.

## 1. Context
- task or surface:
- medium:
- current phase:
- audience:
- primary goal:
- known constraints:

## 2. Findings by layer
### Strategic issues
### Structural issues
### Visual issues
### Accessibility issues
### Token or implementation issues
### Document / presentation architecture issues

## 3. Evidence artifacts
- grid notes:
- type notes:
- color / contrast notes:
- state matrix notes:
- PDF / document notes:
- deck / wayfinding notes:
- content-box / vertical-fill notes:
- page-role architecture notes:
- implementation notes:

## 4. Inventory and consolidation checks
- unique button styles:
- repeated spacing violations:
- repeated type-scale violations:
- hard-coded values that should become tokens:
- inconsistent states:
- recurring accessibility failures:
- PDF structure / tagging failures:
- dashboard density failures:

## 5. Severity map
- fix now:
- fix next:
- defer:
- acceptable tradeoffs:

## 6. Recommended next move
- highest-leverage correction:
- supporting correction:
- what should not be touched yet:
- missing source of truth, if any:

## Example output
### 1. Context
- task or surface: account settings page
- medium: responsive web app
- current phase: audit before rebuild
- audience: enterprise admins
- primary goal: update permissions, billing, and security settings without error
- known constraints: WCAG AA, existing token system, dense information environment

### 2. Findings by layer
#### Strategic issues
- The page treats billing, permissions, and security as one flat surface even though the risk profile of each area is different.
- The surface is framed as “settings” when it actually contains high-consequence admin actions that need stronger confirmation logic.

#### Structural issues
- Navigation depth is unclear: section headers, cards, and side navigation all compete as primary grouping devices.
- Critical actions like “Revoke access” and “Delete workspace” are visually buried in the same rhythm as routine preference toggles.

#### Visual issues
- Three different card styles and two different heading scales appear in one viewport, which weakens scan logic.
- CTA emphasis is diluted because primary blue is used for both navigation chips and commit actions.

#### Accessibility issues
- Focus-visible state on secondary buttons falls below 3:1 non-text contrast.
- Error status relies on red text alone in two validation messages.

#### Token or implementation issues
- Spacing alternates between 12, 16, 20, and 24 with no clear token logic.
- Inputs use hard-coded border colors instead of semantic tokens.

### 3. Evidence artifacts
- grid notes: right sidebar collapses late and causes line lengths above 90 characters on desktop.
- type notes: body copy is 14px in a high-density admin surface where 16px should remain the default for core settings explanations.
- color / contrast notes: warning banner passes WCAG for large text but APCA is weak for the smaller supporting copy.
- state matrix notes: loading, disabled, and success states are not consistently defined across destructive actions.
- implementation notes: button variants appear duplicated in code because visual variants are standing in for semantic action levels.

### 4. Inventory and consolidation checks
- unique button styles: 5
- repeated spacing violations: 11
- repeated type-scale violations: 4
- hard-coded values that should become tokens: border-danger, sidebar-bg, card-shadow-2
- inconsistent states: destructive actions lack a shared pressed/loading/error model
- recurring accessibility failures: low-contrast focus, color-only status, underspecified destructive confirmations

### 5. Severity map
- fix now: permissions and destructive action hierarchy, focus visibility, tokenized status colors
- fix next: card consolidation, type-scale cleanup, sidebar rhythm
- defer: cosmetic illustration refresh
- acceptable tradeoffs: keep current card radius if tokenized and applied consistently

### 6. Recommended next move
- highest-leverage correction: split the page into risk-tiered sections with a dedicated destructive action zone
- supporting correction: consolidate button and card variants into semantic levels
- what should not be touched yet: brand illustration language
- missing source of truth, if any: admin action state matrix
