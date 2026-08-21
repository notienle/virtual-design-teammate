# Errors

- Prevent > detect > recover. Prevention: constraints, confirmation-by-preview (show what will happen), and safe defaults.
- Every error answers: what happened, why (if known), what to do now, and how to get help. Include an error reference ID for support on system errors.
- Severity mapping: field error = inline; operation failure = in-context alert; system-level = page/banner. Never a toast for an error that requires action - toasts vanish.
- Partial failure in batch ops: report per-item results, keep successes, offer retry-failed-only (see enterprise-patterns bulk actions).
- Recovery: retry with backoff for transient, edit-and-resubmit for validation, escalate path for terminal. Log every dead end you design as debt.

# Feedback and notifications

- Match channel to urgency and persistence: inline change (no announcement needed - the UI is the feedback) < toast (transient confirmation, 4-6s, no actions except undo) < banner (persistent condition, dismiss rules stated) < modal (blocking decision only) < notification center (asynchronous, cross-session) < email (out-of-app consequence).
- One event, one channel. Confirm-and-toast-and-banner is noise.
- Undo in the toast for reversible actions is the highest-value pattern in this file: it removes confirmations from the critical path.
- Notification center: group by object, mark read state, deep-link to the thing, and honor per-category preferences.

# Loading and empty states

- Loading: skeleton for structure-known content, spinner only under 1s expectations, staged status text for multi-step operations (see ai-agentic-ux for AI latency), progress bar with numbers for determinate long ops. Keep chrome interactive; never block the whole page for a panel's data.
- Perceived speed: optimistic UI for high-success writes with reconciliation on failure; cache-and-refresh (stale-while-revalidate) with a subtle updated-at.
- Empty states, four kinds, each designed: first-use (teach + primary action), cleared (celebrate + next), no-results (see search), and error-empty (recovery). Every list, table, and dashboard panel ships all four.
