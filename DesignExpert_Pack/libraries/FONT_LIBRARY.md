# Font Library

Use this library to choose, compare, substitute, and deploy typefaces by role, tone, structure, licensing, accessibility, and implementation risk.
This is a lookup and fallback file, not the main behavior file.

Machine-readable companion: `FONT_LIBRARY.json` for fast lookup and low-token retrieval.
Use the JSON companion first for selection/indexing, then return to this markdown file only when nuance, caveats, or examples are needed.

## Use this library when
- the requested font is missing or unclear
- a pairing is needed
- a fallback stack is needed
- licensing or deployment constraints matter
- a premium face needs an open-source substitute
- a variable-font or system-stack substitute is required
- the task needs a shortlist by medium or use case

## Core rules
- preserve approved fonts first
- preserve role and structure before tone
- readability outranks expression by default
- prefer a single variable family when it can cover the system cleanly
- prefer open-source families when licensing is unclear
- note substitutions instead of pretending nothing changed
- use native system stacks when performance and availability matter more than brand novelty
- avoid pairing two near-identical categories unless there is real x-height, width, or tonal contrast

## Selection sequence
1. identify the role: UI, editorial, branding, dashboard, presentation, code, accessibility, multilingual
2. identify the delivery constraint: native, web, app, PDF, social, enterprise, open-source-only, premium allowed
3. identify the structural need: neutral, humanist, geometric, grotesk, serif, mono, display
4. choose the primary family
5. choose the fallback path
6. state licensing / implementation risks

## Role buckets
### UI and product sans
Inter, Roboto, Public Sans, IBM Plex Sans, Mona Sans, Open Sans, Work Sans, Figtree, DM Sans

### Humanist / approachable sans
Open Sans, Source Sans 3, Lato, Seravek, Ubuntu, Gill Sans Nova, DejaVu Sans

### Neutral / premium grotesks
Helvetica Now, Söhne, Aktiv Grotesk, Basis Grotesk, Maison Neue, Univers, Akzidenz-Grotesk, Neue Montreal

### Geometric sans
Montserrat, Satoshi, Avenir Next, Futura Now, Gotham, Brown, Circular, Gilroy

### Editorial serif workhorses
Charter, Source Serif 4, Merriweather, Georgia, Miller Text, Tinos, Lora, Alegreya

### Display serif / luxury / fashion
Tiempos Fine, Editorial New, Didot, Bodoni, GT Sectra, Prata, Migra, Austin

### Technical and code
JetBrains Mono, IBM Plex Mono, Noto Sans Mono, Whyte Mono, Cascadia Code, Source Code Pro, Menlo

### Accessibility-first
Atkinson Hyperlegible, Lexend, Andika, Luciole, FS Me, Tiresias

### Multilingual / global systems
Noto Sans, Noto Serif, Noto Sans Mono, IBM Plex Sans, Source Han Sans, Brill, Gentium Plus

## Use-case shortlists
### UI-safe shortlist
- Inter
- Roboto / Roboto Flex
- Public Sans
- IBM Plex Sans
- Open Sans
- SF Pro when native Apple is allowed

### Editorial-safe shortlist
- Charter
- Source Serif 4
- Merriweather
- Georgia
- Miller Text
- Tinos

### Branding-safe shortlist
- Söhne
- Aktiv Grotesk
- Avenir Next
- GT Sectra
- Didot
- Tiempos Fine
- Editorial New

### Dashboard-safe shortlist
- Inter
- Roboto
- Public Sans
- IBM Plex Sans
- Mona Sans
- JetBrains Mono / IBM Plex Mono for code or metric zones

### Presentation-safe shortlist
- Red Hat Display
- Montserrat Bold
- GT America
- GT Walsheim
- Archivo Black
- Anton for impact-only titles

### Accessibility-safe shortlist
- Atkinson Hyperlegible
- Lexend
- Luciole
- Andika
- FS Me

### Multilingual-safe shortlist
- Noto Sans
- Noto Serif
- IBM Plex Sans
- Source Han Sans
- Gentium Plus

## Premium → open-source substitution matrix
| Premium / commercial | High-quality open-source substitute | Why it works |
|---|---|---|
| Helvetica / SF Pro | Inter / Archivo / Roboto | neo-grotesque neutrality and broad UI fit |
| Proxima Nova / Gotham | Montserrat / Figtree / Work Sans | geometric construction and large apertures |
| Avenir / Frutiger | Lato / Nunito Sans / Open Sans | humanist softness and product readability |
| Graphik | Inter / Figtree / Archivo | neutral, modern, interface-safe substitutes |
| Arnhem / Freight Text | Source Serif 4 / Merriweather | editorial readability and strong text color |
| Times New Roman | Tinos / Source Serif 4 / Gelasio | transitional serif structure |
| Whyte / Söhne Mono | IBM Plex Mono / JetBrains Mono | technical clarity and implementation support |

## Native system fallbacks
- Apple stack: `-apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", Arial, sans-serif`
- Windows stack: `"Segoe UI", Tahoma, Arial, sans-serif`
- Android / cross-platform fallback: `Roboto, "Noto Sans", Arial, sans-serif`
- Monospace fallback: `"JetBrains Mono", "IBM Plex Mono", "SFMono-Regular", Menlo, Consolas, monospace`

## Licensing and deployment checks
- verify whether the face is open source, commercial, proprietary system, or restricted to a provider like Adobe Fonts
- for brand systems, note whether the license must cover desktop, webfont, app embedding, social, or broadcast
- if the user has no clear license, propose an open-source-safe path first
- if performance matters, prefer one variable WOFF2 over many static files when the quality stays high
- if the font is only a native system face, name the nearest cross-platform substitute

## Implementation notes
- default to WOFF2 for web delivery
- use `font-display: swap` unless blocking behavior is explicitly required
- preload only the primary brand/UI face and only the cuts that matter
- when variable fonts exist, prefer them for weight/width/opsz control and smaller request count
- use optical sizing when supported
- if GRAD exists, use it for dark-mode or rendering adjustment before unrelated reflow-causing weight changes

## Fallback logic
1. preserve role
2. preserve structure
3. preserve readability
4. preserve licensing fit
5. preserve tone if possible
6. name the substitution

## Default metrics
- body size starting point for digital UI: 16px minimum
- body leading: roughly 1.5x
- display leading: roughly 1.1x to 1.25x
- line length target: 45–75 CPL, with ~66 CPL as a strong default
- use optical sizing when supported
