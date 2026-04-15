# Design System Failure Diagnosis and Solutions

## Engineering the Design System: A Comprehensive Restoration Framework for Document and Presentation Architectures

### Executive Diagnosis: The Architecture of Failure and the Structural Debt Crisis

The analytical examination of the sixteen documented failures within the "DesignPilot" build session reveals a design system suffering from advanced "structural debt," an architectural condition where the foundational patterns are unable to support the cumulative weight of content growth and iterative feature demands.1 Unlike "technical debt," which often manifests as localized code inefficiencies or individual visual bugs, structural debt is emergent and systemic; it signifies a failure in the underlying abstractions and interaction models.1 The recurring need for full-system rebuilds (#14) suggests that the initial construction lacked a "single source of truth," forcing the development team into a "The Invisibility Tax" scenario, where up to 42% of resources were diverted toward maintaining legacy errors rather than delivering new value.4

The primary diagnostic finding is that the system was built using a "symptom-first" rather than a "roadmap-first" methodology. This led to "Strategic Debt"-conscious but poorly executed shortcuts taken under pressure-and "Accidental Debt," emerging from a lack of understanding regarding the complex interdependencies between typography, color perception, and spatial math.6 For instance, the use of pure black #000000 backgrounds (#01) and subsequent "contrast shock" (#02) highlights a failure in Tier 2 Design Tokens, where brightness inversion was used as a crude proxy for narrative rhythm.7

Furthermore, the document architecture failed to integrate "Information Design Wayfinding." Navigational markers like ghost numerals (#03) and section labels (#04) were treated as decorative "chartjunk" rather than functional landmarks, leading to cognitive overload and "Information Chunking" failures.10 The absence of a table of contents (TOC) and chapter structure (#11) confirms that the system was initially envisioned as a flat sequence of aesthetic assets rather than a structured information environment.7

The resolution of these issues requires moving beyond "iterative patching." A "Structural Reset" is mandatory, utilizing a modular grid system based on Swiss design principles and 8pt spatial math to eliminate the "dead zones" (#07, #16) and "floating content" (#08) that characterized the failed build.14

### Issue Cluster Matrix: Upstream Causes and Solution Patterns

The following matrix maps the symptoms identified in the problem catalogue to their fundamental upstream causes within the design roadmap, providing a blueprint for production-level remediation.

### Deep Research Roadmap: A Production-Level Remediation Strategy

#### Phase 1: Research - Human Perception and Dark Mode Standards

The documented failure of the pure black background (#01) is grounded in the "halation effect" and physiological eye strain. Research into Material Design and dark UI standards demonstrates that pure black (#000000) eliminates the ability to express depth via shadows and creates an excessive contrast ratio that induces visual fatigue.18 For professional documents, a base surface of #121212 or a warm amber-dark like #1D1810 provides a superior foundation because it allows for "Elevation Surfaces".7

In a dark theme, elevation is not communicated through shadows (which are invisible against black) but through "Lightness Overlays"-semi-transparent white layers applied to the base color.18 Higher elevation elements (e.g., cards or buttons) must use lighter surface colors to signal importance.18 Furthermore, research from MIT’s AgeLab suggests that while dark mode may benefit those with "cloudy ocular media" by reducing scattered light, it can be less effective for rapid text scanning in high-ambient-light environments.37 This necessitates the inclusion of "Temperature Shifts" (moving between cool and warm darks) rather than full brightness inversions to maintain "Tonal Consistency" while providing narrative rhythm.7

#### Phase 2: Strategy - Information Density and Cognitive Load

The core strategy for a technical presentation must revolve around Andrew Quagliata’s metrics for "Information Density," which define the relationship between word count, information chunks, and cognitive effort.11 An "information chunk" is any distinct group of content the audience perceives as a standalone unit.11 The build failures noted in Issues #09 and #10 resulted from a disregard for these thresholds.

System-level strategies must enforce the following density tiers:

Narrative/Presentation Mode: Targeted word counts of ~15 words and 1 chunk per slide, maximizing "Redundancy Principle" effects where people learn better from graphics and narration than printed text.11

Hybrid/Report Mode: Targeted word counts of ~85 words and 2-3 chunks, designed to support interactive discussion while remaining standalone-legible.11

High-Density Pre-read: Word counts of ~170 words and 4-5 chunks, intended for independent reading.11

When a slide exceeds these word or chunk counts, the strategy must dictate a "Concept Split," preventing the "Wall of Text" failure mode common in industrial decks.27 This mirrors the McKinsey structure, where content is categorized to avoid duplication and organized from most to least impactful.40

#### Phase 3: Information Architecture - Navigational Wayfinding

The "Flat Sequence" failure (#11) is a primary indicator of absent Information Architecture (IA). Production-level IA for documents must apply Kevin Lynch’s five spatial elements-Paths, Edges, Districts, Nodes, and Landmarks-to the digital canvas.21

Paths: The logical reading order and narrative flow established by vertical logic.41

Edges: Boundary markers like section dividers and table of contents.22

Districts: Thematic zones defined by consistent color temperatures or headers.22

Nodes: Decision points, such as a TOC or index, where the user chooses a direction.22

Landmarks: Unique visual identities at each location, such as a large gold chapter number, to help users "recover position and orientation" within a 100+ page deck.7

To solve "Chrome Duplication" (#04), the IA must distinguish between "Identification Signs" (confirming where the user has arrived) and "Directional Signs" (guiding the user where to go).44 Section labels belong in the persistent header chrome (District-level ID), while slide headlines must be unique to the local content (Landmark-level ID).22

#### Phase 4: UX Structure - Archetypal Slide Skeletons

UX structure defines the "Skeletons" that house components.28 The "floating content" failure in Issue #08 indicates a breakdown in "Proximity Rules." In UX design, elements that share visual characteristics or spatial proximity are perceived as related.28 The restoration of the deck requires a restricted set of layouts:

Top/Bottom Split: Reserved for high-impact hero images or primary headlines over supporting evidence.45

Left/Right Split: The standard for content-heavy slides, aligning with western reading patterns (F-pattern).45

Centre Layout: Used exclusively for chapter dividers, opening slides, and closing statements to signal "Powerful Moments".45

Dynamic Modular Grid: Dividing the slide into 36 or 48 equal fields to allow for asymmetrical pairings (e.g., 7 columns for evidence, 5 for sidebar comments).16

#### Phase 5: UI System - Mathematical Grid Foundations and Vertical Rhythm

The most critical restoration step for the DesignPilot system is the transition from arbitrary spacing to a formalized "Vertical Rhythm" and the 8pt grid system.14 Vertical rhythm is achieved when all design elements are aligned to evenly spaced horizontal lines, creating a predictable and professional experience.48

The mathematical base unit for a 16:9 landscape layout (standard 1280x720px or 1920x1080px) must be 8 pixels, with 4 pixel increments used for fine-tuning small text blocks or icons.14 To solve Issues #05 and #06, the "Content Box" ($CB$) must be calculated as a hard constant derived from the viewport height ($H$), minus fixed margins and chrome headers.7

For a 720pt height system:

$$CB = H - MB - MT - BAND\_H$$

Where $BAND\_H$ is the header chrome height (e.g., 40pt) and margins are 20pt. If the calculation yields $CB = 484$, then every local layout must fill this box exactly.7 Card height ($CH$) for $N$ items with a gutter ($G$) is then calculated as:

$$CH = \frac{CB - (G \times (N-1))}{N}$$

This formula prevents "Bottom Dead Zones" by ensuring components scale to the container’s geometric limits rather than being hard-coded to arbitrary heights (#16).7

#### Phase 6: Style Guide - Tonal Consistency and Decorative Restraint

A production-level style guide must prioritize "Clarity Over Decoration".10 The failure of "Ghost Numerals" (#03, #12) stems from treating functional navigation as an aesthetic watermark.7 The guide must establish that visual hierarchy is created through three primary tools: Size (Bigger = more important), Weight (Bolder = more important), and Contrast (High contrast = focus point).28

Restraint guidelines include:

Color as Signal: Reserve accent colors for "Winner" or recommendation highlights in comparisons, not just decorative flair.28

Chartjunk Prohibition: Remove any decorative lines (overshoots in #06) that do not define a boundary or signal a relationship.51

Temperature Consistency: When shifting between sections, maintain "Tonal Harmony." Moving from a dark cool gray to a dark warm amber provides sections a unique identity without forcing the eye to readapt to new brightness levels.7

#### Phase 7: Design Tokens - Semantic Abstraction for Scalability

To prevent the "Manual Update Fatigue" seen in Issue #13, the system must utilize a three-tier design token architecture.8 This decouples the visual value from the functional intent.

By using tokens, theme switching becomes a single logic change. The user’s desire to "make all pages look like the warm ones" (#13) would be a one-line update in the token mapping file rather than a manual audit of 20 slides.7

#### Phase 8: Implementation - Character Fit and Dynamic Content Logic

Implementation for code-generated PDFs must include "Collision Detection" and "Fit-Content" heuristics to solve clipping issues (#15).31 A fit-content algorithm ensures that an element never exceeds its intrinsic size or its container's limits.32

For components with fixed widths (e.g., grid cells or buttons), the system should calculate the "Maximum Character Threshold":

$$Max\_Chars = \frac{Cell\_Width - (Padding \times 2)}{Average\_Char\_Width}$$

If the content exceeds this threshold, the implementation engine must trigger an automated "Truncation with Tooltip" or a "Font-Step-Down" rule (e.g., dropping from 16pt to 14pt).31 To solve "Label Collision" (#10), the system must enforce a single-word label constraint or an auto-wrap logic that respects the 8pt vertical rhythm.7

#### Phase 9: Validation/QA - Automated Visual Regression and Preflight

The final phase introduces a "Automated Visual Regression Testing" (AVRT) framework.30 AVRT works as a "visual safety net," capturing screenshots of every slide build and performing pixel-by-pixel comparisons against an approved "Baseline".24

The QA framework should include:

Visual Diffing: Highlighting unintended shifts, such as lines leaking into other sections (#06) or button labels overlapping (#10).24

Preflight Checks: Automating the scanning of PDF metadata, color space (CMYK vs. RGB), and font embedding.54

Heuristic Evaluation: Grouping issues into categories like "Aesthetic and Minimalist Design" (#08) or "Recognition Rather than Recall" (#06) to identify recurring patterns of debt.51

### System Rules and Measurable Thresholds

To maintain production integrity, the following quantified rules and logic gates are established as non-negotiable system constraints.

#### Typography and Fit Logic

#### Color and Contrast Logic

Dark Theme Contrast: High-emphasis text must use 87% opacity on dark backgrounds; medium-emphasis uses 60%; disabled text uses 38%.18

Minimum Contrast Ratio: Reject any color combination with a ratio $<$ 4.5:1 for body text or $<$ 3:1 for large graphical elements.18

Background Desaturation: Background hex codes must be desaturated to avoid "optical vibrations".18

Tonal Shift Limit: Temperature shifts between sections should not exceed a $\Delta E$ (Delta-E) threshold that triggers a pupil dilation response (avoiding brightness shocks).64

#### Grid and Geometry Logic

Base Unit: 8pt spatial system with 4pt half-units for icon alignment.14

The 6x6 Rule: Each slide is limited to 6 lines of text and 6 words per line to minimize cognitive load.27

Fill Heuristic: All multi-card rows must be calculated as $100\%$ of $CB$ height; $Dead\_Zone \le 8pt$.7

Safe Zone: Critical text and brand markers must remain $0.125"$ inside the trim line to prevent clipping in PDF exports.54

### The Design Operator’s Build-Time Checklist

This protocol is to be executed before every document generation cycle to ensure adherence to the systemic rules.

#### 1. Information Architecture and Structure

[ ] Cover Logic: Deck starts with a minimal cover (no chrome) and a gold left-rail bookend.7

[ ] TOC Consistency: Table of Contents exists and matches chapter names/page numbers exactly.7

[ ] Chapter Markers: Each section begins with a "Centre Layout" divider slide containing a large landmark number.7

[ ] chrome Audit: Persistent header contains Section ID; slide headline is unique to the page content.7

#### 2. Layout and Grid Math

[ ] content Box Check: Margin-top (MT) and Margin-bottom (MB) are identical; all gaps are 8pt multiples.7

[ ] Vertical Fill: Card/row heights are dynamic ($CB / N$) and fill the vertical space to the footer rule.7

[ ] Line Integrity: All indicator lines (dashed/solid) span exactly from coordinate $Y_1$ to $Y_2$ with zero overshoot.7

[ ] Clustering: Badge, headline, and detail text are grouped within a container with consistent internal spacing.7

#### 3. Density and Content Control

[ ] Concept Split: No slide contains more than one primary concept; complex component slides are split into Registry vs. Demo.7

[ ] Word Count Audit: word counts are $\le$ 170 (hybrid report) or $\le$ 30 (live deck).11

[ ] Chunk Count: Each slide contains $\le$ 5 distinct information groups.11

[ ] Clipping Check: All grid-cell descriptions fit within the cell width at 9pt Mono; no overflow detected.7

#### 4. Tonal and Visual QA

[ ] Temperature Check: Theme shifts occur through hue/temperature adjustments (Warm Amber vs. Cool Gray), not brightness inversions.7

[ ] Ghost Audit: All watermark numerals or background markers are removed or set to $\le$ 10% opacity.7

[ ] Contrast Pass: Text on the highest elevation surface meets the 4.5:1 WCAG AA threshold.18

### The Rebuild Protocol: An Architectural Decision Framework

The recurring failures documented in the problem catalogue (#14) demonstrate that "Iterative Patching" is often a sunken-cost fallacy. When a system accumulates enough structural debt, the design operator must decide whether to "Refactor" or "Rebuild".68

#### Rebuild Triggers (The 5-Point Structural Test)

A system should be rebuilt from scratch if it fails three or more of the following indicators:

Architecture-Content Mismatch: The existing container geometry cannot handle dynamic content length without systemic breakage (#07, #08).1

Logic Inflexibility: Implementing a narrative change (e.g., adding a chapter structure) requires manual edits to every slide (#11, #13).1

Velocity Collapse: The time taken to triage recurring "shadow bugs" (bugs that reappear after a fix) exceeds the time spent building new content (#14).1

Technical Obsolescence: The underlying engine uses hard-coded point values instead of a responsive 8pt grid and semantic tokens.68

Requirement Drift: The original "Minimalist" intent has been replaced by a need for "High-Density Data Visualization" that the original UI system cannot support (#09).70

#### The Rebuild Execution: The "Strangler Fig" Methodology

Total rebuilds carry high delivery risk. Document engineering should instead employ the "Strangler Fig" pattern.70

Step 1: The New Core: Define the new 8pt grid logic and $CB$ constants in a clean repository.15

Step 2: Foundation Migration: Implement Tier 1 and Tier 2 Design Tokens, mapping them to the new tonal temperature shifts.8

Step 3: Component Isolation: Re-engineer the most problematic components (e.g., the dynamic cards and registries) first, ensuring they are grid-compliant.70

Step 4: Systematic Replacement: Swap old slides with new, system-built slides section by section.70

Step 5: Final Deprecation: Once the narrative flow is restored and the AVRT baselines are stable, delete the legacy code entirely.69

### Conclusion: Toward a Document Engineering Paradigm

The restoration of the DesignPilot build system requires a paradigm shift from "Visual Design" to "Document Engineering." By treating a PDF or presentation as a structured information environment governed by mathematical grids, semantic tokens, and cognitive density thresholds, the design operator can eliminate the structural debt that triggers the need for continuous rebuilds.

Success is measured not by the aesthetic polish of a single slide, but by the stability of the system when subjected to variable content. The integration of automated visual regression testing and preflight heuristics provides the "visual safety net" necessary to scale a deck from a flat 10-slide sequence to a complex 200-page report without systemic breakage. The roadmap-beginning with fundamental research into color perception and ending with automated validation-ensures that the real upstream causes of failure are addressed at the architectural level, transforming the design system into a robust, high-velocity production asset.

Works cited

Technical Debt vs Structural Debt: A Complete Guide for Engineering Teams, accessed April 9, 2026, https://dev.to/adamthedeveloper/technical-debt-vs-structural-debt-a-complete-guide-for-engineering-teams-10i0

Design debt: what it is and how to keep it from piling up - Digital Product People, accessed April 9, 2026, https://www.wearedpp.com/thoughts/fixing-design-debt

Design Debt is Ruining Your Product Experience. How Can You Save it, accessed April 9, 2026, https://www.koruux.com/blog/design-debt-ruining-your-product-experience/

What is a Design System? A 2026 Guide With Best Practice Examples - Untitled UI, accessed April 9, 2026, https://www.untitledui.com/blog/what-is-a-design-system

How to Automate Technical Debt Detection with AI | Augment Code, accessed April 9, 2026, https://www.augmentcode.com/learn/how-to-automate-technical-debt-detection-with-ai

The Real Cost of Technical Debt in Product Development - Treetown Tech, accessed April 9, 2026, https://www.treetowntech.com/the-real-cost-of-technical-debt-in-product-development/

DesignPilot_ProblemCatalogue.docx

How to design a dark mode-friendly colour system for enterprise UI - EDL, accessed April 9, 2026, https://www.edl.dk/feed/how-to-design-a-dark-mode-friendly-colour-system-for-enterprise-ui

Dark Mode Design Systems: A Practical Guide | by Ravindi | Bootcamp - Medium, accessed April 9, 2026, https://medium.com/design-bootcamp/dark-mode-design-systems-a-practical-guide-13bc67e43774

Wayfinding Signage Design: Principles, Guidelines & Examples - Pannier Graphics, accessed April 9, 2026, https://www.panniergraphics.com/blog/wayfinding-signage-design

Information Density Is the Key to Smarter Slide Decks, accessed April 9, 2026, https://www.andrewquagliata.com/post/information-density-is-the-key-to-smarter-slide-decks

Wayfinding Design - Alta Planning + Design, accessed April 9, 2026, https://altago.com/wayfinding-design/

(PDF) Document Structure and Layout Analysis - ResearchGate, accessed April 9, 2026, https://www.researchgate.net/publication/226300537_Document_Structure_and_Layout_Analysis

Spacing, grids, and layouts - Design Systems, accessed April 9, 2026, https://www.designsystems.com/space-grids-and-layouts/

8-Point Grid - Spec, accessed April 9, 2026, https://spec.fm/specifics/8-pt-grid

Grids, Guides, Proportions and InDesign Math | Nick Cassway's designBLOG, accessed April 9, 2026, http://nickcassway.com/designblog/?p=623

Insight Presentation Grid System for InDesign - Stephen Kelman, accessed April 9, 2026, https://stephenkelman.co.uk/insight-presentation-grid-system-for-indesign

Dark theme - Material Design, accessed April 9, 2026, https://m2.material.io/design/color/dark-theme.html

10 Common Dark Mode Design Mistakes UI Designers Should Avoid - Medium, accessed April 9, 2026, https://medium.com/@dollyborade07/10-common-dark-mode-design-mistakes-ui-designers-should-avoid-e81f08838fbc

Mastering typography in design systems with semantic tokens and responsive scaling, accessed April 9, 2026, https://uxdesign.cc/mastering-typography-in-design-systems-with-semantic-tokens-and-responsive-scaling-6ccd598d9f21

Complete Wayfinding Signage Guide: Design and Accessibility - Blink Signs, accessed April 9, 2026, https://blinksigns.com/complete-guide-to-wayfinding-signage/

Environmental Graphics and Wayfinding Integration - BlinkSigns, accessed April 9, 2026, https://blinksigns.com/environmental-graphics-wayfinding-integration/

The 8pt Grid System: A Simple Guide to Consistent UI Spacing - Rejuvenate Digital, accessed April 9, 2026, https://www.rejuvenate.digital/news/designing-rhythm-power-8pt-grid-ui-design

AI-Assisted QA: Automated Visual Regression Testing Explained - New Target, inc., accessed April 9, 2026, https://www.newtarget.com/web-insights-blog/visual-regression-testing/

Guidelines for Preparing PowerPoint Slide Presentations - ISMRM, accessed April 9, 2026, https://www.ismrm.org/03/ppguide.htm

Top Eight Rules for Creating a PowerPoint Presentation, accessed April 9, 2026, https://www.pharmacoepi.org/pub/?id=76a123f3-c419-8689-f823-a38e28f5fd02

Word count per slide? : r/instructionaldesign - Reddit, accessed April 9, 2026, https://www.reddit.com/r/instructionaldesign/comments/12yq7d7/word_count_per_slide/

Visual Hierarchy in Design and Presentation - Extended Frames, accessed April 9, 2026, https://extendedframes.com/visual-hierarchy-in-design-and-presentation/

Typography | U.S. Web Design System (USWDS) - Digital.gov, accessed April 9, 2026, https://designsystem.digital.gov/components/typography/

Automated Visual Regression Testing: From Implementation to Tools | by David Auerbach, accessed April 9, 2026, https://medium.com/@david-auerbach/automated-visual-regression-testing-from-implementation-to-tools-dcb3c75ce76d

Ignoring character limits can wreck your product's UX | by Stephanie Schwarz, accessed April 9, 2026, https://uxdesign.cc/ignoring-character-limits-can-wreck-your-products-ux-3c2dc3b6b24a

fit-content - CSS - MDN Web Docs - Mozilla, accessed April 9, 2026, https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content

Typography Principles The Complete 2026 Guide - The Crit, accessed April 9, 2026, https://www.thecrit.co/resources/typography-principles-guide

PDF Validation Software: Automatic Checks Fixes & Validation - DocShifter, accessed April 9, 2026, https://www.docshifter.com/use-cases/automated-pdf-validation/

Mastering Elevation for Dark UI: A Comprehensive Guide - Uxcel, accessed April 9, 2026, https://uxcel.com/blog/mastering-elevation-for-dark-ui-a-comprehensive-guide-342

Mastering Elevation for Dark UI: A Comprehensive Guide - Muzli - Design Inspiration, accessed April 9, 2026, https://medium.muz.li/mastering-elevation-for-dark-ui-a-comprehensive-guide-04cc770dd0d6

12 Principles & Best Practices of Dark Mode Design - Uxcel, accessed April 9, 2026, https://uxcel.com/blog/12-principles-of-dark-mode-design-627

Evidence-Based Presentation Design Recommendations - Multimedia Services, accessed April 9, 2026, https://multimedia.ucsd.edu/best-practices/presentation-design.html

Word count per slide? : r/instructionaldesign - Reddit, accessed April 9, 2026, https://www.reddit.com/r/instructionaldesign/comments/1iiqnsf/word_count_per_slide/

McKinsey Presentation Structure (A Guide for Consultants) - SlideModel, accessed April 9, 2026, https://slidemodel.com/mckinsey-presentation-structure/

5. Design Principles for Wayfinding, accessed April 9, 2026, http://www.ai.mit.edu/projects/infoarch/publications/mfoltz-thesis/node8.html

Designing Clear Wayfinding for Public Spaces - ICN, accessed April 9, 2026, https://icn.com/en-jo/blog/designing-clear-wayfinding-for-public-spaces

2 Wayfinding Design Principles - International Health Facility Guidelines, accessed April 9, 2026, https://healthfacilityguidelines.com/Guidelines/ViewPDF/iHFG/iHFG_part_w_wayfinding_design_principles

Wayfinding Signs for NYC Buildings & Businesses: The Complete Guide –, accessed April 9, 2026, https://signsny.com/blog/wayfinding-business-signage-guide/

4 Useful Business Presentation Layouts (with Examples) - Narratio Creative, accessed April 9, 2026, https://narratiocreative.com/resources/4-useful-business-presentation-layouts/

Using Heuristic Evaluation to Enhance the Visual Display of a Provider Dashboard for Patient-Reported Outcomes - PMC, accessed April 9, 2026, https://pmc.ncbi.nlm.nih.gov/articles/PMC5983070/

8-Point Grid: Vertical Rhythm - Medium, accessed April 9, 2026, https://medium.com/built-to-adapt/8-point-grid-vertical-rhythm-90d05ad95032

Vertical Rhythm In Typography - 8th Light, accessed April 9, 2026, https://8thlight.com/insights/vertical-rhythm-in-typography

Vertical Rhythm - Make Your Web Content More Readable | by Ryan Yu | Medium, accessed April 9, 2026, https://medium.com/@iamryanyu/vertical-rhythm-make-your-web-content-more-readable-cb719e0f77fc

How to make a grid in Keynote with alignment guides + Pro Tips! - Medium, accessed April 9, 2026, https://medium.com/@madeinkeynote/learn-how-to-make-perfect-modular-grids-in-keynote-with-shortcuts-8234cba7a49c

10 Usability Heuristics for User Interface Design - NN/G, accessed April 9, 2026, https://www.nngroup.com/articles/ten-usability-heuristics/

10 UX heuristics every content designer should know • UXCC, accessed April 9, 2026, https://uxcontent.com/10-content-design-heuristics/

Color Consistency in Design Systems - UXPin, accessed April 9, 2026, https://www.uxpin.com/studio/blog/color-consistency-design-systems/

The Pre-Flight Print Checklist For Flawless Work - Ideal Printers, accessed April 9, 2026, https://www.idealprint.com/2026/01/15/the-pre-flight-print-checklist-for-flawless-work/

Button labels - VA.gov Design System, accessed April 9, 2026, https://design.va.gov/content-style-guide/button-labels

Character count | U.S. Web Design System (USWDS), accessed April 9, 2026, https://designsystem.digital.gov/components/character-count/

Visual Regression Testing - All You Need to Know, accessed April 9, 2026, https://www.virtuosoqa.com/post/visual-regression-testing-101

Choosing Preflight Software: A Guide to Features, Benefits & ROI - GlobalVision, accessed April 9, 2026, https://www.globalvision.co/blog/choosing-the-right-preflight-software

Heuristic Evaluations: How to Conduct - NN/G, accessed April 9, 2026, https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/

Basic Typography Rules: What Every Designer Should Know - DepositPhotos Blog, accessed April 9, 2026, https://blog.depositphotos.com/basic-typography-rules.html

Vertical Rhythm in Typography - Imperavi, accessed April 9, 2026, https://imperavi.com/blog/vertical-rhythm-in-typography/

The Golden Rule of Line Length in UX/UI: Why 75 Characters Is Too Many | by Khoa Le, accessed April 9, 2026, https://medium.com/@wblekhoa/talk-aboutthe-optimal-length-of-text-in-ux-ui-525e689f0b71

Typography (Fonts) & Spacing - Division of Central Services (DCS) - Colorado, accessed April 9, 2026, https://dcs.colorado.gov/ids/digital-guidelines/design-tokens/typography-fonts-spacing

8 Tips for Dark Theme Design - UX Planet, accessed April 9, 2026, https://uxplanet.org/8-tips-for-dark-theme-design-8dfc2f8f7ab6

The ultimate guide to visual hierarchy | Canva, accessed April 9, 2026, https://www.canva.com/learn/visual-hierarchy/

The 10-20-30 Rule of PowerPoint - Microsoft 365, accessed April 9, 2026, https://www.microsoft.com/en-us/microsoft-365-life-hacks/presentations/10-20-30-rule-of-powerpoint

Design system best practices: Components and documentation | by Maksym Cherkashyn, accessed April 9, 2026, https://www.designsystemscollective.com/design-system-best-practices-components-and-documentation-bdb020e02172

Mobile App Technical Debt: Rebuild vs Refactor Guide - Dogtown Media, accessed April 9, 2026, https://www.dogtownmedia.com/managing-technical-debt-when-to-rebuild-vs-refactor-your-app/

When to Rebuild vs Refactor a Legacy Web App - DO OK, accessed April 9, 2026, https://dook.pro/blog/delivery/when-to-rebuild-vs-refactor-legacy-web-app/

Should You Rebuild or Refactor Your Legacy System? - Particle41, accessed April 9, 2026, https://particle41.com/insights/rebuild-or-refactor-legacy-system/

Reengineering vs Refactoring vs Rebuilding: What's Best for Your Software?, accessed April 9, 2026, https://corsactech.com/blog/reengineering-vs-refactoring-vs-rebuilding

## Table 1
| Issue Cluster | Roadmap Phase | Upstream Cause | Solution Pattern | Measurable Rules | Failure Mode | Validation Check | Fix Type |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Theme & Tonal Integrity | Phase 7: Design Tokens | Absence of semantic contrast modeling; reliance on pure #000000.18 | Tonal Temperature Shifting; desaturated dark grays (#121212).18 | Contrast Ratio $\ge$ 15.8:1 for dark surfaces.18 | "Contrast Shock" (brightness inversion).7 | WCAG AA 4.5:1 verification.20 | Structural Reset |
| Wayfinding & Restraint | Phase 3: Information Architecture | Navigational markers treated as decorative watermarks (ghost numbers).10 | Clarity-First Navigation; Kevin Lynch's Landmark principles.21 | Marker Opacity $\le$ 10%; unique labels only.7 | "Duplication Fatigue" (chrome vs. header).7 | Eye-tracking simulation; visual noise audit.10 | Systemic Rule |
| Grid Math & Geometry | Phase 5: UI System | Hard-coded point values; lack of a dynamic Content Box ($CB$).7 | 8pt Spacing Scale; dynamic $CB$ fill calculations.15 | $H - MB - MT - BAND\_H = CB$; $CB \in \{8n\}$.7 | "Bottom Dead Zones"; overshoot lines.7 | Automated geometry validation; grid-snap test.24 | Mathematical Patch |
| Density & Hierarchy | Phase 2: Strategy | Violation of Quagliata's Density Thresholds; overloading components.11 | "One-Idea-Per-Slide" constraint; Information Chunking.11 | Word Count $\le$ 170 (Report) or $\le$ 30 (Deck).11 | Cognitive load collapse; "Wall of Text".27 | Chunk count audit; word count trigger.11 | Editorial Constraint |
| Component Integrity | Phase 4: UX Structure | Floating content due to proximity rule failure; label collisions.7 | Containerized Clustering; absolute internal padding.14 | Label width $\le$ Button $X_{span}$; Internal $G \ge 1.5x$ Lead.29 | Element collision; detached descriptions.7 | Automated Visual Regression (AVRT).30 | Component Refactor |
| Typographic Fit | Phase 8: Implementation | Unchecked string expansion; fixed container height without overflow rules.31 | Fit-Content Scaling; character width constraint logic.31 | $W_{avg} \times Chars \le Cell\_W$; Min font 12px.31 | Text clipping/truncation failure.7 | Automated preflight string checks.34 | Implementation Logic |

## Table 2
| Token Tier | Example Name | Value | Intent |
| --- | --- | --- | --- |
| Tier 1: Primitive | Color-Amber-900 | #1D1810 | The raw hex value.8 |
| Tier 2: Alias (Semantic) | bg-surface-primary | ref: Color-Amber-900 | Defines "Purpose" (e.g., Background).9 |
| Tier 3: Component | card-is-not-badge-bg | ref: bg-surface-primary | Specific usage for one component.8 |

## Table 3
| Rule Category | Value / Threshold | Logic Gate / System Action |
| --- | --- | --- |
| Minimum Reading Size | 16px / 12pt 29 | Build fails if body font $<$ 12pt; Warning if $<$ 16px. |
| Headline Size | Body size $\times$ 1.6 60 | Auto-scale headlines using the "Golden Number" ratio. |
| Line Height | 1.5 $\times$ Font Size 29 | Hard constraint to maintain vertical rhythm.48 |
| Line Length (Measure) | 45–75 characters 29 | Auto-wrap or split column if string $>$ 80 characters. |
| Character Padding | 0.12 $\times$ Font Size 63 | Minimum letter-spacing to prevent visual crowding. |
| Button Label Limit | $\le$ 35 characters 55 | Truncate and alert author if label exceeds threshold. |
