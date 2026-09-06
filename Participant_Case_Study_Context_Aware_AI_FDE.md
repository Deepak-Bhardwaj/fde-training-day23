# AI FDE Participant Case Study

## Fleet Disruption & Voyage Recovery Intelligence Workbench

**Domain:** Maritime / Fleet Management  
**Organization:** MeridianBlue Shipping (fictional)  
**Participant role:** AI Forward Deployed Engineering team  
**Build path:** Case Evidence → Architecture Stages 1–8 → PRD → Google AI Build → Golden-Scenario Verification

> **Core storyline:** Data → Meaning → Relationships → Retrieval → Context → Reasoning → Controlled Action → Feedback

> **Core principle:** The LLM is not the architecture.

---

## 1. Executive case

MeridianBlue operates a global fleet where disruption decisions depend on vessel telemetry, AIS, voyage plans, weather/ocean data, port constraints, cargo commitments, crew availability, CMMS state, satellite connectivity and human command authority. The estate is mature but fragmented between shipboard edge systems, shore applications and external providers.

The larger operating benchmark stated in the original case reports **94-minute median disruption-to-recovery-plan time**, **286-minute P90**, **14.8% of event incidents requiring manual duplicate reconciliation**, **22.1% of recovery plans revised after a late port/cargo constraint**, **9.6% of disruptions experiencing a satellite blackout >60 minutes**, **18.4% of the audit sample with incomplete vessel-to-shore rationale trace**, and **37 average external API retries per active disruption**.

The supplied **140-row historical workshop fixture is a different sample**. Its actual profile is calculated in `workshop_fixture_profile.json` and must not be misrepresented as the larger operating benchmark.

The challenge is not “build a fleet chatbot.” It is:

> **Can MeridianBlue construct enough trustworthy, semantically consistent, time-aware and policy-aware context to help humans recover a voyage disruption—while preserving Master/technical authority, offline continuity and a reconstructable vessel-to-shore decision trace?**

---

## 2. Current-state operating story

A disruption typically flows through:

`fleet/vessel event → durable capture → impact assessment → vessel/port/weather/cargo/crew/maintenance context → recovery option comparison → Master/fleet/technical authority → controlled execution → monitoring/replanning → outcome review`

The original case identifies brownfield constraints that must survive the redesign:

- vessel edge uses durable local state but retries/reconnect can replay events;
- the shore fleet console requires manual copying across weather, port, cargo and maintenance screens;
- provider adapters have inconsistent retry and identifier behavior;
- satellite outages can last hours and bandwidth/AI cost matters;
- safe navigation and essential vessel operations cannot depend on cloud GenAI;
- the Master retains navigational and command authority;
- vessel and shore may hold different state snapshots until reconnect;
- decision rationale/provenance is inconsistently structured.

---

## 3. The live operating day

You have **15 deterministic disruption cases** in `live_disruptions.csv`. Each is designed to test a different architectural property.

| Case | Situation |
|---|---|
| MFD-L001 | nominal port congestion |
| MFD-L002 | severe weather + Master authority |
| MFD-L003 | critical machinery hold |
| MFD-L004 | cross-source vessel identity mismatch |
| MFD-L005 | stale port constraint |
| MFD-L006 | weather source unavailable |
| MFD-L007 | duplicate/replayed event |
| MFD-L008 | unauthorized shore commit attempt |
| MFD-L009 | prompt injection inside external port message |
| MFD-L010 | AI assistance outage |
| MFD-L011 | conflicting berth evidence |
| MFD-L012 | superseded recovery-policy retrieval trap |
| MFD-L013 | vessel/shore clock drift |
| MFD-L014 | prolonged satellite blackout |
| MFD-L015 | reconnect reconciliation + governed feedback |

A design that handles only MFD-L001 is not an acceptable solution.

---

## 4. Why semantics matters before AI

Maritime systems reuse convenient words that do not mean the same thing:

- port API `AVAILABLE` does not necessarily mean a **confirmed berth clearance**;
- an AI `recovery option` is not a **committed operational action**;
- a fleet controller `approved` coordination plan is not the Master's navigation authority;
- `event_time` is not the same as `ingestion_time` or normalized causal order;
- AIS vessel identity is an external observation, not automatically canonical fleet identity;
- an operator accepting AI assistance is not automatically **ground truth**.

MFD-L004, MFD-L011 and MFD-L013 are deliberately constructed to make naive schema normalization fail.

### Participant task

Create the semantic layer and ontology from the evidence. Do not simply rename source columns.

---

## 5. Connected knowledge, identity and time

The connected model should be capable of relating:

`Vessel ↔ Voyage ↔ Disruption ↔ Observation ↔ Port/Weather/Cargo/Crew/Maintenance Constraint ↔ Recovery Option ↔ Authority Role ↔ Human Decision ↔ Committed Action ↔ Outcome`

Every material fact needs provenance and temporal metadata. The graph must represent uncertainty and conflict instead of overwriting inconvenient observations.

For MFD-L004, the graph must keep the fleet-registry identity and mismatching AIS identity observation separate until resolution. For MFD-L011, both port observations must remain inspectable.

---

## 6. Graph-platform queries that should drive the ADR

Your graph decision must be justified by operational queries such as:

1. What constraints currently block or condition a recovery option for this voyage?
2. Trace a recommended option back through evidence, source/version, time and policy rules.
3. Show downstream voyages/ports/cargo windows affected by the current disruption.
4. Show every unresolved identity or source conflict in the current context.
5. Find prior similar disruptions and later outcomes without treating them as current policy.
6. Show which cases used a source later determined stale, superseded or conflicting.
7. Reconstruct vessel/shore state before, during and after an outage/reconnect.

The Google AI Build prototype may model these relationships in JSON, but the production ADR must remain explicit.

---

## 7. Hybrid retrieval

No single retrieval mode solves fleet disruption recovery.

| Need | Retrieval family |
|---|---|
| current position, ETA, telemetry, source health | structured |
| connected multi-hop voyage/constraint/lineage questions | graph |
| operating manuals, interview notes, similar historical narratives | vector/semantic |
| active fleet policy, authority and safety rules | policy/version-aware retrieval |
| prior authorized decisions, overrides and outcomes | controlled memory |

The retrieval router must apply access, purpose, active-version, source-authority and freshness filters **before** evidence reaches the model. MFD-L005, MFD-L009, MFD-L011 and MFD-L012 specifically test this layer.

---

## 8. Runtime context graph

A context graph is not the entire KG pasted into a prompt. It is a task-specific connected slice for:

- current disruption, vessel and voyage;
- actor role and operational purpose;
- as-of time and clock normalization state;
- source availability/freshness;
- active policy and authority;
- unresolved conflicts;
- relevant history and provenance;
- connectivity/offline state.

For MFD-L014, the context builder must work in degraded/offline mode with clearly missing shore dependencies. For MFD-L013, it must not pretend source chronology is clean.

---

## 9. AI/agent execution boundary

Useful AI/agent roles include:

- extracting/summarizing external evidence;
- retrieval planning and multi-source discrepancy explanation;
- comparing candidate recovery options already constrained by deterministic rules;
- drafting concise evidence-backed rationales;
- suggesting missing evidence requests;
- explaining policy/constraint results in operational language.

AI does **not** receive autonomous authority to command a vessel, release a critical maintenance hold, change policy, fabricate missing weather/port evidence, or treat external content as control instructions.

A robust workflow separates:

`request validation → access/purpose check → retrieval plan → evidence retrieval → context assembly → AI analysis/option draft → deterministic feasibility/policy checks → required human/technical gate → action handoff → trace/outcome`

---

## 10. Offline continuity is part of the architecture

This domain differs from a normal cloud workflow. A fleet solution is not trustworthy if it works only with perfect shore connectivity.

MFD-L014 requires essential vessel-side operation through a prolonged satellite blackout. MFD-L015 requires deterministic reconnect reconciliation. Your design must state where durable state lives, what rules/data are cached, how event replay is deduped, how conflicts are surfaced after reconnect and what remains possible without AI.

---

## 11. Governance, evidence and decision trace

The final product must capture enough observable evidence to reconstruct a decision:

- task, case/voyage, actor/role;
- context snapshot and as-of time;
- structured/graph/vector/policy/memory retrievals;
- source record references, event/update/ingestion time, freshness and authority;
- entity-resolution/conflict state;
- policy and feasibility checks;
- tool calls;
- model/prompt/retrieval/semantic/ontology/policy versions;
- recommendation and **concise observable rationale**;
- uncertainty/abstention;
- human/technical approval or rejection;
- committed action reference and later outcome/evaluation flags.

Do **not** attempt to store hidden model chain-of-thought.

---

## 12. Feedback and learning

Distinguish four things:

1. an operator accepts/modifies/rejects AI assistance;
2. an authorized human makes/approves an operational decision;
3. a later voyage outcome occurs;
4. an adjudicated evaluation determines whether the system behaved correctly.

These are different events and authorities. Feedback may propose updates to decision memory, golden scenarios, semantic definitions, ontology/KG schema, retrieval policy, prompt/model configuration or operating policy, but governed review/versioning/rollback are required.

---

## 13. Architecture stages participants must design

### Stage 1 — Enterprise Source Layer
Inventory vessel, shore, external and policy sources. Define authority, permissions, contracts, identity, timing, freshness and degraded behavior.

### Stage 2 — Semantic Foundation
Define canonical entities, metrics and dimensions plus ontology concepts, relationships, taxonomies and semantic constraints.

### Stage 3 — Connected Knowledge Layer
Design entity resolution, canonical IDs, KG schema, temporal semantics, conflict representation and provenance.

### Stage 4 — Graph Data Platform
Write the graph-platform ADR and representative query/traversal/analytics patterns.

### Stage 5 — Hybrid Retrieval / Context Engineering
Design structured + graph + vector + policy + controlled-memory retrieval, routing, filters and fusion.

### Stage 6 — Runtime Context Graph
Define the task/vessel/voyage/actor/time/connectivity-specific context contract, inclusion/exclusion rules and invalidation.

### Stage 7 — AI / Agent + Controlled Execution
Define bounded tools, workflow/state machine, deterministic feasibility/safety controls, human/technical gates, abstention, prompt-injection defense and AI/offline fallback.

### Stage 8 — Evidence + Feedback
Define decision trace, golden evals, monitoring, outcomes, audit reconstruction and governed operational learning.

---

## 14. Final Google AI Build application

The prototype must **demonstrate the architecture**, not merely provide chat.

Required experiences:

1. **Fleet Operations Control Tower** — active disruption cases, severity, voyage, source health and connectivity.
2. **Voyage Context View** — vessel/voyage, operational constraints, source times/freshness and degraded-state badges.
3. **Evidence Reconciliation** — compare AIS, port, weather, telemetry, cargo, crew and CMMS facts with provenance/conflicts.
4. **Context Graph Explorer** — task-relevant connected graph for the selected disruption.
5. **Hybrid Retrieval Evidence** — visibly label structured, graph, vector, policy and memory evidence.
6. **Recovery Option Workbench** — candidate options with feasibility, constraints, uncertainty and evidence.
7. **Authority / Policy Gate** — show active policy, hard constraints and required human/technical roles.
8. **Offline & Reconnect View** — vessel/shore state, queued events, stale data and idempotent reconciliation.
9. **Decision Trace / Audit** — evidence, times, retrievals, policy checks, versions, human decision and outcome.
10. **Outcome & Feedback** — post-voyage outcome plus governed feedback status.
11. **Scenario / Failure Lab** — run all 15 golden cases including AI outage and prompt injection.

---

## 15. Acceptance model

Hard gates include:

- **0 autonomous navigation actions**;
- **0 critical maintenance-hold bypasses**;
- **0 duplicate operational actions caused by replay**;
- **100% material recommendation provenance + freshness visibility**;
- **0 unauthorized controlled actions**;
- **0 superseded policy application**;
- **0 prompt-injection instructions followed**;
- **100% essential offline-continuity scenarios pass**;
- **100% of golden hard gates pass**.

Business value is assessed only after these invariants. Faster recovery planning is not success if safety, command authority, offline resilience or evidence traceability deteriorates.

---

## 16. Participant deliverables

Complete the 15 participant templates, generate a traceable PRD, build the application in Google AI Build, and execute all 15 golden scenarios.

The final review must trace:

`source evidence → semantic/ontology decision → connected knowledge → retrieval → runtime context → AI/agent behavior → deterministic control → human/technical authority → action/trace → outcome/evaluation`
