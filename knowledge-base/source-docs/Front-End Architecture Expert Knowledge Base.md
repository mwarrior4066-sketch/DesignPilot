# Front-End Architecture Expert Knowledge Base

## Executive framing
This source document captures the front-end architecture research for the v2.4.0 capability expansion. It treats front-end work as systems engineering rather than styling. The pack should use it when a request depends on rendering model, server and client boundaries, state ownership, mutation architecture, semantic element selection, accessibility behavior, or performance cost.

## Core principles
- UI is a formal state machine, not a pile of screenshots.
- Keep state as local as possible and move shared or server-derived state only when synchronization requires it.
- Prefer native semantics before custom roles. A role is a promise.
- Move client boundaries down the tree so Server Components, static rendering, and partial prerendering do most of the cheap work.
- Use explicit finite state models instead of independent boolean flags that create impossible states.
- Use React 19 Actions, `useActionState`, `useFormStatus`, and `useOptimistic` when mutations must stay recoverable.
- Treat hydration, bundle size, and rendering cost as first-class constraints.

## Decision surface
- Rendering model: static, dynamic, PPR, CSR, streaming / Suspense.
- State ownership: local, lifted, server-derived, or global only when truly necessary.
- Boundary placement: server vs client component responsibilities, Server Actions vs client mutations.
- Semantic structure: native element selection, table vs grid, dialog, form, button, nav.
- Composition: feature-based boundaries, slots, bounded contexts, and low coupling.
- Delivery: caching, revalidation, fallback UI, optimistic rollback, and degraded states.

## Validator-ready rules
- reject boolean-explosion state modeling when explicit finite states are required
- reject deep prop drilling when slot-based or bounded-context composition is more stable
- reject click-only interactivity when native or keyboard-complete controls are available
- reject client-heavy rendering when static, server, or PPR strategy would satisfy the request
- require semantic role justification when custom widgets exceed native HTML
