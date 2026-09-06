# Technology Option Catalog

This is an **option catalog**, not a required stack. Participants must justify choices against scale, connectivity, provenance, latency, governance and operating burden.

| Capability | Workshop option | Production candidates / patterns |
|---|---|---|
| Edge durable state | JSON/local fixture simulation | SQLite/RocksDB/event log, durable edge state machine |
| Event transport | local JSONL | Kafka/Redpanda/Pulsar/MQTT with idempotency/exactly-once effect patterns |
| Structured operational data | CSV/JSON | Postgres/Aurora/SQL Server/lakehouse |
| Semantic contracts | Markdown/JSON schema | data contracts, semantic model/catalog, schema registry |
| Graph | in-memory JSON graph | Neo4j, Neptune, Memgraph, TigerGraph, RDF/triple store or relational graph capability |
| Vector retrieval | simulated tagged text search | pgvector, OpenSearch, Pinecone, Weaviate, Milvus, managed vector services |
| Policy | deterministic fixture rules | OPA/Cedar/rules engine/workflow authorization |
| Orchestration | local state machine | Temporal/Camunda/durable workflow + bounded tool services |
| AI/LLM | Google AI Build prototype | approved enterprise model gateway/provider with eval/observability |
| Observability/evals | trace fixture + golden scenarios | OpenTelemetry + eval platform + audit/event store |

For the Google AI Build prototype, simulate production contracts faithfully rather than claiming the browser prototype is the production graph, policy or workflow engine.
