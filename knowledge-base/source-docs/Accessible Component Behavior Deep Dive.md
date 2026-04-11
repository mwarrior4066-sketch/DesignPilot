# Accessible Component Behavior Deep Dive

## Executive framing
This source document deepens the existing accessibility domain for the v2.4.0 expansion. It shifts the pack from accessibility as surface feedback into accessibility as sequential, behavior-first interaction logic.

## Core principles
- Native first. No ARIA is better than bad ARIA.
- Focus is the primary interaction pointer for keyboard and assistive-technology users.
- Composite widgets need explicit focus-management models such as roving tabindex or `aria-activedescendant`.
- Dialogs, tabs, listboxes, comboboxes, menus, and grids require exact keyboard manifests, focus entry and return rules, and state synchronization.
- Live regions must announce dynamic changes with correct politeness and initial DOM presence.
- Async states need `aria-busy`, status messaging, and announcement discipline.
- Reduced motion, flash limits, and touch-target sizing are implementation requirements.

## Decision surface
- Native vs custom widget justification.
- Focus entry, trapping, restoration, and inert background control.
- Manual vs automatic activation for tabs and other high-latency widgets.
- Error association, `aria-describedby`, `aria-invalid`, alert or status behavior.
- Grid navigation mode vs action mode.
- Combobox input focus vs virtual option focus.
- Motion-safe fallbacks and touch-target separation in dense enterprise UI.

## Validator-ready rules
- custom interactive roles need tab reachability and keyboard handlers
- open dialogs must trap focus and restore it on close
- latency-sensitive tabs should use manual activation rather than automatic activation
- live regions must exist in the initial DOM before updates occur
- reject anti-patterns such as div-soup buttons, hover-only disclosure logic, silent loading, label overrides, and focus resets to page top
