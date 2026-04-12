# Color Library

Use this library to choose, compare, substitute, and deploy **digital color systems** by role, domain, semantic logic, accessibility, dark-mode behavior, and implementation model.
This is the digital/system companion to the print-aware Pantone library.

Machine-readable companion: `COLOR_LIBRARY.json` for fast lookup and low-token retrieval.
Use the JSON companion first for indexing, then this markdown file when nuance, caveats, or domain logic matter.

## Use this library when
- the task is about product, dashboard, app, web, SaaS, editorial, data-vis, healthcare, public-sector, HMI, or brand-interface color systems
- a palette must be token-ready, themeable, or usable across light and dark modes
- semantic role mapping matters more than individual swatches
- the question is about palette structure, neutral strategy, state behavior, or domain fit

## Do not use this library as
- a Pantone replacement for print matching
- a reason to treat a trend palette as production-ready without role mapping
- proof that any hue can safely carry multiple meanings in UI

## Distinct-system counting rule
A distinct palette system is **not** just a hue swap.
Count a system as distinct only when it changes at least one of these:
- primary hue logic
- neutral strategy
- semantic role mapping
- contrast profile
- domain environment or operational constraint
- data-mapping logic

A light and dark theme count as **one integrated system** when they are intentionally paired.
A minor hue shift without a neutral or semantic change is a variant, not a new system.

## Selection sequence
1. identify the environment: consumer UI, enterprise SaaS, public sector, healthcare, HMI, aviation, luxury, editorial, data-vis, AI infra
2. identify the role model: text, surface, border, action, status, chart, accent, brand-expressive layer
3. choose the neutral strategy before the accent family
4. set the chroma budget: restrained, moderate, or high-chroma
5. define state logic: value shift, alpha overlays, or token remapping
6. define accessibility targets: WCAG AA minimum, AAA target, APCA quality target, non-text 3:1
7. define light/dark pairing logic
8. separate brand expression from UI semantics when necessary
9. define implementation model: semantic aliases, scale depth, OKLCH/HSL/HEX storage, CSS token names

## Core rules
- assign color by role before by taste
- neutrals carry most of the system load
- reserve the strongest chroma for the highest-priority actions or signals
- brand colors are not automatically safe for body UI roles
- status semantics must remain stable across themes
- color must not be the only carrier of meaning
- data visualization requires palette logic that matches the data relationship
- treat high-stakes operational systems as a separate class from ordinary web UI

## Default schema for a production-ready system
Each system should define:
- `system_id`
- `environment`
- `domain_cluster`
- `primary_hue_logic`
- `neutral_strategy`
- `semantic_roles`
- `contrast_profile`
- `dark_mode_strategy`
- `state_logic`
- `data_viz_logic`
- `implementation_model`
- `misuse_warnings`

## Domain clusters
### Public sector / institutional
Use authority-first, tokenized systems with strong neutrals and predictable functional colors.
Strong references: USWDS theme and state tokens, GOV.UK functional colors.
Good fits:
- trust-neutral blues with warm-dark text
- restrained accent use
- 4.5:1 minimum everywhere important, AAA preferred for critical paths

### Enterprise SaaS / B2B
Use calm neutrals, one primary accent, and disciplined state colors.
Good fits:
- blue/slate systems
- muted purple/indigo systems
- low-to-moderate chroma dashboards

### Fintech / security
Use trust foundations with a clean expressive layer.
Good fits:
- blue or indigo neutral-core systems
- controlled innovation accents like purple or teal
- avoid allowing expressive brand colors to interfere with number readability

### Healthcare / wellness
Separate clinical clarity from wellness softness.
Good fits:
- clinical care: blue/teal neutrals with high-clarity surfaces
- integrative wellness: sage, warm neutrals, low-glare surfaces
- avoid sterile all-white systems that increase fatigue or anxiety

### Industrial HMI / SCADA / operations
Use mid-gray fatigue-reduction backgrounds and status colors as alarms, not decoration.
Good fits:
- restrained grays
- high-signal status accents used sparingly
- do not make the entire interface chromatic

### Aviation / cockpit / glare-heavy operational screens
Prioritize high-glare readability, narrow accent use, and night-mode comfort.
Good fits:
- blue-averse critical indicators when tiny symbols or dark backgrounds make blue hard to focus
- strong amber/white/green hierarchy when operationally justified

### AI / technical infrastructure
Use neutral precision cores with a controlled high-chroma expressive layer.
Good fits:
- indigo + vivid accent systems
- dark theme systems with strong semantic separation
- do not let neon accents become default text or surface colors

### Luxury / premium / fashion
Use restraint, deep neutrals, and selective accent color.
Good fits:
- black, graphite, plum, emerald, or champagne-adjacent systems
- high contrast only where intentional, not everywhere
- expressive serif/editorial systems may require softer support neutrals

### Editorial / cultural / creative
Use more personality than product UI, but keep hierarchy clear.
Good fits:
- stronger hue relationships
- richer warm or cool neutrals
- palette should still be mapped by role if it touches interface behavior

### Data visualization
Choose the palette type by data logic:
- sequential for ordered magnitude
- diverging for values around a meaningful midpoint
- categorical for unrelated categories
Do not use rainbow scales for ordered data.

## Semantic role model
### Minimum digital roles
- `text/default`
- `text/subtle`
- `surface/base`
- `surface/raised`
- `border/default`
- `action/primary`
- `action/secondary`
- `focus`
- `success`
- `warning`
- `danger`
- `info`

### Recommended extended roles
- `chart/sequential`
- `chart/diverging`
- `chart/categorical`
- `brand/expressive`
- `brand/interface-safe`
- `overlay`
- `disabled`
- `selection`

## State logic
Use one of these models explicitly:
### Value-shift model
- hover: adjacent stronger or weaker step
- active: one more step in the same direction
- disabled: reduced contrast / muted neutral role

### Alpha-overlay model
Best for layered components and shared hue systems.
- hover: overlay token
- active: stronger overlay token
- pressed: highest overlay token
- keep overlays theme-aware

### Mutable-token model
Use when a role maps to different primitives by theme.
- panel background can map to white in light mode and a subtle neutral in dark mode
- overlay and shadow tokens must be theme-specific, not blindly inverted

## Data-visualization rules
- sequential palettes should move clearly in lightness/chroma for magnitude
- diverging palettes need a meaningful midpoint and equalized visual weight on both sides
- categorical sequences should maximize neighbor differentiation
- gradients are not substitutes for sequential or diverging logic
- alert palettes are separate from general chart categories

## Dark-mode rules
- avoid pure white on pure black for long reading
- soften bright text and lift dark surfaces
- map saturated colors symmetrically or intentionally, not by simple inversion
- audit focus, disabled, and border contrast separately from body text

## Best-in-class references
- **USWDS** for role-based government token logic and grade-based palette structure
- **GOV.UK** for functional color discipline and system-level maintainability
- **Radix Colors** for 12-step scales, semantic aliasing, and neutral swapping
- **Primer** for role-based semantic colors across multiple themes
- **Atlassian** for theme-aware tokens, alpha colors, and light/dark symmetry
- **Carbon** for categorical, sequential, diverging, and alert data-vis palette logic
- **Material 3** for paired container/on-color role thinking
- **Tailwind CSS v4** for OKLCH-based palette primitives and broad utility coverage

## Retrieval logic
When comparing or suggesting alternatives, use these vectors:
- domain fit
- neutral bias: slate, zinc, stone, mauve, olive, warm gray
- chroma budget
- contrast posture: restrained, safe, expressive
- device behavior: OLED-first, desktop-neutral, glare-heavy operational
- implementation model: tokenized, utility-first, semantic aliasing, brand-locked

## Pruning rules
Reject or downgrade systems that:
- fail AA on critical text roles without a justified niche role
- rely on color alone for status or hierarchy
- use vibrating high-chroma pairs in normal UI
- overload dense dashboards with too many accents
- duplicate an existing system without a real semantic or domain difference
- work only as moodboards, not as tokenized systems

## Handoff notes
- use `PANTONE_LIBRARY` only when the task becomes explicitly print-aware
- hand off to typography when weight, size, or reading density changes the real contrast outcome
- hand off to dashboard rules when charts or dense numeric interfaces dominate
