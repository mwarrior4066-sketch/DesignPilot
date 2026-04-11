# Layout Reconstruction Brief Template

## Source
- source type: screenshot / PDF / slide / web page / editorial / other
- page or viewport size:
- what must be preserved:
- what may change:

## Inference targets
- margins:
- columns:
- gutters:
- baseline / vertical rhythm:
- repeated modules:
- exception zones:

## Confidence
- strong / medium / weak:
- ambiguous areas:
- fallback model if inference fails:

## Extension request
- what is being added or repaired:
- whether the new content must follow the existing system exactly:
- normalization allowed: yes/no

## Example output
### Source
- source type: PDF spread from an existing annual report
- page or viewport size: A4 portrait, facing pages
- what must be preserved: margins, editorial hierarchy, image placement rhythm, and overall typographic texture
- what may change: body copy text content, figure captions, and one added sidebar callout

### Inference targets
- margins: outer margins appear consistent at roughly one baseline unit larger than inner margins
- columns: two primary text columns with one flexible image/callout span pattern
- gutters: central text gutter is consistent and should be normalized as the master column separator
- baseline / vertical rhythm: body copy appears locked to a stable baseline cadence that should govern new captions and callouts
- repeated modules: section opener pattern, caption style, pull-quote treatment, footer line
- exception zones: full-width image spreads and chapter openers intentionally break the normal text column system

### Confidence
- strong / medium / weak: medium-high
- ambiguous areas: one pull-quote block may be optically aligned rather than mathematically aligned; footer artifact region needs separate handling
- fallback model if inference fails: preserve margin and column structure first, then rebuild local modules on nearest 4pt/8pt rhythm

### Extension request
- what is being added or repaired: replace body copy and add one new sidebar explainer on page three
- whether the new content must follow the existing system exactly: yes for text frames and baseline behavior, no for the new sidebar content block if normalized carefully
- normalization allowed: yes, but only where the original spacing is inconsistent enough to break continuity

## Page architecture
- Page roles already present:
- Wayfinding elements:
- Header/footer contract:
- Content-box or vertical-fill assumptions:
- Dead zones / floating content observed:
