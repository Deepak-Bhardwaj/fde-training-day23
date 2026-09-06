# PRD Generation Prompt

You are converting an **approved AI FDE architecture pack** for the Fleet Disruption & Voyage Recovery Intelligence Workbench into a build-ready PRD.

## Inputs
Use only:
- completed participant Templates 01–13;
- `Participant_Case_Study_Context_Aware_AI_FDE.md`;
- approved evidence/architecture decisions;
- app screen and acceptance requirements.

## Rules
1. Do not invent a capability, data permission, safety authority, policy threshold, integration or production technology that is not approved upstream.
2. Unresolved items must be written as `OPEN_DECISION` with owner/impact; do not silently fill gaps.
3. AI is decision support; it has no autonomous navigation command authority and cannot release critical maintenance holds.
4. Preserve vessel-edge offline continuity, event idempotency/replay handling and reconnect reconciliation.
5. Every functional requirement must state actor, trigger, inputs, behavior, output, evidence/provenance, deterministic control/human gate and error/degraded path.
6. Every AI behavior must map to one or more golden scenarios and acceptance thresholds.
7. Include semantic, ontology/KG, hybrid-retrieval and runtime-context contracts explicitly.
8. Decision trace requires observable evidence and concise rationale; never require hidden chain-of-thought.
9. The Google AI Build prototype uses only synthetic fixtures/local simulation; do not add real vessel, port, cargo, crew or navigation APIs.

## Required PRD sections
Use the structure in `participant_templates/14_PRD_template.md`, with numbered `FR-*`, `NFR-*`, `AI-*`, `DATA-*`, `CTRL-*`, `EVAL-*` and `UX-*` requirements plus a final traceability appendix.

## Final self-check
Reject your own draft if any requirement cannot point to an approved architecture decision/evidence source or if any workflow can turn AI output into autonomous navigation/control.
