---
runtime_card_version: 1.0.0
canonical_skill: src/skills/motion-interaction-expert.md
last_generated: 2026-04-11
overlay: true
---
# motion-interaction-expert.md

## Activation conditions
- the task involves transitions, animations, loading states, or skeleton screens
- the user is specifying feedback timing for interactive elements
- reduced-motion accessibility compliance is required
- motion decisions need to be handed off to engineering with full specifications
- a critique surfaces animation that feels laggy, jarring, or distracting
- the task is purely static layout with no motion implications
- the only motion concern is CSS hover color change with no timing complexity

## Non-activation conditions
- the task is purely static layout with no motion implications
- the only motion concern is CSS hover color change with no timing complexity

## Core decision rules
- micro-interactions (press/select): 70–110ms, ease-out
- micro-interactions (toggle/fade): 100–150ms, ease-out
- panel/modal entry: 200–300ms, ease-out or spring
- panel/modal exit: 150–250ms, ease-in
- route/view change: 300–400ms, ease-in-out
- loading loops: 400–500ms, linear
- below 70ms: motion is unperceived - user gets no feedback signal
- above 500ms for standard interactions: perceived as system lag, not feedback
- feedback animation must begin within 100ms of user input
- loading indicator required when latency exceeds 1 second

## Failure traps
- simultaneous competing animations splitting attention
- missing exit animation breaking spatial model
- ease-in entrance (slow start reads as lag, not polish)
- hover animation on every item in a dense list (noise, not feedback)
- orphaned spinner after process has completed or failed
- ignoring prefers-reduced-motion
- skeleton layout that doesn't match loaded content, causing layout shift on resolve
- decorative expression animation playing during a failed or error state, masking it

## Summary dependencies
- motion-and-interaction-feedback-summary.md
- Motion and Interaction Feedback Expert Research.md

## Escalation triggers
- crisis and monitoring interfaces may use persistent status animations that exceed 500ms if they are looping and clearly communicate live data
- onboarding guidance animations may be slightly longer (up to 600ms) if the motion communicates a gesture the user must learn
- spring physics may replace ease-out for touch-primary interfaces where tactile feel is a product requirement
- when duration is ambiguous, default to the lower bound of the range (faster feels more responsive)
- when easing is ambiguous for an entrance, default to ease-out
- when reduced-motion treatment breaks the information contract, use instant rather than simplified
- animation purpose classification
- duration and easing specified

## Adjacent handoff rules
- hand off to `accessibility-feedback-expert.md` for WCAG SC 2.3.3 and motion-safety compliance
- hand off to `front-end-handoff-expert.md` for implementation-safe token and CSS specification
- hand off to `ui-system-expert.md` when motion decisions require resolving the underlying state transition structure first

## Canonical fallback
- `src/skills/motion-interaction-expert.md`
- `src/knowledge-base/summaries/motion-and-interaction-feedback-summary.md`
- `src/knowledge-base/summaries/Motion and Interaction Feedback Expert Research.md`