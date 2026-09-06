# Learning Objectives and Expected Deliverables

By completing this case, an AI FDE should be able to:

1. separate physical source schemas from canonical business meaning;
2. design a domain ontology and provenance-preserving knowledge graph;
3. choose graph technology from query/operating requirements;
4. design hybrid retrieval instead of relying on vector RAG alone;
5. build a runtime context graph that is task-, actor-, time-, source-health- and policy-aware;
6. keep AI inside bounded decision-support/tool roles;
7. preserve maritime command/technical authority and deterministic safety controls;
8. design for disconnected edge operation, replay and reconnect reconciliation;
9. capture audit-grade observable decision evidence without hidden chain-of-thought;
10. turn architecture decisions into a traceable PRD and Google AI Build application;
11. verify the build with scenario-based evals rather than visual demo quality alone.

## Required submission pack

| # | Deliverable | Minimum evidence |
|---|---|---|
| 1 | Enterprise source inventory | authority, freshness, access, identity, timing, failure behavior |
| 2 | Semantic layer | canonical entities/metrics/mappings/ambiguities |
| 3 | Ontology | concepts, relationships, taxonomies, semantic constraints |
| 4 | Entity-resolution design | canonical IDs, confidence, ambiguity, adjudication, provenance |
| 5 | KG schema | nodes/edges/time/provenance/conflict representation |
| 6 | Graph platform ADR | queries, options, decision, consequences, reversibility |
| 7 | Hybrid retrieval strategy | routing, filters, fusion, fallback, metrics |
| 8 | Runtime context graph | request contract, inclusion/exclusion, invalidation |
| 9 | Agent/control design | tools, state machine, hard controls, human gates, fallback |
| 10 | Decision trace | reconstructable sample trace |
| 11 | Feedback/learning design | authority, review, versioning, rollback |
| 12 | End-to-end architecture | components, trust boundaries, production vs prototype mapping |
| 13 | Traceability matrix | evidence → architecture → PRD → app → scenario/test |
| 14 | PRD | numbered requirements and open decisions |
| 15 | Acceptance evidence | results for all 15 golden scenarios |
