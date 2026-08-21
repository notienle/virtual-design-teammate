---
name: journey-mapping
description: >
  Map experiences over time. This skill should be used when the user asks for a "journey map", "customer
  journey", "experience map", "service blueprint", "end-to-end experience", "map the touchpoints", or wants
  to see where an experience breaks across stages, channels, or teams. Trigger when pain is distributed
  across steps rather than in one screen.
  Lead skill of the /map-journey command.
metadata:
  version: "0.1.0"
  phase: define
---

# Journey mapping

Three formats by scope; choose deliberately and say why.

- **Journey map** - one persona, one goal, through your product. Default choice.
- **Experience map** - the whole ecosystem including channels you don't own (email, partner tools, spreadsheets). Use when the product is one touchpoint among many.
- **Service blueprint** - journey plus the frontstage/backstage machinery (support, provisioning, integrations, teams). Use when fixing the experience requires operational change, not just UI.

## Journey map structure

Columns = stages (name them as user intentions: "evaluate", "first configuration", "recover from an error" - not internal funnel names). Rows:
1. Doing - actions, tools, artifacts
2. Thinking - questions and decisions at each stage
3. Feeling - emotional curve with the trigger for each dip
4. Touchpoints - screens, emails, docs, humans
5. Pain and moments of truth - where trust is won or lost
6. Evidence - which research supports each cell
7. Opportunities - phrased as HMW, sized roughly

Anchor in evidence: build from research-synthesis output, analytics (product-analytics for stage drop-off), and support themes. Cells without evidence get marked as assumptions. For Optimizely surfaces, always include the non-product touchpoints enterprise users really have: CSM, support tickets, documentation, sandbox environments, procurement.

## Service blueprint additions

Below the journey rows: frontstage actions (staff/system visible to user), backstage actions, supporting processes and systems, and the lines of interaction/visibility. Mark failure points where backstage delays surface as user-facing silence.

## Output format

Inline as a structured table plus a short "top 3 moments to fix" summary with evidence. Offer a rendered diagram or a Word/slide version for workshops. Route opportunity prioritization to `design-strategy`, single-screen fixes to `design-critique`.
