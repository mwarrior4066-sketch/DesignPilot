# Component State Matrix Template

Use this when a component needs explicit state behavior. Do not leave states implied.

## Component
- name:
- purpose:
- primary action:
- critical or non-critical:

## States
| State | Visual cue | Interaction rule | Accessibility rule | Token / variable hook |
|---|---|---|---|---|
| Rest |  |  |  |  |
| Hover |  |  |  |  |
| Focus-visible |  |  | 3:1 non-text contrast minimum |  |
| Active / Pressed |  |  |  |  |
| Disabled |  |  | cannot be the only state distinction by color |  |
| Loading |  |  | announce or indicate progress when needed |  |
| Error |  |  | not color-only |  |
| Success |  |  |  |  |

## Keyboard and motion
- Tab order:
- Enter / Space behavior:
- escape / dismissal behavior:
- reduced-motion behavior:

## Example output
### Component
- name: Primary async submit button
- purpose: commit a validated settings change and start a server-side save action
- primary action: Save policy changes
- critical or non-critical: critical

### States
| State | Visual cue | Interaction rule | Accessibility rule | Token / variable hook |
|---|---|---|---|---|
| Rest | Blue fill, white label, subtle shadow | Click/tap enabled when form is valid | Text contrast must pass 4.5:1 | `color.action.primary`, `shadow.button.rest` |
| Hover | Slightly darker blue, shadow lift | Mouse hover only | Hover cannot be the sole cue of interactivity | `color.action.primary.hover` |
| Focus-visible | 2px outer ring + 1px inner border | Keyboard focus retained until move/submit | Focus indicator must meet 3:1 non-text contrast | `color.focus.ring`, `border.focus.inner` |
| Active / Pressed | Darker fill, shadow reduced | Fires action on pointer up / Enter / Space | Pressed state must remain visually distinct from hover | `color.action.primary.pressed` |
| Disabled | Desaturated fill, reduced shadow, stable label contrast | No action; removed from submit path when invalid | Cannot rely on color alone; pair with disabled cursor/text cue | `color.action.disabled`, `opacity.disabled` |
| Loading | Spinner + “Saving…” label, width preserved | Action locked until response or timeout | Progress must be perceivable without motion alone | `motion.spinner`, `label.loading` |
| Error | Red border/ring, optional inline message | Returns focus to button or associated error summary | Error cannot be color-only; include message and icon when needed | `color.status.error`, `icon.error` |
| Success | Green confirmation check + stable text | Button may collapse into success state briefly or reset | Success message must be readable and not motion-dependent | `color.status.success`, `icon.success` |

### Keyboard and motion
- Tab order: follows form order; button is last primary action in sequence
- Enter / Space behavior: both trigger submit when valid
- escape / dismissal behavior: not applicable to core submit itself; related modal confirmations must return focus to trigger
- reduced-motion behavior: spinner remains but avoids bounce/pulse; state changes use opacity/color not large movement
