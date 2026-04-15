# Motion and Interaction Feedback Runtime Summary

This is the operator-safe compiled mirror of a runtime summary.
Use it for quick runtime context. Escalate to a profile or `dist/DESIGNPILOT_DEPLOY.md` when deeper canonical evidence is needed.

## Decision rules
- micro-interactions (press/select): 70–110ms, ease-out
- micro-interactions (toggle/fade): 100–150ms, ease-out
- panel/modal entry: 200–300ms, ease-out or spring
- panel/modal exit: 150–250ms, ease-in
- route/view change: 300–400ms, ease-in-out
- loading loops: 400–500ms, linear
- fast failure: <70ms motion is unperceived (user receives no feedback)
- slow failure: >500ms for standard interactions = perceived system lag
- feedback animation must begin within 100ms of user input or the system feels unresponsive
- loading indicator required when latency exceeds 1 second
- skeleton screens preferred over spinners for content-shaped views
- prefers-reduced-motion must be respected: orientation → instant, decorative → remove
- one structural animation at a time; sequence concurrent changes with ≥50ms offset
- every motion decision in handoff must specify: duration, easing, trigger, reduced-motion alternative

## Failure traps
- simultaneous competing animations splitting attention
- missing exit animation breaking the spatial model
- ease-in entrance (slow start feels like lag, not polish)
- hover animation on every item in a dense list (noise, not feedback)
- orphaned spinner after process completion or failure
- ignoring prefers-reduced-motion
- skeleton layout doesn't match loaded content (causes layout shift on resolve)
- decorative expression animation playing during a failed state, masking the error

## Escalate when
- task involves WCAG SC 2.3.3 (animation from interactions) compliance
- animation is in a high-frequency interaction path and performance cost is uncertain
- reduced-motion treatment would break the information contract of the animation

## Deeper fallback
- `dist/DESIGNPILOT_DEPLOY.md` for full compiled authority
- `src/knowledge-base/source-docs/Motion and Interaction Feedback Expert Research.md` for full depth
