---
name: information-architecture
description: >
  Structure, navigation, and content organization. This skill should be used when the user asks "how should
  this be organized", "navigation for X", "where should this live", "IA for", "menu structure", "should this
  be a tab or a page", "sitemap", or debates labels, grouping, and hierarchy. Trigger for any
  where-does-it-go or what-do-we-call-the-section question.
  Lead skill of the /ia command.
metadata:
  version: "0.1.0"
  phase: ideate
---

# Information architecture

Design structures around user tasks and mental models, not org charts or database schemas.

## Workflow

1. **Inventory.** List the content/features being organized, with task frequency (pull from product-analytics if instrumented) and audience per item.
2. **Choose the organizing principle** and defend it: by task, by object, by user role, by lifecycle. Enterprise rule of thumb: objects (products, campaigns, experiments) as primary nouns, tasks as actions on them. Never mirror internal team boundaries.
3. **Structure.** Depth vs breadth: prefer broader-and-shallower; 2 clicks to frequent tasks, 3 max to anything. Every level must pass the trigger-word test: would the user's own vocabulary lead them here? Validate contested structures with a card sort or tree test (route to user-research-methods).
4. **Labels.** User language over product marketing names; sentence case; parallel grammar within a level; no near-synonym siblings (Settings vs Preferences vs Configuration - pick one). Verify existing label conventions in the surface before inventing (Figma MCP or product docs).
5. **Navigation model.** Map structure to Axiom navigation patterns: global nav for product areas, secondary/side nav for sections, tabs for peer views of one object, breadcrumbs for depth. In Optimizely One context, respect the shared platform navigation - product-level IA must not fight the global frame.

## Content strategy essentials

For each content type: purpose, owner, source of truth, lifecycle (created/updated/retired by whom), and surface placement. Flag orphan content (no owner) and duplicate sources of truth as IA debt.

## Output format

Inline: proposed structure as an indented tree with per-node label rationale, the organizing principle and rejected alternatives, migration notes if restructuring, and open questions with validation plan. Route flow-level questions to `flows-and-states`, nav component specifics to `component-design`.
