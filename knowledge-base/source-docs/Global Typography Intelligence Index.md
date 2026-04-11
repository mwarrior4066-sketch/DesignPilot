<!-- Built from the uploaded Global Typography Intelligence Index and normalized against official type documentation current to April 11, 2026. -->

# Global Typography Intelligence Index for Production Design Systems

## 1. Why the pack needs a typography refresh
The pack already had typography summaries and a font library, but they leaned more on generalized pairings and role buckets than on current implementation constraints. The uploaded research correctly pushed toward a broader production model: script-aware selection, variable-font behavior, dashboard typography, accessibility-specific families, and implementation-safe deployment.

## 2. Current official anchors
### Inter
Inter remains a strong default workhorse for digital interfaces. The official project still positions it as a screen-first typeface designed for computer screens rather than a neutral print carryover.

### Geist
Vercel’s official Geist site now makes an important implementation distinction: npm and zip installs include the **full glyph set** and `font-feature-settings` support, while the easier Google Fonts path is partial. This matters enough to include directly in the pack’s handoff logic.

### IBM Plex
IBM’s current typeface documentation still makes Plex unusually strong for system work because it offers coherent Sans, Serif, Mono, and Condensed families, a broad language story, and official guidance on using Mono versus Sans in technical contexts.

### Atkinson Hyperlegible Next
The accessibility picture changed meaningfully in 2025 when Braille Institute expanded the Atkinson family with **Atkinson Hyperlegible Next** and **Atkinson Hyperlegible Mono**, seven weights, variable support, and over 150 languages. The pack should stop treating Atkinson as a niche four-style face.

### Noto
Noto remains the pack’s most important global script fallback system. Current Noto docs still emphasize that the collection covers more than 1,000 languages and over 150 writing systems and that CJK support must be loaded by script-specific family, not assumed from the base Latin family.

### Variable fonts in CSS
MDN’s current guidance is still that teams should prefer high-level CSS properties like `font-weight`, `font-stretch`, and `font-style`, and use low-level `font-variation-settings` only when those higher-level properties do not expose the axis cleanly.

## 3. Production selection model
A production typography decision should account for:
- role
- script coverage
- readability behavior at real sizes
- numeric/data features
- fallback quality
- licensing
- deployment format

This is broader than “what font looks right.”

## 4. Role buckets the pack should think in
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

## 5. Small-size behavior
For small UI text, the pack should prefer:
- open counters
- high or stable x-height
- enough weight at small sizes
- cleaner spacing
- explicit fallback stacks

This is more important than stylistic purity.

## 6. Dashboard and dense-data typography
Dashboards need more than a “clean sans.” The pack should specifically look for:
- tabular figures
- good distinction between 0/O and 1/l/I
- mono support for code or metric zones
- compact widths without crowding
- weight behavior that does not break interaction states

## 7. Variable-font behavior
Variable fonts are still a strong default when they reduce file count and improve control. But the pack should now be more precise:
- use variable fonts when they simplify the shipped family
- prefer high-level CSS axis controls first
- use low-level `font-variation-settings` only when needed
- define fallback behavior for environments where the chosen variable strategy is not viable

## 8. Localization and script-aware logic
### CJK
CJK work needs script-specific families like Noto Sans JP, Noto Sans SC, Noto Sans TC, Noto Sans KR, or Source Han equivalents. Mixed Latin and CJK typography often needs optical balancing rather than identical nominal sizing.

### Arabic
Arabic-supportive digital systems should start with families that actually solve shaping and RTL needs, such as Noto Sans Arabic, Noto Naskh Arabic, Cairo, or IBM Plex Sans Arabic. The pack should stop treating Arabic support as a footnote to Latin font choice.

### Global fallback stacks
Multilingual systems should define explicit script-aware fallback stacks instead of pretending one Latin face can carry global coverage.

## 9. Accessibility
The pack should keep Atkinson, Lexend, Luciole, and Andika as high-value accessibility options, but use them intentionally rather than ritualistically. The updated Atkinson family is now strong enough to appear in normal production decision trees, especially for low-vision or readable-dashboard contexts.

## 10. Pairing logic
Avoid pairing two fonts that do the same job. Real contrast usually comes from differences in:
- proportion
- rhythm
- width
- x-height
- serif/sans structure
- tonal character

## 11. Licensing and deployment
The pack should keep naming licensing risk explicitly.
Strong defaults:
- open-source first when the license is unclear
- native system face only when native deployment is acceptable
- name the cross-platform substitute if a native or commercial face is recommended

## 12. Resulting pack implications
This refresh means the pack should:
- check script coverage before tone when the system is multilingual
- treat Geist’s install paths differently depending on glyph/feature requirements
- treat Atkinson Hyperlegible Next and Mono as current, not legacy
- prefer explicit numeric/data feature checks for dashboards
- use variable-font guidance that reflects current CSS practice rather than treating `font-variation-settings` as the default hammer
