<!-- Optimized from original source file: Layout Reconstruction Expert Research.docx. All textual content preserved in markdown form for size-efficient packaging. -->

# Layout Reconstruction and Grid Inference Expert

## Research foundation for inference-first layout reconstruction

A “Layout Reconstruction and Grid Inference Expert” is fundamentally different from a grid tutorial: it is an inference system that must work backward from observed artifacts (screenshots, PDFs, legacy files, websites, slides) to recover the latent layout model that likely produced them, and then support safe normalization and extension without “design drift.” This aligns more closely with document layout analysis (DLA) and screen parsing research than with traditional graphic-design instruction. DLA literature consistently frames layout analysis as a preprocessing step that detects and structures regions and their relations; classic approaches are typically categorized as top‑down (split) vs bottom‑up (cluster) vs hybrid, and surveys emphasize that rule sets can become arbitrary and that many algorithms do not naturally produce hierarchical descriptions or robust parameter estimation. [\[1\]](https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf)

For modular editorial grids in print and hybrid media, canonical grid references (e.g., Grid Systems in Graphic Design[\[2\]](https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf)) are best treated as *priors* (what kinds of grids are commonly intended) rather than as direct “how-to” instructions. The publisher description explicitly positions grid systems as a working instrument to conceive, organize, and design solutions across formats. [\[3\]](https://niggli.ch/en/products/rastersysteme-fur-die-visuelle-gestaltung) Typography-driven layout constraints (baseline rhythm, scale discipline) similarly provide priors placed into the inference model: a baseline grid is not just a visual preference, it is a recoverable periodic signal in text baselines and line spacing that can be detected and used to normalize multi-column layouts. [\[4\]](https://helpx.adobe.com/indesign/using/grids.html)

For responsive UI (particularly the common 12/8/4 pattern), the most actionable sources are breakpoint-aware grid specifications and margin/gutter constraints from design systems. Material guidance (older but accessible) states a 12-column responsive UI and explicitly ties margins and gutters to an 8dp baseline grid with discrete allowed widths (8/16/24/40dp). [\[5\]](https://m1.material.io/layout/responsive-ui.html) Material’s newer documentation also describes responsive layouts “based on 4-column, 8-column, and 12-column grids,” and separately notes “12 desktop / 8 tablet / 4 phone,” but the newer site content is not fully readable without JavaScript; therefore, use its searchable statements as a high-level constraint and rely on the accessible older spec for numeric spacing rationale. [\[6\]](https://m2.material.io/design/layout/responsive-layout-grid.html)

For PDFs and “dirty” source documents, it is critical to treat layout inference as a hybrid of geometric reasoning and robust parsing. PDF processing must respect page box semantics (MediaBox/CropBox/BleedBox/TrimBox/ArtBox) and recognize that extracted text order may not match reading order and that kerning operators and encoding details can create non-intuitive geometry and ordering. [\[7\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html) This is why modern document engineering increasingly frames document analysis as a search/optimization problem over plausible interpretations, with evaluation criteria and backtracking rather than one-pass rules that cannot recover from early errors. [\[8\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)

Finally, screenshot-based reconstruction intersects strongly with “pixels-to-structure” systems (screen parsing, design-to-code, vector reconstruction). Systems such as Rewire infer editable vector representations from screenshots; REMAUI and ReDraw infer UI elements, hierarchy, and code prototypes from screenshots; and DCGen identifies concrete failure types (omission, distortion, misarrangement) and shows that segmenting the problem into smaller visual regions can improve output similarity. [\[9\]](https://faculty.washington.edu/ajko/papers/Swearngin2018Rewire.pdf)

## Operator model for grid inference, reconstruction, normalization, and extension

This expert should behave like a layout “reverse compiler.” The goal is not perfect replication of every pixel; the goal is to infer a *stable latent layout model* (grid + baseline rhythm + spacing tokens + alignment constraints + exceptions) that (a) explains most observed placements, (b) can be serialized into implementation primitives, and (c) can be extended without accumulating drift.

### Core representations

**Observed primitives (input-driven)** - **Boxes**: bounding boxes for text runs, images, charts, UI components, or detected graphical blocks (from OCR/detection for screenshots; from PDF objects/content streams for PDFs). [\[10\]](https://ranger.uta.edu/~csallner/papers/nguyen15reverse.pdf)  
- **Lines**: detected text baselines/rows (from OCR engines, or inferred via clustering of text box bottoms). OCR research explicitly fits baselines after line detection and can handle curved baselines; that implies baseline signals can be both periodic and locally non-linear. [\[11\]](https://research.google.com/pubs/archive/33418.pdf)  
- **Whitespace structures**: candidate gutters / separators from maximal empty rectangles and background analysis (especially for document pages). Breuel-style whitespace rectangles formalize “gutter finding” as geometry over obstacles (foreground boxes) and generalize beyond axis-aligned layouts by allowing arbitrary orientations. [\[12\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)

**Latent layout model (inferred)** - **GridSpec**: `{columns, gutters, margins, containerWidthMode(centered|fullWidth), origin, breakpoints, tokenUnit}`; for print/PDF additionally `{pageBoxes, trim, bleed}`. [\[13\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html)  
- **BaselineSpec**: `{baselineStep, baselineStartOffset, baselinePhasePerRegion, textBaselineCurvature(optional)}`; grounded in desktop publishing practice where baseline grid increment is typically body leading. [\[14\]](https://helpx.adobe.com/indesign/using/grids.html)  
- **ConstraintGraph**: a declarative set of alignment/spacing constraints, with priorities (hard vs soft). Constraint solvers such as Cassowary are explicitly designed for UI layout constraints (linear equalities/inequalities) and can solve hierarchies incrementally; newer layout solvers discuss penalties and under/over-specification risks. [\[15\]](https://badros.com/greg/papers/cassowary-tochi.pdf)

**Exceptions model** - **ExceptionSet**: elements or regions that legitimately break the grid (full-bleed images, pull quotes, hero cards, rotated poster typography, dashboard microgrids). The key is to represent exceptions explicitly so the model stays stable instead of “bending” to fit outliers. [\[16\]](https://www.nngroup.com/articles/using-grids-in-interface-designs/)

### Scoring and confidence

Borrow document-engineering ideas: treat layout inference as generating candidate interpretations and scoring them, not as a single deterministic pass. The PDF engineering perspective highlights the “knowledge gap” and inability to backtrack when rules are applied in isolation at one granularity; the corrective is an evaluation-driven search. [\[8\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)

A practical scoring function for an AI operator pack should combine: - **Explained placement**: fraction of element edges that align to inferred grid lines within tolerance. - **Explained rhythm**: fraction of text baselines that land on the inferred baseline grid within tolerance. - **Simplicity**: fewer parameters (columns count from a small set; discrete spacing steps; consistent gutters). - **Stability under perturbation**: similar grid recovered across adjacent pages/screens, and after removing small outliers. - **Exception compactness**: outliers should cluster into a small number of semantically plausible exceptions (e.g., hero, callout, chart annotation), instead of forcing multiple competing grids. [\[17\]](https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf)

## Topic playbook for strict layout reconstruction

Each topic is written as an implementation-oriented “operating contract” for the expert.

**Topic: Grid inference from existing layouts**

**Definition**  
Inferring the latent column structure, gutters, margins, and alignment lines that best explain observed placements of layout elements (text, images, components) in a single artifact or across a set of related artifacts. Document layout analysis literature frames this as identifying and structuring regions and relations; methods include top-down splitting, bottom-up clustering, and hybrid approaches. [\[18\]](https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf)

**Why it matters**  
Without a grid model, reconstruction degenerates into one-off absolute positioning that cannot be normalized or extended. UI reverse engineering work (e.g., generating a view hierarchy from screenshots) explicitly depends on inferring structure and grouping beyond isolated elements. [\[19\]](https://ranger.uta.edu/~csallner/papers/nguyen15reverse.pdf)

**Default rules**  
1) Prefer **background/whitespace-driven column discovery** when the medium supports it (documents, PDFs, editorials): find candidate separators as maximal empty rectangles between foreground obstacles. Breuel-style methods treat whitespace rectangles as concise major layout features and can generalize to rotated layouts by allowing arbitrary orientations. [\[12\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)  
2) Prefer **alignment clustering** (x-positions of left/right edges, centers) when whitespace is unreliable (UI screenshots, dense dashboards).  
3) Fit multiple candidate grids and score them; do not commit to the first plausible grid. Use a search/score approach to avoid “rules in isolation” that are hard to backtrack. [\[20\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)  
4) Infer **nested grids** when a region shows strong internal regularity but misaligns with the global grid (common in dashboards and card sections).

**Exception rules**  
- Non-Manhattan layouts (rotations, angled columns, posters) require oriented separators and rotation-tolerant inference; axis-aligned whitespace separators may fail when the page is rotated even slightly. [\[21\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)  
- Projection-based top-down algorithms such as X‑Y cut are best treated as limited-domain operators: they are sensitive to parameters and historically target Manhattan layouts; they can be the “algorithm of choice” only when target documents have limited variability and the split grammar can be specified. [\[22\]](https://www.dfki.de/fileadmin/user_upload/import/5012_Shafait-xycut-PAMI.pdf)  
- For PDFs, never assume extracted text order is reading order; treat geometry as primary, and validate order using spatial grouping. [\[23\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)

**Fallback logic**  
- If column separators are ambiguous, infer a **single manuscript column** with strong margins, then infer internal sub-structure as nested grids for repeated regions.  
- If multiple grids score similarly, choose the one that is (a) simpler and (b) more stable across pages/screens (cross-sample agreement), and mark the rest as alternates with confidence scores.

**Failure conditions**  
- Competing plausible grids with no clear winner (multi-modal distribution of alignment lines).  
- Grid “shifts” across scroll states or pages without semantic cause (indicates mixed templates).  
- Excessive exception rate: if many elements must be labeled as exceptions, the inferred grid is likely wrong or the artifact is inconsistent legacy. [\[24\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)

**Measurable thresholds**  
- Operator-pack default: **Grid confidence** ≥ 0.75 to auto-apply; 0.55–0.75 requires “soft snap” only; \<0.55 triggers fallback strategies.  
- Separator validity (document mode): candidate gutters must separate substantial content on both sides; whitespace rectangles are meaningful when they separate text rather than being internal “holes.” [\[12\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)  
- Cross-sample stability: same family of column counts recovered across ≥70% of related pages/screens.

**Implementation guidance for an AI operator pack**  
- Implement a **GridCandidateGenerator** with pluggable strategies: `whitespace_rectangles`, `alignment_cluster`, `projection_split (xy_cut)`, `template_match`.  
- Add a **GridCandidateScorer** combining explained placement + simplicity + exception compactness.  
- Log and serialize: `gridSpec`, `confidence`, `exceptions`, `evidence` (alignment histograms, gutter rectangles).  
- Maintain explicit **grid anchors**: left margin line, right margin line, and column boundaries; these become constraints for later normalization and extension.

**Test cases**  
- Multi-column editorial PDF page with images spanning multiple columns; expect discovery of 2–5 columns and stable gutters, with images spanning integer column ranges. [\[25\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)  
- Dashboard screenshot with card grid; global 12-col grid is weak but internal card grid is strong; expect nested microgrid inside content region with consistent gutter.  
- Poster with rotated headline and axis-aligned body text; expect primary axis-aligned grid plus a rotated exception group, not a rotated global grid. [\[26\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)

**Topic: Margin, gutter, and column reconstruction**

**Definition**  
Recovering the outer margins, internal gutters (spaces between columns), and the number/width of columns of a layout container, expressed in normalized units and aligned to a coordinate system appropriate to the medium (CSS pixels, dp, PDF points, print mm). Material documentation provides explicit discrete values and a baseline unit approach for margins/gutters; PDF libraries define page boxes and clipping regions that interact with perceived margins. [\[27\]](https://m1.material.io/layout/responsive-ui.html)

**Why it matters**  
Margins/gutters/columns are the core parameters that allow snap, reflow, and responsive adaptation. They also define where exceptions start (full-bleed, edge-to-edge). Inconsistent margin inference is a prime cause of drift when extending layouts.

**Default rules**  
1) Identify the **layout container** first (page crop box in PDF; main content frame in UI; slide safe area) and infer margins relative to that container, not relative to raw image edges. [\[28\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html)  
2) Infer **margins as robust extrema** of aligned content edges: use the densest left-edge alignment cluster as the left margin; similarly for right.  
3) Infer **gutters** from repeated inter-column whitespace (document mode) or repeated gaps between aligned components (UI mode).  
4) Constrain reconstructed values to **tokenizable steps** when the design system suggests it (e.g., 8dp multiples for Material-like layouts). [\[5\]](https://m1.material.io/layout/responsive-ui.html)

**Exception rules**  
- Full-bleed media intentionally violates margins; treat those as exceptions and do not expand margins to “include” them.  
- Some layouts mix unequal margins and gutters; Material explicitly allows margins and gutters to differ. [\[5\]](https://m1.material.io/layout/responsive-ui.html)  
- PDF CropBox may clip content; perceived margins should be inferred from the visible region definition, not MediaBox alone. [\[29\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html)

**Fallback logic**  
- If gutters are irregular, infer a **single-column** container and store repeated gaps as local spacing tokens rather than global gutters.  
- If margins differ across pages, infer per-template margin sets and cluster pages into templates.

**Failure conditions**  
- No stable margin clusters (content left edges vary continuously).  
- Gutter candidates overlap text (indicates that inter-column whitespace is not actually empty; common when OCR boxes are noisy).  
- PDF coordinate transforms (rotation/UserUnit) not handled, causing wrong scale. UserUnit can rescale default user space units; do not assume fixed 1/72 inch scaling everywhere. [\[30\]](https://kb.itextpdf.com/itext/how-to-get-the-userunit-from-a-pdf-file)

**Measurable thresholds**  
- Column width coefficient of variation (CV) ≤ 0.08 for “uniform column grid.”  
- Gutter width CV ≤ 0.12 for “stable gutters.”  
- Margin asymmetry ratio: `max(mL, mR)/min(mL, mR)` \> 1.6 flags likely asymmetric template (acceptable) vs inference noise (needs review).

**Implementation guidance**  
- Normalize all geometry into a common unit system and store: `{unit, dpi_assumption_if_raster, page_box}`. PDF libraries define box rectangles in default user space units; external DPI is needed to convert to pixels because PDFs do not have intrinsic resolution. [\[31\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html)  
- Build a `SpacingTokenizer` that snaps inferred distances to a small set of tokens (e.g., multiples of an inferred base unit); this supports legacy normalization.  
- Export mappings: `CSS grid-template-columns`, `Figma layout grid settings`, or `InDesign margin/column settings` depending on target.

**Test cases**  
- UI screen using 8dp rhythm: margins 24dp, gutters 16dp; verify recovered values snap to allowed discrete set and match margin=gutter mismatch allowance. [\[5\]](https://m1.material.io/layout/responsive-ui.html)  
- PDF with CropBox smaller than MediaBox; verify margins are inferred relative to CropBox/visible region. [\[29\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html)

**Topic: Baseline rhythm reconstruction**

**Definition**  
Recovering the underlying vertical rhythm system (baseline grid increment and phase) that aligns text across columns and often drives vertical spacing for other elements. Desktop publishing documentation describes baseline grids as document-wide alignment tools where the increment is typically set to body leading and can start relative to top page or top margin with a configurable offset. [\[32\]](https://helpx.adobe.com/indesign/using/grids.html)

**Why it matters**  
Baseline rhythm is the vertical stabilizer for editorial layouts and text-heavy UIs. Without it, normalization creates “wobble” where lines across columns stop aligning, and extension tends to drift as new text blocks choose inconsistent leading.

**Default rules**  
1) Infer baseline increment primarily from **text-line spacing** in body text blocks, not from headings or captions. InDesign guidance explicitly recommends setting baseline increment to equal body text leading “in most cases.” [\[33\]](https://helpx.adobe.com/indesign/using/grids.html)  
2) Infer baseline phase (`startOffset`) relative to a container reference (top of page vs top margin), mirroring publishing configuration options. [\[32\]](https://helpx.adobe.com/indesign/using/grids.html)  
3) Use OCR baseline fitting or proxy baselines from text bbox bottoms; OCR research shows baselines may be curved and fitted with splines after line detection. [\[11\]](https://research.google.com/pubs/archive/33418.pdf)  
4) Allow **regional baseline grids**: sidebars and tables may use different leading and should not force a global baseline change.

**Exception rules**  
- Decorative typography (posters) and UI components (cards) may not align to baseline; treat as baseline-independent modules.  
- Curved baselines (scans, distortions) need local baseline models; OCR explicitly handles curved baselines via fitted splines. [\[11\]](https://research.google.com/pubs/archive/33418.pdf)  
- PDFs can encode text as positioned fragments; do not assume consistent line order or consistent y increments per extracted text stream. [\[23\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)

**Fallback logic**  
- If baseline increment cannot be reliably inferred, fall back to a **spacing unit grid** (e.g., 4px/8px) derived from common deltas across vertical gaps, and treat text leading as independent per style.  
- If multiple increments compete, choose the one that best fits the majority body style; mark alternates.

**Failure conditions**  
- Mixed leading styles interleaved (legacy documents) causing multi-modal baseline spacing.  
- OCR line detection errors (merged lines, missed diacritics) that corrupt baseline estimates; baseline fitting occurs after line finding and assumes line detection is mostly correct. [\[11\]](https://research.google.com/pubs/archive/33418.pdf)  
- Applying a single baseline grid across heterogeneous zones when the source layout intentionally uses multiple rhythms.

**Measurable thresholds**  
- Baseline fit residual (std dev of `(y_baseline mod step)`) ≤ 1.25px at 1× raster resolution for “strong baseline.”  
- Coverage: ≥80% of body text lines align within tolerance to treat baseline as global; otherwise treat baseline as per-region.

**Implementation guidance**  
- Implement `BaselineEstimator` with: (a) body-text classifier, (b) robust step detection (autocorrelation or clustering of y deltas), (c) phase inference, (d) optional curvature model.  
- Store baseline as a first-class object used by normalization: snapping y positions and vertical paddings.  
- When exporting to publishing-oriented settings, align to baseline grid configuration fields (start offset, increment). [\[32\]](https://helpx.adobe.com/indesign/using/grids.html)

**Test cases**  
- Two-column editorial page with body text aligned across columns; expect single baseline step and stable phase. [\[33\]](https://helpx.adobe.com/indesign/using/grids.html)  
- Scanned page with slight warping near binding; expect local-baseline correction, not global baseline failure. [\[11\]](https://research.google.com/pubs/archive/33418.pdf)

**Topic: 12/8/4 responsive inference**

**Definition**  
Inferring a breakpoint-aware grid mapping where the same design system logically reflows across device classes using a 12-column (desktop), 8-column (tablet), and 4-column (phone) structure. Material’s responsive guidance describes 12-column responsive UI and discrete margin/gutter values tied to an 8dp baseline, and separately identifies 4/8/12 column grids across devices. [\[34\]](https://m1.material.io/layout/responsive-ui.html)

**Why it matters**  
Most reconstruction targets require re-implementable layout specs; a single static grid is insufficient if the operator must extend designs responsively. Also, many “inferred grids” fail because they overfit one screenshot width and cannot generalize to other breakpoints.

**Default rules**  
1) Infer a **canonical column count family** rather than one fixed grid: attempt {12, 8, 4} first if the artifact resembles Material-like responsive layouts, because device/adaptive evidence supports that mapping. [\[35\]](https://m2.material.io/design/layout/responsive-layout-grid.html)  
2) Prefer **consistent margins/gutters** across breakpoints and allow column widths to flex; Material guidance emphasizes consistent margin/gutter widths rather than column width. [\[5\]](https://m1.material.io/layout/responsive-ui.html)  
3) Classify the grid container mode: **full-width** (fluid columns) vs **centered** (fixed columns with margins growing), matching responsive grid behavior descriptions. [\[5\]](https://m1.material.io/layout/responsive-ui.html)  
4) Snap inferred spacing to baseline increments (8dp‑like) when evidence is strong (repeated 8/16/24/40 deltas). [\[5\]](https://m1.material.io/layout/responsive-ui.html)

**Exception rules**  
- Dense dashboards and large tables may not follow 12/8/4; they often use bespoke microgrids or split panes.  
- Some responsive designs collapse directly to 1 column on mobile; treat 4-col as an implementation grid rather than a visible “layout grid.” Nielsen Norman Group notes cases where desktop uses 12 columns and mobile reflows; do not hardcode 4-col if evidence shows single-stack. [\[36\]](https://www.nngroup.com/articles/using-grids-in-interface-designs/)  
- Side panels can exist outside the responsive grid and “squeeze” content; treat panels as separate containers rather than forcing them into column math. [\[5\]](https://m1.material.io/layout/responsive-ui.html)

**Fallback logic**  
- If you only have one screenshot size, infer the local grid but produce **hypothetical breakpoint projections** by mapping spans proportionally (e.g., 6/12 → 4/8 → 2/4) and flag as low-confidence until validated on more sizes.  
- If elements do not align to integer spans, fall back to `flex/flow` constraints rather than a strict column grid.

**Failure conditions**  
- Producing breakpoint grids that create non-integer spans for most elements.  
- Inferred margins/gutters change unpredictably across breakpoints (indicates wrong container mode or mixed templates).  
- Treating overlays and temporary panels as grid content rather than as separate layers. [\[5\]](https://m1.material.io/layout/responsive-ui.html)

**Measurable thresholds**  
- Integer-span coverage: ≥70% of major blocks map to integer column spans at inferred breakpoints to call it a “column grid responsive layout.”  
- Margin/gutter invariance: at least one of {margin, gutter} should remain constant across breakpoints in the inferred spec when the system indicates it (Material’s emphasis). [\[5\]](https://m1.material.io/layout/responsive-ui.html)

**Implementation guidance**  
- Store responsive grid spec as a list of breakpoint entries: `[{bp: phone, cols:4, margin, gutter}, ...]` with inheritance rules.  
- Provide `SpanMapper` to convert fixed pixel widths into column spans per breakpoint.  
- Integrate a constraint solver layer for reflow; constraint-based solvers support linear constraints and hierarchies used by layout systems. [\[15\]](https://badros.com/greg/papers/cassowary-tochi.pdf)

**Test cases**  
- Product listing UI: 12-col desktop with 3–4 cards per row; expect mapping to 8-col tablet, 4-col phone with consistent gutters. [\[37\]](https://m2.material.io/design/layout/responsive-layout-grid.html)  
- UI with persistent side nav: verify panel outside grid behavior and content “squeeze.” [\[5\]](https://m1.material.io/layout/responsive-ui.html)

**Topic: Editorial vs dashboard vs poster exceptions**

**Definition**  
A domain-aware layer that modifies grid inference, baseline rhythm expectations, and exception handling based on layout genre: editorial pages emphasize reading order and baseline/columns; dashboards emphasize dense modularity, nested grids, and alignment for scanning; posters emphasize expressive hierarchy and may use rotated or non-Manhattan structures.

**Why it matters**  
A single inference policy that assumes Manhattan multi-column text will fail on posters (rotation/overlaps) and will over-constrain dashboards (where multiple microgrids coexist). Document analysis research explicitly distinguishes Manhattan vs non-Manhattan and notes many methods assume Manhattan layouts, which cannot be assumed in general. [\[38\]](https://www.marenglenbiba.net/icdar09.pdf)

**Default rules**  
1) Editorial mode: prioritize (a) column separator inference via whitespace rectangles, (b) baseline grid reconstruction, (c) reading-order heuristics and block hierarchy. [\[39\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)  
2) Dashboard mode: prioritize (a) repeated card/tile geometry, (b) nested grids, (c) alignment clustering over whitespace, (d) constraint-based layouts for resizable panels. Constraint solver literature notes that under/over-specification impacts results; dashboards often require flexible constraint systems. [\[40\]](https://yuejiang-nj.github.io/Publications/2020CHI_ORCSolver/paper.pdf)  
3) Poster mode: allow large exceptions; treat rotation as first-class; prefer oriented whitespace and geometry rather than projection-based Manhattan assumptions. [\[26\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)

**Exception rules**  
- Hybrid documents (editorial with infographic dashboard section) require multiple local modes.  
- “Collage” posters can have weak or absent grids; treat the task as reconstruction + redesign recommendation rather than strict preservation.  
- Dashboards may use rules like “align to cards not columns”; do not force a 12-col grid if the dominant structure is a tile matrix.

**Fallback logic**  
- Auto-classify genre using signals: text density and line continuity (editorial), presence of repeated equal-sized panels and charts (dashboard), large hero imagery with sparse text and possible rotation (poster).  
- If classification confidence is low, run all three inference profiles and pick highest score.

**Failure conditions**  
- Misclassifying posters as editorials: projection/column inference fails due to rotation and yields fragmented blocks. [\[41\]](https://www.dfki.de/fileadmin/user_upload/import/5012_Shafait-xycut-PAMI.pdf)  
- Misclassifying dashboards as editorials: baseline inference overfits and forces irrelevant vertical rhythm.  
- Treating callouts/pull quotes as new grid columns rather than exceptions.

**Measurable thresholds**  
- Poster rotation indicator: if \>15% of detected text boxes have orientation not within ±3° of the dominant axis, poster/non-Manhattan handling becomes default. [\[26\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)  
- Dashboard repetition indicator: if ≥6 similarly sized rectangles repeat on a grid-like lattice, enable dashboard microgrid inference.

**Implementation guidance**  
- Implement `LayoutGenreClassifier` → selects inference policy + scoring weights.  
- Encode “genre exceptions” as explicit patterns: full-bleed, rotated block, overlay label, chart legend.  
- Maintain layered model: global grid + local grids + exceptions.

**Test cases**  
- Magazine spread with pull quote crossing columns; preserve baseline/columns and mark quote as exception span.  
- Dashboard with resizable left filter panel; treat as separate container with constraints outside main grid. [\[42\]](https://m1.material.io/layout/responsive-ui.html)  
- Poster with rotated title and aligned body rectangle: infer base grid for body; rotate-only exception for title. [\[26\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)

**Topic: Normalization of inconsistent legacy layouts**

**Definition**  
Given a layout whose implied grid is inconsistent (mixed spacing, off-by-1 alignments, multiple templates), produce a normalized grid+spacing system that (a) preserves recognizable structure, (b) reduces arbitrary variation, and (c) provides stable constraints for future extension.

**Why it matters**  
Legacy layouts are often “dirty”: inconsistent margins across screens, slightly different gutters, mixed baseline increments. If the expert tries to preserve every inconsistency, it cannot produce reusable rules; if it over-normalizes, it destroys recognizable structure. Document analysis recognizes that rule-based systems can become arbitrary and that tuned parameters matter; modern dataset work emphasizes robustness across diverse layouts because accuracy drops on more challenging layouts. [\[43\]](https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf)

**Default rules**  
1) Normalize using **robust central tendencies**: median margin/gutter/column widths rather than mean, to resist outliers.  
2) Prefer **tokenization**: convert observed spacings into a small set of spacing tokens (base unit + multiples). Material-like systems support 8dp-based increments; editorial systems support leading-driven increments. [\[44\]](https://m1.material.io/layout/responsive-ui.html)  
3) Preserve **relative structure** first: column spans, ordering, grouping; then snap micro-geometry (pixels/points).  
4) Separate **template variance** from noise: cluster screens/pages into templates prior to normalization.

**Exception rules**  
- When inconsistencies are semantically meaningful (e.g., different section templates), do not normalize across them; instead produce a `TemplateFamily` with shared token systems.  
- For scanned documents with skew/noise, use rotation/cleanup tolerant methods; projection methods can be sensitive to border noise and parameter choices. [\[45\]](https://www.dfki.de/fileadmin/user_upload/import/5012_Shafait-xycut-PAMI.pdf)

**Fallback logic**  
- If normalization would move too many elements, downgrade from “hard snap” to “soft snap” and only normalize new additions.  
- If inferred base unit differs by region, store multiple spacing systems but connect them via mapping rules (e.g., 10pt leading ≈ 8pt baseline \* 1.25).

**Failure conditions**  
- Over-normalization: semantic emphasis and hierarchy destroyed (e.g., hero no longer stands out).  
- Under-normalization: too many tokens; spacing remains inconsistent.  
- Drift across iterations: applying normalization repeatedly changes output each time (should converge).

**Measurable thresholds**  
- Token count budget: default ≤ 8 spacing tokens per template; exceeding triggers re-clustering or relaxed constraints.  
- Movement budget: median absolute movement of snapped elements ≤ 0.25×gutter (or ≤2px for 1× UI) to apply automatically; beyond requires “preserve grid, don’t snap content.”

**Implementation guidance**  
- Provide `NormalizeLayout` operator that takes `{gridSpec, baselineSpec, elements}` and outputs `{normalizedElements, tokenMap, diffReport}`.  
- Use an evaluation/backtracking loop; PDF engineering sources emphasize difficulties when approaches cannot backtrack. [\[8\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)  
- Log a “diff heatmap” (which elements moved, by how much, and why) to support human review in operator workflows.

**Test cases**  
- Legacy web page family where gutters vary between 18–22px; normalize to 20px while keeping hero and nav exceptions.  
- Multi-page PDF where some pages have 2 columns and some 3; cluster templates, infer two GridSpecs, normalize within each. [\[46\]](https://research.ibm.com/publications/doclaynet-a-large-human-annotated-dataset-for-document-layout-segmentation)

**Topic: Screenshot-based structural reconstruction**

**Definition**  
Recovering structured, editable layout representations (components, groups, constraints) from raster images of UIs, documents, posters, or slides. Research systems show that screenshots are “flat” and unstructured; reconstruction aims to infer vector components and their hierarchical relationships. [\[47\]](https://faculty.washington.edu/ajko/papers/Swearngin2018Rewire.pdf)

**Why it matters**  
Screenshots are a primary input class for design operator packs (e.g., “rebuild this UI”). Without structural reconstruction, the expert can only approximate visuals and cannot support reuse, editing, or extension.

**Default rules**  
1) Segment the screenshot into candidate regions, then infer structure. DCGen’s motivating study identifies omission, distortion, and misarrangement as key failure types for vision+LLM generation and shows segment-aware processing improves similarity. [\[48\]](https://arxiv.org/html/2406.16386v1)  
2) Use OCR and component detection to produce primitive boxes; then cluster into groups (rows/columns/lists), similar to reverse engineering approaches that identify UI elements and infer hierarchy. [\[49\]](https://ranger.uta.edu/~csallner/papers/nguyen15reverse.pdf)  
3) Infer repeated structures (lists, grids) via similarity and lattice detection; treat them as components with parameters.

**Exception rules**  
- Shadows, gradients, and overlays are not layout structure; treat as stylistic layers attached to components, not as containers.  
- Vector-like screenshots (sharp edges) can be reconstructed more reliably than compressed/anti-aliased ones; increase tolerances for low-quality images.

**Fallback logic**  
- If full hierarchy inference is unstable, output a “flat but aligned” layer set plus a proposed hierarchy with low confidence.  
- If OCR is unreliable, use visual grouping and treat text as blocks; allow later refinement.

**Failure conditions**  
- Element omission: missing small icons/labels due to segmentation thresholds. [\[48\]](https://arxiv.org/html/2406.16386v1)  
- Misarrangement: grouping errors (wrong parent container) causing layout drift on reflow; screen parsing focuses specifically on relationships, not just boxes. [\[50\]](https://machinelearning.apple.com/research/screen-parsing)  
- Over-splitting: dividing one component into many due to internal borders.

**Measurable thresholds**  
- Coverage: ≥95% of visible pixels attributable to some component layer for “full reconstruction,” else partial.  
- Hierarchy confidence: ≥0.7 if repeated patterns (list items) are consistently grouped.

**Implementation guidance**  
- Implement `ScreenshotParse` operator returning: `{elements, groups, relations, gridEvidence, textEvidence}`.  
- Integrate a “segment-first” pipeline: `global segmentation → local description → reassembly`, mirroring DCGen’s divide-and-conquer logic. [\[48\]](https://arxiv.org/html/2406.16386v1)  
- Provide `VectorizeIfPossible` options inspired by Rewire: reconstruct UI components as editable objects with shape and style properties. [\[51\]](https://faculty.washington.edu/ajko/papers/Swearngin2018Rewire.pdf)

**Test cases**  
- Mobile chat screen with repeated list rows; expect proper list grouping and alignment constraints. [\[52\]](https://ranger.uta.edu/~csallner/papers/nguyen15reverse.pdf)  
- Web landing page hero with overlay CTA; expect overlay as layered exception, not a separate grid column.  
- Screenshot of dashboard with 3 chart cards; expect card component + nested chart containers.

**Topic: Document-layout extension without drift**

**Definition**  
Adding new content (blocks, cards, sections, pages) to a reconstructed layout while preserving the inferred grid/baseline/spacing system, so that the design remains consistent over time. Constraint solving literature frames layout as satisfying linear constraints with priorities; document engineering warns about inflexible rules and highlights the need for evaluation/backtracking. [\[53\]](https://badros.com/greg/papers/cassowary-tochi.pdf)

**Why it matters**  
Most real workflows are not restoration-only. The operator pack must support “extend this report,” “add a new card,” “insert a new section,” and keep the system from drifting away from the inferred grid after multiple edits.

**Default rules**  
1) Treat the inferred grid and baseline as **hard constraints**, and content placement as **soft constraints** unless it is part of a declared exception pattern.  
2) Extension must choose spans and positions that preserve integer column spans and baseline alignment when those are the dominant system.  
3) Use **constraint-solving** to resolve conflicts (e.g., competing preferred widths) rather than ad hoc resizing. Cassowary is designed for incremental UI constraint solving over linear equations/inequalities. [\[54\]](https://badros.com/greg/papers/cassowary-tochi.pdf)  
4) Re-run evaluation after extension; if quality drops below threshold, backtrack and try next candidate insertion layout.

**Exception rules**  
- Adding new exception types should be rare and explicit; otherwise the model slowly shifts to accommodate novel content.  
- For PDFs, ensure extension respects page boxes and clipping regions; new content must not unintentionally fall into bleed/crop zones. [\[28\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html)  
- For dashboards, extension may occur within microgrids rather than the global grid.

**Fallback logic**  
- If constraints are under-specified (many solutions), use a secondary objective: minimize deviation from original alignment distribution (“least change”).  
- If constraints are over-specified (no solution), relax soft constraints in priority order (e.g., internal padding → card width → span) and preserve global grid first. Constraint solver literature warns under/over-specification leads to unpredictability or conflicts. [\[55\]](https://yuejiang-nj.github.io/Publications/2020CHI_ORCSolver/paper.pdf)

**Failure conditions**  
- Drift: repeated extensions move the effective margin/gutter/baseline away from original.  
- Constraint oscillation: two states alternate on re-solve (indicates ambiguous priorities).  
- Overlapping / clipping introduced by extension.

**Measurable thresholds**  
- Drift budget: after an extension, grid parameters must not change by more than 1 “token step” (e.g., 8dp) without explicit “redesign grid” decision. [\[56\]](https://m1.material.io/layout/responsive-ui.html)  
- Post-extension score: `layoutScore(new) ≥ 0.9 × layoutScore(original)` to auto-accept.

**Implementation guidance**  
- Provide `ExtendLayout` operator that takes `{gridSpec, baselineSpec, constraintGraph, newContentSpec}` → outputs `{placements, updatedConstraints, diff}`.  
- Use a constraint solver backend (Cassowary-like) for linear constraints; ORC-style solvers show that constraints are low-level and hard to specify directly, motivating higher-level layout abstractions (row/column/flow). [\[15\]](https://badros.com/greg/papers/cassowary-tochi.pdf)  
- Keep a persistent “grid-lock” mode: grid cannot change unless a redesign decision is made.

**Test cases**  
- Insert a new editorial sidebar: must align to baseline and column grid, not force new column widths. [\[33\]](https://helpx.adobe.com/indesign/using/grids.html)  
- Add a new dashboard filter pill row: should wrap within container using flow constraints, keep card grid intact. [\[55\]](https://yuejiang-nj.github.io/Publications/2020CHI_ORCSolver/paper.pdf)

**Topic: When to preserve vs redesign the grid**

**Definition**  
A decision policy that determines whether the inferred grid should be preserved (snap and extend within it) or whether the artifacts are inconsistent enough that a new normalized grid should be proposed (redesign), while still respecting recognizable structure.

**Why it matters**  
Preserving a bad/inconsistent grid makes every extension brittle; redesigning too aggressively breaks brand/layout identity. UX guidance warns that breaking grids can make scanning harder when done unintentionally; grid breaking should be deliberate. [\[57\]](https://www.nngroup.com/articles/using-grids-in-interface-designs/)

**Default rules**  
Preserve the grid when:  
- A single grid explains most placements with low exception rate.  
- Baseline rhythm is strong across text-heavy areas.  
- Grid is stable across related pages/screens (same template family).

Redesign (normalize) when:  
- Multiple grids compete without stability across samples (template drift).  
- Exception rate remains high even after introducing plausible exception patterns.  
- Spacing cannot be tokenized into a small coherent set without large movements. [\[58\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)

**Exception rules**  
- Products with known legacy constraints (e.g., pixel-perfect compliance) may require preserve-first even at higher exception rates; treat normalization as “suggested refactor” not mandatory.  
- Certain artifacts (posters) can legitimately avoid a strong grid; preservation may mean preserving a *composition* rather than a grid.

**Fallback logic**  
- If undecidable, preserve grid for reconstruction output, but also generate a **redesign candidate** grid and provide a diff with predicted benefits (reduced token count, improved alignment coverage).

**Failure conditions**  
- Premature redesign: grid changes cause cascade changes that alter semantics/hierarchy.  
- Premature preservation: extension keeps adding exceptions until the model becomes unusable.

**Measurable thresholds**  
- Preserve if `exceptionAreaRatio ≤ 0.18` and `gridConfidence ≥ 0.75`.  
- Redesign if `exceptionAreaRatio ≥ 0.35` or `tokenCount > 10` after normalization.  
- Require manual review if in between.

**Implementation guidance**  
- Implement `PreserveOrRedesignDecision` returning `{decision, evidence, thresholdsTriggered}`.  
- Provide explainability: surfaces which signals caused redesign recommendation (template variance, spacing entropy).  
- If redesign, constrain proposals to known grid families (12/8/4 for responsive UIs, 2–6 columns for editorials depending on page size) and baseline increments tied to body leading. [\[59\]](https://m1.material.io/layout/responsive-ui.html)

**Test cases**  
- Legacy marketing site with inconsistent section paddings but consistent columns: preserve columns, normalize spacing tokens.  
- Multi-template dashboard where each module uses different card widths: redesign into shared token system and per-module microgrids.

**Topic: Failure modes in inferred layouts**

**Definition**  
A taxonomy of ways inferred layouts can be wrong or brittle: mis-detected structure, wrong grid family, wrong exceptions, drift over time, incorrect coordinate transforms, and false confidence. DCGen explicitly identifies omission, distortion, and misarrangement as failure classes in screenshot-to-code. PDF engineering highlights backtracking difficulty and PDF-specific issues such as text order and kerning jumps. [\[60\]](https://arxiv.org/html/2406.16386v1)

**Why it matters**  
Strict operators must fail safely. A reconstruction expert should detect when inference is unreliable and switch to conservative behaviors (soft snap, partial reconstruction, or redesign suggestion).

**Default rules**  
1) Always produce an explicit `FailureReport` when confidence is below threshold.  
2) Prefer “partial but correct” outputs (grid only, or structure only) over full reconstructions with silent errors.

**Exception rules**  
- In screenshots, small decorative omissions may be acceptable if the goal is layout structure; in compliance workflows they may not.  
- In PDFs, reading order reconstruction is distinct from geometric grid inference; keep separate confidence channels. [\[61\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)

**Fallback logic**  
- Switch to segment-wise processing for screenshots to mitigate omission/misarrangement, consistent with divide-and-conquer evidence. [\[48\]](https://arxiv.org/html/2406.16386v1)  
- Switch from projection-based inference to oriented whitespace or clustering for non-Manhattan pages. [\[41\]](https://www.dfki.de/fileadmin/user_upload/import/5012_Shafait-xycut-PAMI.pdf)  
- If PDF text order is unreliable, rebuild order from geometry and clustering; do not trust stream order. [\[23\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)

**Failure conditions**  
- High omission rate in reconstruction output.  
- Misarrangement: elements placed in wrong parent container, causing layout breakage on resize. [\[62\]](https://arxiv.org/html/2406.16386v1)  
- Distortion: element sizes changed to fit wrong grid. [\[48\]](https://arxiv.org/html/2406.16386v1)  
- Coordinate mismatch: PDF rotation/UserUnit not handled; margins/boxes wrong; elements clip incorrectly. [\[63\]](https://kb.itextpdf.com/itext/how-to-get-the-userunit-from-a-pdf-file)  
- Parameter sensitivity (notably in projection algorithms): wrong thresholds cause over/under-segmentation. [\[22\]](https://www.dfki.de/fileadmin/user_upload/import/5012_Shafait-xycut-PAMI.pdf)

**Measurable thresholds**  
- Omission: missing \>2% of detected text blocks or \>5% of icon-sized primitives triggers failure. [\[48\]](https://arxiv.org/html/2406.16386v1)  
- Misarrangement: adjacency graph edges (expected neighbors) preserved \<85% triggers failure.  
- Drift: inferred grid parameters differ \>1 token step between iterations triggers failure.

**Implementation guidance**  
- Create a `layout-failure-taxonomy` and map each failure to: detection signals, severity, auto-mitigation, human escalation guidance.  
- For PDFs, include checks for page boxes, cropping, and known text-stream anomalies (kerning jumps). [\[64\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)  
- For screenshots, include segment-aware generation and verification passes (global-to-local-to-global), taken directly from the divide-and-conquer improvements. [\[48\]](https://arxiv.org/html/2406.16386v1)

**Test cases**  
- PDF with multi-column text where extracted text order is interleaved across columns; system must detect order inconsistency and reconstruct reading order geometrically. [\[23\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)  
- Screenshot with repeated list items where one icon is missed; must flag omission (low severity) and optionally repair. [\[65\]](https://arxiv.org/html/2406.16386v1)

## Operator-pack implementation blueprint

This section translates the playbook into a modular “design operator pack” architecture.

### Required operators and contracts

**Operator:** `ingest_artifact`  
Input: `{type: screenshot|pdf|html|slide, bytes|url, metadata}`  
Output: `{coordinateSpace, pages_or_viewports, render(s), rawObjects_if_vector}`  
- PDFs and vector sources: prefer object extraction; document engineering highlights that PDFs can provide encoded symbols and reduce need for OCR, but still need layout parsing. [\[66\]](https://www.cs.rit.edu/~rlaz/files/n_t_sf.pdf)  
- Raster sources: render at stable DPI and store DPI assumption.

**Operator:** `extract_primitives`  
Output: `{boxes[], textRuns[], images[], lines[], styleHints[]}`  
- For PDFs: parse page boxes; PDFBox-style APIs expose MediaBox/CropBox/BleedBox/TrimBox/ArtBox semantics and defaults (often CropBox). [\[29\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html)  
- For screenshots: OCR text boxes + detection boxes; keep uncertainty.

**Operator:** `infer_grid`  
Output: `{gridSpec, confidence, evidence, exceptionsCandidate}`  
- Implement multi-strategy candidates: whitespace rectangles (max empty rectangles), alignment clustering, projection splits (XY-cut) for limited domains, and oriented separators for non-Manhattan. [\[67\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)

**Operator:** `infer_baseline`  
Output: `{baselineSpec, confidence, evidence}`  
- Use document publishing defaults (increment ≈ body leading; configurable start relative to top/margins). [\[32\]](https://helpx.adobe.com/indesign/using/grids.html)  
- Support curved baseline models (OCR spline fitting). [\[11\]](https://research.google.com/pubs/archive/33418.pdf)

**Operator:** `build_constraint_graph`  
Output: `{constraints[], priorities, solvableStatus}`  
- Use constraint-solver compatible forms; Cassowary solves linear constraints incrementally and is designed for UI relations. [\[54\]](https://badros.com/greg/papers/cassowary-tochi.pdf)  
- For expressive layouts, allow soft constraints + objective penalty functions; layout solver literature discusses penalty comparators and priorities. [\[55\]](https://yuejiang-nj.github.io/Publications/2020CHI_ORCSolver/paper.pdf)

**Operator:** `normalize_layout`  
Output: `{normalizedElements, tokenMap, diffReport}`  
- Implement tokenization; align to baseline/grid when safe; otherwise soft snap.

**Operator:** `extend_layout`  
Output: `{newPlacements, updatedConstraints, driftReport}`  
- Must enforce grid lock unless redesign decision triggers.

**Operator:** `preserve_or_redesign`  
Output: `{decision, redesignedGridSpec?, rationale}`

**Operator:** `export_spec`  
Output targets: `{cssGridSpec, figmaConstraints, pdfTemplateSpec, slideMasterSpec}`  
- Include reading order separately for docs.

### Data schema sketch

A minimal serialization for downstream agents/tools:

- `GridSpec`: `{container: {x,y,w,h}, mode, cols, gutters[], margins, tracks[], breakpoints?}`
- `BaselineSpec`: `{step, start, relativeTo, regions?}`
- `LayoutGraph`: nodes = elements; edges = containment + alignment + spacing; attributes include confidence and source evidence.
- `ExceptionSet`: `{type, elements, rule}`
- `Quality`: `{gridConfidence, baselineConfidence, explainedPlacement, tokenEntropy, driftIndex}`

### Verification passes

Use multi-pass verification inspired by segment-aware pipelines: - Pass 1: detect primitives and coarse groups.  
- Pass 2: infer grids/baselines, snap softly, compute explained ratios.  
- Pass 3: re-segment ambiguous zones, refine, and re-score.  
DCGen’s results support that dividing into smaller visual segments mitigates omission/distortion/misarrangement in multimodal generation. [\[48\]](https://arxiv.org/html/2406.16386v1)

## Quality gates and failure taxonomy

This section defines a strict, measurable taxonomy aligned to operator pack needs, combining screenshot/system failures and PDF/document failures.

### Core failure classes

**Structural failures** - Missing primitives (omission) and over-splitting (fragmentation). [\[48\]](https://arxiv.org/html/2406.16386v1)  
- Wrong grouping / wrong parent (misarrangement). Screen parsing explicitly targets relationships and grouping beyond element detection. [\[50\]](https://machinelearning.apple.com/research/screen-parsing)

**Geometric model failures** - Wrong grid family (e.g., forcing 12-col on a microgrid dashboard).  
- Wrong margins/gutters due to cropping/box mismatch in PDFs. [\[29\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html)  
- Wrong baseline step due to mixed leading or OCR line errors. [\[68\]](https://research.google.com/pubs/archive/33418.pdf)

**Document-engineering failures** - Reading order errors due to PDF content stream not matching reading order; kerning operators jumping across columns; encoding unknown. [\[23\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)  
- No backtracking: rules applied at one granularity produce irreversible errors (“knowledge gap” and “difficult to backtrack”). [\[8\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)

**Parameter sensitivity failures** - Projection segmentation (XY-cut) sensitivity: wrong thresholds cause over/under-segmentation; projection methods also struggle beyond Manhattan layouts. [\[22\]](https://www.dfki.de/fileadmin/user_upload/import/5012_Shafait-xycut-PAMI.pdf)

### Quality-gate defaults

- **Auto-apply** (hard snap + extension permitted):  
  `gridConfidence ≥ 0.75` AND `baselineConfidence ≥ 0.70` (if baseline relevant) AND `explainedPlacement ≥ 0.80`.

- **Conservative** (soft snap, no redesign, extension requires confirmation):  
  `gridConfidence 0.55–0.75` OR `tokenEntropy high` OR `templateVariance detected`.

- **Fail safe** (structure-only output, plus diagnostics):  
  `gridConfidence < 0.55` OR omission/misarrangement exceed thresholds, or PDF reading-order inconsistency detected.

These gates intentionally mirror the need for evaluation/iteration rather than single-pass rules emphasized in document analysis critiques. [\[69\]](https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf)

## Deliverable markdown documents

The following are *copy-paste ready* contents for the requested deliverables. They are written so the master file can drive an agent, and the rule files can be used as strict operator policies.

**File:** `layout-reconstruction-grid-inference-expert.md`

Purpose: Define the expert agent’s mission, data contracts, inference rules, and failure-safe behaviors.

- Scope  
  The expert infers, reconstructs, normalizes, and extends layout systems from screenshots, PDFs, websites, slides, posters, editorials, dashboards, and inconsistent legacy sources.  
  Primary outputs: `GridSpec`, `BaselineSpec`, `ConstraintGraph`, `ExceptionSet`, `QualityReport`.

- Source priorities  
  Use grid/baseline priors from design systems and editorial practice (e.g., Grid Systems in Graphic Design[\[2\]](https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf); The Elements of Typographic Style[\[70\]](https://machinelearning.apple.com/research/screen-parsing); Making and Breaking the Grid[\[71\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html)) as priors, not as inference outputs; use document layout analysis and screen parsing research for inference and reconstruction mechanics. [\[72\]](https://niggli.ch/en/products/rastersysteme-fur-die-visuelle-gestaltung)

- Geometry and coordinate policy  
  PDFs: Respect page boxes and clipping semantics; PDF libraries define MediaBox/CropBox/BleedBox/TrimBox/ArtBox and defaults; never assume extracted text order equals reading order; handle UserUnit and rotation. [\[73\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html)  
  Screenshots: Treat DPI as an external rendering parameter; store it explicitly. [\[74\]](https://www.leadtools.com/help/sdk/dh/to/pdf-coordinate-system.html)

- Inference pipeline  
  1) Ingest → normalize coordinate space → extract primitives.  
  2) Infer candidate grids (whitespace rectangles; alignment clustering; limited-domain XY-cut; oriented separators). [\[75\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)  
  3) Infer baseline rhythm (increment≈body leading; phase relative to margin/page). [\[14\]](https://helpx.adobe.com/indesign/using/grids.html)  
  4) Build constraint graph; solve with priority (hard grid/baseline; soft content fit). Cassowary-like incremental constraint solving supports UI layout constraints. [\[15\]](https://badros.com/greg/papers/cassowary-tochi.pdf)  
  5) Normalize (tokenize spacing; snap within budget; produce diff report).  
  6) Extend without drift (grid lock; evaluate; backtrack). [\[20\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)  
  7) Export (CSS grid / layout constraints / publishing settings) and produce failure taxonomy report.

- Confidence and safety  
  Use evaluation-driven scoring; never silently hard-snap low-confidence models; produce `FailureReport` with remediation. Document engineering stresses the cost of inflexible, non-backtrackable rules. [\[8\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)

- The ten-topic playbook  
  Use the “Topic playbook for strict layout reconstruction” section of this report verbatim as the operational ruleset for the agent (topics: grid inference; margins/gutters/columns; baseline; 12/8/4 inference; genre exceptions; legacy normalization; screenshot reconstruction; extension; preserve vs redesign; failure modes).

**File:** `grid-inference-rules.md`

- Grid inference hierarchy  
  Prefer whitespace-rectangle inference for document-like layouts because maximal whitespace rectangles are demonstrated as major layout features and can be computed with branch-and-bound style methods. [\[12\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)  
  Prefer alignment clustering for dense UIs/dashboards where whitespace is unreliable.

- Candidate families  
  UI: {12, 8, 4} responsive family if evidence supports; Material guidance ties margins/gutters to an 8dp baseline and lists discrete values; treat these as snapping priors. [\[76\]](https://m1.material.io/layout/responsive-ui.html)  
  Editorial: {1, 2, 3, 4, 5, 6} columns; prefer exactly one global grid + nested grids rather than many globals.

- Separator validity rule (documents)  
  A gutter candidate must separate substantial foreground on both its long sides; otherwise it is “internal whitespace” and must not define columns. [\[12\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)

- Projection split rule (XY-cut)  
  Use only when (a) Manhattan layout assumption holds and (b) you can tune parameters for the domain; the method is parameter-sensitive and struggles beyond Manhattan layouts, but it is simple, fast, and can be controlled via split grammars in constrained domains. [\[22\]](https://www.dfki.de/fileadmin/user_upload/import/5012_Shafait-xycut-PAMI.pdf)

- Output contract  
  Always output `gridSpec + confidence + evidence + exceptionsCandidate`, plus a list of alternates if confidence \< 0.75.

**File:** `baseline-reconstruction-rules.md`

- Baseline increment prior  
  Default increment = body leading; this matches publishing configuration guidance. [\[32\]](https://helpx.adobe.com/indesign/using/grids.html)

- Baseline phase prior  
  Baseline grid start is relative to top-of-page or top margin; infer both and select the one yielding lower residual. [\[32\]](https://helpx.adobe.com/indesign/using/grids.html)

- Curved baseline support  
  Allow local baseline fitting; OCR research fits baselines using splines after line detection and can handle curved baselines. [\[11\]](https://research.google.com/pubs/archive/33418.pdf)

- Multi-rhythm rule  
  Sidebars/tables can use distinct rhythm; do not force global baseline if coverage \< 80%.

**File:** `legacy-layout-normalization-rules.md`

- Tokenization-first normalization  
  Normalize spacing into a limited set of tokens; constrain moves to a movement budget; if exceeded, switch to “normalize only new content.” Material-like discrete spacing and baseline guidance can serve as priors where appropriate. [\[44\]](https://m1.material.io/layout/responsive-ui.html)

- Template clustering  
  Cluster pages/screens into templates before normalization; datasets like DocLayNet exist because layouts vary widely and robustness drops when models overfit narrower domains. [\[77\]](https://research.ibm.com/publications/doclaynet-a-large-human-annotated-dataset-for-document-layout-segmentation)

- Backtracking requirement  
  Normalization must be reversible; document engineering highlights that rule-based approaches can be difficult to backtrack and inflexible at one granularity. [\[8\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)

**File:** `screenshot-reconstruction-rules.md`

- Segment-aware reconstruction  
  Use divide-and-conquer segmentation; DCGen identifies omission/distortion/misarrangement and shows segmentation improves similarity. [\[48\]](https://arxiv.org/html/2406.16386v1)

- Hierarchy inference  
  Infer groups/relations (rows, columns, lists) not just boxes; screen parsing centers the task of predicting UI elements and their relationships from a screenshot. [\[50\]](https://machinelearning.apple.com/research/screen-parsing)

- Editable vector goal  
  Prefer outputs as editable objects with shape/style properties (Rewire-style). [\[51\]](https://faculty.washington.edu/ajko/papers/Swearngin2018Rewire.pdf)

**File:** `layout-failure-taxonomy.md`

- Screenshot failures (primary)  
  Omission, distortion, misarrangement. [\[48\]](https://arxiv.org/html/2406.16386v1)

- Document/PDF failures (primary)  
  Reading-order mismatch; kerning operators jumping columns; encoding unknown; overprinting; text embedded in images; inability to backtrack. [\[78\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)

- Algorithmic failures  
  Manhattan-only assumptions in projection methods; parameter sensitivity causing over/under-segmentation. [\[22\]](https://www.dfki.de/fileadmin/user_upload/import/5012_Shafait-xycut-PAMI.pdf)

- Constraint failures  
  Under/over-specification leads to unpredictability/conflicts; constraint-solver literature flags these dynamics. [\[40\]](https://yuejiang-nj.github.io/Publications/2020CHI_ORCSolver/paper.pdf)

- Severity map  
  Define severity levels: `S0 cosmetic`, `S1 local structure`, `S2 global grid`, `S3 reading order/content integrity`, `S4 unsafe drift`.

**File:** `layout-test-cases.md`

- Test case format  
  Each test case includes: `input`, `expected GridSpec`, `expected BaselineSpec`, `expected exceptions`, `quality gates`, `failure expectations`.

- Baseline editorial tests  
  Two-column editorial page: baseline step ≈ leading; alignment across columns. [\[33\]](https://helpx.adobe.com/indesign/using/grids.html)

- Non-Manhattan tests  
  Poster with rotated headline: oriented exception + axis-aligned body grid. [\[26\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)

- PDF geometry tests  
  PDF with CropBox smaller than MediaBox: infer margins from visible region, not raw page size; handle page boxes. [\[29\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html)

- Screenshot UI tests  
  Chat list screenshot: detect repeated rows, infer list component and hierarchy. [\[79\]](https://ranger.uta.edu/~csallner/papers/nguyen15reverse.pdf)

- Design-to-code stress tests  
  Screenshots where naive generation omits small elements; ensure omission detected and reported. [\[48\]](https://arxiv.org/html/2406.16386v1)

A. Condensed operating spec  
A strict Layout Reconstruction and Grid Inference Expert must: (1) extract primitives into a normalized coordinate system; (2) infer GridSpec (columns/gutters/margins) using multi-strategy candidate generation and evaluation; (3) infer BaselineSpec where text rhythm is dominant; (4) build a ConstraintGraph with hard/soft priorities and solve using constraint-solver compatible forms; (5) normalize inconsistent layouts via tokenization and bounded snapping; (6) extend layouts under grid lock with evaluation and backtracking; (7) expose explicit exceptions; (8) emit confidence scores and FailureReports for unsafe states. The design is evaluation-driven because rule-only approaches are inflexible and hard to backtrack, and PDFs/screenshots introduce ordering and segmentation hazards. [\[80\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf)

B. Grid inference decision tree

    Start
      ↓
    Classify artifact: PDF/vector? screenshot/raster? web DOM?
      ↓
    Extract primitives (boxes/lines/whitespace evidence)
      ↓
    Genre classify: editorial vs dashboard vs poster vs mixed
      ↓
    Generate grid candidates:
        if document-like → whitespace rectangles + oriented variants
        if UI-like       → alignment clustering + nested microgrids
        if constrained domain & Manhattan → optional XY-cut
      ↓
    Score candidates (placement explainability + simplicity + exception compactness + stability)
      ↓
    gridConfidence ≥ 0.75 ?
       ├─ yes → lock GridSpec; infer BaselineSpec if text-heavy; build constraints
       └─ no  → try alternates; fall back to manuscript grid or local grids; soft snap only
      ↓
    If extending:
       Solve constraints; evaluate drift; backtrack if score drops
      ↓
    Emit: GridSpec, BaselineSpec, Constraints, Exceptions, Quality, FailureReport (if any)

[\[81\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)

C. Reconstruction checklist  
- Confirm coordinate space and container bounds (PDF boxes; screenshot DPI). [\[31\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html)  
- Extract primitives with uncertainty annotations.  
- Run genre classifier; choose inference profile. [\[82\]](https://www.marenglenbiba.net/icdar09.pdf)  
- Infer candidate grids; retain top N with scores. [\[83\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf)  
- Infer baseline rhythm if text-heavy; validate coverage. [\[14\]](https://helpx.adobe.com/indesign/using/grids.html)  
- Build constraint graph; label hard vs soft; check solvability. [\[15\]](https://badros.com/greg/papers/cassowary-tochi.pdf)  
- Produce reconstruction output + evidence + confidence + explicit exceptions.  
- If confidence low, produce partial safe output + FailureReport.

D. Normalization checklist  
- Cluster pages/screens into templates before normalizing. [\[77\]](https://research.ibm.com/publications/doclaynet-a-large-human-annotated-dataset-for-document-layout-segmentation)  
- Tokenize spacing/base unit; set token budget. [\[44\]](https://m1.material.io/layout/responsive-ui.html)  
- Snap within movement budget; otherwise soft snap only.  
- Verify convergence: repeated normalization should not change results materially.  
- Emit diff report and drift risk.

E. Twenty stress-test prompts  
1) “Given this scanned newspaper page with 6 columns and rotated sidebar ads, infer the global grid and list all non-Manhattan exceptions.”  
2) “Reconstruct the baseline grid from a PDF report where body text is aligned but headings break rhythm; output BaselineSpec and exception policy.”  
3) “From this dashboard screenshot with 12 cards, infer whether it’s a global 12-col grid or a tile microgrid; justify using measurable thresholds.”  
4) “This legacy UI has margins that vary by 6–10px across screens-normalize spacing tokens without shifting the hero section.”  
5) “Infer a 12/8/4 responsive mapping from a single desktop screenshot; output low-confidence breakpoint projections and what additional evidence you need.”  
6) “Extract layout from a PDF where text is not in reading order and kerning jumps across columns; recover reading order and grid separately.”  
7) “Poster: large full-bleed image, rotated title, tiny footer grid-decide preserve vs redesign and explain failure risks.”  
8) “Slides: infer slide master grid from 8 slides with inconsistent placements; cluster into templates and normalize.”  
9) “UI screenshot with heavy drop shadows: ensure shadows don’t become containers; reconstruct structure.”  
10) “Editorial spread with pull quotes spanning columns: preserve baseline and mark pull quote as controlled exception.”  
11) “PDF with CropBox smaller than MediaBox: infer margins and safe area correctly.”  
12) “Document with tables that break column rhythm: infer table microgrid without changing global columns.”  
13) “Mixed artifact: left side is editorial text, right side is dashboard with charts-run mixed-genre inference and output two coordinated grids.”  
14) “Run XY-cut on a Manhattan bank statement and show parameter sensitivity boundaries; then switch to whitespace rectangles and compare.”  
15) “Screenshot-to-code: detect and report omission/misarrangement failures after reconstruction; output FailureReport.”  
16) “Infer baseline on a warped scan near a book binding; allow curvature; quantify residual.”  
17) “Decide whether to redesign an inconsistent legacy layout where exceptionAreaRatio is 0.38 but the brand template must stay recognizable.”  
18) “Reconstruct a mobile UI list where separators are 1px lines that OCR misses; infer grouping anyway.”  
19) “Extend a reconstructed layout by adding a new section; prevent drift; show constraints and post-extension score.”  
20) “Given 5 related web pages, infer if they share a grid system; if not, cluster templates and output one GridSpec per cluster.”

[\[1\]](https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf) [\[2\]](https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf) [\[17\]](https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf) [\[18\]](https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf) [\[43\]](https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf) [\[69\]](https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf) https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf

<https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub2003015.pdf>

[\[3\]](https://niggli.ch/en/products/rastersysteme-fur-die-visuelle-gestaltung) [\[72\]](https://niggli.ch/en/products/rastersysteme-fur-die-visuelle-gestaltung) https://niggli.ch/en/products/rastersysteme-fur-die-visuelle-gestaltung

<https://niggli.ch/en/products/rastersysteme-fur-die-visuelle-gestaltung>

[\[4\]](https://helpx.adobe.com/indesign/using/grids.html) [\[14\]](https://helpx.adobe.com/indesign/using/grids.html) [\[32\]](https://helpx.adobe.com/indesign/using/grids.html) [\[33\]](https://helpx.adobe.com/indesign/using/grids.html) https://helpx.adobe.com/indesign/using/grids.html

<https://helpx.adobe.com/indesign/using/grids.html>

[\[5\]](https://m1.material.io/layout/responsive-ui.html) [\[27\]](https://m1.material.io/layout/responsive-ui.html) [\[34\]](https://m1.material.io/layout/responsive-ui.html) [\[42\]](https://m1.material.io/layout/responsive-ui.html) [\[44\]](https://m1.material.io/layout/responsive-ui.html) [\[56\]](https://m1.material.io/layout/responsive-ui.html) [\[59\]](https://m1.material.io/layout/responsive-ui.html) [\[76\]](https://m1.material.io/layout/responsive-ui.html) https://m1.material.io/layout/responsive-ui.html

<https://m1.material.io/layout/responsive-ui.html>

[\[6\]](https://m2.material.io/design/layout/responsive-layout-grid.html) [\[35\]](https://m2.material.io/design/layout/responsive-layout-grid.html) [\[37\]](https://m2.material.io/design/layout/responsive-layout-grid.html) https://m2.material.io/design/layout/responsive-layout-grid.html

<https://m2.material.io/design/layout/responsive-layout-grid.html>

[\[7\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html) [\[13\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html) [\[28\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html) [\[29\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html) [\[31\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html) [\[71\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html) [\[73\]](https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html) https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html

<https://pdfbox.apache.org/docs/2.0.2/javadocs/org/apache/pdfbox/pdmodel/PDPage.html>

[\[8\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf) [\[20\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf) [\[23\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf) [\[24\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf) [\[58\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf) [\[61\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf) [\[64\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf) [\[78\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf) [\[80\]](https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf) https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf

<https://pdfa.org/wp-content/uploads/2025/10/0-3-15_30-TamirHassan-Extracting_Data_From_PDF_Tables.pdf>

[\[9\]](https://faculty.washington.edu/ajko/papers/Swearngin2018Rewire.pdf) [\[47\]](https://faculty.washington.edu/ajko/papers/Swearngin2018Rewire.pdf) [\[51\]](https://faculty.washington.edu/ajko/papers/Swearngin2018Rewire.pdf) https://faculty.washington.edu/ajko/papers/Swearngin2018Rewire.pdf

<https://faculty.washington.edu/ajko/papers/Swearngin2018Rewire.pdf>

[\[10\]](https://ranger.uta.edu/~csallner/papers/nguyen15reverse.pdf) [\[19\]](https://ranger.uta.edu/~csallner/papers/nguyen15reverse.pdf) [\[49\]](https://ranger.uta.edu/~csallner/papers/nguyen15reverse.pdf) [\[52\]](https://ranger.uta.edu/~csallner/papers/nguyen15reverse.pdf) [\[79\]](https://ranger.uta.edu/~csallner/papers/nguyen15reverse.pdf) https://ranger.uta.edu/~csallner/papers/nguyen15reverse.pdf

<https://ranger.uta.edu/~csallner/papers/nguyen15reverse.pdf>

[\[11\]](https://research.google.com/pubs/archive/33418.pdf) [\[68\]](https://research.google.com/pubs/archive/33418.pdf) https://research.google.com/pubs/archive/33418.pdf

<https://research.google.com/pubs/archive/33418.pdf>

[\[12\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf) [\[21\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf) [\[25\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf) [\[26\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf) [\[39\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf) [\[67\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf) [\[75\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf) [\[81\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf) [\[83\]](https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf) https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf

<https://www.dfki.de/fileadmin/user_upload/import/1998_2003-breuel-icdar.pdf>

[\[15\]](https://badros.com/greg/papers/cassowary-tochi.pdf) [\[53\]](https://badros.com/greg/papers/cassowary-tochi.pdf) [\[54\]](https://badros.com/greg/papers/cassowary-tochi.pdf) https://badros.com/greg/papers/cassowary-tochi.pdf

<https://badros.com/greg/papers/cassowary-tochi.pdf>

[\[16\]](https://www.nngroup.com/articles/using-grids-in-interface-designs/) [\[36\]](https://www.nngroup.com/articles/using-grids-in-interface-designs/) [\[57\]](https://www.nngroup.com/articles/using-grids-in-interface-designs/) https://www.nngroup.com/articles/using-grids-in-interface-designs/

<https://www.nngroup.com/articles/using-grids-in-interface-designs/>

[\[22\]](https://www.dfki.de/fileadmin/user_upload/import/5012_Shafait-xycut-PAMI.pdf) [\[41\]](https://www.dfki.de/fileadmin/user_upload/import/5012_Shafait-xycut-PAMI.pdf) [\[45\]](https://www.dfki.de/fileadmin/user_upload/import/5012_Shafait-xycut-PAMI.pdf) https://www.dfki.de/fileadmin/user_upload/import/5012_Shafait-xycut-PAMI.pdf

<https://www.dfki.de/fileadmin/user_upload/import/5012_Shafait-xycut-PAMI.pdf>

[\[30\]](https://kb.itextpdf.com/itext/how-to-get-the-userunit-from-a-pdf-file) [\[63\]](https://kb.itextpdf.com/itext/how-to-get-the-userunit-from-a-pdf-file) https://kb.itextpdf.com/itext/how-to-get-the-userunit-from-a-pdf-file

<https://kb.itextpdf.com/itext/how-to-get-the-userunit-from-a-pdf-file>

[\[38\]](https://www.marenglenbiba.net/icdar09.pdf) [\[82\]](https://www.marenglenbiba.net/icdar09.pdf) https://www.marenglenbiba.net/icdar09.pdf

<https://www.marenglenbiba.net/icdar09.pdf>

[\[40\]](https://yuejiang-nj.github.io/Publications/2020CHI_ORCSolver/paper.pdf) [\[55\]](https://yuejiang-nj.github.io/Publications/2020CHI_ORCSolver/paper.pdf) https://yuejiang-nj.github.io/Publications/2020CHI_ORCSolver/paper.pdf

<https://yuejiang-nj.github.io/Publications/2020CHI_ORCSolver/paper.pdf>

[\[46\]](https://research.ibm.com/publications/doclaynet-a-large-human-annotated-dataset-for-document-layout-segmentation) [\[77\]](https://research.ibm.com/publications/doclaynet-a-large-human-annotated-dataset-for-document-layout-segmentation) https://research.ibm.com/publications/doclaynet-a-large-human-annotated-dataset-for-document-layout-segmentation

<https://research.ibm.com/publications/doclaynet-a-large-human-annotated-dataset-for-document-layout-segmentation>

[\[48\]](https://arxiv.org/html/2406.16386v1) [\[60\]](https://arxiv.org/html/2406.16386v1) [\[62\]](https://arxiv.org/html/2406.16386v1) [\[65\]](https://arxiv.org/html/2406.16386v1) https://arxiv.org/html/2406.16386v1

<https://arxiv.org/html/2406.16386v1>

[\[50\]](https://machinelearning.apple.com/research/screen-parsing) [\[70\]](https://machinelearning.apple.com/research/screen-parsing) https://machinelearning.apple.com/research/screen-parsing

<https://machinelearning.apple.com/research/screen-parsing>

[\[66\]](https://www.cs.rit.edu/~rlaz/files/n_t_sf.pdf) https://www.cs.rit.edu/~rlaz/files/n_t_sf.pdf

<https://www.cs.rit.edu/~rlaz/files/n_t_sf.pdf>

[\[74\]](https://www.leadtools.com/help/sdk/dh/to/pdf-coordinate-system.html) https://www.leadtools.com/help/sdk/dh/to/pdf-coordinate-system.html

<https://www.leadtools.com/help/sdk/dh/to/pdf-coordinate-system.html>
