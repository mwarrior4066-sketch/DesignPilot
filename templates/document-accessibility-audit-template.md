# Document Accessibility Audit Template

## Document context
- file type:
- must remain selectable: yes/no
- must remain accessible: yes/no
- known standard target: PDF/UA / tagged PDF / unknown

## Structure
- headings tagged:
- lists tagged:
- tables structured:
- figures have alt text:
- artifacts marked:

## Reading order
- logical reading order valid:
- multi-column order checked:
- form fields / annotations checked:

## Text integrity
- fonts embedded:
- Unicode mapping valid:
- ligature extraction safe:
- OCR needed: yes/no

## Findings
- blocker issues:
- warning issues:
- safe fixes:
- risky tradeoffs:

## Example output
### Document context
- file type: tagged PDF export of a quarterly compliance report
- must remain selectable: yes
- must remain accessible: yes
- known standard target: PDF/UA-aligned tagged PDF

### Structure
- headings tagged: partially; H1 and H2 exist, but several section headers are visually bold only
- lists tagged: yes in narrative sections, no in one recommendations block
- tables structured: partially; main summary table lacks explicit header association on repeated rows
- figures have alt text: two charts do, one summary diagram does not
- artifacts marked: footer line and page number are not yet marked as artifacts

### Reading order
- logical reading order valid: mostly, but one two-column spread reads chart caption before left-column body text
- multi-column order checked: yes, and one spread fails
- form fields / annotations checked: not applicable in this file

### Text integrity
- fonts embedded: yes
- Unicode mapping valid: mostly, but one ligature extraction issue was detected in copied text
- ligature extraction safe: no, needs correction before final release
- OCR needed: no, source is already digital text

### Findings
- blocker issues: missing artifact marking, one broken multi-column reading order, one figure with no alt text, one ligature extraction failure
- warning issues: inconsistent list tagging and weak table header associations
- safe fixes: retag footer/page numbers as artifacts, correct figure alt text, repair heading tags, normalize table headers
- risky tradeoffs: rebuilding the affected two-column spread may disturb line breaks, so reading-order repair should be done before visual cleanup
