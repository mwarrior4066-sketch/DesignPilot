# Pantone Library

Use this library for **print-aware color selection** when Pantone, spot color, CMYK fallback risk, coated vs uncoated behavior, or premium print decisions matter.

This is the **operational library**, not the full research source.
For deeper rationale, use:
- `src/knowledge-base/summaries/pantone-production-summary.md`
- `src/knowledge-base/source-docs/Technical Reference Framework for Pantone Systems and Production-Aware Design Operations.md`
- `src/libraries/PANTONE_NUMBERS.json` for numerical lookup (hex, CMYK, RGB for all 574 U/C colors)

## Important truth conditions
- Pantone spot, CMYK, RGB, and Hex are **not interchangeable**.
- RGB and Hex values in this file are **approximations for digital coordination only**.
- CMYK values are **process-oriented approximations**, not guarantees.
- Coated and uncoated targets should be treated as **different visual targets**, not a single color with two finishes.
- Metallics and neons should generally be treated as **spot-only**.

Machine-readable companion: `PANTONE_LIBRARY.json` for fast lookup and low-token retrieval.
Use the JSON companion first for selection/indexing, then return to this markdown file only when nuance, caveats, or examples are needed.

## Use this library when
- the task is print-aware
- the user asks for Pantone references or brand print anchors
- a style guide needs Pantone + CMYK + digital approximation notes
- packaging, editorial print, posters, signage, or premium collateral are involved
- a digital palette needs a print-side note or a process-safe fallback

## Do not use this library as
- a claim that Hex equals Pantone truth
- a replacement for press profiling, ICC workflows, or real proofing
- a reason to guess an exact Pantone from a vague color word

## Decision rules
- choose by **use case + substrate + process**, not by hue alone
- keep Pantone as the print anchor when fidelity matters
- prefer **Extended Gamut / ECG** over standard CMYK when available for high-fidelity spot simulation
- if exact process simulation is weak, choose a nearby process-safer Pantone rather than faking precision
- if Delta E is expected to exceed ~3, warn clearly; if it exceeds ~5, treat the process approximation as a failure state
- use bright yellows, limes, and light golds very cautiously for small type

## Fallback hierarchy
1. Spot Pantone ink
2. ECG / 7-color process simulation
3. Lab*-to-process conversion using the house ICC profile
4. Process-safe adjacent Pantone substitute
5. RGB/Hex approximation with a clear warning that it is digital-only guidance

## Pairing and legibility rules
- pair `130 C`, `116 C`, and similar bright yellows with **black or near-black text**
- pair `186 C`, `2935 C`, and similarly deep saturated reds/blues with **white text**
- avoid small text in high-luminance golds and bright limes on white
- use deep neutrals for long-form reading and dense document systems
- treat metallics as accents, not running-text colors

## Entry schema
Each Pantone entry may include:
- `PMS`
- `Family`
- `Tone`
- `Use`
- `Hex (Approx)`
- `CMYK (Approx)`
- `Risk`
- `Notes`

## Quick selection matrix

### Institutional / finance / civic
- Conservative: `288 C`, `540 C`, `286 C`, `301 C`, `425 C`, `Cool Gray 11 C`
- Process-safer: `300 C`, `285 C`, `424 C`, `429 C`
- Premium restraint: `4515 C`, `7499 C`, `Black 6 C`

### Tech / software / dashboards
- Conservative: `286 C`, `300 C`, `2945 C`, `321 C`, `425 C`
- Process-safer: `300 C`, `285 C`, `279 C`, `427 C`
- High-impact: `2935 C`, `321 C`, `267 C`

### Healthcare / wellness / organic
- Conservative: `279 C`, `321 C`, `564 C`, `5807 C`
- Process-safer: `279 C`, `564 C`, `337 C`, `338 C`
- High-impact: `382 C`, `376 C` (only with strong contrast logic)

### Luxury / beauty / premium packaging
- Conservative: `Black 6 C`, `262 C`, `696 C`, `877 C`
- Premium: `871 C`, `10077 C`, `10412 C`, `267 C`, `262 C`
- Caution: metallics and neons require spot workflows; do not fake them in process print

### Food / beverage / youth energy
- Conservative: `186 C`, `1375 C`, `158 C`, `1235 C`
- High-impact: `485 C`, `Orange 021`, `165 C`, `116 C`
- Caution: very vivid oranges and limes often collapse or dull in CMYK

## Expanded family pools

### Blues and navies - trust, institutional clarity, process stability
| PMS | Family | Tone | Use | Hex (Approx) | CMYK (Approx) | Risk | Notes |
|---|---|---|---|---|---|---|---|
| 288 C | Blue | Heritage | Institutional | #002D72 | 100,80,6,32 | Low | Strong heritage and corporate anchor |
| 540 C | Navy | Authoritative | Corporate | #003057 | 100,57,12,66 | Low | Stable dark brand anchor |
| 286 C | Royal | Trustworthy | Finance/Tech | #0033A0 | 100,66,0,2 | Low | Classic corporate blue |
| 2935 C | Blue | Vivid | Software/UI | #0056BD | 100,46,0,0 | Medium | Use white text only |
| 300 C | Blue | Professional | Civic | #005EB8 | 100,44,0,0 | Low | Strong process stability |
| 285 C | Azure | Contemporary | Tech | #0072CE | 89,43,0,0 | Medium | Good digital bridge blue |
| 279 C | Sky | Calm | Healthcare | #418FDE | 68,34,0,0 | Low | Good for clean health systems |
| 284 C | Blue | Youthful | Education | #6CACE4 | 56,18,0,0 | Low | Lighter educational tone |
| 646 C | Slate | Restrained | Editorial | #5E8AB4 | 60,30,10,10 | Low | Muted editorial blue |
| 2945 C | Blue | Stable | Industrial | #004C97 | 100,53,2,16 | Low | Reliable large fills |
| 280 C | Blue | Traditional | Military | #012169 | 100,78,0,54 | Low | Deep formal blue |
| 281 C | Blue | Royal | Traditional | #00205B | 100,72,0,32 | Low | Tight royal navy |
| 282 C | Blue | Dark | Classic | #041E42 | 100,68,0,54 | Low | Strong classic navy |
| 287 C | Blue | Deep | Corporate | #003087 | 100,69,0,11 | Low | Good enterprise anchor |
| 289 C | Navy | Deepest | Formal | #0C2340 | 100,60,10,50 | Low | Very dark formal navy |
| 299 C | Blue | Sky | Health | #00A3E0 | 85,19,0,0 | Low | Clean bright health/tech blue |
| 301 C | Blue | Classic | Government | #004B87 | 100,45,0,18 | Low | Institutional stability |
| 302 C | Blue | Dark | Technical | #003B5C | 100,48,12,58 | Low | Strong industrial blue |
| 3025 C | Blue | Summer Night | Entertainment | #005172 | 100,24,11,52 | Low | Softer deep-blue alternative |
| 5415 C | Blue | Soft Slate | Editorial/Institutional | #567B8A | 57,23,10,31 | Low | Restrained muted blue |
| 7455 C | Blue | Bold | Tech | #5279BC | 72,50,0,0 | Medium | Better for large areas than tiny text |

### Greens and teals - wellness, eco, organic, process caution
| PMS | Family | Tone | Use | Hex (Approx) | CMYK (Approx) | Risk | Notes |
|---|---|---|---|---|---|---|---|
| 3425 C | Green | Organic | Premium F&B | #006747 | 100,10,69,44 | Low | Deep premium organic green |
| 356 C | Green | Heritage | Agriculture | #007A33 | 90,0,100,18 | Low | Stable strong brand green |
| 364 C | Green | Rugged | Outdoor | #4A7729 | 65,0,100,42 | Low | Good rugged natural tone |
| 321 C | Teal | Modern | Tech/Health | #008C95 | 100,0,37,10 | High | Risky in CMYK; strong teal anchor |
| 3278 C | Teal | Luxurious | Beauty | #008767 | 99,0,69,0 | High | Strong beauty packaging teal |
| 382 C | Lime | Vibrant | Safety/Youth | #C4D600 | 29,0,100,0 | Extreme | Spot-oriented; dangerous for small text |
| 2299 C | Green | Canopy | Wellness | #A4D233 | 38,0,94,0 | Medium | Good wellness accent |
| 564 C | Green | Mint | Skincare | #86C8BC | 43,0,23,0 | Low | Calm mint for wellness |
| 7483 C | Green | Deep | Traditional | #275E3D | 77,0,82,65 | Low | Good dark organic anchor |
| 376 C | Green | Energetic | Sustainable | #84BD00 | 50,0,100,0 | High | Better as accent or large block |
| 325 C | Teal | Electric | Modern | #64CCC9 | 54,0,20,0 | High | Use with caution in process print |
| 337 C | Green | Soft | Natural | #97D5CC | 40,0,23,0 | Low | Soft natural green |
| 338 C | Green | Fresh | Wellness | #7ECDC3 | 49,0,28,0 | Low | Good muted wellness companion |
| 339 C | Green | Emerald | Luxury | #00A389 | 100,0,60,3 | Low | Good for stronger emerald tone |
| 347 C | Green | Vivid | Sports | #009A44 | 100,0,86,3 | Low | Saturated but relatively stable |
| 355 C | Green | Pure | Safety | #009639 | 91,0,100,0 | Medium | Pair with white carefully |
| 5807 C | Green | Sage | Eco | #D8DCB1 | 15,5,40,0 | Low | Muted sage for wellness/editorial |

### Reds and oranges - urgency, appetite, energy
| PMS | Family | Tone | Use | Hex (Approx) | CMYK (Approx) | Risk | Notes |
|---|---|---|---|---|---|---|---|
| 485 C | Red | Stimulate | Fast Food | #DA291C | 0,95,100,0 | Medium | Classic appetite-driving red |
| 186 C | Red | Professional | Corporate | #C8102E | 0,100,81,4 | Low | Pair with white type |
| 1788 C | Red | Classic | CPG | #EE334E | 0,84,71,0 | Medium | Bright consumer red |
| Orange 021 | Orange | Playful | Retail | #FF5800 | 0,65,100,0 | High | Strong spot feel; process risk |
| 165 C | Orange | Energetic | Apparel | #FF6720 | 0,59,96,0 | High | Better with ECG than standard CMYK |
| 1375 C | Orange | Warm | Premium Food | #FF9E1B | 0,45,94,0 | Low | Great premium warm orange |
| 7417 C | Coral | Trendy | Fashion | #E04F39 | 0,82,82,0 | Medium | High digital mismatch risk |
| 187 C | Red | Luxurious | Wine/Dining | #A6192E | 7,100,82,26 | Low | Strong premium burgundy-red |
| 158 C | Orange | Spicy | Packaging | #E87722 | 0,61,97,0 | Medium | Safer muted orange |
| 200 C | Red | Dramatic | Entertainment | #BA0C2F | 0,100,63,12 | Low | Strong high-contrast red |
| 173 C | Red | Warm | Accents | #CF4520 | 0,82,94,2 | Low | Good warm red-orange |
| 185 C | Red | Vivid | Modern | #E4002B | 0,91,76,0 | Medium | Common modern red |
| 188 C | Maroon | Regal | Premium | #6A202B | 16,100,65,58 | Low | Deep luxury red |
| 1495 C | Orange | Soft | Wellness | #FF8F1C | 0,50,85,0 | Low | Soft sunny orange |
| 151 C | Orange | Vivid | Youth | #FF8200 | 0,51,100,0 | High | Strong youth energy |
| 130 C | Yellow-Orange | Safety | Packaging | #F2A900 | 0,32,100,0 | Medium | Use with black text only |

### Yellows and warm golds - clarity, energy, legibility caution
| PMS | Family | Tone | Use | Hex (Approx) | CMYK (Approx) | Risk | Notes |
|---|---|---|---|---|---|---|---|
| 116 C | Yellow | Vibrant | Modern | #FFCD00 | 0,14,100,0 | Medium | Strong brand yellow |
| 109 C | Yellow | Happy | Retail | #FFD100 | 0,9,100,0 | Low | Youthful and bright |
| 107 C | Yellow | Classic | F&B | #FBE122 | 0,0,92,0 | Low | Clean warm yellow |
| 1235 C | Yellow | Warm | Consumer | #FFB81C | 0,31,98,0 | Low | Strong warm yellow |
| 130 C | Yellow | Vivid | Safety | #F2A900 | 0,32,100,0 | Medium | Keep black text only |
| 100 C | Yellow | Pale | Minimalist | #F6EB61 | 0,0,56,0 | Low | Soft near-white yellow |
| 124 C | Yellow | Vivid | Power | #EAAA00 | 0,30,100,0 | Medium | Strong deeper gold |
| 4515 C | Tan-Gold | Restrained | Institutional | #B3A369 | 13,19,62,28 | Medium | Good print anchor, risky on white for small digital text |
| 7499 C | Ivory | Classic | Editorial | #F1E6B2 | 1,1,10,1 | Low | Soft premium light tone |

### Neutrals, grays, blacks - restraint, systems, dense reading
| PMS | Family | Tone | Use | Hex (Approx) | CMYK (Approx) | Risk | Notes |
|---|---|---|---|---|---|---|---|
| Cool Gray 1 C | Gray | Clinical | Minimalist | #D9D9D6 | 0,0,0,6 | Low | Near-white fill |
| Cool Gray 8 C | Gray | Technical | Industrial | #888B8D | 0,0,0,45 | Low | Stable process gray |
| Cool Gray 11 C | Gray | Authoritative | Tech | #53565A | 44,34,22,77 | Low | Strong technical dark |
| Warm Gray 1 C | Neutral | Organic | Eco-Luxury | #D7D2CB | 3,3,6,7 | Low | Soft tactile neutral |
| Warm Gray 9 C | Neutral | Heritage | Architecture | #756E65 | 45,40,45,15 | Low | Warmer dark neutral |
| 425 C | Gray | Conservative | Corporate | #54585A | 48,29,26,76 | Low | Excellent corporate dark gray |
| Black 6 C | Black | Powerful | Luxury | #111111 | 100,79,44,93 | Low | Richer than plain black |
| 427 C | Gray | Clean | Clinical | #D0D3D4 | 9,4,10,8 | Low | Great for lines and UI borders |
| 424 C | Gray | Authority | Corporate | #707372 | 34,26,31,54 | Low | Stable mid-dark gray |
| 432 C | Black-Gray | Formal | Power | #333F48 | 65,43,26,78 | Low | Deep structured dark |
| 433 C | Black | Near-black | Formal | #1D252D | 90,68,41,90 | Low | Strong premium black |

### Purples, plums, magentas - luxury, fashion, creative intensity
| PMS | Family | Tone | Use | Hex (Approx) | CMYK (Approx) | Risk | Notes |
|---|---|---|---|---|---|---|---|
| 267 C | Purple | Regal | Luxury | #5F249F | 81,99,0,0 | High | Strong saturated purple |
| 262 C | Plum | Dramatic | Fashion | #51284F | 58,92,12,54 | Low | Stable luxury plum |
| 219 C | Magenta | Vibrant | Youth | #E4007C | 0,97,44,13 | High | High-risk vivid magenta |
| 696 C | Rose | Soft | Cosmetics | #A14A62 | 0,54,39,37 | Low | Good restrained luxury rose |
| 226 C | Pink | Vivid | Retail | #D0006F | 0,100,48,20 | High | Strong magenta-pink |
| 255 C | Violet | Deep | Spiritual | #6A2A5B | 52,100,0,32 | Medium | Rich deep violet |
| 666 C | Lavender | Calm | Wellness | #9E8FB0 | 36,39,2,5 | Low | Soft calm lavender |
| 2725 C | Blue-Violet | Playful | Tech Accent | #776CB1 | 65,65,0,0 | High | Often shifts blue in process |
| 7655 C | Orchid | Creative | Arts | #A45C98 | 33,72,0,0 | Medium | Good artistic orchid |
| 228 C | Berry | Premium | F&B Pack | #8D1D58 | 40,100,40,18 | Low | Strong premium berry |

### Browns, sands, warm naturals - heritage, eco-luxury, editorial warmth
| PMS | Family | Tone | Use | Hex (Approx) | CMYK (Approx) | Risk | Notes |
|---|---|---|---|---|---|---|---|
| 4625 C | Brown | Deep | Sustainable | #4F2C1D | 30,72,74,80 | Low | Strong deep brown |
| 7586 C | Brown | Warm | Eco-Luxury | #964F2E | 0,69,89,41 | Low | Warm premium brown |
| 7407 C | Sand | Neutral | Heritage | #CBA052 | 6,36,79,12 | Low | Good heritage sand |
| 7527 C | Neutral | Cedar | Organic | #DAD7CB | 3,4,14,8 | Low | Excellent muted neutral |
| 457 C | Ochre | Heritage | Traditional | #AD9001 | 6,23,97,26 | Low | Warm heritage ochre |
| 705 C | Champagne | Elegant | High-end | #FAF1DC | 0,4,12,2 | Low | Soft premium light tone |
| 4545 C | Tan | Sandy | Wellness | #E6D9BD | 5,10,30,0 | Low | Good soft tan |

### Metallics and neons - spot-only accents
| PMS | Family | Tone | Use | Hex (Approx) | CMYK (Approx) | Risk | Notes |
|---|---|---|---|---|---|---|---|
| 871 C | Gold | Wealth | Luxury | #84754E | 40,45,80,5 | Extreme | Spot ink required |
| 10077 C | Silver | Modern | Packaging | #8A8D8F | 45,35,35,10 | Extreme | Packaging metallic, durable/coatable |
| 10412 C | Rose Gold | Elegant | Beauty | #B76E79 | 25,55,45,0 | Extreme | Packaging metallic, durable/coatable |
| 877 C | Silver | Technical | Industrial | #8A8D8F | 45,35,35,1 | Extreme | Commercial metallic silver |
| 801 C | Neon Blue | Electric | Safety | #0093D3 | N/A | Total | Fluorescent, do not simulate as process truth |
| 802 C | Neon Green | Alert | Safety | #44D62C | N/A | Total | Spot-only neon green |
| 804 C | Neon Orange | Impact | Sports | #FF585D | N/A | Total | Spot-only neon orange |
| 806 C | Neon Pink | Bold | Fashion | #FF33CC | N/A | Total | Spot-only neon pink |
| 9020 C | Pastel Yellow | Soft | Baby/Wellness | #FCEA76 | 0,0,56,0 | Low | Good chromatic pastel |
| 9140 C | Pastel Green | Airy | Wellness | #A7D08C | 20,0,30,0 | Low | Gentle pastel green |

## Process-safe substitutions and warnings
- If `321 C`, `3278 C`, `382 C`, `376 C`, `Orange 021`, neon colors, or metallics are required in process-only printing, warn that exact fidelity is unlikely.
- For identity-critical print jobs, prefer a **Pantone-first, digital-approximation-second** rule.
- For PDFs and office-print workflows, fall back to stable dark blues, restrained greens, and process-safe neutrals instead of extreme metallic/neon/vivid options.
- If the brief needs a gold on digital white, use a darker digital companion rather than the print anchor itself.

## Common safe companion colors
- `425 C` / `Cool Gray 11 C` for dense UI or document text
- `427 C` / `Cool Gray 1 C` for lines, fills, dividers, and restrained backgrounds
- `Black 6 C` for premium dark anchors
- `7499 C`, `7527 C`, and `705 C` for soft premium light surfaces

## Missing-color rule
If the exact Pantone is missing here:
- check `src/libraries/PANTONE_NUMBERS.json` for numerical values across all 574 U/C colors
- prefer a nearby family substitute with lower process risk
- state clearly when the result is approximate
- do not invent an exact Pantone mapping from a vague digital color alone
