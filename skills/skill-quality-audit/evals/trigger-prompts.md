# Trigger prompt set - starter

Purpose: input data for Grader 2 (collision matrix) in skill-quality-audit, and seed set for
behavioral evals via skill-creator. 3 prompts per lead skill: one obvious, one casual, one
deliberately ambiguous (expected winner noted). Extend when adding skills.

## Define

design-strategy: "help me build a UX strategy for Commerce Connect onboarding" | "which of these 6 CAB opportunities should we tackle first in H2" | AMBIG "is this feature worth doing" (winner: design-strategy; success-metrics only defines how to measure it)
prd-to-design-plan: "here's the PRD for bulk price editing, what's the design work" | "I have a fuzzy idea about improving connector setup, help me frame it" | AMBIG "kick off the new campaign module" (winner: prd-to-design-plan mode B)
success-metrics: "how do we measure success for the new import flow" | "PM wants a KPI for this, what should it be" | AMBIG "define success for the redesign" (winner: success-metrics; design-strategy takes the bet-level question)
journey-mapping: "map the merchandiser journey from catalog import to first publish" | "where does the onboarding experience break end to end" | AMBIG "map out how users set up a connector" (winner: journey-mapping if cross-stage; flows-and-states if single flow - matrix must document the tiebreak: stage count)

## Ideate

design-critique: "roast this screen" + screenshot | "any issues with this Figma frame?" | AMBIG "does this table look right" (winner: design-critique; enterprise-patterns only when DESIGNING a new table)
enterprise-patterns: "spec a bulk edit flow for the product table" | "how should saved views work in the order list" | AMBIG "this table feels cluttered" (winner: design-critique with information-density lens; enterprise-patterns supports)
interaction-patterns: "design the validation for this form" | "what should the empty state do here" | AMBIG "search isn't working well for users" (winner: interaction-patterns if designing; design-critique if judging an existing build)
flows-and-states: "map the flow for connector setup including errors" | "what states does this screen need" | AMBIG "what screens do we need for approvals" (winner: flows-and-states)
information-architecture: "where should audit logs live in the nav" | "is this a tab or a separate page" | AMBIG "users can't find the settings" (winner: information-architecture; ux-writing if it's purely the label)
visual-design: "the hierarchy on this dashboard feels flat, how do I fix it while designing" | "which chart for revenue by region over time" | AMBIG "make this screen look better" (winner: design-critique first to diagnose, visual-design to redesign)
ux-writing: "write the error message for a failed sync" | "empty state copy for the campaigns list" | AMBIG "this dialog is confusing" (winner: design-critique; ux-writing if user asks for rewrite only)
accessibility: "is this accessible, check WCAG" | "contrast check on these colors" | AMBIG "can keyboard users use this table" (winner: accessibility)
ux-laws: "why do users always miss this button, what's the principle" | "explain Hick's law for this menu" | AMBIG "why is this flow tiring" (winner: ux-laws for the why; design-critique for the full audit)

## Handoff

developer-handoff: "package this design for engineering" | "write acceptance criteria for the import flow" | AMBIG "eng asked what happens when the list is empty" (winner: developer-handoff; flows-and-states supports)

## Testing

experiment-design: "create a hypothesis for moving the publish button" | "how long should this A/B test run, sample size?" | AMBIG "test whether the new flow is better" (winner: experiment-design for traffic tests; note usability testing is parked - say so)
prototype-strategy: "should I prototype this in Figma or code" | "what fidelity do I need to test the drag interaction" | AMBIG "I want to try this idea out quickly" (winner: prototype-strategy)

## Others

skill-quality-audit: "audit this skill file before I merge it" | "/skill-eval on the new journey-mapping skill" | AMBIG "is this skill good" (winner: skill-quality-audit)
