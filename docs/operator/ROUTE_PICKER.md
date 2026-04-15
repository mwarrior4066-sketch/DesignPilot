# Route Picker

Use this file to choose the right launcher without reading internal architecture.

Start broad, then narrow:
- first choose the task cluster that matches the job
- then choose the launcher inside that cluster
- then load the launcher plus `dist/SESSION_ZERO.md`

Manual route + contract + skill assembly is a maintainer/debug path only.

## UI and system structure

### Accessibility Feedback Audit
- Single-file launcher: `dist/runtime/task_launchers/accessibility_feedback_audit.md`
- Manual route card: `dist/runtime/route_cards/rt_accessibility_feedback_audit.md`
- Manual contract card: `dist/runtime/contracts_lite/accessibility_feedback_audit.md`
- Best fit: Use when a user task is blocked or degraded by semantic, focus, keyboard, or announcement failures.

### Color System Specification
- Single-file launcher: `dist/runtime/task_launchers/color_system_spec.md`
- Manual route card: `dist/runtime/route_cards/rt_color_system_spec.md`
- Manual contract card: `dist/runtime/contracts_lite/color_system_spec.md`
- Best fit: Use when the job is to define roles, tokens, and state behavior for color rather than pick nicer hues.

### Component Specification
- Single-file launcher: `dist/runtime/task_launchers/component_spec.md`
- Manual route card: `dist/runtime/route_cards/rt_component_spec.md`
- Manual contract card: `dist/runtime/contracts_lite/component_spec.md`
- Best fit: Use when a reusable system component needs state-safe documentation.

### Dashboard Audit
- Single-file launcher: `dist/runtime/task_launchers/dashboard_audit.md`
- Manual route card: `dist/runtime/route_cards/rt_dashboard_audit.md`
- Manual contract card: `dist/runtime/contracts_lite/dashboard_audit.md`
- Best fit: Use for KPI hierarchy and chart-logic evaluation, not generic screen cleanup.

### Graphic Critique
- Single-file launcher: `dist/runtime/task_launchers/graphic_critique.md`
- Manual route card: `dist/runtime/route_cards/rt_graphic_critique.md`
- Manual contract card: `dist/runtime/contracts_lite/graphic_critique.md`
- Best fit: Use when the key problem is focal structure, type/image balance, or distance legibility.

### Type System Recommendation
- Single-file launcher: `dist/runtime/task_launchers/type_system_recommendation.md`
- Manual route card: `dist/runtime/route_cards/rt_type_system_recommendation.md`
- Manual contract card: `dist/runtime/contracts_lite/type_system_recommendation.md`
- Best fit: Use when the job is to define a repeatable type system instead of suggest a single font.

### UI Structure Critique
- Single-file launcher: `dist/runtime/task_launchers/ui_structure_critique.md`
- Manual route card: `dist/runtime/route_cards/rt_ui_structure_critique.md`
- Manual contract card: `dist/runtime/contracts_lite/ui_structure_critique.md`
- Best fit: Prefer this route when the user wants structural diagnosis before polish.

## Brand and communication

### Brand Positioning Pass
- Single-file launcher: `dist/runtime/task_launchers/brand_positioning_pass.md`
- Manual route card: `dist/runtime/route_cards/rt_brand_positioning.md`
- Manual contract card: `dist/runtime/contracts_lite/brand_positioning_pass.md`
- Best fit: Use when the system must decide who the brand is for and how it earns trust.

### Case Study Rewrite
- Single-file launcher: `dist/runtime/task_launchers/case_study_rewrite.md`
- Manual route card: `dist/runtime/route_cards/rt_case_study_rewrite.md`
- Manual contract card: `dist/runtime/contracts_lite/case_study_rewrite.md`
- Best fit: Use when communication quality depends on narrative order and proof clarity, not just editing.

### Text Humanization Revision
- Single-file launcher: `dist/runtime/task_launchers/text_humanization_revision.md`
- Manual route card: `dist/runtime/route_cards/rt_text_humanization.md`
- Manual contract card: `dist/runtime/contracts_lite/text_humanization_revision.md`
- Best fit: Use when the governing need is prose-quality revision rather than structural rewriting or route-level diagnosis.

## Research and planning

### UX Research Gap Map
- Single-file launcher: `dist/runtime/task_launchers/ux_research_gap_map.md`
- Manual route card: `dist/runtime/route_cards/rt_ux_research_gap_map.md`
- Manual contract card: `dist/runtime/contracts_lite/ux_research_gap_map.md`
- Best fit: Use when the answer must separate known evidence from assumptions and map the next studies.

## Routes that should usually escalate

### API Reliability and Security Review
- Launcher: `dist/runtime/task_launchers/api_reliability_security_review.md`
- Recommended startup: `dist/DEPLOY_UI.md` or full kernel
- Best fit: Use when the governing decision is failure, retry, authorization, or resilience semantics for APIs or tools.

### Back-End Feasibility Review
- Launcher: `dist/runtime/task_launchers/backend_feasibility_review.md`
- Recommended startup: `dist/DEPLOY_UI.md` or full kernel
- Best fit: Reveal back-end implications before treating the request as visual-only.

### Back-End Architecture Spec
- Launcher: `dist/runtime/task_launchers/backend_architecture_spec.md`
- Recommended startup: `dist/DEPLOY_UI.md` or full kernel
- Best fit: Use when the governing decision is the structure of the backend system itself.

### Front-End Implementation Review
- Launcher: `dist/runtime/task_launchers/frontend_implementation_review.md`
- Recommended startup: `dist/DEPLOY_UI.md` or full kernel
- Best fit: Use when the governing decision is front-end architecture rather than generic handoff or UI critique.

### Layout Reconstruction Plan
- Launcher: `dist/runtime/task_launchers/layout_reconstruction_plan.md`
- Recommended startup: `dist/DEPLOY_UI.md` or full kernel
- Best fit: Use when structure must be inferred from an existing artifact instead of redesigned from scratch.

### PDF Remediation Plan
- Launcher: `dist/runtime/task_launchers/pdf_remediation_plan.md`
- Recommended startup: `dist/DEPLOY_UI.md` or full kernel
- Best fit: Prioritize semantic preservation and verification over surface patching.

### Visual Input Prepass
- Launcher: `dist/runtime/task_launchers/visual_input_prepass.md`
- Recommended startup: `dist/DEPLOY_CORE.md` or full kernel
- Best fit: Use when you need visual evidence extraction before deciding the real governing route.
