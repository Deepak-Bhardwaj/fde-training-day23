# Architecture Decision Guardrails

- Do not start from “we need a maritime chatbot”.
- Do not collapse event time, ingestion time and normalized time into one field.
- Do not treat AIS identity observations as canonical vessel identity without resolution.
- Do not collapse conflicting port facts into a single convenient value.
- Do not feed every KG fact into the LLM; context is task-specific and permission/freshness filtered.
- Do not let vector similarity choose active policy versions.
- Do not let AI issue navigation commands, release maintenance holds or override policy.
- Do not let cloud/AI failure degrade safe/essential shipboard workflow.
- Do not log hidden chain-of-thought; log observable evidence, controls and concise rationale.
- Do not let operator acceptance or later outcome automatically rewrite policy/model/ontology.
