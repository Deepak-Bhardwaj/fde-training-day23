# Participant Runbook — Fleet Context-Aware AI FDE Case

## Operating rule

Work in the sequence below. Do not jump directly from CSVs to an LLM prompt. The product is the **architecture + controlled workflow + evidence**, not the model demo.

## Step 0 — Read the case and traps

Read `Participant_Case_Study_Context_Aware_AI_FDE.md`, `architecture/Concept_Cheat_Sheet.md`, and every evidence README. Run `python scripts/profile_baseline.py` to compare the source-case benchmark with the actual 140-row workshop fixture.

## Stage 1 — Enterprise sources

Use Template 01. Inventory sources, owner/authority, access, identifiers, event/update/ingestion time, freshness threshold and degraded behavior. Identify which data is edge-local, shore-only, external, restricted or conditional.

**Gate:** you can explain what happens if PORT, WEATHER, SATELLITE or AI is unavailable.

## Stage 2 — Semantic foundation

Use Templates 02–03. Resolve ambiguous terms and define canonical business meaning. Separate observations from decisions and authority. Define ontology concepts/relationships/taxonomies and semantic constraints.

**Gate:** `AVAILABLE`, `APPROVED`, `RECOVERY_OPTION`, `EVENT_TIME`, and `GROUND_TRUTH` have unambiguous meanings.

## Stage 3 — Connected knowledge

Use Templates 04–05. Design entity resolution and the temporal/provenance KG. Demonstrate MFD-L004 and MFD-L011 without overwriting ambiguity/conflict.

**Gate:** every material graph fact can point back to source/time/version/resolution evidence.

## Stage 4 — Graph platform

Use Template 06. Start from query patterns, outage/update patterns, provenance and operating burden. Choose technology and document reversibility. The workshop can simulate the graph in JSON.

## Stage 5 — Hybrid retrieval

Use Template 07. Route exact state to structured retrieval, connected questions to graph, narratives/manuals to vector, active rules to policy retrieval and prior decisions/outcomes to controlled memory. Define filtering/fusion and conflict behavior.

## Stage 6 — Runtime context graph

Use Template 08. Define a context request and response contract. Include actor, voyage/case, as-of time, clock state, connectivity, source health/freshness, authority, conflicts and provenance. State invalidation triggers.

## Stage 7 — AI / agent + controlled execution

Use Template 09. Define bounded tools, state machine, deterministic constraints, human/technical gates, abstention and AI/offline fallback. Test MFD-L002, MFD-L003, MFD-L008, MFD-L009, MFD-L010 and MFD-L014 before declaring the design safe enough to build.

## Stage 8 — Evidence + feedback

Use Templates 10–11. Produce a reconstructable trace and a governed learning loop. Ensure accepted AI assistance does not become automatic truth/policy/model update.

## Architecture integration

Use Template 12 to connect all eight stages into one target architecture and distinguish production technology from the Google AI Build simulation.

## PRD

Use Template 14 plus `google_ai_build/01_PRD_GENERATION_PROMPT.md`. The PRD may only implement approved architecture decisions. Any unresolved permission, authority, data or technology issue becomes `OPEN_DECISION` rather than an invented requirement.

## Google AI Build

1. Run `python scripts/build_app_fixture.py`.
2. Provide the PRD, `02_GOOGLE_AI_BUILD_MASTER_PROMPT.md`, screen requirements and `06_app_fixture_bundle.json` to Google AI Build.
3. Build an evidence-centric application, not a generic chatbot.
4. Keep the prototype local/synthetic; do not add real vessel, port, cargo, crew or navigation integrations.

## Verification

Run all 15 golden scenarios and record results in Template 15. Complete Template 13 traceability. Then run:

```bash
python scripts/sanity_check.py
```

A release/demo claim requires every hard gate to pass.
