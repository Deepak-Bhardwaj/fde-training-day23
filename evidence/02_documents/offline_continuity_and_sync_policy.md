# Offline Continuity and Synchronization Policy

Vessel-side essential workflow uses durable local state and cached approved rules. During loss of shore connectivity:

- capture events locally with sequence/dedupe identifiers;
- preserve local decision/approval evidence;
- never require cloud AI for safe/essential operation;
- mark shore-dependent data stale/unavailable;
- on reconnect, reconcile by idempotency key and causal/sequence metadata;
- never convert replayed events into duplicate operational actions.
