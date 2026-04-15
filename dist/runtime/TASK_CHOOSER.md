# TASK_CHOOSER

Use this file to pick the launcher that best matches the main job you need done.

Start with the user-level question, not the internal route:
- what are you trying to do
- what is the main failure, decision, or deliverable
- which launcher best fits that job

Use launcher-first startup whenever possible.

## UI and system structure

### Accessibility Feedback Audit
- Launcher: `dist/runtime/task_launchers/accessibility_feedback_audit.md`
- Default mode: lightweight
- Recommended profile on escalation: `dist/DEPLOY_UI.md`
- Best fit: Use when a user task is blocked or degraded by semantic, focus, keyboard, or announcement failures.

### Color System Specification
- Launcher: `dist/runtime/task_launchers/color_system_spec.md`
- Default mode: lightweight
- Recommended profile on escalation: `dist/DEPLOY_UI.md`
- Best fit: Use when the job is to define roles, tokens, and state behavior for color rather than pick nicer hues.

### Component Specification
- Launcher: `dist/runtime/task_launchers/component_spec.md`
- Default mode: lightweight
- Recommended profile on escalation: `dist/DEPLOY_UI.md`
- Best fit: Use when a reusable system component needs state-safe documentation.

### Dashboard Audit
- Launcher: `dist/runtime/task_launchers/dashboard_audit.md`
- Default mode: lightweight
- Recommended profile on escalation: `dist/DEPLOY_UI.md`
- Best fit: Use for KPI hierarchy and chart-logic evaluation, not generic screen cleanup.

### Front-End Implementation Review
- Launcher: `dist/runtime/task_launchers/frontend_implementation_review.md`
- Default mode: profile-only or full
- Recommended profile on escalation: `dist/DEPLOY_UI.md`
- Best fit: Use when the governing decision is front-end architecture rather than generic handoff or UI critique.

### Graphic Critique
- Launcher: `dist/runtime/task_launchers/graphic_critique.md`
- Default mode: lightweight
- Recommended profile on escalation: `dist/DEPLOY_BRAND.md`
- Best fit: Use when the key problem is focal structure, type/image balance, or distance legibility.

### Layout Reconstruction Plan
- Launcher: `dist/runtime/task_launchers/layout_reconstruction_plan.md`
- Default mode: profile-only or full
- Recommended profile on escalation: `dist/DEPLOY_UI.md`
- Best fit: Use when structure must be inferred from an existing artifact instead of redesigned from scratch.

### Type System Recommendation
- Launcher: `dist/runtime/task_launchers/type_system_recommendation.md`
- Default mode: lightweight
- Recommended profile on escalation: `dist/DEPLOY_UI.md`
- Best fit: Use when the job is to define a repeatable type system instead of suggest a single font.

### UI Structure Critique
- Launcher: `dist/runtime/task_launchers/ui_structure_critique.md`
- Default mode: lightweight
- Recommended profile on escalation: `dist/DEPLOY_UI.md`
- Best fit: Prefer this route when the user wants structural diagnosis before polish.


## Brand and communication

### Brand Positioning Pass
- Launcher: `dist/runtime/task_launchers/brand_positioning_pass.md`
- Default mode: lightweight
- Recommended profile on escalation: `dist/DEPLOY_BRAND.md`
- Best fit: Use when the system must decide who the brand is for and how it earns trust.

### Case Study Rewrite
- Launcher: `dist/runtime/task_launchers/case_study_rewrite.md`
- Default mode: lightweight
- Recommended profile on escalation: `dist/DEPLOY_BRAND.md`
- Best fit: Use when communication quality depends on narrative order and proof clarity, not just editing.

### Text Humanization Revision
- Launcher: `dist/runtime/task_launchers/text_humanization_revision.md`
- Default mode: lightweight
- Recommended profile on escalation: `dist/DEPLOY_BRAND.md`
- Best fit: Use when the governing need is prose-quality revision rather than structural rewriting or route-level diagnosis.


## Research and planning

### UX Research Gap Map
- Launcher: `dist/runtime/task_launchers/ux_research_gap_map.md`
- Default mode: lightweight
- Recommended profile on escalation: `dist/DEPLOY_BRAND.md`
- Best fit: Use when the answer must separate known evidence from assumptions and map the next studies.


## Other specialized routes

### API Reliability and Security Review
- Launcher: `dist/runtime/task_launchers/api_reliability_security_review.md`
- Default mode: profile-only or full
- Recommended profile on escalation: `dist/DEPLOY_UI.md`
- Best fit: Use when the governing decision is failure, retry, authorization, or resilience semantics for APIs or tools.

### Back-End Feasibility Review
- Launcher: `dist/runtime/task_launchers/backend_feasibility_review.md`
- Default mode: profile-only or full
- Recommended profile on escalation: `dist/DEPLOY_UI.md`
- Best fit: Reveal back-end implications before treating the request as visual-only.

### Back-End Architecture Spec
- Launcher: `dist/runtime/task_launchers/backend_architecture_spec.md`
- Default mode: profile-only or full
- Recommended profile on escalation: `dist/DEPLOY_UI.md`
- Best fit: Use when the governing decision is the structure of the backend system itself.

### PDF Remediation Plan
- Launcher: `dist/runtime/task_launchers/pdf_remediation_plan.md`
- Default mode: profile-only or full
- Recommended profile on escalation: `dist/DEPLOY_UI.md`
- Best fit: Prioritize semantic preservation and verification over surface patching.
