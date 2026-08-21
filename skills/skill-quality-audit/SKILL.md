---
name: skill-quality-audit
description: >
  Quality-check and audit skill files - the benchmark for this pack. This skill should be used when the
  user types /skill-eval, asks to "audit this skill", "quality check a skill", "review this SKILL.md",
  "validate the pack", "check trigger collisions", "is this skill good enough to merge", or contributes
  a new/changed skill for review. Runs three graders: structural validation (script), trigger audit
  (descriptions + collision matrix), and content quality (rubric). Also use before any release of the pack.
metadata:
  version: "0.2.0"
  phase: others
---

# Skill quality audit

Three graders, run in order - each catches what the previous cannot. Two modes: **single-skill** (a contribution or change; run all graders on it plus a collision check against the pack) and **whole-pack** (release audit; run everything on everything).

## Grader 1 - Structural (deterministic)

Run `scripts/validate.py` from this skill's directory against the plugin root (bash: `python3 skills/skill-quality-audit/scripts/validate.py <plugin-root>`). It checks: manifest validity, frontmatter parses with name matching directory, description present and under limits, SKILL.md under 500 lines, referenced files exist, routing mentions point to skills that exist (active or parked), and duplicate names. Any failure is a **Blocker** - do not proceed to judgment graders until structure passes.

## Grader 2 - Trigger audit (judgment)

**Description rubric** - grade each description pass/fail with quoted evidence:
- Third person, starts with what it does, includes "use when" trigger situations
- Contains realistic trigger phrases a designer would actually type (not just topic nouns)
- States at least one do-NOT-use boundary with the sibling skill named
- No overclaim: description promises only what the body delivers

**Collision matrix** - the pack-level check nothing else does:
1. Take the prompt set in `evals/trigger-prompts.md` (or generate 3-5 realistic prompts per skill under audit, including deliberately ambiguous ones).
2. For each prompt, reading ONLY the descriptions, predict which skill fires; record confidence.
3. Build the matrix: prompts x skills. Every off-diagonal hit (prompt intended for A, routed to B) is a finding naming which description to tighten and how.
4. Ambiguous-by-design prompts ("this table feels cluttered") must resolve to a documented winner; "either could fire" is a **Major**.

## Grader 3 - Content quality (rubric)

Grade the body against pack conventions, each criterion pass/fail with a quoted line as evidence:
- **Imperative and specific.** Instructions command ("check contrast at 4.5:1"), never hedge ("ensure good accessibility"). Generic advice a non-Optimizely skill could contain is a finding.
- **Progressive disclosure.** Lean SKILL.md, depth in references/; reference files referenced by exact path; nothing duplicated between them.
- **No memory-asserted facts.** Anything verifiable live (token values, component props, current product behavior) instructs verification via MCP, never states values from memory.
- **Workflow completeness.** Numbered or clearly ordered steps; output format defined; edge/failure behavior stated (what to do when a connector or dependency is missing).
- **Routing discipline.** Boundaries to sibling skills explicit; no skill silently re-implements a sibling's job.
- **Pack voice.** Sentence case, no em-dashes, concrete Optimizely grounding where relevant, realistic-but-fake data only.

## Consistency and variance note

For skills whose output quality matters most (critique, specs), recommend a 3-run variance check on one golden task: same input three times, compare finding counts and severity distribution. High variance = ambiguous instructions; name the ambiguous section.

## Finding format and verdict

Findings use the pack standard: severity (Blocker / Major / Minor / Polish), location (file + section), issue, why it matters, fix. Verdict per skill: **merge** (no Blockers/Majors), **merge with fixes** (Minors listed), **revise** (Majors), **reject** (Blockers or structural fails). Whole-pack mode adds: collision matrix summary, worst offenders, and top 3 pack-level risks.

## Boundaries

This skill audits skill files; it does not run behavioral evals against live Claude sessions - offer the built-in skill-creator's eval loop for that, seeded with `evals/trigger-prompts.md`.
