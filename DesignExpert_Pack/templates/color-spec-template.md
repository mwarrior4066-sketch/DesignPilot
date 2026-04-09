# Color Spec Template

Use this when the task needs a real color system, not loose palette suggestions.

## Context
- medium:
- brand/system context:
- light mode / dark mode / both:
- print-aware: yes/no
- density/risk level:

## Role map
- text:
- surface:
- border:
- action:
- accent:
- success:
- warning:
- error:
- info:
- chart categories:

## Contrast targets
- body text:
- large text:
- non-text UI:
- APCA targets if used:

## Dark mode behavior
- surface shift:
- text shift:
- accent shift:
- state shift:

## Print notes
- RGB:
- CMYK:
- Pantone:
- known tradeoffs:

## Failure checks
- color-only meaning avoided:
- dark-mode halation checked:
- inaccessible brand colors reassigned or corrected:
- dense-data palette restrained:

## Example output
### Context
- medium: SaaS web app + investor deck
- brand/system context: enterprise asset governance platform
- light mode / dark mode / both: both
- print-aware: yes
- density/risk level: high-density UI, moderate brand expressiveness

### Role map
- text: neutral-950 / neutral-100 in dark mode
- surface: neutral-0, neutral-25, neutral-75; dark surfaces shift to neutral-950 / 900 / 850
- border: neutral-200 / neutral-700
- action: blue-600 primary, blue-500 hover, blue-700 pressed
- accent: teal-500 reserved for highlight metrics and selected data states
- success: green-700 / green-400
- warning: amber-700 / amber-400
- error: red-700 / red-400
- info: sky-700 / sky-400
- chart categories: blue, teal, violet, amber, coral with restrained saturation and label support

### Contrast targets
- body text: WCAG 4.5:1 minimum, target APCA Lc 75+
- large text: WCAG 3:1 minimum, target APCA Lc 60+
- non-text UI: 3:1 minimum for focus, key controls, and component boundaries
- APCA targets if used: body 75–80, labels 70+, headlines 60–65

### Dark mode behavior
- surface shift: avoid pure black; base on #121212 / #1A1A1A / #232323 ladder
- text shift: use softened light like #E8E8E8 instead of pure white for sustained reading
- accent shift: reduce saturation slightly in dark mode to avoid vibration
- state shift: success/warning/error hues become slightly lighter but less neon

### Print notes
- RGB: primary UI blue = #2563EB
- CMYK: convert by intended stock and process, do not assume exact parity
- Pantone: use Pantone only for identity-critical print moments, not routine UI specs
- known tradeoffs: screen teal loses subtlety in CMYK, warning amber needs separate print verification

### Failure checks
- color-only meaning avoided: yes, all alerts pair color with icon and text label
- dark-mode halation checked: yes, no pure white on pure black for long reading
- inaccessible brand colors reassigned or corrected: yes, brand cyan moved to accent-only use
- dense-data palette restrained: yes, chart colors capped and paired with direct labels
