# Accessible Component Behavior Deep Dive

## Executive framing
This source document deepens the existing accessibility domain for the DesignPilot expansion. It shifts the pack from accessibility as surface feedback into accessibility as sequential, behavior-first interaction logic.

## Why this document matters
A large percentage of accessibility failures do not come from missing labels alone. They come from broken interaction models:
- focus disappears or lands unpredictably
- keyboard flow diverges from visual flow
- composite widgets expose states inconsistently
- async updates never get announced
- custom UI patterns overpromise what they can support

This document exists to make component behavior a first-class accessibility concern rather than a checklist afterthought.

## Core principles
- Native first. No ARIA is better than bad ARIA.
- Focus is the primary interaction pointer for keyboard and assistive-technology users.
- Composite widgets need explicit focus-management models such as roving tabindex or `aria-activedescendant`.
- Dialogs, tabs, listboxes, comboboxes, menus, and grids require exact keyboard manifests, focus entry and return rules, and state synchronization.
- Live regions must announce dynamic changes with correct politeness and initial DOM presence.
- Async states need `aria-busy`, status messaging, and announcement discipline.
- Reduced motion, flash limits, and touch-target sizing are implementation requirements.

## Decision surface
- Native vs custom widget justification
- Focus entry, trapping, restoration, and inert background control
- Manual vs automatic activation for tabs and other high-latency widgets
- Error association, `aria-describedby`, `aria-invalid`, alert or status behavior
- Grid navigation mode vs action mode
- Combobox input focus vs virtual option focus
- Motion-safe fallbacks and touch-target separation in dense enterprise UI

## Native versus custom
The first accessibility decision is whether the team should build the custom widget at all. Native elements already encode a large amount of accessibility behavior. Custom widgets are only justified when the interaction or visual requirements truly exceed what native HTML can support.

DesignPilot should therefore treat “custom interactive role” as a burden of proof. The design or implementation must name:
- why native behavior is insufficient
- what keyboard model will be used
- how focus is managed
- how state is announced
- how disabled, loading, and error states behave

## Focus architecture
Focus must be designed as a system, not a byproduct.

Questions every complex component should answer:
- where does focus enter?
- what gets initial focus?
- how does the user move through the interactive surface?
- how does focus leave?
- where does focus return after dismissal or completion?
- what happens if async content appears or disappears while focus is inside the component?

A missing answer to any of these questions is usually a serious accessibility risk.

## Composite widgets
### Tabs
Tabs require a clear relationship between tablist, tabs, and tab panels. Automatic activation is acceptable only when latency is low enough that focus movement does not feel trapped by content loading. When latency is non-trivial, manual activation is safer.

### Dialogs
Dialogs require focus trapping, inert or otherwise inactive background behavior, clear labelling, escape behavior, and focus restoration. A dialog that opens without a reliable first focus target is not ready.

### Listboxes and comboboxes
These patterns fail frequently because teams mix input focus, option focus, and visual selection states. The component must name whether focus remains in the input, moves through options, or is represented virtually.

### Grids
Grids need an explicit navigation model. Is the user in navigation mode or action mode? Are cells focusable, or are controls inside the cells focusable? A grid without a clear mode model is a likely failure point.

## Errors and validation
Accessible error handling requires:
- stable association between control and message
- visible error states that are not color-only
- clear timing for when errors appear
- live announcement only when needed
- preservation of user context rather than sudden focus jumps

## Async and live regions
Dynamic UI often fails because state changes are visible but silent. Good async accessibility requires:
- persistent live region containers in the DOM before updates
- appropriate politeness (`status` versus `alert` posture)
- `aria-busy` or similar state signaling where relevant
- messages that describe progress or completion meaningfully

## Dense interfaces
Enterprise dashboards and data-heavy tools often compress spacing and interactive zones until accessibility breaks. Touch targets, focus indicators, keyboard reachability, and visible state changes must remain intact under dense conditions.

## Motion and sensory safety
Animation is not neutral. Components should define:
- reduced-motion behavior
- non-motion fallback cues for state change
- flashing and rapid-transition safety
- clarity of state changes even with motion disabled

## Validator-ready rules
- custom interactive roles need tab reachability and keyboard handlers
- open dialogs must trap focus and restore it on close
- latency-sensitive tabs should use manual activation rather than automatic activation
- live regions must exist in the initial DOM before updates occur
- reject anti-patterns such as div-soup buttons, hover-only disclosure logic, silent loading, label overrides, and focus resets to page top

## Failure patterns
- custom widget chosen for styling convenience only
- focus enters but never returns meaningfully
- keyboard model differs from visual model without explanation
- loading state announced visually but not programmatically
- reduced-motion path strips out critical state feedback
- error state visible but not associated with the right field

## DesignPilot stance
This domain should push the pack to evaluate behavior over screenshots. A visually correct component that fails in focus, state, or announcement logic is not accessibility-complete.


## Review checklist for DesignPilot
When this source is active, the system should ask:
- What is the exact focus entry, movement, and exit model?
- Are keyboard behavior and visual behavior aligned?
- Which state changes need announcement and with what urgency?
- What happens under dense layout, motion reduction, or async loading?
- Is the component using native behavior where possible instead of custom interaction debt?

## Deliverable implications
This document should influence accessibility feedback, component specs, dashboard audits, and front-end review whenever interaction logic matters. A visually good component that fails its behavioral accessibility model should still be treated as incomplete.
