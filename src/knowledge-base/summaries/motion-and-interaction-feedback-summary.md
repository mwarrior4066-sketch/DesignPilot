---
summary_version: 1.0.0
source_reference:
  - src/knowledge-base/source-docs/Motion and Interaction Feedback Expert Research.md
last_updated: 2026-04-13
synchronized: true
domain: motion-interaction
---

# Motion and Interaction Feedback Summary

## Animation purpose taxonomy

| Purpose | Required or optional | Must communicate | Failure mode |
|---|---|---|---|
| Orientation | Required on structural change | Spatial relationship and hierarchy between states | Teleportation: element appears/disappears without spatial trajectory |
| Feedback | Required on every interactive element | Action was registered; state changed | Timing failure: animation >100ms after input = perceived unresponsive |
| Status | Required when process >1 second | System is active; progress estimate if available | Orphaned spinner: animation continues after process dies |
| Guidance | Optional; required during onboarding | Priority and importance of next action | Attention hijacking: too frequent or aggressive; distracts from primary task |
| Expression | Optional; low-frequency moments only | Brand personality through physics and choreography | Performance bloat: decorative animations increase load time |

## Duration and easing thresholds

| Motion category | Duration min | Duration max | Easing function |
|---|---|---|---|
| Micro-interaction (press/select) | 70ms | 110ms | Ease-out |
| Micro-interaction (toggle/fade) | 100ms | 150ms | Ease-out |
| Transition (panel/modal entry) | 200ms | 300ms | Ease-out or spring |
| Transition (panel/modal exit) | 150ms | 250ms | Ease-in |
| Transition (route/view change) | 300ms | 400ms | Ease-in-out |
| Loading (spinner/loop) | 400ms | 500ms | Linear |
| Attention/guidance | 300ms | 500ms | Ease-in-out |

Failure at fast extreme (<70ms): motion is unperceived; user gets no feedback.
Failure at slow extreme (>500ms for standard interactions): perceived as system lag, not feedback.

Easing rules:
- Ease-out: elements entering the screen (starts fast, lands gently)
- Ease-in: elements leaving the screen (picks up momentum on exit)
- Ease-in-out: movements entirely within the viewport
- Linear: constant-state loops (spinners, progress bars)
- Spring: touch interactions requiring tactile feel

## Feedback latency tiers

| Latency | User perception | Required animation response |
|---|---|---|
| <100ms | Instantaneous | State change only; no loading indicator needed |
| 100ms–1s | Slight delay | Subtle feedback (button state, optimistic UI) |
| 1s–10s | System working | Loading indicator required; progress bar if estimable |
| >10s | Unacceptable wait | Progress bar + estimated time + cancel option required |

Optimistic UI rule: animate success state immediately for reversible, low-risk actions; roll back with clear error animation if the server rejects.
Rollback animation: must reverse the original animation direction to communicate failure.

## Reduced motion system

`prefers-reduced-motion: reduce` treatment:

| Animation type | Full motion | Reduced motion treatment |
|---|---|---|
| Entrance/exit transitions | Slide or scale | Opacity only (fade) or instant |
| Loading spinner | Rotating animation | Static indicator or opacity pulse |
| Attention guidance | Movement-based | Color or border highlight only |
| Route transition | Slide between views | Instant or cross-fade |
| Decorative/expression | Full choreography | Remove entirely |

Hard rule: the information contract of the animation must survive the reduced-motion treatment. If the animation communicated a spatial relationship (orientation), an opacity-only fallback breaks that contract - use an instant transition instead.

## State transition logic

Rules for animating UI state changes:
- Show/hide: fade + scale (entry ease-out, exit ease-in)
- Expand/collapse: height animation with ease-out; never clip or jump
- Selection: immediate state change + micro-interaction confirmation
- Focus: instant visual change; do not animate focus ring appearance
- Error: shake or color change within 100ms; do not animate error text in
- Loading → content: skeleton dissolves as content fades in simultaneously (prevents layout shift)
- Empty → populated: staggered entry for list items (30–50ms delay between items, max 5 items staggered)

Simultaneous transition rule: animate only one structural change at a time. If two panels must change, sequence them with a 50ms offset minimum.

## Loading patterns

| Latency | Pattern | When to use |
|---|---|---|
| <100ms | No indicator | Action is perceived as instant |
| 100ms–1s | Button loading state | Inline action; prevents double-submit |
| 1s–3s | Skeleton screen | Content-shaped load; prevents layout shift |
| 3s–10s | Progress bar | Estimable process; file upload, multi-step |
| >10s | Progress bar + cancel | Long process; user must be able to abort |

Skeleton screen fidelity rule: must match the loaded layout within one container width. Skeleton that bears no resemblance to the loaded content creates layout shift and erodes trust.

## Motion failure pattern catalogue

1. **Simultaneous competing animations**: two or more elements animate at the same time, splitting attention
2. **Missing exit animation**: overlay closes instantly with no exit; breaks spatial model
3. **Ease-in entrance**: new content enters slowly and accelerates - feels heavy and unresponsive
4. **Hover animation on every item in a dense list**: produces visual noise instead of feedback
5. **Orphaned spinner**: loading animation continues after the process has completed or failed
6. **Animation on every keystroke**: text input feedback animations cause performance degradation and distraction
7. **Reduced-motion override**: system ignores `prefers-reduced-motion` and plays full animations regardless
8. **Layout shift on skeleton resolution**: skeleton dimensions don't match loaded content; page reflows on load
9. **Duration mismatch across related components**: modal opens at 300ms but related backdrop animates at 600ms - inconsistent feel
10. **Decoration masking system status**: expression animation plays during a failed state, hiding the error from the user

## Handoff specification requirements

Every motion decision handed off to engineering must specify:
- Duration (ms)
- Easing function (CSS cubic-bezier or named keyword)
- Trigger condition (on mount, on hover, on state change)
- Reduced-motion alternative

Motion token naming convention:
- `motion-duration-micro`: 100ms
- `motion-duration-standard`: 250ms
- `motion-duration-complex`: 350ms
- `motion-easing-enter`: ease-out
- `motion-easing-exit`: ease-in
- `motion-easing-standard`: ease-in-out
