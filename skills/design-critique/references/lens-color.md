# Lens: color

Evaluate contrast, palette coherence, semantic meaning, accessibility of color use.

- **Contrast (measure, don't eyeball).** Text 4.5:1 (3:1 for 18px+/14px bold+), UI component boundaries and states 3:1, focus indicators 3:1 against adjacent. Compute from actual hex values; findings cite the ratio ("2.9:1, needs 4.5:1"). WCAG failures = Blocker.
- **Semantic integrity.** Danger/success/warning/info drawn from Axiom semantic tokens and used for their meaning only - red for a brand accent next to red-for-error is a Major. One meaning per color per screen.
- **Color-alone coding.** Any status, category, or chart series distinguished by hue only fails; require paired icon, label, pattern, or position. Check the colorblind read (deuteranopia collapses red/green status dots).
- **Accent economy.** One accent doing the attention job; count competing saturated elements. Large saturated fills on data-dense screens fatigue - recommend tinted backgrounds with strong foreground instead.
- **Token compliance.** Hexes map to Axiom color tokens (verify); raw hexes and near-miss values are findings with the correct token named. Dark mode: semantic tokens used so it survives; flag hardcoded values that will break.
- **Chart color.** Gray for context, color for the point; sequential ramps for magnitude, categorical palettes capped ~6 before grouping.
