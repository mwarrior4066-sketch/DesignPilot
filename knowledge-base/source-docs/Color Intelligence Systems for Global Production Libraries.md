<!-- Built from the uploaded Color Library Expansion Research Plan and normalized against official system documentation current to April 11, 2026. -->

# Color Intelligence Systems for Global Production Libraries

## 1. Why the pack needs a digital color library
The pack already had strong print-aware support through the Pantone library, but it lacked a dedicated digital color library for production UI systems. That gap made it harder to answer questions about semantic roles, themeable systems, data visualization, and domain-specific palette logic without jumping straight from high-level summary prose into print references.

A production color library should treat a palette system as more than a list of swatches. It should capture neutral strategy, semantic role mapping, accessibility posture, state logic, light/dark behavior, and misuse warnings. The uploaded research was directionally right on this point, and the refresh keeps that structure while tightening it around official system documentation.

## 2. Distinct-system counting
A distinct system is not just a hue shift. Count a new system only when at least one of these changes in a meaningful way:
- neutral strategy
- semantic role mapping
- contrast posture
- operational environment
- data-mapping logic
- brand-expression vs interface-safety separation

Integrated light and dark themes should usually count as one system when they are intentionally paired.

## 3. Current official reference anchors
### Tailwind CSS v4
Tailwind’s current default palette is exposed as **11-step scales** and surfaced in **OKLCH** values in the official docs. This matters because it gives the pack a stronger default mental model for perceptual palette construction than a raw RGB-first workflow.

### Radix Colors
Radix remains one of the best references for **semantic aliasing**, **12-step scale thinking**, and **neutral swapping**. Its docs continue to show why teams should alias scale names into roles like accent, success, danger, and use-case aliases rather than hard-coding hue names everywhere.

### USWDS
USWDS still provides one of the cleanest official explanations of **theme tokens**, **state tokens**, and **grade-based color families**. The grade model is especially useful because it regularizes lightness across families instead of treating each hue as an isolated ladder.

### GOV.UK
GOV.UK remains a strong reference for **functional colors**, maintainability, and “use the system function, not copied hex values” discipline. Its 2026 releases also reinforce that current system colors and type scales are evolving together, not as independent decoration.

### Primer
Primer continues to show how semantic colors can be mapped across multiple themes with foreground, background, and border roles separated from raw primitives.

### Atlassian
Atlassian remains one of the clearest references for **role-based tokens**, **alpha colors**, and **light/dark symmetry**. Their current docs still explain theme-aware token mapping better than many systems that only publish hex ramps.

### Carbon
Carbon’s official data-vis palette guidance remains valuable because it distinguishes **categorical**, **sequential**, **diverging**, and **alert** palettes and explicitly explains why category sequences are ordered the way they are.

### Material 3
Material 3 remains useful for paired role thinking like `primary` / `on-primary` and `primary-container` / `on-primary-container`, which keeps contrast baked into the role model rather than bolted on after the fact.

## 4. Role-first palette construction
A production color system should define color by role before style. At minimum, the pack should think in terms of:
- text/default and text/subtle
- surface/base and surface/raised
- border/default
- action/primary and action/secondary
- focus
- info, success, warning, danger
- chart/categorical, chart/sequential, chart/diverging
- brand/expressive vs brand/interface-safe

This is the core shift from “palette picking” to “color architecture.”

## 5. State logic
The uploaded research was right to emphasize state intelligence. In practice the pack should support three state models:
### Value shift
Move one or two steps up/down a ramp for hover and active.

### Alpha overlays
Use theme-aware alpha tokens for hover, pressed, overlays, shadows, and layered surfaces.

### Mutable tokens
Map one semantic role to a different primitive in light and dark themes when that is the correct perceptual behavior.

## 6. Data visualization logic
The color library should explicitly separate:
- **categorical** palettes for unrelated categories
- **sequential** palettes for ordered magnitude
- **diverging** palettes for values around a meaningful midpoint
- **alert** palettes for status and operational messaging

The pack should block rainbow scales for ordered data unless the task is explicitly non-analytic or decorative.

## 7. Domain clusters the pack now needs to understand
The uploaded research identified the right missing zones. The strongest cluster model for the pack is:
- public sector / institutional
- enterprise SaaS / B2B
- fintech / security
- healthcare / wellness
- industrial HMI / SCADA / operations
- aviation / cockpit / glare-heavy operational
- AI / technical infrastructure
- luxury / premium
- editorial / cultural / creative
- data visualization

## 8. High-stakes domains
### Industrial HMI
Operational interfaces should treat color as a signal, not decoration. The default posture should be restrained neutrals with sparse alarm colors.

### Aviation / cockpit
Very small blue details on dark backgrounds can be visually weak for critical reading; the pack should not assume ordinary web palette logic transfers cleanly into cockpit-style interfaces.

### Healthcare
Healthcare splits into at least two different system types:
- clinical clarity systems
- wellness / comfort systems
The pack should not collapse these into one generic “medical blue” answer.

## 9. Accessibility posture
The pack should continue using WCAG as the baseline legal/compatibility floor, but for quality it should also keep perceptual reasoning in play.
Important persistent rules:
- 4.5:1 minimum for standard text
- 3:1 minimum for large text and non-text UI contrast when applicable
- avoid using color as the only carrier of state or meaning
- audit dark mode separately; do not assume a light-mode pass survives theme inversion

## 10. Dark mode
Dark mode is not simple inversion. Current official systems still converge on the same core ideas:
- avoid pure white on pure black for normal long reading
- lift dark surfaces rather than flattening them all to one value
- remap semantic roles by theme rather than copying the same hexes everywhere
- treat overlays, borders, and shadows as theme-aware tokens

## 11. OKLCH and perceptual structure
The uploaded research highlighted OKLCH, and that direction remains useful. The pack should not pretend every system needs OKLCH storage, but it should understand OKLCH as a strong working model for building more perceptually even ramps and for keeping semantic colors visually balanced across hues.

## 12. Quality pruning
The library should reject systems that:
- fail critical contrast without a very narrow niche role
- overload dashboards with accent color
- use vibrating high-chroma pairs in ordinary UI
- duplicate existing systems without a meaningful semantic or domain difference
- function only as moodboards and not as tokenized systems

## 13. Resulting pack implications
This refresh means the pack should:
- load a digital `COLOR_LIBRARY` before Pantone for most digital work
- ask which environment the palette is for before proposing colors
- separate brand color from interface color when semantics conflict
- distinguish chart logic from interface status logic
- distinguish public-sector, healthcare, HMI, AI, and luxury systems instead of treating all palettes as ordinary web UI
