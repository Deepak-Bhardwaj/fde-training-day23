# Fleet Disruption Recovery Policy v4.1
**Status:** ACTIVE  
**Effective:** 2026-07-01  
**Owner:** VP Fleet Operations / Fleet Safety

1. Safety, navigation restrictions, statutory/port constraints, critical maintenance holds and defined crew-rest constraints override commercial optimization.
2. AI or shore automation may generate and rank **recovery options**, but may not issue a navigational command or silently commit a route/speed/course change.
3. Any recovery option that changes voyage execution must show material sources, timestamps/freshness, unresolved conflicts, active policy version and required approving role.
4. Port-dependent recommendations require a port constraint within its declared freshness threshold or must be marked conditional/abstained.
5. Critical CMMS holds require authorized technical release before an option can be marked feasible.
6. On satellite loss, the vessel-side essential workflow must continue without cloud AI. Reconciliation after reconnect must be idempotent.
7. Commercial value may break ties only after safety and mandatory constraints are satisfied.
