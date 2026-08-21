---
name: enterprise-patterns
description: >
  Enterprise B2B UI patterns - the bread and butter of Optimizely screens. This skill should be used when
  the user designs data tables or grids, filtering and faceted search, bulk actions and multi-select,
  roles and permissions UX, settings and admin pages, setup wizards, integration/connector flows, or audit
  logs and activity feeds. Trigger on "table for", "bulk edit", "filters", "saved views", "permissions",
  "admin settings", "setup wizard", "connector", "sync status", "audit log". Do NOT use for universal
  patterns like plain forms or search (route to interaction-patterns).
  Co-lead of the /design-pattern command (enterprise pattern types).
metadata:
  version: "0.1.0"
  phase: ideate
---

# Enterprise patterns

Patterns for multi-tenant, permissioned, data-dense work. Before specifying, check how existing Optimizely surfaces solve it (Figma MCP, product docs, Axiom `get_patterns`) - consistency across Configured Commerce, CoCo, OCP, and CMS beats local optimality.

| Designing... | Read |
|---|---|
| Tables, grids, dense data display | references/data-tables.md |
| Filters, facets, saved views, bulk actions | references/filtering-and-bulk-actions.md |
| Roles, permissions, settings, admin | references/permissions-and-settings.md |
| Wizards, connectors/integrations, audit logs | references/wizards-connectors-audit-logs.md |

## Universal enterprise rules

- The competitor is a spreadsheet: any workflow users currently do in Excel must be at least as fast in-product or provide export.
- Scale honesty: design for the 95th percentile account (thousands of rows, dozens of users), demo with realistic volume, and state pagination/virtualization needs in the spec.
- Multi-tenancy: every screen answers "which account/project am I in" without scrolling; cross-tenant leakage in pickers and search is a critical bug - flag it in specs.
- Reversibility ladder: undo > soft-delete with restore > confirm > hard block. Choose per blast radius and say why.
- Everything permissioned: spec the read-only and no-access variant of every screen (see permissions reference).

## Output format

Inline spec with states, edge cases at scale, and permission variants. Copy to `ux-writing`, component props to `component-design`, WCAG specifics to `accessibility`.
