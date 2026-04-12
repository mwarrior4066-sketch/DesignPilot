# Route Picker

Use this file to choose the right startup path without reading internal architecture.

Start broad, then narrow:
- first choose the task cluster that matches the job
- then choose the route inside that cluster
- then load the matching contract and only the needed skill cards

## UI and system structure

### Accessibility Feedback Audit
- Route card: `dist/lite_routes/rt_accessibility_feedback_audit.md`
- Contract card: `dist/lite_contracts/accessibility_feedback_audit.md`
- Starter pack: `dist/lite_starters/accessibility_feedback_audit.md`
- Use when: Use when a user task is blocked or degraded by semantic, focus, keyboard, or announcement failures.

### Color System Specification
- Route card: `dist/lite_routes/rt_color_system_spec.md`
- Contract card: `dist/lite_contracts/color_system_spec.md`
- Starter pack: `dist/lite_starters/color_system_spec.md`
- Use when: Use when the job is to define roles, tokens, and state behavior for color rather than pick nicer hues.

### Component Specification
- Route card: `dist/lite_routes/rt_component_spec.md`
- Contract card: `dist/lite_contracts/component_spec.md`
- Starter pack: `dist/lite_starters/component_spec.md`
- Use when: Use when a reusable system component needs state-safe documentation.

### Dashboard Audit
- Route card: `dist/lite_routes/rt_dashboard_audit.md`
- Contract card: `dist/lite_contracts/dashboard_audit.md`
- Starter pack: `dist/lite_starters/dashboard_audit.md`
- Use when: Use for KPI hierarchy and chart-logic evaluation, not generic screen cleanup.

### Graphic Critique
- Route card: `dist/lite_routes/rt_graphic_critique.md`
- Contract card: `dist/lite_contracts/graphic_critique.md`
- Starter pack: `dist/lite_starters/graphic_critique.md`
- Use when: Use when the key problem is focal structure, type/image balance, or distance legibility.

### Type System Recommendation
- Route card: `dist/lite_routes/rt_type_system_recommendation.md`
- Contract card: `dist/lite_contracts/type_system_recommendation.md`
- Starter pack: `dist/lite_starters/type_system_recommendation.md`
- Use when: Use when the job is to define a repeatable type system instead of suggest a single font.

### UI Structure Critique
- Route card: `dist/lite_routes/rt_ui_structure_critique.md`
- Contract card: `dist/lite_contracts/ui_structure_critique.md`
- Starter pack: `dist/lite_starters/ui_structure_critique.md`
- Use when: Prefer this route when the user wants structural diagnosis before polish.

## Brand and communication

### Brand Positioning Pass
- Route card: `dist/lite_routes/rt_brand_positioning.md`
- Contract card: `dist/lite_contracts/brand_positioning_pass.md`
- Starter pack: `dist/lite_starters/brand_positioning_pass.md`
- Use when: Use when the system must decide who the brand is for and how it earns trust.

### Case Study Rewrite
- Route card: `dist/lite_routes/rt_case_study_rewrite.md`
- Contract card: `dist/lite_contracts/case_study_rewrite.md`
- Starter pack: `dist/lite_starters/case_study_rewrite.md`
- Use when: Use when communication quality depends on narrative order and proof clarity, not just editing.

### Text Humanization Revision
- Route card: `dist/lite_routes/rt_text_humanization.md`
- Contract card: `dist/lite_contracts/text_humanization_revision.md`
- Starter pack: `dist/lite_starters/text_humanization_revision.md`
- Use when: Use when the governing need is prose-quality revision rather than structural rewriting or route-level diagnosis.

## Research and planning

### UX Research Gap Map
- Route card: `dist/lite_routes/rt_ux_research_gap_map.md`
- Contract card: `dist/lite_contracts/ux_research_gap_map.md`
- Starter pack: `dist/lite_starters/ux_research_gap_map.md`
- Use when: Use when the answer must separate known evidence from assumptions and map the next studies.

## Routes that should usually escalate

### API Reliability and Security Review
- Recommended startup: `dist/DEPLOY_UI.md` or full kernel
- Route card: `dist/lite_routes/rt_api_reliability_security.md`
- Use when: Use when the governing decision is failure, retry, authorization, or resilience semantics for APIs or tools.

### Back-End Feasibility Review
- Recommended startup: `dist/DEPLOY_UI.md` or full kernel
- Route card: `dist/lite_routes/rt_backend_feasibility.md`
- Use when: Reveal back-end implications before treating the request as visual-only.

### Back-End Architecture Spec
- Recommended startup: `dist/DEPLOY_UI.md` or full kernel
- Route card: `dist/lite_routes/rt_backend_systems_architecture.md`
- Use when: Use when the governing decision is the structure of the backend system itself.

### Front-End Implementation Review
- Recommended startup: `dist/DEPLOY_UI.md` or full kernel
- Route card: `dist/lite_routes/rt_frontend_architecture.md`
- Use when: Use when the governing decision is front-end architecture rather than generic handoff or UI critique.

### Layout Reconstruction Plan
- Recommended startup: `dist/DEPLOY_UI.md` or full kernel
- Route card: `dist/lite_routes/rt_layout_reconstruction_plan.md`
- Use when: Use when structure must be inferred from an existing artifact instead of redesigned from scratch.

### PDF Remediation Plan
- Recommended startup: `dist/DEPLOY_UI.md` or full kernel
- Route card: `dist/lite_routes/rt_pdf_remediation.md`
- Use when: Prioritize semantic preservation and verification over surface patching.

### Visual Input Prepass
- Recommended startup: `dist/DEPLOY_CORE.md` or full kernel
- Route card: `dist/lite_routes/rt_visual_input.md`
- Use when: Use when you need visual evidence extraction before deciding the real governing route.
