# Front-End Architecture Expert Knowledge Base

## Executive framing
This source document captures the front-end architecture research for the DesignPilot expansion. It treats front-end work as systems engineering rather than styling. The pack should use it when a request depends on rendering model, server and client boundaries, state ownership, mutation architecture, semantic element selection, accessibility behavior, or performance cost.

## Problem statement
Front-end requests are often described visually but fail structurally. The common mistakes are:
- state modeled as scattered booleans instead of explicit finite states
- client logic placed too high in the tree
- semantic structure treated as a styling concern
- performance cost hidden behind convenience abstractions
- mutation flows designed without rollback, pending, or error behavior

This knowledge base exists so DesignPilot can evaluate the real implementation shape behind a front-end request.

## Core principles
- UI is a formal state machine, not a pile of screenshots.
- Keep state as local as possible and move shared or server-derived state only when synchronization requires it.
- Prefer native semantics before custom roles. A role is a promise.
- Move client boundaries down the tree so Server Components, static rendering, and partial prerendering do most of the cheap work.
- Use explicit finite state models instead of independent boolean flags that create impossible states.
- Use React 19 Actions, `useActionState`, `useFormStatus`, and `useOptimistic` when mutations must stay recoverable.
- Treat hydration, bundle size, and rendering cost as first-class constraints.

## Decision surface
- Rendering model: static, dynamic, PPR, CSR, streaming / Suspense
- State ownership: local, lifted, server-derived, or global only when truly necessary
- Boundary placement: server vs client component responsibilities, Server Actions vs client mutations
- Semantic structure: native element selection, table vs grid, dialog, form, button, nav
- Composition: feature-based boundaries, slots, bounded contexts, and low coupling
- Delivery: caching, revalidation, fallback UI, optimistic rollback, and degraded states

## Rendering model
A front-end plan should name how the UI is delivered. DesignPilot should distinguish between:
- static or mostly static rendering
- dynamic server rendering
- client-side rendering
- partial prerendering or streaming
- mixed models with explicit server/client boundaries

The right rendering strategy depends on freshness, personalization, interactivity, and performance posture.

## State ownership
State should stay as local as possible. Shared state is justified only when synchronization or multiple consumers actually require it. DesignPilot should flag:
- premature global stores
- duplicated server-derived state in the client
- impossible states created by unrelated boolean flags
- forms or filters with no clear ownership model

## Mutation architecture
Mutation paths need explicit pending, success, error, and rollback behavior. A front-end request that says “just save the form” is underdefined until it names:
- where the action runs
- how optimistic updates behave
- what the user sees while pending
- how failure recovers
- what state persists after an error

## Semantic structure
HTML element selection is not cosmetic. DesignPilot should evaluate whether the chosen structure actually matches the interaction model. Examples:
- table vs grid
- button vs div with click handler
- dialog vs generic overlay
- form with submit semantics vs custom assembled controls

## Boundary placement
Server/client boundaries should be intentional. A plan that pushes large trees client-side for convenience should be challenged when static or server rendering could do more work cheaply.

## Composition strategy
Healthy front-end architecture uses bounded contexts, stable interfaces, and feature-based composition. Warning signs include:
- deep prop drilling with no composition reason
- shared component shells that know too much about business state
- monolithic containers mixing unrelated concerns
- slots or boundaries omitted where they would reduce coupling

## Performance posture
Performance should be treated as an architectural decision surface. DesignPilot should require at least a minimal stance on:
- hydration cost
- bundle size
- render frequency
- fallback behavior under poor network conditions
- loading and error states

## Validator-ready rules
- reject boolean-explosion state modeling when explicit finite states are required
- reject deep prop drilling when slot-based or bounded-context composition is more stable
- reject click-only interactivity when native or keyboard-complete controls are available
- reject client-heavy rendering when static, server, or PPR strategy would satisfy the request
- require semantic role justification when custom widgets exceed native HTML

## Failure patterns
- beautiful component tree with no explicit state model
- form submission flow with no pending/error recovery
- custom widget chosen before native option was evaluated
- server/client boundary chosen by habit rather than data or interactivity needs
- over-shared global state introduced to solve a local problem

## DesignPilot stance
This knowledge base should push the pack to judge front-end work as architecture: state, boundaries, semantics, mutation safety, and performance. Styling quality alone is not enough.


## Review checklist for DesignPilot
When this knowledge base is active, the system should ask:
- What rendering model is implied by the feature’s freshness and personalization needs?
- Which state truly belongs on the client, and which should remain server-derived?
- Are pending, success, error, and rollback states fully described?
- Does the semantic structure match the interaction model?
- Is the chosen composition model likely to reduce or increase coupling over time?

## Deliverable implications
This document should materially shape front-end architecture review, component-spec work, dashboard audits, and UI structure critique whenever implementation realism matters. A response that talks about front-end quality only in terms of layout polish is underusing this knowledge base.
