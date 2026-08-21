# Lens: composition

Evaluate balance, whitespace, rhythm, and gestalt structure.

- **Alignment integrity.** Edges align to a grid: count distinct left-edge x-positions in a column layout - more than 3-4 unexplained edges reads as clutter. Optical alignment beats mathematical for icons/mixed elements; flag near-misses (2-3px off) as Polish, structural misalignment as Minor/Major.
- **Grouping (gestalt).** Proximity: intra-group spacing visibly smaller than inter-group (at least ~1.5x). Common region: containers only where proximity can't do the job - box-in-box-in-box means spacing failed. Similarity: same-kind items share treatment. Test: remove all borders mentally - does structure survive?
- **Balance and density distribution.** Visual weight distributed intentionally (not necessarily symmetric); detect stranded corners, lopsided pages where nav+filters outweigh content, and orphaned elements floating without an anchor.
- **Rhythm.** Spacing steps from the Axiom scale, applied consistently: same relationship = same gap everywhere. Random 12/14/18/22px gaps = token drift finding.
- **Breathing room at edges.** Content respecting page margins and container padding; text touching card edges is a Minor that reads as broken.
- **Responsive composition.** If multiple breakpoints shown: does the grouping logic survive reflow, or do unrelated items collide on narrow widths?
