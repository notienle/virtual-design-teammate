---
name: experiment-design
description: >
  Design trustworthy A/B tests and experiments. This skill should be used when the user asks to "design an
  experiment", "A/B test this", "test which version", "sample size", "is this result significant", "read
  these experiment results", or wants to validate a design change with live traffic. Trigger for any
  measure-it-in-production question - and yes, dogfood Optimizely Experimentation.
  Lead skill of the /hypothesis and /test-plan commands.
metadata:
  version: "0.1.0"
  phase: test
---

# Experiment design

We sell experimentation; our experiments should be exemplary. Design tests that can actually change a decision.

## Experiment spec

1. **Hypothesis.** Because we observed [evidence], we believe [change] for [population] will cause [outcome], measured by [metric] moving [direction, expected magnitude]. No evidence? Route to research-orchestrator first - experiments confirm and size; they're expensive discovery.
2. **Variants.** Control + minimal-difference treatment(s): one conceptual change per variant or attribution dies. Screenshot/spec each; note implementation parity risks (perf differences contaminate results).
3. **Metrics.** One primary (decision-maker), guardrails (what must not degrade: task success, latency, support contacts), and diagnostics (to explain the why). Exact definitions per product-analytics discipline: event, population, window.
4. **Population and unit.** Who's eligible, randomization unit (user vs account - B2B usually account to avoid within-account contamination), exclusions, and expected sample per week from current traffic (pull via product-analytics).
5. **Power and duration.** State minimum detectable effect worth acting on, then size honestly: small MDE on low-traffic enterprise surfaces can mean months - say so, and offer alternatives (bigger design swing, proxy metric, usability test instead). Run full business cycles (1-2+ weeks minimum); never stop on first significance.
6. **Decision rules, pre-committed.** Ship if primary improves and guardrails hold; kill if...; extend if... Written before launch, or the result will be negotiated after.

## Reading results

Check sample ratio mismatch first (allocation off = invalid test). Report: effect size with confidence interval (not just p), guardrails, segment consistency (interpret segment surprises as hypotheses, not conclusions - multiple comparisons lie). Flag novelty effects on changed UI; distinguish "no effect" from "underpowered". A trustworthy null is a finding: it kills a belief cheaply.

## When NOT to experiment

Sample too small for the MDE, change is a quality/consistency fix (just ship), measurement can't reach the outcome, or the ethical bar fails (experimenting on pricing transparency, etc. - see design-critique ethics lens). Recommend the honest alternative.

## Output format

Inline spec ready for Optimizely Experimentation setup. Route metric plumbing to product-analytics, result narratives for stakeholders to design-communication.
