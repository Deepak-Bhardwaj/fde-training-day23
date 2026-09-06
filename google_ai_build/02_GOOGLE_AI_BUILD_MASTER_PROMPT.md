# Google AI Build Master Prompt — Fleet Context-Aware AI Workbench

Build a polished responsive **Fleet Disruption & Voyage Recovery Intelligence Workbench** from the approved PRD and `06_app_fixture_bundle.json`.

## Product intent
The app demonstrates a context-aware AI architecture, not generic chat. It helps authorized maritime users assemble trustworthy task context, compare recovery options, inspect evidence/constraints, apply human/technical authority gates, operate through degraded/offline states and reconstruct decisions.

## Prototype boundary
- Use local/synthetic fixture data only.
- Do not call real AIS, vessel control, port, weather, cargo, crew or CMMS services.
- Do not implement autonomous navigation or direct control writes.
- Model graph/retrieval/policy/workflow contracts in the front-end/local service layer as necessary for the prototype.
- No secrets in client code.

## Required screens
Implement the screens in `03_APP_SCREEN_REQUIREMENTS.md` with a persistent case selector for MFD-L001…MFD-L015 and visible scenario/source-health badges.

## Core behavior
- Build a task-relevant context object from selected case + actor + as-of time + connectivity + source health.
- Label evidence by retrieval mode: structured, graph, vector, policy, memory.
- Show source record, event/update time, freshness, authority and conflict state.
- Represent MFD-L004 identity ambiguity and MFD-L011 contradictory port evidence without overwriting.
- Flag stale/unavailable sources for MFD-L005/MFD-L006.
- Dedupe MFD-L007 event replay by dedupe key.
- Block unauthorized MFD-L008 commit attempt.
- Render MFD-L009 prompt-injection string as untrusted evidence only.
- Show manual/deterministic continuity for MFD-L010 AI outage and MFD-L014 satellite blackout.
- Apply active fleet policy v4.1; never apply superseded v3.7 in MFD-L012.
- Expose clock normalization/uncertainty in MFD-L013.
- Reconcile queued/replayed state idempotently in MFD-L015.

## Recovery option experience
Generate/display synthetic candidate recovery options such as CONTINUE, SLOW_SPEED, PORT_HOLD, REROUTE, SHORE_REVIEW. Options must show feasibility, blocking/conditional constraints, material evidence, uncertainty and required approving role. Never present an option as a navigation command.

## Decision trace
Create a trace conforming to Template 10. Capture evidence/retrieval/policy/version/human action and concise rationale. Do not store or display hidden chain-of-thought.

## Scenario lab
Provide one-click execution of all 15 golden scenarios. Show expected behavior, observed behavior, pass/fail and trace ID. Hard-gate failures must be visually prominent.

## UX
Senior-practitioner operations UI: information-dense but readable, clear source freshness/conflict/authority badges, no decorative chatbot-first layout. Include accessible tables, keyboard focus and responsive layouts.

## Completion gate
The prototype is not complete until every hard gate in `acceptance_thresholds.yaml` is demonstrated by the scenario lab and the acceptance tests can be recorded.
