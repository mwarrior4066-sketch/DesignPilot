# Color System Specification Example
Fixture: tests/fixtures/color-system-pass.prompt.md
Validation result: tests/evals/color-system-pass.eval.json

## Input Prompt
Create a semantic color system for a B2B scheduling product. The current palette mixes brand colors with status colors, success and active states are too close, and dark mode was bolted on late.

## Selected Route and Loaded Skills
- Route: `rt_color_system_spec`
- Task contract: `color_system_spec`
- Mode: REBUILD
- Phase: tokens
- Skills: `color-system-expert.md`, `accessibility-feedback-expert.md`
- Known tensions: brand expression vs semantic clarity, vividness vs contrast safety

## Final Output
### Role model
Stop treating the palette as the system. The system needs semantic roles first: surface, text, action, status, chart series, and border/support roles. Brand hue can still live inside the action role, but it should not also own success and active state meaning.

### Token map
- Create core tokens for neutral, brand, success, warning, danger, and info families.
- Create alias tokens for UI roles such as `surface/default`, `text/primary`, `action/primary`, `status/success`, and `status/danger`.
- Keep hover, focus, disabled, and selected as explicit state aliases rather than manual hex overrides.
- Deprecate direct palette references in product screens. The migration path is palette family -> alias token -> component state.

### Contrast and state rules
Use a measurable contrast floor for text pairings and state surfaces. Body text pairings should meet a 4.5:1 threshold or the APCA equivalent. Success and active cannot share the same family if the user has to interpret state quickly. The obvious alternative is to let brand green serve both meanings, but that preserves the current ambiguity. Instead, keep active tied to the action role and reserve success for outcome feedback with icon and label support so the system does not rely on color alone.

### Migration notes
Start with high-risk areas: buttons, banners, badges, and chart legend states. Map them to aliases first, then phase out one-off hex values. The tradeoff is a short-term token migration cost versus long-term consistency across light and dark themes. Consistency should win because dark mode is already revealing role drift.


- Migration note: keep chart roles separate from status roles so series meaning does not collapse into alert semantics.
- Verification note: spot-check high-risk token pairs in both light and dark themes before rollout.

## Why This Passed
- It defines semantic roles instead of giving a taste-only palette review.
- It uses token, alias, and state language that can survive implementation handoff.
- It names a contrast threshold and rejects a palette-only alternative.
- It gives a migration sequence rather than pretending a new palette can replace the system overnight.

## What Would Have Failed
- Recommending nicer colors with no role map.
- Letting one brand color carry active, success, and warning meaning.
- Calling the palette accessible without contrast or non-color rules.

## Revision Pass
The weak draft proposed a cleaner teal palette and brighter success green. The corrected version made role ownership explicit and turned the palette into token-backed behavior.
