# Global Typography Intelligence Index for Production Design Systems

<!-- Built from the uploaded Global Typography Intelligence Index and normalized against official type documentation current to April 11, 2026. -->

## Purpose
This source document expands the pack’s typography intelligence from general pairings into a production-aware system covering script support, variable-font behavior, dashboard typography, licensing, accessibility, and implementation-safe deployment.

## Why the pack needs a typography refresh
The pack already had typography summaries and a font library, but they leaned more on generalized pairings and role buckets than on current implementation constraints. The uploaded research correctly pushed toward a broader production model: script-aware selection, variable-font behavior, dashboard typography, accessibility-specific families, and implementation-safe deployment.

Typography in DesignPilot should therefore be treated as a systems decision, not just an aesthetic one.

## Current official anchors
### Inter
Inter remains a strong default workhorse for digital interfaces. The official project still positions it as a screen-first typeface designed for computer screens rather than a neutral print carryover.

### Geist
Vercel’s official Geist site makes an implementation distinction that matters operationally: npm and zip installs include the full glyph set and `font-feature-settings` support, while the easier Google Fonts path is partial.

### IBM Plex
IBM’s current typeface documentation still makes Plex unusually strong for system work because it offers coherent Sans, Serif, Mono, and Condensed families, a broad language story, and official guidance on technical versus interface usage.

### Atkinson Hyperlegible Next
The accessibility picture changed meaningfully when Braille Institute expanded the Atkinson family with Atkinson Hyperlegible Next and Atkinson Hyperlegible Mono, seven weights, variable support, and broad language coverage. The pack should stop treating Atkinson as a niche four-style face.

### Noto
Noto remains the pack’s most important global-script fallback system. The collection covers more than 1,000 languages and over 150 writing systems, but CJK support must be loaded by script-specific family rather than assumed from base Latin coverage.

### Variable fonts in CSS
Modern CSS guidance still points teams toward high-level properties like `font-weight`, `font-stretch`, and `font-style` first, with `font-variation-settings` reserved for axis control that cannot otherwise be expressed cleanly.

## Production selection model
A serious typography decision should account for:
- role
- script coverage
- readability behavior at real sizes
- numeric/data features
- fallback quality
- licensing
- deployment format
- performance cost
- variable-axis behavior

This is broader than “what font looks right.”

## Role buckets the pack should think in
### UI / product sans
Inter, Geist Sans, Public Sans, IBM Plex Sans, Roboto Flex, Open Sans

### Humanist / approachable sans
Open Sans, Source Sans 3, Lato, IBM Plex Sans

### Premium / neutral grotesks
Söhne, Akkurat, Graphik, Atlas Grotesk, Aktiv Grotesk

### Geometric sans
Avenir Next, Montserrat, Gotham, Brown, Circular, Poppins

### Editorial serif workhorses
Charter, Source Serif 4, Tiempos Text, Literata, Merriweather, Georgia

### Display / prestige serifs
Editorial New, GT Sectra, Canela, Ogg, Didot, Bodoni Moda, Tiempos Fine

### Technical and code
JetBrains Mono, IBM Plex Mono, Geist Mono, Cascadia Code, Source Code Pro

### Accessibility-first
Atkinson Hyperlegible Next, Atkinson Hyperlegible Mono, Lexend, Andika, Luciole

### Multilingual systems
Noto families, Source Han families, IBM Plex, Brill, Gentium Plus

## Small-size behavior
For small UI text, the pack should prefer:
- open counters
- stable x-height
- sufficient weight at small sizes
- clear spacing
- explicit fallback stacks

Small-size readability matters more than stylistic purity in dense interfaces.

## Dashboard and dense-data typography
Dashboards need more than a “clean sans.” The pack should explicitly look for:
- tabular figures
- clear distinction between 0/O and 1/l/I
- mono support for code or metric zones
- compact widths without crowding
- weight behavior that does not break interaction states
- fallback stacks that preserve numeric clarity

## Variable-font behavior
Variable fonts are a strong default when they reduce file count and improve control. But the pack should be precise:
- use variable fonts when they simplify the shipped family
- prefer high-level CSS axis controls first
- use low-level `font-variation-settings` only when needed
- define fallback behavior when the variable strategy is not viable
- verify whether the distribution path includes the needed glyph set and features

## Localization and script-aware logic
### CJK
CJK work needs script-specific families like Noto Sans JP, Noto Sans SC, Noto Sans TC, Noto Sans KR, or Source Han equivalents. Mixed Latin and CJK typography often needs optical balancing rather than identical nominal sizing.

### Arabic
Arabic-supportive systems should start with families that actually solve shaping and RTL needs, such as Noto Sans Arabic, Noto Naskh Arabic, Cairo, or IBM Plex Sans Arabic. Arabic support should not be treated as a footnote to a Latin-first decision.

### Global fallback stacks
Multilingual systems should define explicit script-aware fallback stacks instead of pretending one Latin face can carry global coverage.

## Accessibility
The pack should keep Atkinson, Lexend, Luciole, and Andika as high-value accessibility options, but use them intentionally rather than ritualistically. Readability-supportive faces should be tied to actual low-vision, dense-UI, or cognitive-load requirements.

## Pairing logic
Avoid pairing two fonts that do the same job. Real contrast usually comes from differences in:
- proportion
- rhythm
- width
- x-height
- serif/sans structure
- tonal character

A pair should divide labor clearly rather than duplicate mood.

## Licensing and deployment
The pack should keep naming licensing risk explicitly.

Strong defaults:
- open-source first when license is unclear
- native system face only when native deployment is acceptable
- name the cross-platform substitute if a native or commercial face is recommended
- distinguish between design exploration choices and shippable implementation choices

## Decision questions DesignPilot should ask
- What scripts does this product actually need to support?
- Does the typography need dense numeric clarity, narrative warmth, or both?
- Will the team ship via npm, bundled assets, CDN, or system fonts?
- Do the chosen fonts support the required figure styles and weights?
- Is accessibility a surface constraint or a core selection driver?

## DesignPilot stance
Typography should be evaluated as a production system: role, coverage, readability, fallback posture, and implementation method. The pack should not let “good taste” substitute for deployment reality.


## Review checklist for DesignPilot
Use this source to ask:
- What role does the type need to serve: UI, editorial, data, code, accessibility, or multilingual support?
- Does the chosen family actually cover the required scripts and figure behavior?
- What shipping path and licensing posture are assumed?
- Will the typography still work at dense UI sizes and under real fallback conditions?
- Is the recommendation based on implementation reality rather than naming prestige alone?

## Success conditions
This knowledge base succeeds when typography recommendations stop being generic mood advice and become production-aware decisions with explicit role, coverage, fallback, and deployment logic.
