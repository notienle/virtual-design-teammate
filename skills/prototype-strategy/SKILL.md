---
name: prototype-strategy
description: >
  Choose prototyping fidelity and method, and hand off to build. This skill should be used when the user
  asks "should I prototype this", "what fidelity", "Figma or code prototype", "how do I test this idea",
  "set up a sandbox for", or is about to build a prototype and needs the approach. The BUILDING itself
  happens in Claude Code with the team sandbox setup - this skill picks the method and writes the handover.
  Loaded by the /test-plan command stack.
metadata:
  version: "0.1.0"
  phase: prototype
---

# Prototype strategy

A prototype is a question wearing a costume. Start from the question; pick the cheapest costume that answers it.

## Fidelity selection

| Question to answer | Method |
|---|---|
| Is the concept/value understood | Sketch or narrative walkthrough, static frames |
| Can users navigate/find (structure) | Clickable low-fi flow, tree/click test (user-research-methods) |
| Can users complete the task (flow + comprehension) | Figma clickable prototype, realistic content |
| Does the interaction feel right (timing, direct manipulation, AI streaming) | Coded prototype - Figma can't fake these |
| Will it work with real data density/latency | Coded prototype with realistic volume |
| Will stakeholders fund it (vision) | Polished coded prototype or high-fi frames + narrative |

Rules: realistic content always (lorem ipsum invalidates comprehension tests); build only the paths under test and design honest dead ends ("not in this prototype"); one prototype per major question - a franken-prototype answering everything answers nothing well.

## Coded prototype handover (Claude Code + sandbox)

The team stack: Next.js + Axiom v3 React components + TypeScript, sandbox repos per product area (CoCo-sandbox, OCP-sandbox pattern), deployed to Vercel for shareable links. When the choice is code, produce a handover brief for Claude Code:

1. The question this prototype answers, and who will see it (test participants vs stakeholders - changes polish bar).
2. Scope: screens/flows in, dead-end handling, states required (pull from flows-and-states).
3. Data: realistic fake dataset shape and volume; never real customer data, credentials, or internal financials in a deployed prototype - Vercel links leak.
4. Axiom components involved (verified names via MCP) and any intentional deviations.
5. Interaction specs that motivated code: timings, streaming behavior, drag behavior.
6. Definition of done: the demo script or test tasks it must support.

## After the prototype

Route testing design to `user-research-methods`, findings to `research-synthesis`, and the keep/kill/iterate decision back to `design-strategy`. Prototypes are disposable; log what the prototype taught, then let it die - promoting prototype code to production is engineering's call, not a default.
