---
name: design-strategy
description: >
  Strategic design direction and prioritization. This skill should be used when the user asks about
  "north star", "vision", "design principles", "prioritize these opportunities", "impact vs effort",
  "reward effort scorecard", "what should we do first", "define the metric", "how do we measure success",
  or needs to connect design choices to business outcomes and H1/H2 planning. Trigger for any
  which-bet-and-why conversation. Lead skill of the /strategize command; route metric definition
  to success-metrics.
metadata:
  version: "0.1.0"
  phase: define
---

# Design strategy

Help make bets legible: what we're aiming at, why these opportunities first, and how we'll know it worked.

## North star and vision

A north star describes the experience at its best in user-outcome terms, 1-3 years out, opinionated enough to say no with. Structure: the shift (from X to Y), 3-4 pillars each with a vivid "you'll know we're there when..." moment, and explicit tensions resolved (e.g., power vs simplicity: we choose defaults with escape hatches). Test: does it exclude plausible roadmap items? If everything fits, it's a poster, not a strategy.

## Design principles

3-5, each: name, one-line rule, a real tradeoff it settles, and a this-not-that example from an Optimizely surface. Kill any principle no reasonable person would oppose ("be user-centered").

## Opportunity prioritization

Default model: simple multi-dimension scorecard, few dimensions, anchored scales.
- Dimensions: user impact (severity x reach, evidenced), business impact (revenue/retention/cost, route sizing to product-analytics), effort (design + eng, get an eng gut-check), confidence in the evidence.
- Score 1-3 or 1-5 with written anchors per level; never average away confidence - show it as its own column.
- Output: ranked table, the top cut with rationale, and what evidence would change the ranking. Resist false precision; the scorecard structures argument, it doesn't replace judgment.

## Measurability

Every prioritized bet needs its success made falsifiable - route metric definition (primary, guardrails, baselines, targets) to `success-metrics`; do not define metrics here.


## Output format

Inline, decision-ready. Strategy documents for exec circulation go to Word/slides via the optimizely-brand skill with design-communication structuring the narrative.
