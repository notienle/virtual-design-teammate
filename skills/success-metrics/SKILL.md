---
name: success-metrics
description: >
  Define success metrics for any initiative. This skill should be used when the user asks "how do we
  measure success", "define the metric", "what's the KPI", "success criteria for", "set a target",
  "guardrails for this launch", or whenever a plan, PRD, strategy, or experiment needs its outcome made
  measurable. Lead skill of the /define-metrics command; also loaded by /strategize, /map-journey,
  /hypothesis and /test-plan stacks. Trigger even when metrics are mentioned casually - an initiative
  without a defined metric is a finding.
metadata:
  version: "0.2.0"
  phase: define
---

# Success metrics

Make "it worked" falsifiable before the work starts. Refuse vanity politely: page views measure traffic, not success.

## Metric definition workflow

1. **Anchor on the user outcome, not the output.** Shipped screens and feature usage are outputs; the metric is the behavior change they should cause ("merchandisers complete price setup without support tickets", not "price setup page visits").
2. **Primary metric - exactly one.** The decision-maker: if it moves, the initiative worked. Write its exact definition: event(s), population, time window, unit of analysis (user vs account - B2B usually account).
3. **Guardrails.** What must not degrade: task success elsewhere, latency, support contact rate, adoption of adjacent features. 2-4, each with its own definition.
4. **Leading indicator.** The early signal readable in days/weeks when the primary needs a quarter (activation step completion as a leading indicator of retention).
5. **Baseline and target.** Current value, target, and the reasoning for the target (comparable launches, benchmark, or explicit judgment - labeled). No baseline available = an instrumentation gap; flag what event tracking must ship WITH the feature, or the metric is fiction.
6. **Counter-gaming check.** How could this metric look good while users suffer? Add the guardrail that catches it.

## Rules

- Definitions are exact or they are debates deferred: "active" gets a definition, "engagement" gets banned or decomposed.
- Percentages carry their base ("of 1,240 accounts"); small segments report absolute counts too.
- One initiative, one primary. Dashboards can hold many numbers; decisions can't.
- If analytics access exists (product-analytics skill or PowerBI MCP connected), pull the baseline now; otherwise state the pull needed and proceed with the definition.

## Output format

Inline metric spec: primary (with full definition), guardrails, leading indicator, baseline, target with reasoning, instrumentation needs. Route "test it with traffic" to `experiment-design`, "tie it to the roadmap bet" to `design-strategy`, "report the impact after" to `design-communication`.
