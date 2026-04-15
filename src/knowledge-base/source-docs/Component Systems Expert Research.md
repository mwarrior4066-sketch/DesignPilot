<!-- Optimized from original source file: Component Systems Expert Research.docx. All textual content preserved in markdown form for size-efficient packaging. -->

# Component Systems Expert Specification for DesignPilot

## Evidence base and scope

This specification is a production-oriented synthesis of: W3C[\[1\]](https://designsystem.digital.gov/components/status/) guidance (WCAG 2.2, WAI-ARIA Authoring Practices Guide, HTML-ARIA, and Using ARIA), mature component libraries and design systems (U.S. Web Design System[\[2\]](https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com), Carbon Design System[\[3\]](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria/?utm_source=chatgpt.com), GOV.UK Design System[\[4\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), Apple[\[5\]](https://carbondesignsystem.com/components/data-table/accessibility/), Microsoft[\[6\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com), Atlassian[\[7\]](https://carbondesignsystem.com/components/button/usage/)), and implementation references including Mozilla[\[8\]](https://carbondesignsystem.com/components/data-table/usage/) (MDN), Deque Systems[\[9\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com), and Nielsen Norman Group[\[10\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com). [\[11\]](https://www.w3.org/WAI/ARIA/apg/?utm_source=chatgpt.com)

The goal is not a “component list,” but a strict “Component Systems Expert” agent spec that can make production-level decisions across: component inventories, variant and state models, responsive and theming behavior, accessibility by component type, dense-data behaviors, and implementation-ready handoff. The rules below prioritize testable behavior and measurable thresholds over visual styling alone. [\[12\]](https://designsystem.digital.gov/components/status/)

## Inventory, coverage, governance, and handoff

### Component inventory and system coverage

**Definition.**  
A component inventory is the canonical registry of all UI building blocks (components, patterns, utilities, tokens) that a product team is allowed to ship, with explicit scope, status, owners, and supported behaviors. “System coverage” is the portion of product UI that can be built using these canonical blocks without one-off custom UI. [\[13\]](https://designsystem.digital.gov/components/status/)

**Why it matters for a Component Systems Expert.**  
An expert agent can only make reliable reuse vs. build decisions if it has an authoritative list of what exists, what is stable, and how each component is meant to behave. Mature systems publish inventories and lifecycle status so teams can decide whether using a component is safe; for example, USWDS publicly tracks components and labels them “Stable,” “Discussion started,” “Proposal in progress,” etc., which is the exact kind of machine-actionable “coverage” signal an operator pack needs. [\[14\]](https://designsystem.digital.gov/components/status/)

**Default rules.**  
1) **Maintain a single source of truth “component registry.”** Each entry must include: purpose, “when to use / when not to use,” variants, sizes, states, responsive rules, theming rules, accessibility rules, and code availability (frameworks, packages). This mirrors the documentation structure used in mature systems (e.g., component pages with usage + accessibility + code guidance). [\[15\]](https://designsystem.digital.gov/)  
2) **Track lifecycle status for every component and pattern (including proposals).** Use a status model similar to USWDS lifecycle and status tables to prevent accidental adoption of unstable components. [\[16\]](https://designsystem.digital.gov/components/lifecycle/)  
3) **Inventory is behavioral, not visual.** A component is “in inventory” only if it has defined interaction behavior, state coverage, and accessibility expectations (not just a Figma symbol or a screenshot). WCAG success criteria are written as testable statements for conformance; your inventory must match that “testability” standard. [\[17\]](https://www.w3.org/TR/WCAG22/)  
4) **De-duplicate by function, not by shape.** If multiple components solve the same task (e.g., “four date pickers that do the same thing”), inventory work must consolidate them into one canonical component with variants. [\[18\]](https://www.thinkcompany.com/guides/a-guide-to-design-systems/?utm_source=chatgpt.com)  
5) **Coverage is measured per product surface.** Track which screens and flows are built from inventory components; this is a governance tool to prevent drift (see “enforcer” and lifecycle governance guidance). [\[19\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)

**Exception rules.**  
1) **Product-specific “edge components”** are allowed only when (a) the behavior is genuinely unique, and (b) the component is explicitly flagged “local-only” in the registry with a “do-not-promote” tag and an expiration/review date. (Rationale: reduces system clutter and drift.) [\[20\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)  
2) **Prototypes and experiments** may use temporary components, but must be isolated behind feature flags and never be treated as inventory coverage unless promoted through governance. [\[21\]](https://designsystem.digital.gov/components/lifecycle/)  
3) **Highly regulated or legally constrained replicas** (forms that must match paper forms) can justify deviations, consistent with WCAG’s “Essential” exception logic for certain constraints. [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

**Fallback logic.**  
If the registry does not contain a matching component:  
- First, attempt **composition from primitives** (layout + typography + existing controls) rather than creating a new bespoke component.  
- If composition cannot satisfy required behavior, initiate a **new component proposal** (with lifecycle status and mandatory spec fields) rather than shipping a one-off. This mirrors published component lifecycle “proposal → evaluation → release” governance patterns. [\[23\]](https://designsystem.digital.gov/components/lifecycle/)

**Failure conditions.**  
- “Phantom components”: design assets exist but there is no behavioral/as-built spec.  
- Duplicate components in production solving the same task with different states/keyboard behavior.  
- No lifecycle status: teams cannot tell if a component is safe to adopt. [\[24\]](https://www.thinkcompany.com/guides/a-guide-to-design-systems/?utm_source=chatgpt.com)

**Measurable thresholds.**  
- **Inventory completeness:** ≥95% of registry entries include: variants, sizes, states, accessibility, responsive rules, and code availability (coverage fields).  
- **Duplication budget:** For any function cluster (e.g., “date selection”), ≤1 canonical component in “Stable” status; alternates must be formally deprecated or explicitly “local-only.” [\[25\]](https://www.thinkcompany.com/guides/a-guide-to-design-systems/?utm_source=chatgpt.com)  
- **Coverage ratio:** For each product surface, track “UI built from inventory” vs “custom UI”; governance review triggers if custom UI exceeds 10–15% for two consecutive releases (operator-pack heuristic aligned to anti-drift governance rationale). [\[26\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)  
- **Freshness:** Registry “last reviewed” date per component; review overdue if \>180 days on high-change components (tables, navigation, forms). (Heuristic; enforced because documentation and intent drift is a common failure mode.) [\[20\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)

**Implementation guidance for an AI operator pack.**  
- Represent the inventory as machine-readable objects (JSON/YAML) plus human docs. Minimum fields:  
- `id`, `name`, `category`, `purpose`, `do`, `dont`, `anatomy`, `variants`, `sizes`, `states`, `a11y`, `responsive`, `theming`, `tokens`, `dependencies`, `status`, `owner`, `version`, `tests`.  
- Include a “status gate”: the agent may only recommend “Stable” components by default; “Proposal/Discussion” components require an explicit justification and risk acknowledgement. This matches published lifecycle/status practices. [\[27\]](https://designsystem.digital.gov/components/status/)  
- Add “duplicate detection”: if the request resembles an existing component’s `purpose` or `tasks`, the agent must recommend reuse + extension proposal rather than a new component. [\[18\]](https://www.thinkcompany.com/guides/a-guide-to-design-systems/?utm_source=chatgpt.com)

**Test cases.**  
- A team proposes “Toast” while an “Alert” component exists; the expert must route to an inventory check, then either reuse existing alert/toast guidance or create a proposal entry with status “Discussion started.” [\[28\]](https://designsystem.digital.gov/components/status/)  
- A product has 3 “tables” with different selection mechanics; the expert must consolidate into a single data-table spec with variants and a lifecycle deprecation plan. [\[29\]](https://carbondesignsystem.com/components/data-table/usage/)  
- A new “date picker” is requested; the expert must enforce “de-duplicate by function,” audit existing date components/patterns, and only then approve a new proposal if required behaviors are not covered. [\[30\]](https://www.thinkcompany.com/guides/a-guide-to-design-systems/?utm_source=chatgpt.com)

### Component governance and reuse

**Definition.**  
Governance is the decision process for introducing, changing, versioning, and deprecating components and tokens; reuse is the enforced default behavior that keeps product UI consistent and accessible at scale. [\[31\]](https://designsystem.digital.gov/components/lifecycle/)

**Why it matters for a Component Systems Expert.**  
Even strong design systems fail without enforcement and clear ownership; governance defines who decides, how exceptions are handled, and how drift is prevented. An expert agent must operationalize governance as “gates” and “budgets” (variant budgets, duplication budgets, accessibility gates). [\[32\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)

**Default rules.**  
1) **Lifecycle-based gates.** New components enter via proposal and mature through defined phases; USWDS, for example, documents proposal phases and a minimum comment period (45 days) before evaluation, which is a concrete governance mechanism. [\[33\]](https://designsystem.digital.gov/components/lifecycle/)  
2) **Contributions are multi-artifact.** A contribution includes proposal/design/code/docs/assets; defining contribution scope prevents “design-only” or “code-only” drift. [\[34\]](https://medium.com/eightshapes-llc/defining-design-system-contributions-eb48e00e8898?utm_source=chatgpt.com)  
3) **Accessibility is non-negotiable for promotion to stable.** Systems that publish accessibility testing status (like Carbon’s component testing status) effectively encode this gate. [\[35\]](https://carbondesignsystem.com/components/data-table/usage/)  
4) **Versioning and deprecation must be explicit.** A component’s API and behavior changes must be versioned; deprecated components remain documented with migration guidance until removed. USWDS explicitly discusses refining and retiring components as part of lifecycle. [\[36\]](https://designsystem.digital.gov/components/lifecycle/)  
5) **Reuse-first defaults.** The expert must prefer extending an existing component (new prop, new token hook) over minting a new component. Drift is a known systemic risk when teams extend independently. [\[37\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)

**Exception rules.**  
- A product team may “fork” a component only under a documented emergency: security, legal, or critical delivery constraint-and must file a merge-back or deprecation plan. (Heuristic tied to governance drift risks.) [\[37\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)  
- Components that require domain-specific workflows (e.g., specialized medical charting) can remain local, but must still meet accessibility and token contracts. [\[38\]](https://www.w3.org/TR/WCAG22/)

**Fallback logic.**  
If governance is missing or unclear:  
- Freeze creation of new components/variants.  
- Use existing stable components; if none fit, compose from primitives and file a proposal ticket (do not ship a new standalone component silently). [\[39\]](https://designsystem.digital.gov/components/lifecycle/)

**Failure conditions.**  
- “Shadow design system”: teams rebuild components outside the system because contributions are too hard.  
- Centralized bottleneck without clear pathways, leading to workarounds and fragmentation. [\[40\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)

**Measurable thresholds.**  
- **Governance SLA:** proposal triage within 10 business days; “proposal open for comment” period minimum enforced (e.g., 45 days) if adopting USWDS-like approach. [\[33\]](https://designsystem.digital.gov/components/lifecycle/)  
- **Adoption metric:** % of new UI built with stable components; if it drops quarter-over-quarter, trigger governance and documentation review (“enforcer” function). [\[20\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)  
- **Contribution throughput:** median time from proposal approval to first usable release; long lead times correlate with shadow systems (heuristic). [\[19\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)

**Implementation guidance for an AI operator pack.**  
- Encode governance as **decision gates**: “stable-only by default,” “variant budget checks,” “a11y gate checks,” “token contract checks.”  
- Require the agent to output: (a) decision, (b) risk level, (c) governance step triggered (reuse, extension, proposal, deprecation). [\[39\]](https://designsystem.digital.gov/components/lifecycle/)

**Test cases.**  
- A designer requests a “secondary button used alone for primary action.” The agent must block and cite the system rule: secondary should not be used in isolation for primary action; propose primary/tertiary alternatives. [\[41\]](https://carbondesignsystem.com/components/button/usage/)  
- A new “grid” variant is requested; the agent must check existing grid modes and only allow if it can be expressed via existing gutter/breakpoint system or settings. [\[42\]](https://carbondesignsystem.com/elements/2x-grid/overview/)

### Documentation and handoff standards

**Definition.**  
Documentation and handoff standards are the minimum required artifacts that make a component implementable and testable in production: behavior, states, accessibility, tokens, and code integration-not just visuals. [\[43\]](https://designsystem.digital.gov/)

**Why it matters for a Component Systems Expert.**  
An expert agent must be able to produce “implementation-ready” decisions: what to build, how it behaves, what tokens it uses, and how to verify it. Mature systems publish component pages that include when-to-use guidance, variants, anatomy, sizing, interaction rules, and accessibility. Carbon’s data table page, for example, includes explicit behavior rules (sorting states, toolbar action limits, batch-mode effects, loading guidance) and separate accessibility guidance (keyboard interaction, tab order for controls within tables). [\[44\]](https://carbondesignsystem.com/components/data-table/usage/)

**Default rules.**  
1) **Every component doc must include a “when not to use” section.** This prevents misuse; e.g., Carbon explicitly says not to use a data table “as a replacement for a spreadsheet application,” which is a behavior and scope boundary. [\[45\]](https://carbondesignsystem.com/components/data-table/usage/)  
2) **Every component doc must include state model + keyboard model.** For composite widgets, use the ARIA APG keyboard interface guidance and pattern-specific key bindings (grid, combobox, menus, dialogs). [\[46\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com)  
3) **Every component doc must define size + density options.** Dense UI needs explicit row/height guidance; Carbon provides row sizes for data table and rules that header row matches row size. [\[47\]](https://carbondesignsystem.com/components/data-table/usage/)  
4) **Tokens are a contract.** Document which design tokens drive which component parts (spacing, color, typography, radii). Use a standard token exchange format where feasible (Design Tokens Community Group format module). [\[48\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com)  
5) **Handoff includes test artifacts.** At minimum: unit tests for state transitions, keyboard navigation checks for composite widgets, and accessibility audits. Carbon’s published accessibility testing statuses illustrate the expectation that stable components are tested. [\[35\]](https://carbondesignsystem.com/components/data-table/usage/)

**Exception rules.**  
- “Incubating” components may have partial docs, but must be clearly labeled as not stable (status gate) and must not be default recommendations. [\[27\]](https://designsystem.digital.gov/components/status/)  
- Platform-native components (e.g., unmodified `<input type="date">`) may rely on user agent behavior, but docs must record the dependency and known limitations. [\[49\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

**Fallback logic.**  
If documentation is incomplete:  
- Treat component as **unstable**.  
- Prefer a documented alternative or a simpler native element.  
- If unavoidable, require a “doc patch” as part of the implementation task. [\[50\]](https://designsystem.digital.gov/components/status/)

**Failure conditions.**  
- Doc drift: implementation changes but docs remain stale, leading to misuse.  
- No explicit keyboard or accessibility guidance for composite widgets.  
- Tokens are undocumented, leading to hard-coded styles and theming failures. [\[51\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)

**Measurable thresholds.**  
- **Doneness:** A component cannot be promoted to stable unless it has: usage boundaries, variants/sizes, state model, a11y model, responsive model, token mapping, and tests (operator-pack gate aligned to lifecycle practices). [\[52\]](https://designsystem.digital.gov/components/lifecycle/)  
- **Doc parity:** “Docs updated within the same release” for any behavior change (governance policy). [\[39\]](https://designsystem.digital.gov/components/lifecycle/)  
- **Token compliance:** 0 hard-coded colors/spacing in component source except where documented as essential (token contract requirement). [\[53\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com)

**Implementation guidance for an AI operator pack.**  
- Require the agent to output a **component spec block** in a fixed template (fields above), then a **handoff block**:  
- `Design`: anatomy, tokens, variants, states, responsive rules, theming rules  
- `Dev`: API props/events, DOM structure, ARIA mapping, CSS hooks  
- `QA`: test matrix (states × input modality × theme), a11y checks, visual regression targets  
- Include a token-format validator in the pipeline if you adopt the DTCG interchange format. [\[54\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com)

**Test cases.**  
- A component proposal arrives with visuals only. The expert must reject promotion, produce a missing-artifacts list, and propose how to document keyboard + a11y behavior. [\[55\]](https://www.w3.org/TR/WCAG22/)  
- A component uses hard-coded colors; the expert must refactor to semantic tokens and verify contrast in light/dark/forced-colors contexts. [\[56\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com)

## Variants, sizes, spacing, composition, and state coverage

### Variants, sizes, and composition rules

**Definition.**  
- A **variant** is a deliberately supported, named configuration of a component that changes semantics or emphasis (e.g., button emphasis levels, selection vs. expansion table variants).  
- A **size scale** is the bounded set of supported dimensions (heights, paddings, typography) a component may take.  
- **Composition rules** define which components can contain or align with others, including ordering rules and layout constraints for groups. [\[57\]](https://carbondesignsystem.com/components/button/usage/)

**Why it matters for a Component Systems Expert.**  
Variant explosion is a primary source of drift: every additional variant multiplies state coverage, accessibility burden, responsive behavior, and theming requirements. Mature systems constrain variance while giving explicit composition guidance-for example, Carbon’s button guidance specifies primary-button placement rules across contexts (full pages vs wizards), recommended variant combinations within button groups, and spacing constraints around icons and labels. [\[58\]](https://carbondesignsystem.com/components/button/usage/)

**Default rules.**  
1) **Variants must map to user intent.** Do not create visual-only variants; each variant must correspond to a distinct semantic intent or interaction role (primary vs destructive vs tertiary, selectable vs expandable, etc.). Carbon’s button and data table docs demonstrate intent-based variants (danger styles, selection/expansion variants). [\[59\]](https://carbondesignsystem.com/components/button/usage/)  
2) **Cap variant count using mature-system baselines.** As a strong default:  
- Button: limit to emphasis variants comparable to established systems (e.g., Carbon primary/secondary/tertiary/ghost + danger variants; Material-family buttons list multiple emphasis types). [\[60\]](https://carbondesignsystem.com/components/button/usage/)  
- Data table: favor a small number of structural variants (default, selection, expansion) rather than bespoke hybrids. [\[61\]](https://carbondesignsystem.com/components/data-table/usage/)  
3) **Use a bounded size scale and document it.** Carbon documents discrete button sizes and data-table row sizes, with explicit height values and pairing rules (e.g., toolbar height must match certain row sizes). Adopt a similar bounded scale rather than arbitrary pixel values. [\[62\]](https://v10.carbondesignsystem.com/components/button/style/)  
4) **Spacing uses tokenized recipes, not custom margins.** Both Carbon and USWDS base spacing on consistent token scales (Carbon’s 2/4/8 multiples; USWDS spacing units based on 8px multiples). Your system should require spacing tokens for internal padding and external layout gaps. [\[63\]](https://carbondesignsystem.com/elements/spacing/overview/?utm_source=chatgpt.com)  
5) **Composition rules are explicit and context-sensitive.** Examples of enforceable composition rules:  
- Button groups: primary placement differs by context (full pages vs wizards/dialogs) and certain combinations are recommended/avoided. [\[41\]](https://carbondesignsystem.com/components/button/usage/)  
- Data tables: avoid nesting tables inside tables; place tables in main content area with enough width to avoid truncation; cap toolbar actions (“up to five”) and overflow the rest. [\[64\]](https://carbondesignsystem.com/components/data-table/usage/)  
6) **Component-specific micro-constraints are part of the spec.** E.g., “no label or element within 16px of button borders,” and icon-label spacing minimums are enforceable constraints that prevent dense UI collisions. [\[65\]](https://carbondesignsystem.com/components/button/style/)

**Exception rules.**  
- **Editorial/marketing vs product UI.** Carbon explicitly distinguishes “productive” button sizes from “large expressive” for marketing/editorial contexts; treat marketing variants as separate scope to avoid polluting product UI. [\[66\]](https://v10.carbondesignsystem.com/components/button/style/)  
- **Dense admin tools** may require smaller row sizes, but must still meet minimum target size requirements or spacing exceptions and maintain keyboard support. [\[67\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
- **Platform constraints** (native controls) can override size/spacing rules if user agent determines sizing and you do not modify it. [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

**Fallback logic.**  
When a request asks for a new variant/size:  
1) Try to express it as **tokens + existing variant** (theme token override, density setting) rather than a new named variant. [\[68\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com)  
2) If the behavior truly differs, propose a **new variant** only if it (a) has unique intent, (b) fits within variant budgets, and (c) includes full state/a11y/responsive/theming specs. [\[69\]](https://designsystem.digital.gov/components/lifecycle/)  
3) If you cannot fully specify it, defer to composition (build the experience from existing pieces) and open a proposal. [\[70\]](https://designsystem.digital.gov/components/lifecycle/)

**Failure conditions.**  
- Variant created solely for a single screen’s styling preference.  
- Size options become continuous (arbitrary heights), breaking alignment and density control.  
- Composition creates conflicting hierarchy (e.g., two primary actions visible simultaneously; Carbon warns against primary in header if primary exists below). [\[71\]](https://carbondesignsystem.com/components/button/usage/)

**Measurable thresholds.**  
- **Variant budget per component:** default ≤5 intent-based variants (aligning with mature-system patterns for high-frequency controls). [\[72\]](https://carbondesignsystem.com/components/button/usage/)  
- **Size budget per component:** default ≤5 discrete sizes per component; data tables explicitly support five row sizes and require header-row matching (use this as a density model). [\[73\]](https://carbondesignsystem.com/components/data-table/usage/)  
- **Spacing compliance:** 100% of spacing values must reference tokens (Carbon spacing tokens; USWDS spacing unit tokens). [\[63\]](https://carbondesignsystem.com/elements/spacing/overview/?utm_source=chatgpt.com)  
- **Composition rule coverage:** every multi-control pattern (button group, toolbar, table toolbar, form layouts) must have at least one “do-not” misuse rule (“when not to use”). [\[74\]](https://carbondesignsystem.com/components/button/usage/)

**Implementation guidance for an AI operator pack.**  
- Model variants as an **intent taxonomy** plus **presentation modifiers**:  
- `intent`: default \| primary \| secondary \| tertiary \| destructive \| passive  
- `modifiers`: iconOnly, leadingIcon, fullWidth, compact, fluid, etc.  
- Encode **composition constraints** as validators:  
- button-group ordering rules  
- toolbar action count limit  
- table nesting prohibition  
- Provide “token recipes” for spacing: use only spacing tokens, never ad-hoc margins. [\[75\]](https://carbondesignsystem.com/elements/spacing/overview/?utm_source=chatgpt.com)

**Test cases.**  
- Request: “Add a ‘super-primary’ button style.” Expected: reject as intent-duplicate; recommend existing primary + theme tokens; if destructive, route to danger variant. [\[76\]](https://carbondesignsystem.com/components/button/usage/)  
- Request: “Compact table but keep tall header.” Expected: reject; header row must match row size. [\[73\]](https://carbondesignsystem.com/components/data-table/usage/)  
- Request: “Add 9 toolbar actions to table.” Expected: cap at five; overflow menu for the rest. [\[64\]](https://carbondesignsystem.com/components/data-table/usage/)

### Required state coverage by component type

**Definition.**  
State coverage is the complete set of interactive, validation, and lifecycle states a component must support-across input modalities (mouse, keyboard, touch) and contexts (forms, tables, dialogs)-including how states layer and how focus moves. [\[77\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com)

**Why it matters for a Component Systems Expert.**  
States are where production quality breaks: missing focus styles, unclear disabled/read-only differences, improper keyboard behavior, and incomplete loading/empty/error states cause accessibility failures and user confusion. Research and system guidance explicitly emphasize distinguishing multiple interaction states (e.g., 5 button states: enabled, disabled, hovered, focused, pressed). [\[78\]](https://www.nngroup.com/articles/button-states-communicate-interaction/?utm_source=chatgpt.com)

**Default rules.**  
1) **Baseline for any interactive control:** must support enabled, hover (if pointer), pressed/active, focus, and disabled. [\[79\]](https://www.nngroup.com/articles/button-states-communicate-interaction/?utm_source=chatgpt.com)  
2) **Disabled vs read-only are distinct.** Carbon defines disabled as removing interaction; read-only preserves readability and screen-reader access, without interactive affordances. Treat these as separate states with separate semantics. [\[80\]](https://carbondesignsystem.com/patterns/disabled-states/)  
3) **Form controls require validation states.** Carbon form guidance lists enabled, active (typing), focus, error, warning, disabled, skeleton; adopt this as minimum for form contexts, with error/warning requiring user response for submission gating. [\[81\]](https://carbondesignsystem.com/components/form/usage/)  
4) **Selection controls require selection states.** Checkboxes may be dual-state or tri-state (including “partially checked/indeterminate”); data-table selection includes header checkbox with indeterminate state when some rows are selected. [\[82\]](https://www.w3.org/WAI/ARIA/apg/patterns/?utm_source=chatgpt.com)  
5) **Disclosure controls require expanded/collapsed and open/closed states** with correct focus management; composite widgets must follow APG focus management practices. [\[83\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com)  
6) **Loading is explicit and context-appropriate.** Use skeleton states for initial “content not loaded yet” in data/container components and loading indicators for processing; Carbon explicitly restricts skeleton usage (do not skeletonize toast/modals/menus themselves) and recommends skeletons only for a few seconds (or one to three seconds in an alternate Carbon publication). [\[84\]](https://carbondesignsystem.com/patterns/loading-pattern/)  
7) **Focus visibility must be maintained and not obscured.** WCAG 2.2 adds requirements that focus not be obscured (minimum) and defines focus appearance expectations; your component states must preserve focus indication under overlays/sticky headers. [\[85\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)

**Exception rules.**  
- **Hover state is optional** for touch-only experiences; do not rely on hover as the only way to reveal critical information. (If using hover, ensure equivalent focus behavior.) [\[86\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)  
- **Disabled contrast requirements:** WCAG non-text contrast excludes inactive components; Carbon explicitly notes disabled styling is not subject to WCAG contrast compliance for certain components. Treat disabled contrast as best-effort but not the same compliance target as active UI. [\[87\]](https://w3c.github.io/wcag21/understanding/non-text-contrast.html)  
- **Skeleton states not applicable** to action components in most cases; default to no skeleton for buttons/inputs unless there is a strong reason. [\[88\]](https://carbondesignsystem.com/patterns/loading-pattern/)

**Fallback logic.**  
- If a component cannot support the full required state model, **downgrade to a simpler native control** (or a less interactive pattern) rather than shipping incomplete states. This aligns with the “use native HTML first” principle and avoids creating inaccessible custom widgets. [\[89\]](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)  
- If the component is data-driven and loading is uncertain, **default to skeleton for structure + progressive loading** for details. [\[88\]](https://carbondesignsystem.com/patterns/loading-pattern/)

**Failure conditions.**  
- Missing keyboard focus indication or focus becomes hidden under fixed headers/overlays. [\[90\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)  
- Indeterminate selection states (checkbox/table) not implemented, leading to incorrect bulk-selection semantics. [\[82\]](https://www.w3.org/WAI/ARIA/apg/patterns/?utm_source=chatgpt.com)  
- Skeleton used for popovers/menus/modals themselves, which Carbon explicitly advises against. [\[88\]](https://carbondesignsystem.com/patterns/loading-pattern/)  
- “Disabled” used when “read-only” is required (important information becomes inaccessible). [\[80\]](https://carbondesignsystem.com/patterns/disabled-states/)

**Measurable thresholds.**  
- **State completeness score:** for each component type, required states implemented ÷ required states defined in the matrix; must be 100% for stable status. [\[91\]](https://designsystem.digital.gov/components/status/)  
- **Focus integrity:** 0 known cases where focus indicator is fully obscured; verify against WCAG 2.2 focus-not-obscured expectations. [\[92\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)  
- **Loading correctness:** skeleton visible duration typically seconds, not minutes; long-running tasks should use progress indicators/notifications rather than indefinite spinners. [\[88\]](https://carbondesignsystem.com/patterns/loading-pattern/)

**Implementation guidance for an AI operator pack.**  
- Encode a **state matrix by component type** (see Appendix C) and require the agent to reference it for every component decision.  
- Require the agent to output:  
- `State list` (including which states are modality-specific)  
- `State precedence` (e.g., disabled overrides hover/pressed; error overrides neutral border)  
- `Announcements` (which state transitions require screen reader announcements; e.g., validation errors, async save success). [\[93\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html)

**Test cases.**  
- A toggle switch must support: focus, pressed, disabled, selected/unselected, and optionally loading; verify keyboard toggling and screen-reader name/state. [\[94\]](https://www.w3.org/WAI/ARIA/apg/?utm_source=chatgpt.com)  
- A form field with helper text must expose instructions on focus and show error messaging in text (not color alone). [\[95\]](https://carbondesignsystem.com/components/form/usage/)  
- A sticky header must not cover the focus ring for elements below; verify focus-not-obscured. [\[90\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)

## Accessibility rules by component type

### Component accessibility rules

**Definition.**  
Component accessibility rules are the required semantics, keyboard interactions, focus management behaviors, contrast/target-size thresholds, and error messaging behaviors that make each component usable by people with disabilities across assistive technologies. [\[96\]](https://www.w3.org/TR/WCAG22/)

**Why it matters for a Component Systems Expert.**  
A component system is only “production-level” if its components are operable and understandable via keyboard and assistive tech, and if their states are perceivable (focus, error, disabled, selected). WCAG provides testable criteria (contrast, target size, focus visibility, error identification), while ARIA APG provides widget-level keyboard/focus patterns for composite components (combobox, grid, tabs, dialogs, menus). [\[97\]](https://www.w3.org/TR/WCAG22/)

**Default rules.**  
1) **Native-first semantics.** Use native HTML elements/attributes with built-in semantics and behavior whenever possible; only use ARIA to fill gaps for custom widgets. This is a widely repeated rule in accessibility guidance and is reinforced by authoring-rule specs (HTML-ARIA) and developer references. [\[98\]](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)  
2) **ARIA must follow authoring rules.** If using ARIA, follow HTML-ARIA conformance requirements to avoid invalid/overridden roles and redundant or harmful ARIA. [\[99\]](https://www.w3.org/TR/html-aria/)  
3) **Keyboard is required.** Every interactive component must be fully operable via keyboard, with focus management and predictable navigation. For composite widgets, follow APG guidance on managing focus within a composite (combobox, grid, menu, tabs, etc.). [\[100\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com)  
4) **Focus visibility and non-obscuring are required.** Ensure focus is visible and not obscured by author-created content; meet WCAG 2.2 expectations for focus not obscured (and consider stronger focus appearance guidance as best practice). [\[85\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)  
5) **Contrast thresholds.**  
- Text contrast: ≥4.5:1 for normal text, ≥3:1 for large text (WCAG 2.2 contrast minimum). [\[101\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)  
- Non-text contrast: ≥3:1 for UI component boundaries and state indicators (WCAG non-text contrast). [\[102\]](https://w3c.github.io/wcag21/understanding/non-text-contrast.html)  
6) **Target size threshold.** Interactive targets must be at least 24×24 CSS pixels, or satisfy spacing/equivalent/inline/user-agent/essential exceptions as defined in WCAG 2.2. This is especially important for dense UI toolbars and icon actions. [\[103\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
7) **Error messaging is textual and actionable.**  
- Errors must be identified in text (not only color) and associated to the field. [\[104\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html)  
- Provide labels/instructions and (when possible) suggestions to correct errors. [\[105\]](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html)  
- For page-level form validation, show both an error summary and inline error messages (GOV.UK guidance). [\[106\]](https://design-system.service.gov.uk/components/error-summary/)  
8) **Tables and dense components must be keyboard-navigable.** Carbon data table guidance states that standard table variants incorporate keyboard operation and that interactive controls inside cells remain in the tab order; if you create a composite grid, follow APG grid keyboard interactions. [\[107\]](https://carbondesignsystem.com/components/data-table/accessibility/)  
9) **Respect user preference media features for accessibility.** Use `prefers-color-scheme`, `prefers-contrast`, and forced-colors support to remain legible in user-defined high contrast modes. [\[108\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-color-scheme)  
10) **Resize and reflow resilience.** Text must be resizeable up to 200% without loss of content/functionality (WCAG resize text), so components must be built to wrap/flow rather than clip critical labels. [\[101\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)

**Exception rules.**  
- Disabled controls are excluded from non-text contrast requirements; Carbon also notes disabled styling may not be subject to WCAG contrast compliance. Still, disabled state must remain perceivable and must not mislead as enabled. [\[109\]](https://w3c.github.io/wcag21/understanding/non-text-contrast.html)  
- Inline links in text are exempt from the 24×24 target size requirement; but spacing/line height should still support activation and readability. [\[110\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
- Essential dense visualizations can be exempted under WCAG target-size essential exception; however, WCAG encourages equivalent functionality where practical. [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

**Fallback logic.**  
- If a custom widget fails keyboard or screen-reader requirements, replace it with a native control (select, input, details/summary, dialog behavior) or a fully APG-compliant implementation. [\[111\]](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)  
- If contrast cannot be achieved with brand colors, adopt semantic/system colors for critical text and boundaries and reserve brand colors for accents. [\[112\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)

**Failure conditions.**  
- Missing accessible name/label (inputs, icon-only buttons).  
- Keyboard trap in dialogs/menus/grids; inability to reach controls inside table cells. [\[113\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com)  
- Error indicated only by color, or errors not described in text. [\[114\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html)  
- Touch targets below 24×24 without spacing exception compliance. [\[115\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
- Focus indicator hidden under sticky UI. [\[90\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)

**Measurable thresholds.**  
- Contrast: text ≥4.5:1; non-text UI boundaries/state indicators ≥3:1. [\[116\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)  
- Target size: ≥24×24 CSS px, or meets WCAG exceptions. [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
- Focus: focus indicator not obscured (minimum). [\[117\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)  
- Form validation: error identification in text + labels/instructions + (when possible) error suggestion; plus error summary pattern for page-level errors. [\[118\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html)

**Implementation guidance for an AI operator pack.**  
- Bundle an “A11y rule engine” with:  
- ARIA APG pattern mappings (role/state/property + keyboard events) [\[119\]](https://www.w3.org/WAI/ARIA/apg/?utm_source=chatgpt.com)  
- WCAG gates for contrast, target size, focus, errors [\[120\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)  
- HTML-ARIA conformance checks [\[121\]](https://www.w3.org/TR/html-aria/)  
- Require the agent to output a per-component “accessible behavior spec”: name/description strategy, keyboard map, focus order rules, error association strategy, and user preference support (forced-colors/prefers-contrast). [\[122\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com)

**Test cases.**  
- Icon-only button in a toolbar: verify accessible name, 24×24 target size, visible focus ring, and non-text contrast of icon/border. [\[123\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
- Form submission with 3 invalid fields: ensure error summary at top plus inline error messages; each summary item links to the field; errors described in text. [\[124\]](https://design-system.service.gov.uk/components/error-summary/)  
- Custom combobox: verify APG combobox behavior, focus management, and keyboard interactions. [\[125\]](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/?utm_source=chatgpt.com)  
- Forced-colors mode: verify that borders/focus rings remain visible and legible. [\[126\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors)

## Responsive and adaptive component behavior

### Responsive component behavior

**Definition.**  
Responsive component behavior is the set of rules that define how a component adapts layout, density, content, and interactions across viewport and container sizes, including breakpoints and “window size classes.” [\[127\]](https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com)

**Why it matters for a Component Systems Expert.**  
An expert agent must make predictable choices about when to stack vs inline, when to collapse actions into overflow, when to switch navigation patterns, and how to preserve accessibility (target sizes, focus visibility) under density changes. Mature systems explicitly document responsive grids (mobile-first grids, breakpoints, and modes) and recommend testing at standard breakpoints. [\[128\]](https://designsystem.digital.gov/utilities/layout-grid/)

**Default rules.**  
1) **Use a declared breakpoint system, not ad-hoc breakpoints.**  
- Material guidance uses window size classes (compact/medium/expanded/large/extra-large). [\[129\]](https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com)  
- USWDS uses a mobile-first 12-column flexbox grid and configurable utility breakpoints. [\[130\]](https://designsystem.digital.gov/utilities/layout-grid/)  
- Carbon 2x grid provides standard breakpoints and multiple gutter modes (wide/narrow/condensed). [\[131\]](https://carbondesignsystem.com/elements/2x-grid/overview/)  
2) **Component-level responsiveness is explicit.** Each component must define: min container width, wrap strategy, truncation rules, and which controls collapse into overflow at smaller sizes. Carbon’s data table gives explicit guidance about width, truncation avoidance, and overflow behavior for actions. [\[132\]](https://carbondesignsystem.com/components/data-table/usage/)  
3) **Maintain target size and spacing under density changes.** Dense layouts must still meet WCAG target size requirements or spacing exceptions; if density breaks targets, provide a density toggle or alternative UI. [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
4) **Avoid “responsive-only” hidden functionality.** If actions are moved into overflow, they must remain reachable by keyboard, screen readers, and without hover dependence. [\[133\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com)  
5) **Prefer progressive disclosure for complex toolbars.** Carbon explicitly recommends overflow menus/combo buttons when actions exceed the toolbar limit; this is a responsive strategy for dense actions. [\[64\]](https://carbondesignsystem.com/components/data-table/usage/)  
6) **Tables have defined responsive strategies.** When columns exceed available width: use horizontal scroll with sticky headers cautiously, or switch to alternative presentations (cards, lists) depending on task; do not cram or truncate critical identifiers. (Heuristic aligned with Carbon’s “give tables width, avoid truncation” guidance.) [\[134\]](https://carbondesignsystem.com/components/data-table/usage/)

**Exception rules.**  
- **Fixed-width data** (IDs, short codes) may require horizontal scrolling; in these cases, ensure focus not obscured and maintain keyboard navigation. [\[135\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)  
- **Highly dense dashboards** may violate ideal spacing; provide user controls for density and consider WCAG target-size “spacing exception” and “essential” conditions where appropriate. [\[67\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

**Fallback logic.**  
- If a component cannot responsively adapt without breaking accessibility or comprehension, switch to a simpler component (list, card, pagination) and preserve task completion. Carbon lists similar components as alternatives for organizing/navigating data (accordion/list/pagination/structured list). [\[136\]](https://carbondesignsystem.com/components/data-table/usage/)

**Failure conditions.**  
- Critical actions disappear at some breakpoints.  
- Focus ring or focused element becomes hidden under sticky elements. [\[90\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)  
- Dense mode creates targets smaller than 24×24 without spacing exception compliance. [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
- Responsive behavior differs between visually similar components (inconsistent collapse rules), causing user confusion. [\[137\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)

**Measurable thresholds.**  
- **Breakpoint coverage:** for each component, tests run at each declared breakpoint/window-size-class. [\[138\]](https://carbondesignsystem.com/elements/2x-grid/overview/)  
- **Responsiveness contract:** each component defines `minWidth`, `wrap`, `overflow`, and `collapse` rules; 100% required for stable status. [\[139\]](https://designsystem.digital.gov/components/status/)  
- **Accessibility under responsiveness:** target size and focus-not-obscured checks pass at each breakpoint. [\[140\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

**Implementation guidance for an AI operator pack.**  
- Add a “responsive solver” that:  
- maps requested layout to the system grid (12-col USWDS-like, 16-col Carbon-like, or window-size classes) [\[141\]](https://designsystem.digital.gov/utilities/layout-grid/)  
- applies collapse strategies: reorder, wrap, overflow, progressive disclosure (e.g., table toolbar overflow) [\[64\]](https://carbondesignsystem.com/components/data-table/usage/)  
- validates target sizes and focus visibility at each breakpoint. [\[140\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

**Test cases.**  
- A button group in a narrow side panel: the expert must recommend vertical stacking rules and spacing constraints, preserving hierarchy. [\[41\]](https://carbondesignsystem.com/components/button/usage/)  
- A data table with 12 columns on tablet width: the expert must recommend width-first placement, overflow/scroll strategy, and keep sorting/filtering controls keyboard-accessible. [\[142\]](https://carbondesignsystem.com/components/data-table/usage/)  
- A form with 2-column layout on desktop: ensure labels align; consider grid gutter modes if adopting Carbon-like grid approaches. [\[143\]](https://carbondesignsystem.com/elements/2x-grid/usage/)

## Dark mode and theming at component level

### Dark mode and theming at component level

**Definition.**  
Component-level theming is the token-driven mapping of component parts (surfaces, text, borders, icons, state layers, focus rings) to semantic design tokens in each theme (light, dark, high-contrast/forced colors), including how interactive states render. [\[144\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com)

**Why it matters for a Component Systems Expert.**  
Dark mode is not a palette swap; it changes contrast relationships, perceived elevation, and state visibility. Apple’s dark mode guidance emphasizes maintaining sufficient contrast (minimum 4.5:1, with stronger targets like 7:1 as a goal) and warns against bright flashes in “dark interface” contexts that can harm users with light sensitivity. [\[145\]](https://developer.apple.com/design/human-interface-guidelines/dark-mode?utm_source=chatgpt.com)

**Default rules.**  
1) **Theme via semantic tokens, not raw colors.** Use design tokens as the exchangeable, named variables that define color, spacing, typographic scale, etc.; adopt a standard token format when interoperating across tools. [\[146\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com)  
2) **Support system theme preferences.** Use `prefers-color-scheme` to respect user system light/dark preference. [\[147\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-color-scheme)  
3) **Support high contrast and user overrides.** Forced colors mode can be essential for readability; handle `forced-colors` and `prefers-contrast` gracefully and avoid “opting out” unless absolutely necessary. [\[148\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors)  
4) **Contrast gates apply in each theme.**  
- Text: ≥4.5:1 minimum (normal), ≥3:1 large text. [\[149\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)  
- Non-text UI boundaries/state indicators: ≥3:1. [\[150\]](https://w3c.github.io/wcag21/understanding/non-text-contrast.html)  
These must be validated independently per theme and per state (hover, focus, selected).  
5) **Avoid “white flashes” in dark mode.** For dark-interface contexts, ensure that loading states, skeletons, and overlays do not flash bright backgrounds; Apple’s dark interface criteria explicitly call out avoiding bright content that breaks the dark experience. [\[151\]](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria/?utm_source=chatgpt.com)  
6) **State visibility must survive theming.** If you use state overlays (hover/focus), they must remain perceivable in dark mode and in high-contrast modes; do not encode state only as subtle alpha on near-black backgrounds (operator-pack enforcement aligned with contrast and focus criteria). [\[152\]](https://w3c.github.io/wcag21/understanding/non-text-contrast.html)

**Exception rules.**  
- Brand colors may be used for accents, but if they break contrast, they cannot be used for essential text/boundaries; substitute semantic system colors. [\[153\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)  
- Disabled/inactive components are not subject to non-text contrast requirements, but must still be clearly non-interactive. [\[154\]](https://w3c.github.io/wcag21/understanding/non-text-contrast.html)  
- Data visualization color systems may require specialized palettes; ensure patterns are readable under `prefers-contrast` and forced colors where possible. (Heuristic anchored to forced-colors importance.) [\[155\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors)

**Fallback logic.**  
If theme tokens produce contrast failures:  
1) Switch from custom colors to system/semantic colors for foreground text and boundaries. [\[156\]](https://developer.apple.com/design/human-interface-guidelines/dark-mode?utm_source=chatgpt.com)  
2) If forced-colors is active, allow user-agent colors to drive borders/text rather than fighting the mode. [\[126\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors)  
3) Reduce visual reliance on color by adding shape/weight cues (borders, icons, labels). [\[157\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html)

**Failure conditions.**  
- Theme swap makes focused state indistinguishable. [\[90\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)  
- Skeleton/loading creates bright flashes in dark interface contexts. [\[158\]](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria/?utm_source=chatgpt.com)  
- Forced-colors mode renders key controls invisible due to author colors overriding user palette. [\[126\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors)

**Measurable thresholds.**  
- Contrast: meet WCAG contrast minimums in both light and dark themes. [\[116\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)  
- Forced colors: at least one successful pass in forced-colors active for core flows (auth, primary navigation, data table interactions). [\[159\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors)  
- Theme completeness: 100% of components map to semantic tokens; no hard-coded colors for essential UI. [\[160\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com)

**Implementation guidance for an AI operator pack.**  
- Store per-component token maps: `surface`, `onSurface`, `border`, `focusRing`, `stateOverlayHover`, `stateOverlayPressed`, `danger`, `warning`, etc.  
- Require theme testing across:  
- light/dark via `prefers-color-scheme` [\[147\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-color-scheme)  
- high contrast via `forced-colors` and `prefers-contrast` [\[161\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors)  
- minimum contrast gates (text + non-text). [\[116\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)

**Test cases.**  
- In dark mode, verify that a focused input’s border/focus ring is visible and not obscured under sticky headers. [\[162\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)  
- In forced-colors mode, verify that table borders, selection indicators, and focus states remain perceivable. [\[163\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors)  
- In dark mode, skeleton states should not render bright backgrounds; verify perceived dark continuity. [\[158\]](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria/?utm_source=chatgpt.com)

## Dashboard and dense-data component rules

### Dashboard and dense-data component rules

**Definition.**  
Dense-data component rules govern how tables/grids, filters, toolbars, pagination, batch actions, and inline actions behave in data-heavy screens (dashboards, admin panels), including performance strategies (progressive loading, virtualization) and accessibility constraints. [\[164\]](https://carbondesignsystem.com/components/data-table/usage/)

**Why it matters for a Component Systems Expert.**  
Dense-data UIs are where component systems are most likely to fail: keyboard navigation becomes complex, focus can be lost, selection states multiply, and performance constraints push teams toward custom grids that often degrade accessibility. Carbon’s data table documentation is unusually explicit about variants, row sizes, toolbar limits, sorting states, batch-mode effects, and loading strategies-representing the level of guidance required for a production “expert agent.” [\[142\]](https://carbondesignsystem.com/components/data-table/usage/)

**Default rules.**  
1) **Choose the correct table model: static table vs interactive grid.**  
- Use a semantic HTML table for primarily readable tabular data with normal tab order controls embedded.  
- Use an interactive grid pattern only when you truly need cell navigation and spreadsheet-like interaction. APG’s grid pattern exists for interactive tabular data; treat it as a “composite widget” with explicit keyboard rules. [\[165\]](https://www.w3.org/WAI/ARIA/apg/patterns/grid/?utm_source=chatgpt.com)  
2) **Data table variants are constrained and explicit.** Carbon defines default, selection, and expansion variants, and documents how they combine (e.g., expandable + selectable), including ordering of expansion vs selection icons. Use this “bounded variants + composition constraints” approach. [\[61\]](https://carbondesignsystem.com/components/data-table/usage/)  
3) **Row size and density are first-class.** Carbon data table supports five row sizes with rules: header row matches row size; extra-large recommended only for 2 lines of content. Adopt a similar “density dial” with clear pairing rules for toolbars/batch bars. [\[166\]](https://carbondesignsystem.com/components/data-table/usage/)  
4) **Toolbar action limits + overflow strategy.** Carbon explicitly recommends up to five actions in a table toolbar, using overflow menus/combo buttons for more actions; enforce this limit to keep toolbars scannable and responsive. [\[64\]](https://carbondesignsystem.com/components/data-table/usage/)  
5) **Sorting/selection states are fully specified.** Carbon defines three sorting states (unsorted, sorted-up, sorted-down) and selection semantics including an indeterminate header checkbox. These must be in the state matrix and tests. [\[167\]](https://carbondesignsystem.com/components/data-table/usage/)  
6) **Batch mode behavior disables conflicting actions.** Carbon specifies that when batch mode is active, single row actions (icons/overflow menus) should be disabled; enforce as a composition rule. [\[64\]](https://carbondesignsystem.com/components/data-table/usage/)  
7) **Loading strategy for dashboards:** prefer skeletons for data/container components during initial load and progressive loading; avoid skeletonizing menus/modals/toasts themselves. Skeleton time is short (seconds). [\[168\]](https://carbondesignsystem.com/patterns/loading-pattern/)  
8) **Keyboard support is non-negotiable.** Carbon data table accessibility guidance specifies keyboard reachability for sortable headers and that interactive controls inside cells are in the tab order. If you implement a grid, follow APG key bindings. [\[107\]](https://carbondesignsystem.com/components/data-table/accessibility/)  
9) **Touch target rules apply in dense toolbars.** Icon actions and inline row actions must still satisfy WCAG 2.2 target size minimum or spacing exceptions; if impossible, provide alternative controls (row action menu) that meet the criterion. [\[67\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

**Exception rules.**  
- **Essential dense targets:** WCAG acknowledges some dense targets may be essential (e.g., maps, dense data viz) but encourages equivalent functionality where practical. This is relevant for very dense data visualization tooltips or micro-actions. [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
- **Virtualization/performance:** if virtualization is needed, you must preserve focus order and screen reader navigation; treat virtualization as a high-risk feature requiring explicit testing gates (heuristic reinforced by the complexity noted in dense-data keyboard patterns and real-world data grid keyboard models). [\[169\]](https://www.w3.org/WAI/ARIA/apg/patterns/grid/?utm_source=chatgpt.com)

**Fallback logic.**  
If an interactive grid cannot be made accessible or testable:  
- Fall back to:  
- plain table + pagination,  
- table + row-level disclosure panel, or  
- list/card presentation.  
Carbon points to pagination and other components for data navigation; pagination is treated as a separate component. [\[170\]](https://carbondesignsystem.com/components/data-table/accessibility/)

**Failure conditions.**  
- “Spreadsheet replacement” misuse: trying to replicate Excel interactions without a full grid/a11y model. Carbon explicitly says not to use data tables as a spreadsheet replacement. [\[171\]](https://carbondesignsystem.com/components/data-table/usage/)  
- Keyboard cannot reach column menus, filters, or row actions. [\[172\]](https://carbondesignsystem.com/components/data-table/accessibility/)  
- Indeterminate selection not supported. [\[167\]](https://carbondesignsystem.com/components/data-table/usage/)  
- Overloaded toolbar (\>5 actions) without overflow. [\[64\]](https://carbondesignsystem.com/components/data-table/usage/)  
- Density breaks target size. [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

**Measurable thresholds.**  
- **Row-size support:** must implement the declared set of row sizes; header row must match; toolbar pairing rules enforced. [\[173\]](https://carbondesignsystem.com/components/data-table/usage/)  
- **Toolbar action limit:** default ≤5 visible actions; overflow for more. [\[64\]](https://carbondesignsystem.com/components/data-table/usage/)  
- **Keyboard coverage:** 100% of table interactions reachable via keyboard (sort, select, expand, pagination, row actions). [\[174\]](https://carbondesignsystem.com/components/data-table/accessibility/)  
- **Target size compliance:** all actionable icons meet 24×24 or spacing/equivalent exception. [\[115\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
- **Loading correctness:** skeleton usage limited to appropriate component categories and short duration. [\[168\]](https://carbondesignsystem.com/patterns/loading-pattern/)

**Implementation guidance for an AI operator pack.**  
- Provide a “dense-data blueprint” with required subcomponents: toolbar, filter/search, sorting, pagination, selection, batch actions, row actions, loading, empty. Carbon’s data table page offers an example of enumerating these behaviors as universal rules. [\[134\]](https://carbondesignsystem.com/components/data-table/usage/)  
- Embed APG grid pattern and keyboard interface rules as references whenever a component is classified as a composite widget. [\[83\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com)  
- Require output of “interaction map” (keyboard + pointer) per dense component. Carbon explicitly lists keyboard reachability for sortable headers and tab order strategies. [\[175\]](https://carbondesignsystem.com/components/data-table/accessibility/)

**Test cases.**  
- A selectable + expandable table: verify icon order (expand before select), indeterminate header checkbox, and that batch mode disables row actions. [\[64\]](https://carbondesignsystem.com/components/data-table/usage/)  
- Sorting: verify unsorted/sorted-up/sorted-down states and keyboard operation (tab to header, activate sort). [\[175\]](https://carbondesignsystem.com/components/data-table/accessibility/)  
- Dense icon actions: verify 24×24 minimum or spacing exception and keyboard access. [\[176\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

## Failure taxonomy and operator pack deliverables

### Failure modes in component systems

**Definition.**  
Failure modes are the recurring ways component systems degrade in production: drift, inconsistency, inaccessible behavior, variant explosion, broken theming, and documentation rot-leading teams to bypass the system and rebuild UI ad hoc. [\[177\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)

**Why it matters for a Component Systems Expert.**  
The expert agent must not only recommend the “happy path,” but detect early signals of drift and enforce guardrails. NNGroup explicitly argues that design systems fail without someone enforcing rules; without enforcement, teams interpret components differently, creating inconsistencies and accessibility gaps. [\[178\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)

**Default rules.**  
1) **Drift detection is mandatory.** Track component duplication, variant proliferation, and usage divergence; trigger governance review when thresholds exceeded (see Topic 1/10). [\[179\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)  
2) **Accessibility regressions block release for stable components.** WCAG criteria are testable; accessibility is not optional and should be integrated “in all phases,” consistent with published accessibility-process documentation (e.g., USWDS). [\[180\]](https://www.w3.org/TR/WCAG22/)  
3) **Documentation drift is treated as a production defect.** If behavior changes without docs, users will misuse components; treat doc updates as part of the same change. [\[19\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)  
4) **Token drift is treated as a contract violation.** If teams hard-code values, theming and platform adaptation fail; use design token standards to keep interoperability. [\[146\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com)  
5) **Composite widgets are high-risk.** Any grid/combobox/menu/dialog built outside APG patterns is likely to fail keyboard/focus expectations; require explicit APG alignment and tests. [\[181\]](https://www.w3.org/WAI/ARIA/apg/?utm_source=chatgpt.com)

**Exception rules.**  
- Emergency product fixes may temporarily violate some system rules, but must create follow-up tasks for remediation and must not become “silent defaults.” (Governance exception.) [\[39\]](https://designsystem.digital.gov/components/lifecycle/)

**Fallback logic.**  
When failure risk is high:  
- Prefer stable, simpler components and progressive disclosure patterns.  
- Freeze new variants and route proposals through lifecycle. [\[182\]](https://designsystem.digital.gov/components/status/)

**Failure conditions.**  
- Teams implement “almost the same component” in multiple places due to missing or slow governance. [\[37\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)  
- Component states differ across repos (hover/focus/pressed inconsistent), causing usability and accessibility issues. [\[183\]](https://www.nngroup.com/articles/button-states-communicate-interaction/?utm_source=chatgpt.com)  
- Dark mode breaks contrast or causes bright flashes. [\[184\]](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria/?utm_source=chatgpt.com)  
- Dense-data grids trap keyboard users or lose focus. [\[185\]](https://www.w3.org/WAI/ARIA/apg/patterns/grid/?utm_source=chatgpt.com)

**Measurable thresholds.**  
- **Variant explosion threshold:** if any component exceeds variant/size budgets, it must be reviewed and consolidated. [\[186\]](https://carbondesignsystem.com/components/button/usage/)  
- **A11y regression threshold:** any new WCAG failure in core flows is release-blocking for stable components. [\[187\]](https://www.w3.org/TR/WCAG22/)  
- **Doc drift threshold:** any behavior change without doc update is a defect. [\[39\]](https://designsystem.digital.gov/components/lifecycle/)

**Implementation guidance for an AI operator pack.**  
- Implement automated gates:  
- token linting (no hard-coded values) [\[53\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com)  
- accessibility linting/scanning (ARIA validity, contrast, target size) [\[188\]](https://www.w3.org/TR/html-aria/)  
- keyboard interaction tests for composites (APG alignment) [\[83\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com)  
- state-matrix completeness checks. [\[189\]](https://www.nngroup.com/articles/button-states-communicate-interaction/?utm_source=chatgpt.com)  
- Require the agent to produce a “risk report” on any proposed new component/variant: expected state multiplication, a11y complexity, responsive/theming impacts. [\[190\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)

**Test cases.**  
- A team proposes a custom grid to mimic Excel. The expert must warn about composite-widget requirements, require APG compliance, and otherwise recommend a simpler table + pagination approach. [\[191\]](https://www.w3.org/WAI/ARIA/apg/patterns/grid/?utm_source=chatgpt.com)  
- A theme override adds hard-coded colors. The expert must refactor to tokens and re-run contrast checks in light/dark/forced-colors. [\[192\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com)  
- A form error state is indicated only by red border. The expert must require textual error identification and (ideally) suggestions. [\[193\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html)

### Operator pack markdown deliverables

The following deliverables are designed to be copied into your operator-pack repository as strict policy modules. They are intentionally “rules-first” and can be used as system prompts, validators, or spec templates.

#### `component-systems-expert.md`

**Purpose:** Canonical operating spec for the expert agent: decision loop, budgets, cross-cutting rules, and required artifacts.

**Contents to include (outline):**  
- Mission and non-goals  
- Canonical decision loop (reuse → compose → extend → propose) [\[16\]](https://designsystem.digital.gov/components/lifecycle/)  
- Variant/size/state budgets anchored to mature-system examples (buttons, tables, forms) [\[194\]](https://carbondesignsystem.com/components/button/usage/)  
- Accessibility gates (contrast, focus, target size, errors, ARIA rules) [\[195\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)  
- Responsive and theming requirements (breakpoints/window size classes, prefers-color-scheme/forced-colors) [\[196\]](https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com)  
- Dense-data rules (table toolbars, selection/sorting states, loading strategy) [\[197\]](https://carbondesignsystem.com/components/data-table/usage/)  
- Appendices A–E (below)

#### `component-inventory-rules.md`

**Purpose:** Machine-actionable policies for building and maintaining the component registry, including lifecycle and status gates.

**Minimum rules to include:**  
- Registry schema and required fields [\[198\]](https://designsystem.digital.gov/)  
- Lifecycle phases and promotion requirements (proposal → stable → deprecated) [\[16\]](https://designsystem.digital.gov/components/lifecycle/)  
- De-duplication policy and consolidation workflow [\[18\]](https://www.thinkcompany.com/guides/a-guide-to-design-systems/?utm_source=chatgpt.com)  
- Governance triggers and thresholds (coverage ratio, duplication budget) [\[37\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)

#### `variant-and-state-rules.md`

**Purpose:** Enforceable variant taxonomy, size scale policies, and required state coverage.

**Minimum rules to include:**  
- Intent-driven variant taxonomy + budgets [\[72\]](https://carbondesignsystem.com/components/button/usage/)  
- Size scales anchored to mature systems (button heights; table row sizes) [\[199\]](https://v10.carbondesignsystem.com/components/button/style/)  
- State matrix per component type (baseline + specialized) [\[200\]](https://carbondesignsystem.com/components/form/usage/)  
- State precedence and overlap rules (disabled overrides hover/pressed; batch mode disables row actions) [\[201\]](https://carbondesignsystem.com/patterns/disabled-states/)

#### `responsive-component-rules.md`

**Purpose:** Breakpoints/window-size-class rules, component collapse strategies, and responsive testing gates.

**Minimum rules to include:**  
- Declared breakpoint system (Material window size classes OR system grid breakpoints) [\[202\]](https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com)  
- Collapse strategies: wrap → overflow → progressive disclosure [\[203\]](https://carbondesignsystem.com/components/data-table/usage/)  
- Accessibility under responsiveness: target sizes and focus-not-obscured gates [\[140\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

#### `component-accessibility-rules.md`

**Purpose:** Component-type accessibility requirements (names, roles, keyboard, focus, errors, contrast, target size).

**Minimum rules to include:**  
- Native-first + ARIA conformance rules [\[89\]](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)  
- Contrast minimums (text and non-text) [\[116\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)  
- Target size minimum and exceptions [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
- Error summary + inline errors pattern for forms (page-level) [\[204\]](https://design-system.service.gov.uk/components/error-summary/)  
- Composite widget keyboard patterns (APG) [\[83\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com)  
- Forced colors and prefers-contrast support [\[205\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors)

#### `component-failure-taxonomy.md`

**Purpose:** Structured catalog of failure modes with detection signals and mitigations.

**Minimum categories to include:**  
- Inventory failures (duplication, missing status) [\[25\]](https://www.thinkcompany.com/guides/a-guide-to-design-systems/?utm_source=chatgpt.com)  
- Variant/state failures (explosion, missing focus/error/loading) [\[206\]](https://www.nngroup.com/articles/button-states-communicate-interaction/?utm_source=chatgpt.com)  
- Accessibility failures (contrast, target size, ARIA misuse, keyboard traps) [\[207\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)  
- Theming failures (dark-mode contrast, forced-colors invisibility, bright flashes) [\[208\]](https://developer.apple.com/design/human-interface-guidelines/dark-mode?utm_source=chatgpt.com)  
- Dense-data failures (grid misuse, selection/sorting bugs, keyboard reachability) [\[209\]](https://carbondesignsystem.com/components/data-table/usage/)  
- Governance failures (no enforcer, slow contribution, doc drift) [\[19\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com)

#### `component-test-cases.md`

**Purpose:** Executable test-case library (manual + automated) structured by component type and risk.

**Minimum sections to include:**  
- State-matrix tests (each required state) [\[189\]](https://www.nngroup.com/articles/button-states-communicate-interaction/?utm_source=chatgpt.com)  
- Keyboard navigation tests for composites (APG patterns) [\[83\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com)  
- Contrast + target-size tests [\[210\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)  
- Responsive tests across breakpoints/window size classes [\[211\]](https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com)  
- Theme tests: light/dark + forced-colors + prefers-contrast [\[212\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-color-scheme)  
- Dense-data interaction tests (sorting/selection/batch/expansion/pagination) [\[213\]](https://carbondesignsystem.com/components/data-table/usage/)

**A. Condensed operating spec**

**Role.** You are the Component Systems Expert. Your output must be implementation-ready: component choice, variants/sizes, full state model, responsive behavior, theming behavior, accessibility behavior, and a test plan.

**Hard gates (non-negotiable).**  
- Use **inventory-first**: reuse stable components by default; anything else is composition or proposal. [\[27\]](https://designsystem.digital.gov/components/status/)  
- Use **native-first accessibility semantics**; ARIA only when needed and must conform to HTML-ARIA and APG patterns. [\[214\]](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)  
- Meet **WCAG 2.2 thresholds** for contrast, target size, focus, and error messaging patterns. [\[120\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)  
- Enforce **variant/size budgets** and require full state/a11y/responsive/theming spec for any new variant. [\[194\]](https://carbondesignsystem.com/components/button/usage/)  
- Dense-data components must implement explicit sorting/selection/loading/pagination behavior and keyboard access. [\[142\]](https://carbondesignsystem.com/components/data-table/usage/)

**Decision outputs must always include:**  
- Component decision (reuse/compose/extend/propose)  
- Variant + size selection with rationale  
- Required states + precedence rules  
- Accessibility spec (name/role/keyboard/focus/errors/contrast/target size)  
- Responsive behavior spec (collapse rules, overflow, min widths)  
- Theme behavior spec (light/dark/forced-colors)  
- Test cases (minimum 5 per component; more for composites)

**B. Component decision tree**

Start  
→ **Is there an existing Stable inventory component that matches the user task?** (function, not shape)  
- Yes → **Reuse**  
- Does it need only token/theme changes? → Apply tokens  
- Does it need a minor behavior extension? → Propose extension (no new component)  
- No → **Can the behavior be composed from existing primitives/components with documented rules?**  
- Yes → **Compose** (document composition constraints and required states)  
- No → **Is this a known pattern class (combobox/grid/dialog/menu/tabs)?**  
- Yes → Implement strictly per APG pattern and HTML-ARIA rules; then file proposal for inventory promotion  
- No → **Propose new component**  
- Must include: variants/sizes/state model/a11y/responsive/theme/tokens/tests + lifecycle status “Proposal”

At every branch → Run gates: contrast, target size, focus-not-obscured, error messaging, keyboard completeness, token compliance.

**C. Required state matrix by component type**

Legend: **R** = required, **C** = conditional (depends on usage), **N/A** = not applicable

| Component type               | Enabled | Hover | Pressed    | Focus             | Disabled | Read-only | Loading | Skeleton     | Error/Invalid            | Warning     | Selected/Checked | Indeterminate     | Expanded/Open | Empty |
|------------------------------|---------|-------|------------|-------------------|----------|-----------|---------|--------------|--------------------------|-------------|------------------|-------------------|---------------|-------|
| Button                       | R       | C     | R          | R                 | R        | N/A       | C       | C (rare)     | N/A                      | N/A         | C (toggle)       | N/A               | N/A           | N/A   |
| Icon button                  | R       | C     | R          | R                 | R        | N/A       | C       | C (rare)     | N/A                      | N/A         | C                | N/A               | N/A           | N/A   |
| Link                         | R       | C     | C          | R                 | C (rare) | N/A       | N/A     | N/A          | N/A                      | N/A         | Visited (C)      | N/A               | N/A           | N/A   |
| Text input / textarea        | R       | C     | Active (R) | R                 | R        | C         | C       | C            | R                        | C           | N/A              | N/A               | N/A           | C     |
| Select / combobox            | R       | C     | C          | R                 | R        | C         | C       | C            | R                        | C           | R                | N/A               | Open (R)      | C     |
| Checkbox                     | R       | C     | C          | R                 | R        | C         | C       | C            | C                        | C           | R                | C (tri-state)     | N/A           | N/A   |
| Radio group                  | R       | C     | C          | R                 | R        | C         | C       | C            | C                        | C           | R                | N/A               | N/A           | N/A   |
| Switch / toggle              | R       | C     | R          | R                 | R        | C         | C       | C            | C                        | C           | R                | N/A               | N/A           | N/A   |
| Tabs                         | R       | C     | C          | R                 | C        | N/A       | C       | C            | N/A                      | N/A         | R (active tab)   | N/A               | N/A           | N/A   |
| Menu / dropdown              | R       | C     | C          | R                 | C        | N/A       | C       | N/A          | N/A                      | N/A         | C                | N/A               | Open (R)      | C     |
| Dialog / modal               | R       | N/A   | N/A        | R                 | N/A      | N/A       | C       | C (internal) | C                        | C           | N/A              | N/A               | Open (R)      | N/A   |
| Alert / toast / notification | N/A     | N/A   | N/A        | C (if actionable) | N/A      | N/A       | C       | C (rare)     | Error (R if error alert) | Warning (C) | N/A              | N/A               | N/A           | N/A   |
| Data table (non-grid)        | R       | C     | C          | R                 | C        | N/A       | R       | R            | C                        | C           | C                | C (header select) | C (expansion) | R     |
| Data grid (interactive)      | R       | C     | C          | R                 | C        | N/A       | R       | R            | C                        | C           | C                | C                 | C             | R     |

Notes the expert must enforce:  
- “Hover” is conditional and must not be the only discoverability mechanism. [\[215\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com)  
- Loading/skeleton usage is constrained; avoid skeletonizing menus/modals/toasts themselves. [\[88\]](https://carbondesignsystem.com/patterns/loading-pattern/)  
- Target-size minimum still applies; dense UIs must satisfy size or spacing exceptions. [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
- Data-grid behavior must follow APG grid keyboard interactions if implemented as a composite widget. [\[216\]](https://www.w3.org/WAI/ARIA/apg/patterns/grid/?utm_source=chatgpt.com)

**D. Component audit checklist**

Inventory and governance  
- Component exists in registry with status and owner. [\[27\]](https://designsystem.digital.gov/components/status/)  
- “When to use / when not to use” documented. [\[45\]](https://carbondesignsystem.com/components/data-table/usage/)  
- Variant/size budgets respected; new variants follow proposal workflow. [\[217\]](https://designsystem.digital.gov/components/lifecycle/)  
- Token mapping documented; no hard-coded spacing/colors for essential UI. [\[53\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com)

States and behavior  
- All required states in matrix implemented with precedence rules. [\[218\]](https://carbondesignsystem.com/components/form/usage/)  
- Loading strategy correct (skeleton vs spinner; duration appropriate; no skeleton for prohibited surfaces). [\[168\]](https://carbondesignsystem.com/patterns/loading-pattern/)  
- Dense-data behavior matches rules (toolbar action cap, selection/sorting states, batch-mode disables row actions). [\[219\]](https://carbondesignsystem.com/components/data-table/usage/)

Accessibility  
- Native-first semantics; ARIA conformance check passed. [\[220\]](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)  
- Keyboard operation complete (including composites per APG). [\[83\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com)  
- Focus visible and not obscured. [\[90\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)  
- Contrast meets WCAG minimums (text + non-text). [\[116\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)  
- Target sizes meet 24×24 or spacing/equivalent exceptions. [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
- Errors are text-based, associated, actionable; page-level error summary pattern used where appropriate. [\[221\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html)

Responsive and theming  
- Responsive behavior defined at each breakpoint/window-size-class. [\[211\]](https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com)  
- Actions remain reachable when collapsed into overflow; no “hover-only” controls. [\[222\]](https://carbondesignsystem.com/components/data-table/usage/)  
- Light/dark supported via `prefers-color-scheme`; forced-colors and prefers-contrast tested. [\[223\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-color-scheme)

**E. 20 stress-test prompts**

1\) “We need a new ‘super-primary’ button for marketing AND product UI-should it be one component?”  
2) “This icon-only action in a dense table row is 16×16. Make it compliant without changing visuals.” [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
3) “Add 11 actions to the data table toolbar, all visible on desktop.” [\[64\]](https://carbondesignsystem.com/components/data-table/usage/)  
4) “Design a selectable + expandable table where ‘select all’ needs an indeterminate state.” [\[64\]](https://carbondesignsystem.com/components/data-table/usage/)  
5) “A sticky header hides the focus ring on inputs when tabbing. Fix it per WCAG 2.2.” [\[117\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com)  
6) “We want a custom combobox that supports typeahead, multi-select, and async loading. Specify keyboard + ARIA.” [\[224\]](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/?utm_source=chatgpt.com)  
7) “In dark mode, a skeleton loader flashes bright white on first paint. Prevent this.” [\[158\]](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria/?utm_source=chatgpt.com)  
8) “Forced-colors mode removes our button borders and users can’t see focus. What do we do?” [\[126\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors)  
9) “A team created three different DatePicker components. Consolidate into inventory with minimal breakage.” [\[18\]](https://www.thinkcompany.com/guides/a-guide-to-design-systems/?utm_source=chatgpt.com)  
10) “A ‘disabled’ field must remain readable by screen readers. How should it be modeled?” [\[225\]](https://carbondesignsystem.com/patterns/disabled-states/)  
11) “Our table is being used as an Excel replacement with inline cell editing. Should we keep it?” [\[171\]](https://carbondesignsystem.com/components/data-table/usage/)  
12) “Make the form error strategy: inline errors + page summary + suggested fixes.” [\[226\]](https://design-system.service.gov.uk/components/error-summary/)  
13) “Make the spacing system consistent: convert random 14px gaps into tokenized spacing.” [\[227\]](https://designsystem.digital.gov/design-tokens/spacing-units/?utm_source=chatgpt.com)  
14) “A mobile layout needs the same actions as desktop, but only 2 can fit. Decide collapse strategy.” [\[228\]](https://carbondesignsystem.com/components/data-table/usage/)  
15) “A list of links in text fails target size. Apply WCAG exceptions correctly.” [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
16) “We added a custom ARIA role to a native element and now screen readers behave oddly. Diagnose.” [\[229\]](https://www.w3.org/TR/html-aria/)  
17) “Data table sorting needs three states + keyboard toggle. Specify state model and tests.” [\[219\]](https://carbondesignsystem.com/components/data-table/usage/)  
18) “A dense toolbar has adjacent small icon targets. Use spacing exception rather than resizing-validate.” [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)  
19) “Define governance workflow for adding a new component, including community comment period and status.” [\[16\]](https://designsystem.digital.gov/components/lifecycle/)  
20) “Our design tokens need to be shared across tools. Choose a token format and validation approach.” [\[230\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com)

[\[1\]](https://designsystem.digital.gov/components/status/) [\[12\]](https://designsystem.digital.gov/components/status/) [\[13\]](https://designsystem.digital.gov/components/status/) [\[14\]](https://designsystem.digital.gov/components/status/) [\[27\]](https://designsystem.digital.gov/components/status/) [\[28\]](https://designsystem.digital.gov/components/status/) [\[50\]](https://designsystem.digital.gov/components/status/) [\[91\]](https://designsystem.digital.gov/components/status/) [\[139\]](https://designsystem.digital.gov/components/status/) [\[182\]](https://designsystem.digital.gov/components/status/) https://designsystem.digital.gov/components/status/

<https://designsystem.digital.gov/components/status/>

[\[2\]](https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com) [\[127\]](https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com) [\[129\]](https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com) [\[196\]](https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com) [\[202\]](https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com) [\[211\]](https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com) Applying layout – Material Design 3

<https://m3.material.io/foundations/layout/applying-layout/window-size-classes?utm_source=chatgpt.com>

[\[3\]](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria/?utm_source=chatgpt.com) [\[151\]](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria/?utm_source=chatgpt.com) [\[158\]](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria/?utm_source=chatgpt.com) [\[184\]](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria/?utm_source=chatgpt.com) Dark Interface evaluation criteria - Manage App Accessibility

<https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria/?utm_source=chatgpt.com>

[\[4\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) [\[22\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) [\[49\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) [\[67\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) [\[103\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) [\[110\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) [\[115\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) [\[123\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) [\[140\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) [\[176\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html

<https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html>

[\[5\]](https://carbondesignsystem.com/components/data-table/accessibility/) [\[107\]](https://carbondesignsystem.com/components/data-table/accessibility/) [\[170\]](https://carbondesignsystem.com/components/data-table/accessibility/) [\[172\]](https://carbondesignsystem.com/components/data-table/accessibility/) [\[174\]](https://carbondesignsystem.com/components/data-table/accessibility/) [\[175\]](https://carbondesignsystem.com/components/data-table/accessibility/) https://carbondesignsystem.com/components/data-table/accessibility/

<https://carbondesignsystem.com/components/data-table/accessibility/>

[\[6\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com) [\[85\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com) [\[86\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com) [\[90\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com) [\[92\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com) [\[117\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com) [\[135\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com) [\[162\]](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com) Understanding SC 2.4.11: Focus Not Obscured (Minimum) ...

<https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html?utm_source=chatgpt.com>

[\[7\]](https://carbondesignsystem.com/components/button/usage/) [\[41\]](https://carbondesignsystem.com/components/button/usage/) [\[57\]](https://carbondesignsystem.com/components/button/usage/) [\[58\]](https://carbondesignsystem.com/components/button/usage/) [\[59\]](https://carbondesignsystem.com/components/button/usage/) [\[60\]](https://carbondesignsystem.com/components/button/usage/) [\[71\]](https://carbondesignsystem.com/components/button/usage/) [\[72\]](https://carbondesignsystem.com/components/button/usage/) [\[74\]](https://carbondesignsystem.com/components/button/usage/) [\[76\]](https://carbondesignsystem.com/components/button/usage/) [\[186\]](https://carbondesignsystem.com/components/button/usage/) [\[194\]](https://carbondesignsystem.com/components/button/usage/) https://carbondesignsystem.com/components/button/usage/

<https://carbondesignsystem.com/components/button/usage/>

[\[8\]](https://carbondesignsystem.com/components/data-table/usage/) [\[29\]](https://carbondesignsystem.com/components/data-table/usage/) [\[35\]](https://carbondesignsystem.com/components/data-table/usage/) [\[44\]](https://carbondesignsystem.com/components/data-table/usage/) [\[45\]](https://carbondesignsystem.com/components/data-table/usage/) [\[47\]](https://carbondesignsystem.com/components/data-table/usage/) [\[61\]](https://carbondesignsystem.com/components/data-table/usage/) [\[64\]](https://carbondesignsystem.com/components/data-table/usage/) [\[73\]](https://carbondesignsystem.com/components/data-table/usage/) [\[132\]](https://carbondesignsystem.com/components/data-table/usage/) [\[134\]](https://carbondesignsystem.com/components/data-table/usage/) [\[136\]](https://carbondesignsystem.com/components/data-table/usage/) [\[142\]](https://carbondesignsystem.com/components/data-table/usage/) [\[164\]](https://carbondesignsystem.com/components/data-table/usage/) [\[166\]](https://carbondesignsystem.com/components/data-table/usage/) [\[167\]](https://carbondesignsystem.com/components/data-table/usage/) [\[171\]](https://carbondesignsystem.com/components/data-table/usage/) [\[173\]](https://carbondesignsystem.com/components/data-table/usage/) [\[197\]](https://carbondesignsystem.com/components/data-table/usage/) [\[203\]](https://carbondesignsystem.com/components/data-table/usage/) [\[209\]](https://carbondesignsystem.com/components/data-table/usage/) [\[213\]](https://carbondesignsystem.com/components/data-table/usage/) [\[219\]](https://carbondesignsystem.com/components/data-table/usage/) [\[222\]](https://carbondesignsystem.com/components/data-table/usage/) [\[228\]](https://carbondesignsystem.com/components/data-table/usage/) https://carbondesignsystem.com/components/data-table/usage/

<https://carbondesignsystem.com/components/data-table/usage/>

[\[9\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com) [\[48\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com) [\[53\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com) [\[54\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com) [\[56\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com) [\[68\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com) [\[144\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com) [\[146\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com) [\[160\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com) [\[192\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com) [\[230\]](https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com) Design Tokens Format Module 2025.10

<https://www.designtokens.org/tr/drafts/format/?utm_source=chatgpt.com>

[\[10\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com) [\[46\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com) [\[77\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com) [\[83\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com) [\[100\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com) [\[113\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com) [\[122\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com) [\[133\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com) [\[215\]](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com) Developing a Keyboard Interface \| APG \| WAI

<https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/?utm_source=chatgpt.com>

[\[11\]](https://www.w3.org/WAI/ARIA/apg/?utm_source=chatgpt.com) [\[94\]](https://www.w3.org/WAI/ARIA/apg/?utm_source=chatgpt.com) [\[119\]](https://www.w3.org/WAI/ARIA/apg/?utm_source=chatgpt.com) [\[181\]](https://www.w3.org/WAI/ARIA/apg/?utm_source=chatgpt.com) ARIA Authoring Practices Guide \| APG \| WAI

<https://www.w3.org/WAI/ARIA/apg/?utm_source=chatgpt.com>

[\[15\]](https://designsystem.digital.gov/) [\[43\]](https://designsystem.digital.gov/) [\[198\]](https://designsystem.digital.gov/) https://designsystem.digital.gov/

<https://designsystem.digital.gov/>

[\[16\]](https://designsystem.digital.gov/components/lifecycle/) [\[21\]](https://designsystem.digital.gov/components/lifecycle/) [\[23\]](https://designsystem.digital.gov/components/lifecycle/) [\[31\]](https://designsystem.digital.gov/components/lifecycle/) [\[33\]](https://designsystem.digital.gov/components/lifecycle/) [\[36\]](https://designsystem.digital.gov/components/lifecycle/) [\[39\]](https://designsystem.digital.gov/components/lifecycle/) [\[52\]](https://designsystem.digital.gov/components/lifecycle/) [\[69\]](https://designsystem.digital.gov/components/lifecycle/) [\[70\]](https://designsystem.digital.gov/components/lifecycle/) [\[217\]](https://designsystem.digital.gov/components/lifecycle/) https://designsystem.digital.gov/components/lifecycle/

<https://designsystem.digital.gov/components/lifecycle/>

[\[17\]](https://www.w3.org/TR/WCAG22/) [\[38\]](https://www.w3.org/TR/WCAG22/) [\[55\]](https://www.w3.org/TR/WCAG22/) [\[96\]](https://www.w3.org/TR/WCAG22/) [\[97\]](https://www.w3.org/TR/WCAG22/) [\[180\]](https://www.w3.org/TR/WCAG22/) [\[187\]](https://www.w3.org/TR/WCAG22/) https://www.w3.org/TR/WCAG22/

<https://www.w3.org/TR/WCAG22/>

[\[18\]](https://www.thinkcompany.com/guides/a-guide-to-design-systems/?utm_source=chatgpt.com) [\[24\]](https://www.thinkcompany.com/guides/a-guide-to-design-systems/?utm_source=chatgpt.com) [\[25\]](https://www.thinkcompany.com/guides/a-guide-to-design-systems/?utm_source=chatgpt.com) [\[30\]](https://www.thinkcompany.com/guides/a-guide-to-design-systems/?utm_source=chatgpt.com) A guide to meeting your design system goals

<https://www.thinkcompany.com/guides/a-guide-to-design-systems/?utm_source=chatgpt.com>

[\[19\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com) [\[20\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com) [\[26\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com) [\[32\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com) [\[37\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com) [\[40\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com) [\[51\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com) [\[137\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com) [\[177\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com) [\[178\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com) [\[179\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com) [\[190\]](https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com) Your Design System Needs an Enforcer

<https://www.nngroup.com/articles/design-system-enforcer/?utm_source=chatgpt.com>

[\[34\]](https://medium.com/eightshapes-llc/defining-design-system-contributions-eb48e00e8898?utm_source=chatgpt.com) Defining Design System Contributions \| by Nathan Curtis

<https://medium.com/eightshapes-llc/defining-design-system-contributions-eb48e00e8898?utm_source=chatgpt.com>

[\[42\]](https://carbondesignsystem.com/elements/2x-grid/overview/) [\[131\]](https://carbondesignsystem.com/elements/2x-grid/overview/) [\[138\]](https://carbondesignsystem.com/elements/2x-grid/overview/) https://carbondesignsystem.com/elements/2x-grid/overview/

<https://carbondesignsystem.com/elements/2x-grid/overview/>

[\[62\]](https://v10.carbondesignsystem.com/components/button/style/) [\[66\]](https://v10.carbondesignsystem.com/components/button/style/) [\[199\]](https://v10.carbondesignsystem.com/components/button/style/) https://v10.carbondesignsystem.com/components/button/style/

<https://v10.carbondesignsystem.com/components/button/style/>

[\[63\]](https://carbondesignsystem.com/elements/spacing/overview/?utm_source=chatgpt.com) [\[75\]](https://carbondesignsystem.com/elements/spacing/overview/?utm_source=chatgpt.com) Spacing

<https://carbondesignsystem.com/elements/spacing/overview/?utm_source=chatgpt.com>

[\[65\]](https://carbondesignsystem.com/components/button/style/) https://carbondesignsystem.com/components/button/style/

<https://carbondesignsystem.com/components/button/style/>

[\[78\]](https://www.nngroup.com/articles/button-states-communicate-interaction/?utm_source=chatgpt.com) [\[79\]](https://www.nngroup.com/articles/button-states-communicate-interaction/?utm_source=chatgpt.com) [\[183\]](https://www.nngroup.com/articles/button-states-communicate-interaction/?utm_source=chatgpt.com) [\[189\]](https://www.nngroup.com/articles/button-states-communicate-interaction/?utm_source=chatgpt.com) [\[206\]](https://www.nngroup.com/articles/button-states-communicate-interaction/?utm_source=chatgpt.com) Button States: Communicate Interaction

<https://www.nngroup.com/articles/button-states-communicate-interaction/?utm_source=chatgpt.com>

[\[80\]](https://carbondesignsystem.com/patterns/disabled-states/) [\[201\]](https://carbondesignsystem.com/patterns/disabled-states/) [\[225\]](https://carbondesignsystem.com/patterns/disabled-states/) https://carbondesignsystem.com/patterns/disabled-states/

<https://carbondesignsystem.com/patterns/disabled-states/>

[\[81\]](https://carbondesignsystem.com/components/form/usage/) [\[95\]](https://carbondesignsystem.com/components/form/usage/) [\[200\]](https://carbondesignsystem.com/components/form/usage/) [\[218\]](https://carbondesignsystem.com/components/form/usage/) https://carbondesignsystem.com/components/form/usage/

<https://carbondesignsystem.com/components/form/usage/>

[\[82\]](https://www.w3.org/WAI/ARIA/apg/patterns/?utm_source=chatgpt.com) Patterns \| APG \| WAI

<https://www.w3.org/WAI/ARIA/apg/patterns/?utm_source=chatgpt.com>

[\[84\]](https://carbondesignsystem.com/patterns/loading-pattern/) [\[88\]](https://carbondesignsystem.com/patterns/loading-pattern/) [\[168\]](https://carbondesignsystem.com/patterns/loading-pattern/) https://carbondesignsystem.com/patterns/loading-pattern/

<https://carbondesignsystem.com/patterns/loading-pattern/>

[\[87\]](https://w3c.github.io/wcag21/understanding/non-text-contrast.html) [\[102\]](https://w3c.github.io/wcag21/understanding/non-text-contrast.html) [\[109\]](https://w3c.github.io/wcag21/understanding/non-text-contrast.html) [\[150\]](https://w3c.github.io/wcag21/understanding/non-text-contrast.html) [\[152\]](https://w3c.github.io/wcag21/understanding/non-text-contrast.html) [\[154\]](https://w3c.github.io/wcag21/understanding/non-text-contrast.html) https://w3c.github.io/wcag21/understanding/non-text-contrast.html

<https://w3c.github.io/wcag21/understanding/non-text-contrast.html>

[\[89\]](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) [\[98\]](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) [\[111\]](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) [\[214\]](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) [\[220\]](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA

<https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA>

[\[93\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html) [\[104\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html) [\[114\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html) [\[118\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html) [\[157\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html) [\[193\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html) [\[221\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html) https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html

<https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html>

[\[99\]](https://www.w3.org/TR/html-aria/) [\[121\]](https://www.w3.org/TR/html-aria/) [\[188\]](https://www.w3.org/TR/html-aria/) [\[229\]](https://www.w3.org/TR/html-aria/) https://www.w3.org/TR/html-aria/

<https://www.w3.org/TR/html-aria/>

[\[101\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com) [\[112\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com) [\[116\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com) [\[120\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com) [\[149\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com) [\[153\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com) [\[195\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com) [\[207\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com) [\[210\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com) Web Content Accessibility Guidelines (WCAG) 2.2

<https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com>

[\[105\]](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html) https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html

<https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html>

[\[106\]](https://design-system.service.gov.uk/components/error-summary/) [\[124\]](https://design-system.service.gov.uk/components/error-summary/) [\[204\]](https://design-system.service.gov.uk/components/error-summary/) [\[226\]](https://design-system.service.gov.uk/components/error-summary/) https://design-system.service.gov.uk/components/error-summary/

<https://design-system.service.gov.uk/components/error-summary/>

[\[108\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-color-scheme) [\[147\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-color-scheme) [\[212\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-color-scheme) [\[223\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-color-scheme) https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-color-scheme

<https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-color-scheme>

[\[125\]](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/?utm_source=chatgpt.com) [\[224\]](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/?utm_source=chatgpt.com) Combobox Pattern \| APG \| WAI

<https://www.w3.org/WAI/ARIA/apg/patterns/combobox/?utm_source=chatgpt.com>

[\[126\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors) [\[148\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors) [\[155\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors) [\[159\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors) [\[161\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors) [\[163\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors) [\[205\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors) https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors

<https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/forced-colors>

[\[128\]](https://designsystem.digital.gov/utilities/layout-grid/) [\[130\]](https://designsystem.digital.gov/utilities/layout-grid/) [\[141\]](https://designsystem.digital.gov/utilities/layout-grid/) https://designsystem.digital.gov/utilities/layout-grid/

<https://designsystem.digital.gov/utilities/layout-grid/>

[\[143\]](https://carbondesignsystem.com/elements/2x-grid/usage/) https://carbondesignsystem.com/elements/2x-grid/usage/

<https://carbondesignsystem.com/elements/2x-grid/usage/>

[\[145\]](https://developer.apple.com/design/human-interface-guidelines/dark-mode?utm_source=chatgpt.com) [\[156\]](https://developer.apple.com/design/human-interface-guidelines/dark-mode?utm_source=chatgpt.com) [\[208\]](https://developer.apple.com/design/human-interface-guidelines/dark-mode?utm_source=chatgpt.com) Dark Mode \| Apple Developer Documentation

<https://developer.apple.com/design/human-interface-guidelines/dark-mode?utm_source=chatgpt.com>

[\[165\]](https://www.w3.org/WAI/ARIA/apg/patterns/grid/?utm_source=chatgpt.com) [\[169\]](https://www.w3.org/WAI/ARIA/apg/patterns/grid/?utm_source=chatgpt.com) [\[185\]](https://www.w3.org/WAI/ARIA/apg/patterns/grid/?utm_source=chatgpt.com) [\[191\]](https://www.w3.org/WAI/ARIA/apg/patterns/grid/?utm_source=chatgpt.com) [\[216\]](https://www.w3.org/WAI/ARIA/apg/patterns/grid/?utm_source=chatgpt.com) Grid (Interactive Tabular Data and Layout Containers) Pattern

<https://www.w3.org/WAI/ARIA/apg/patterns/grid/?utm_source=chatgpt.com>

[\[227\]](https://designsystem.digital.gov/design-tokens/spacing-units/?utm_source=chatgpt.com) Spacing units \| U.S. Web Design System (USWDS)

<https://designsystem.digital.gov/design-tokens/spacing-units/?utm_source=chatgpt.com>
