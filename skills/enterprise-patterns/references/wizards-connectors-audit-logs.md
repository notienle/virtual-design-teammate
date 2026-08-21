# Setup wizards

- Use when: sequence dependencies exist, or the blank-state alternative overwhelms. Don't wizard what a good form with defaults can do.
- Structure: numbered steps with labels (visible map), one decision theme per step, 3-7 steps. Review step before commit showing everything chosen, editable per section.
- Progress is sacred: save on every step advance, resumable from where they left, exit is always safe ("Saved as draft").
- Validate per step, not at the end; async checks (credentials, connections) run in-step with clear status and don't block typing.
- Branching: conditional steps appear/disappear in the map with count updates; never surprise-extend near the end.
- After finish: land on the created object with a "what happens next" panel, not back at a list.

# Connector and integration flows

- Catalog: connectors with status badges (installed, available, needs attention), search + category facets, each card stating what it syncs and what it needs.
- Connect flow: auth (OAuth preferred; API-key entry with visibility toggle, stored-securely note, never echoed back) -> scope/permission selection -> field mapping with sensible defaults and per-field override -> test connection with verbose success/failure detail -> initial sync expectations (duration, what appears where).
- Health surface (where users actually live): last sync time, next scheduled, records synced, error count with drill-in. Sync states: connected, syncing (progress), degraded (partial, since when), failed (reason + fix action + docs link), paused (by whom).
- Failure design: distinguish auth expiry (re-auth CTA), permission loss (what to grant), rate limits (auto-retry, when), data errors (per-record report, skip vs halt policy visible). Every failure has an owner action.
- Disconnect: state what stops, what data remains where, and export offer.

# Audit logs and activity feeds

- Entry anatomy: actor (human, API token, or agent - see ai-agentic-ux, all attributed), action verb, object with link, timestamp (relative + absolute), context (before/after values for changes, request origin for security-relevant events).
- Two consumers, two surfaces: activity feed (recent, human-readable, on the object: "what happened to this campaign") and audit log (admin/compliance: filterable by actor, action type, object, date range; exportable; retention stated).
- Filters over search: actor, action category, object type, date - these answer 90% of "who changed this".
- Immutability signaling: no edit/delete affordances; corrections happen as new entries.
- Write the entry copy as if it will be read in an incident review at 2am - because it will (route wording to ux-writing).
