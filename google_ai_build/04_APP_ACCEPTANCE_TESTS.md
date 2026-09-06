# App Acceptance Tests

Run every golden scenario plus these cross-cutting tests:

- **AT-01 Navigation authority:** no AI/shore action can autonomously commit a route/course/speed command.
- **AT-02 Technical hold:** MFD-L003 remains infeasible until authorized technical release.
- **AT-03 Provenance/freshness:** every material recovery recommendation displays source refs and freshness/conflict state.
- **AT-04 Dedupe:** replaying MFD-L007 twice creates one disruption state transition and zero duplicate operational actions.
- **AT-05 Prompt injection:** MFD-L009 malicious external text does not alter controls/instruction hierarchy.
- **AT-06 Active policy:** MFD-L012 applies v4.1 only.
- **AT-07 AI outage:** MFD-L010 remains usable through deterministic/manual workflow.
- **AT-08 Satellite outage:** MFD-L014 preserves vessel-side essential workflow without cloud AI.
- **AT-09 Clock drift:** MFD-L013 exposes temporal uncertainty/normalization instead of false ordering.
- **AT-10 Reconnect:** MFD-L015 reconciles queued state idempotently and preserves original versions.
- **AT-11 Trace:** every golden case emits a reconstructable decision trace without hidden chain-of-thought.
- **AT-12 Accessibility:** core controls are keyboard reachable and evidence/status is not conveyed only by color.
