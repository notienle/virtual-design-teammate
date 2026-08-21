---
name: prd-to-design-plan
description: >
  The starting point of any design project, however it arrives. This skill should be used when the user
  shares a PRD, epic, feature spec, or Jira/Confluence requirements ("review this PRD", "what's the design
  work here", "turn this into a design plan"), AND when there are no requirements yet and the problem needs
  framing ("frame this problem", "write a brief", "kick off", "how might we", "define the problem", a fuzzy
  idea that needs structure). Also use to reframe stuck feature debates around jobs-to-be-done. Part of the
  /strategize command stack.
metadata:
  version: "0.2.0"
  phase: define
---

# PRD to design plan

Own the start of every project. Two modes depending on what exists; state which mode is running.

## Mode A - requirements exist (PRD, epic, spec)

1. **Extract the skeleton.** Goal and success metrics, target users, in-scope capabilities, explicit non-goals, dependencies, timeline. Quote the PRD's own words; note where it is silent.
2. **Interrogate the framing.** Is the problem evidenced or asserted? Does the metric measure user outcome or feature shipment (route definition to `success-metrics`)? Are "requirements" solutions in disguise? List challenges plainly, each with a question for the PM.
3. **Map the design surface.** Screens and flows touched (new vs modified), states each flow needs (loading, empty, error, permission-denied - PRDs almost never list these), copy needs, Axiom components involved (verify via Axiom MCP), cross-surface impact.
4. **Identify design risks** and what would de-risk each: judgment, a spike, or research (note research skills are currently parked; flag the gap honestly).
5. **Plan the work.** Design tasks in sequence with rough sizes, decision checkpoints with named deciders, needs from PM/eng with dates, review plan.
6. **Number the open questions.** Each with: why it blocks or shapes design, the default assumption if unanswered, and the owner.

## Mode B - no requirements yet (frame the problem)

Build the brief a PRD would have needed:
1. **Problem statement.** Who has the problem, what happens today, what it costs, and the evidence. Tag every claim: evidence, assumption, or decision. Zero solution words.
2. **Why now.** Strategy, customer commitment, competitive pressure, or tech change.
3. **Users and context.** Which archetypes (from design-context), in which surface, at what moment.
4. **How might we.** 1-3 HMW statements at the right altitude - test: can you name a solution the HMW rules out? If not, narrow.
5. **Success criteria.** Route metric definition to `success-metrics`; keep criteria behavioral.
6. **Constraints and non-goals.** Technical, Axiom, timeline, and explicitly what this will NOT do.
7. **Risks, open questions, stakeholders.** Owners and resolution paths; decider named.

Quality bar: someone could disagree with the framing. A brief nobody could object to says nothing.

## JTBD reframing (either mode)

When a feature debate is stuck on "what", pull it back to "why": When [situation], I want to [motivation], so I can [outcome]. Capture functional, emotional (feel in control, avoid blame), and social (look competent) jobs, plus what they hire today (including spreadsheets and email). Jobs are stable; solutions churn - write them solution-free.

## Output format

Inline: mode stated, then the plan or brief, then numbered open questions. Offer a Word version via the optimizely-brand skill for circulation. Route strategy-level direction to `design-strategy`, journeys to `journey-mapping`.
