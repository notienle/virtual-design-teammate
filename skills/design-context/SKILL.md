---
name: design-context
description: >
  Optimizely product, user, and design system context. This skill should be loaded with EVERY design task -
  critique, research, specs, copy, strategy - so answers reflect real Optimizely surfaces, user types, Axiom
  conventions, and voice. Trigger whenever design-partner-core loads, whenever a specific Optimizely product
  (CMS, Configured Commerce, Commerce Connect, CoCo, OCP, ODP, Experimentation, CMP) is named, or whenever
  output must sound or look like Optimizely.
metadata:
  version: "0.1.0"
  phase: spine
---

# Optimizely design context

Apply this context silently. Do not recite it back to the user; let it shape the work.

## Design system of record

Axiom v3 is the single source of truth for components, tokens, patterns, and icons.

- Verify before asserting: use the Axiom MCP (`search_components`, `get_tokens`, `get_patterns`, `search_icons`) for current names, props, and values. Never quote a token value or component prop from memory when the MCP is connected.
- Use the Figma MCP (`get_design_context`, `get_screenshot`, `get_variable_defs`) when the user references a Figma file or node.
- If neither connector is available, say so, continue with general guidance, and mark anything unverified.
- Prefer composing existing Axiom components over inventing new ones. A new component proposal needs: the gap it fills, why existing components cannot compose it, and at least two consuming surfaces.

## Product surfaces

- Optimizely One platform: shared navigation, OptiID authentication, cross-product Home.
- CMS (content management), CMP (content marketing), Configured Commerce (B2B commerce), Commerce Connect / CoCo (composable commerce services), OCP (Optimizely Connect Platform - integrations and app development), ODP (data platform), Web Experimentation and Feature Experimentation.
- Platform & Commerce Design (PCD) owns Commerce Connect, OCP, Configured Commerce, and CMS surfaces.

## Users

Primary archetypes, in rough frequency order per surface:
- Marketers and content editors (CMS, CMP): non-technical, task-driven, hate losing work.
- Merchandisers and commerce managers (Configured Commerce, CoCo): data-heavy workflows, bulk operations, spreadsheets are the competitor.
- Developers (OCP, CoCo APIs, Experimentation SDKs): docs-first, judge the product by its error messages.
- Admins and IT (all surfaces): permissions, provisioning, audit, integration health.

Enterprise context: multi-tenant, role-based access, long sessions, dense data, migration anxiety. Users are experts in their job, novices in our IA.

## Voice

Optimizely voice in UI: clear, confident, helpful, never cute at the user's expense. Sentence case everywhere. Say what happened and what to do next. No blame ("something went wrong" beats "you entered an invalid value" when the system is at fault). Route detailed copy work to `ux-writing`.

## Output conventions

- Deliverables that leave the chat (Word, PowerPoint) must follow the organization optimizely-brand skill.
- Never include real customer data, credentials, or internal financials in prototypes, examples, or specs. Use realistic-but-fake data.
- English for professional outputs.
