# Source Format Map

The pack stores text-heavy source documents as markdown to reduce pack size while preserving wording. Visual-first references are kept in original form when imagery matters (for example, the Pantone PDF).

| Original source | Optimized source | Extracted media | Notes |
|---|---|---|---|
| AI Design Operator Pack Improvement Brief.docx | AI Design Operator Pack Improvement Brief.md | - | Text preserved in markdown |
| AI Design Operator Pack Research.docx | AI Design Operator Pack Research.md | - | Text preserved in markdown |
| AI PDF Creation_ Grid and Typography.docx | AI PDF Creation_ Grid and Typography.md | - | Text preserved in markdown |
| Accessibility and Feedback Expert Research.docx | Accessibility and Feedback Expert Research.md | - | Text preserved in markdown |
| Back-End Aware Planner for DesignPilot.docx | Back-End Aware Planner for DesignPilot.md | - | Text preserved in markdown |
| DesignPilot_ProblemCatalogue(1).docx | DesignPilot Problem Catalogue.md | - | Text preserved in markdown |
| Design System Failure Diagnosis and Solutions(1).docx | Design System Failure Diagnosis and Solutions.md | - | Text preserved in markdown |
| Brand Strategy Expert for DesignPilot.docx | Brand Strategy Expert for DesignPilot.md | - | Text preserved in markdown |
| Case-Study Structure and Narrative Order.docx | Case-Study Structure and Narrative Order.md | src/knowledge-base/source-media/Case-Study Structure and Narrative Order | Text preserved in markdown; media extracted and preserved |
| Color Expert Agent Research.docx | Color Expert Agent Research.md | - | Text preserved in markdown |
| Color Library Expansion Research Plan.docx | Color Intelligence Systems for Global Production Libraries.md | - | Research normalized into a tighter markdown source with current official references |
| Component Systems Expert Research.docx | Component Systems Expert Research.md | - | Text preserved in markdown |
| Comprehensive Typeface Database and Systematic Engineering Report for Design Systems.docx | Comprehensive Typeface Database and Systematic Engineering Report for Design Systems.md | - | Text preserved in markdown |
| Comprehensive UI_UX Project Roadmap.docx | Comprehensive UI_UX Project Roadmap.md | - | Text preserved in markdown |
| Dashboard Expert Research.docx | Dashboard Expert Research.md | - | Text preserved in markdown |
| Design Strategy and Communication Research.docx | Design Strategy and Communication Research.md | - | Text preserved in markdown |
| Exception and Failure Taxonomy Expert Research.docx | Exception and Failure Taxonomy Expert Research.md | - | Text preserved in markdown |
| Front-End Handoff Expert Research.docx | Front-End Handoff Expert Research.md | - | Text preserved in markdown |
| Grid Systems Guide_ Presentation, App, Web.docx | Grid Systems Guide_ Presentation, App, Web.md | - | Text preserved in markdown |
| Industry & Demographic Encompassing Design Toolkit.docx | Industry & Demographic Encompassing Design Toolkit.md | - | Text preserved in markdown |
| Layout Reconstruction Expert Research.docx | Layout Reconstruction Expert Research.md | - | Text preserved in markdown |
| PDF Document Accessibility Expert Research.docx | PDF Document Accessibility Expert Research.md | - | Text preserved in markdown |
| Strict Graphic Design Expert for DesignPilot.docx | Strict Graphic Design Expert for DesignPilot.md | - | Text preserved in markdown |
| The Global Typographic Landscape of 2026.docx | The Global Typographic Landscape of 2026.md | - | Text preserved in markdown |
| The Global Typography Intelligence Index.docx | Global Typography Intelligence Index.md | - | Research normalized into a tighter markdown source with current official references |
| Writing Clarity and UX Copy Expert Research.docx | Writing Clarity and UX Copy Expert Research.md | - | Text preserved in markdown |
| pantone_color_chart.pdf | PANTONE_NUMBERS.json | src/libraries/ | Converted to JSON: 574 U/C colors with hex, CMYK, RGB. PDF removed from pack to reduce size. |


Pack-history, optimization, and validation notes live in `CHANGELOG.md`.

- `AI Operator Pack Validation & Stress Testing.docx` -> `src/knowledge-base/source-docs/AI Operator Pack Validation & Stress Testing.md`

- `src/knowledge-base/source-docs/Technical Reference Framework for Pantone Systems and Production-Aware Design Operations.md` is stored as markdown because it is text-heavy and operational.


## Machine-readable library indexes
- `src/libraries/COLOR_LIBRARY.json` - compact machine-readable digital color-system index for low-token lookup
- `src/libraries/PANTONE_LIBRARY.json` - compact machine-readable Pantone index for low-token lookup
- `src/libraries/FONT_LIBRARY.json` - compact machine-readable font index for low-token lookup


## Internal operational files
- `PROJECT_FILE_SYSTEM_PROTOCOL.md` - runtime control file
- `PROJECT_LOGGING_PROTOCOL.md` - runtime control file
- `projects/_project-template/` - folder template

- PROJECT_PORTABLE_WORKSPACE_PROTOCOL.md

| AI_Design_Operator_Pack__UI_System_Architecture.docx | UI System Expert Research.md | - | Text preserved in markdown; new dedicated source for ui-system-expert skill |
| AI_UX_Decision_Design_Cognitive_Foundations.docx | UX Cognition Expert Research.md | - | Text preserved in markdown; new dedicated source for ux-cognition domain |
| AI_Motion_Design_Operator_Pack.docx | Motion and Interaction Feedback Expert Research.md | - | Text preserved in markdown; new source and skill for motion-interaction domain |
