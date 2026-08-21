# Lens: typography

Evaluate scale usage, readability, consistency, token compliance.

- **Scale discipline.** Every size on screen maps to the Axiom type scale (verify via get_tokens) - off-scale sizes are findings with the nearest token named. Count distinct size+weight combos: over ~6 per screen signals improvised hierarchy.
- **Hierarchy mechanics.** Heading levels distinguishable at a glance and used semantically in order (no h2 look after h4 look). Label vs value vs helper text: three visibly distinct treatments, used consistently across the screen.
- **Readability.** Body line length 45-75ch; line height ~1.4-1.6 body, tighter for headings; adequate paragraph spacing vs line spacing ratio (grouping must beat separation). Tables: no wrapped cell text in compact mode, truncation with full-value affordance.
- **Weight economy.** Two weights carrying hierarchy beats four; bold used for scan targets, not emphasis-of-everything. All-caps only where the system prescribes (check pattern), never for long strings.
- **Case and punctuation.** Sentence case per Optimizely convention - flag Title Case drift, inconsistent terminal periods in helper text, mixed date/number formats.
- **Truncation and overflow.** Long product names, emails, URLs: is behavior specced (truncate middle for IDs, end for names, tooltip/full-view access)? Missing = Minor, primary-identifier unrecoverable = Major.
