---
name: visual-design
description: >
  Visual craft: hierarchy, typography, color, spacing, layout grids, data visualization, motion, and
  adaptive design (responsive, dark mode, localization-ready layouts). This skill should be used when the
  user asks "does this look right", "improve the hierarchy", "type scale", "spacing feels off", "chart for
  this data", "which color", "layout for this page", or any how-should-it-look question. Do NOT use for
  full critique of a finished screen (route to design-critique) - use this when DESIGNING, not judging.
  Loaded by the /design-pattern stack.
metadata:
  version: "0.1.0"
  phase: ideate
---

# Visual design

Craft in service of comprehension. Every visual decision must answer: what should the user see first, second, and never have to see at all. Verify token and scale values against the Axiom MCP (`get_tokens`) before quoting them; never invent values.

## Hierarchy

Establish exactly one entry point per screen; size, weight, color, and position are a budget - spend on what matters, refund elsewhere. Sequence check: squint (or blur) and name the first three things you see; if they aren't the user's first three tasks, redistribute weight. Prefer spacing and position over adding weight; bolding everything is bolding nothing.

## Typography

Use the Axiom type scale; no off-scale sizes. Hierarchy through 2 weights and 3-4 sizes max per screen. Line length 45-75 characters for reading text; data-dense tables exempt. Line height: looser for paragraphs, tighter for headings and table cells. Sentence case per Optimizely convention.

## Color

Semantic first: color from Axiom semantic tokens (danger, success, warning, info, accent) carries meaning; decorative color is a last resort. One accent doing the "look here" job per view. Never encode meaning in color alone - pair with icon, label, or position (accessibility skill owns the contrast math; consult it for ratios).

## Spacing and layout

Spacing scale from Axiom tokens; consistent rhythm beats generous-but-random gaps. Group with whitespace before boxes and dividers (proximity is the cheapest grouping tool). Grid: define columns, gutters, and regions per breakpoint; content areas should map to the grid, not float. Enterprise density: default comfortable, offer compact for data-heavy screens rather than compromising both.

## Data visualization

Chart from the question: comparison = bar, trend = line, part-of-whole = stacked bar (pie only under 4 slices), distribution = histogram, correlation = scatter. Zero-baseline for bars; label directly instead of legends when under 5 series; gray for context, color for the point being made. Every chart needs: title stating the takeaway, axis units, source and window. Tables beat charts when users need exact values.

## Motion

Motion explains change: where things came from, where they went. Durations 150-250ms for micro, 250-400ms for surface-level; ease-out for entering, ease-in for exiting. Respect prefers-reduced-motion always. No motion for decoration in enterprise workflows.

## Adaptive

Responsive: define behavior per component (reflow, collapse, hide with access path) - never truncate primary actions. Dark mode: use semantic tokens so it's free; check elevated-surface contrast and desaturate large color fields. Localization-ready: layouts survive +35% text length (German), avoid text in images, icons+labels over icon-only.

## Output format

Inline: the recommendation, the principle behind it, and the one alternative considered. Route done-screen judgment to `design-critique`, token architecture to `design-tokens`.
