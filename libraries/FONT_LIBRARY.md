# Font Library

Use this library to choose, compare, substitute, and deploy typefaces by role, script coverage, readability, implementation risk, licensing, and fallback quality.
This is a lookup and fallback file, not the main behavior file.

Machine-readable companion: `FONT_LIBRARY.json` for fast lookup and low-token retrieval.
Use the JSON companion first for selection/indexing, then return to this markdown file when nuance, caveats, or implementation notes are needed.

## Use this library when
- the requested font is missing or unclear
- a pairing or fallback stack is needed
- script coverage or localization matters
- licensing or deployment constraints matter
- a premium face needs an open-source substitute
- tabular figures, mono support, or variable-font behavior matter
- the task needs a shortlist by medium, domain, or implementation profile

## Core rules
- preserve approved fonts first
- preserve role and structure before tone
- readability outranks expression by default
- choose by script support before style if the product is multilingual
- prefer a single variable family when it can cover the system cleanly
- prefer open-source families when licensing is unclear
- note substitutions instead of pretending nothing changed
- use native system stacks when performance and availability matter more than brand novelty
- avoid pairing two near-identical categories unless there is real x-height, width, rhythm, or tonal contrast

## Selection sequence
1. identify the role: UI, editorial, branding, dashboard, presentation, code, accessibility, multilingual
2. identify the script and region needs: Latin-only, CJK, Arabic, Cyrillic, multi-script, RTL
3. identify the delivery constraint: native, web, app, PDF, enterprise, open-source-only, premium allowed
4. identify the structural need: grotesk, humanist sans, geometric sans, serif, slab, mono, display
5. check the feature need: tabular figures, coding ligatures, variable axes, optical sizing, narrow widths, mono pair
6. choose the primary family
7. choose the fallback path
8. state licensing / implementation risks

## Role buckets
### UI and product sans
Inter, Geist Sans, Public Sans, IBM Plex Sans, Roboto Flex, Mona Sans, Open Sans, Work Sans, Figtree, DM Sans

### Humanist / approachable sans
Open Sans, Source Sans 3, Lato, IBM Plex Sans, Seravek, Ubuntu, Gill Sans Nova, DejaVu Sans

### Neutral / premium grotesks
Söhne, Akkurat, Graphik, Atlas Grotesk, Aktiv Grotesk, Basis Grotesk, Maison Neue, Neue Montreal, Univers, Akzidenz-Grotesk

### Geometric sans
Montserrat, Satoshi, Avenir Next, Futura PT / Futura Now, Gotham, Brown, Circular, Gilroy, Poppins

### Editorial serif workhorses
Charter, Source Serif 4, Merriweather, Georgia, Tiempos Text, Literata, Lora, Alegreya, Garamond, Baskerville

### Display serif / luxury / fashion
Editorial New, Tiempos Fine, GT Sectra, Canela, Ogg, Didot, Bodoni Moda, Austin, Signifier

### Technical and code
JetBrains Mono, IBM Plex Mono, Geist Mono, Noto Sans Mono, Source Code Pro, Cascadia Code, Fira Code, Menlo

### Accessibility-first
Atkinson Hyperlegible Next, Atkinson Hyperlegible Mono, Lexend, Andika, Luciole, FS Me, Tiresias

### Multilingual / global systems
Noto Sans, Noto Serif, Noto Sans Mono, Noto Sans CJK, Noto Serif CJK, Source Han Sans, Source Han Serif, IBM Plex Sans, Brill, Gentium Plus

### Arabic-supportive / RTL-safe starting points
Noto Sans Arabic, Noto Naskh Arabic, Cairo, IBM Plex Sans Arabic, 29LT Bukra when licensed

## Domain shortlists
### UI-safe shortlist
- Inter
- Geist Sans
- Public Sans
- IBM Plex Sans
- Roboto Flex
- SF Pro when native Apple is allowed

### Dashboard-safe shortlist
- Inter
- Geist Sans
- IBM Plex Sans
- Public Sans
- Roboto Flex
- JetBrains Mono / IBM Plex Mono / Geist Mono for code or metric zones

### Public-sector shortlist
- Public Sans
- Noto Sans
- IBM Plex Sans
- Source Sans 3
- Sarabun when the region/system demands it

### Editorial-safe shortlist
- Charter
- Source Serif 4
- Tiempos Text
- Literata
- Merriweather
- Georgia

### Branding-safe shortlist
- Söhne
- Akkurat
- Graphik
- Avenir Next
- GT Sectra
- Editorial New
- Canela

### Accessibility-safe shortlist
- Atkinson Hyperlegible Next
- Atkinson Hyperlegible Mono
- Lexend
- Luciole
- Andika

### Multilingual-safe shortlist
- Noto Sans
- Noto Serif
- Noto Sans CJK / Source Han Sans
- IBM Plex Sans
- Noto Sans Arabic / IBM Plex Sans Arabic / Cairo

## Feature filters
### Strong small-size UI behavior
Inter, Geist Sans, IBM Plex Sans, Public Sans, Open Sans, Roboto Flex

### Tabular figures and dense-data friendliness
Inter, IBM Plex Sans, Geist Sans, Roboto Flex, IBM Plex Mono, JetBrains Mono

### Variable-first families
Roboto Flex, Inter, Mona Sans, Atkinson Hyperlegible Next, Atkinson Hyperlegible Mono, Recursive, Cabinet Grotesk

### Developer / technical products
Geist Sans + Geist Mono, IBM Plex Sans + Plex Mono, Inter + JetBrains Mono, Mona Sans + Hubot Sans when brand expression matters

### Multiscript systems
Noto families, Source Han families, IBM Plex Sans, Brill

## Premium → open-source substitution matrix
| Premium / commercial | High-quality open-source substitute | Why it works |
|---|---|---|
| Helvetica / SF Pro | Inter / Public Sans / Roboto Flex | neo-grotesque neutrality and broad UI fit |
| Graphik / Suisse / Neue Montreal | Inter / Figtree / Archivo | neutral modern product behavior |
| Proxima Nova / Gotham | Montserrat / Work Sans / Figtree | geometric construction and wider public availability |
| Avenir / Frutiger | Lato / Open Sans / Nunito Sans | humanist softness and readability |
| Freight Text / Miller Text | Source Serif 4 / Literata / Merriweather | editorial readability and strong text color |
| Didot / Bodoni | Bodoni Moda / Playfair Display | high-contrast editorial feel with easier access |
| Whyte / Söhne Mono | IBM Plex Mono / JetBrains Mono / Geist Mono | technical clarity and implementation support |

## Family profiles
### Inter
- best for: product UI, dashboards, documentation
- strengths: screen-first design, open counters, wide ecosystem adoption
- caution: still name fallback stacks and tabular needs explicitly

### Geist Sans / Geist Mono
- best for: developer-facing products, docs, modern app UI
- strengths: tight developer/designer positioning, mono companion, easy Next.js/npm path
- caution: Google Fonts delivery is easier but does **not** include the full glyph set or font-feature-settings support that npm/zip installs provide

### IBM Plex Sans / Serif / Mono
- best for: enterprise systems, documentation, global products, code-heavy environments
- strengths: coherent multi-subfamily system, large language support, strong mono companion
- caution: brand voice is more technical than neutral-luxury

### Public Sans
- best for: public sector, civic tools, accessible neutral UI
- strengths: high clarity, institutional trust, open-source
- caution: less distinctive for expressive branding

### Atkinson Hyperlegible Next / Mono
- best for: accessibility-sensitive interfaces, readable UI, inclusive dashboards
- strengths: stronger letter distinction, 2025 expanded family, variable support, mono option
- caution: use when accessibility value is real; it is not a universal branding default

### Noto / Source Han families
- best for: multilingual and multiscript systems
- strengths: script coverage, harmonious global fallback strategy, open licensing
- caution: do not load unnecessary script families on the web

### Editorial New / GT Sectra / Canela / Tiempos
- best for: prestige editorial and premium branding
- strengths: strong tone and hierarchy
- caution: pair with a quieter support face and name licensing constraints clearly

## Native system fallbacks
- Apple stack: `-apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", Arial, sans-serif`
- Windows stack: `"Segoe UI", Tahoma, Arial, sans-serif`
- Android / cross-platform fallback: `Roboto, "Noto Sans", Arial, sans-serif`
- Mono fallback: `"JetBrains Mono", "IBM Plex Mono", "SFMono-Regular", Menlo, Consolas, monospace`
- Global sans fallback: `"Noto Sans", "Inter", Arial, sans-serif`

## Licensing and deployment checks
- verify whether the face is open-source, commercial, proprietary system, or provider-restricted
- for brand systems, note whether the license must cover desktop, webfont, app embedding, broadcast, or social outputs
- if the font is only a native system face, name the nearest cross-platform substitute
- if performance matters, prefer one variable WOFF2 over many static files when the quality stays high
- if a family has separate script packages, only ship what the product actually uses

## Implementation notes
- default to WOFF2 for web delivery
- use `font-display: swap` unless blocking behavior is explicitly required
- preload only the primary UI/brand family and only the cuts that matter
- when variable fonts exist, prefer them for weight/width/opsz control and smaller request count
- use high-level CSS properties like `font-weight`, `font-stretch`, `font-style`, and `font-optical-sizing` before dropping to low-level `font-variation-settings`
- use `font-variation-settings` only when the axis you need is not otherwise exposed cleanly
- if GRAD exists, use it for dark-mode rendering adjustment before unrelated reflow-causing weight changes
- for dashboards, specify tabular figures when numbers must align

## Localization notes
- CJK systems usually need script-specific families like Noto Sans JP, Noto Sans SC, Noto Sans TC, Noto Sans KR, or Source Han equivalents
- mixed Latin + CJK typography often needs optical balancing, not just the same nominal size
- Arabic products need families with proper RTL and shaping support; start with Noto Sans Arabic, Noto Naskh Arabic, Cairo, or IBM Plex Sans Arabic
- multilingual systems should define script-aware fallback stacks explicitly

## Fallback logic
1. preserve role
2. preserve script coverage
3. preserve structure
4. preserve readability
5. preserve licensing fit
6. preserve tone if possible
7. name the substitution

## Default metrics
- body size starting point for digital UI: 16px minimum
- body leading: roughly 1.5x
- display leading: roughly 1.1x to 1.25x
- line length target: 45–75 CPL, with ~66 CPL as a strong default
- use optical sizing when supported
