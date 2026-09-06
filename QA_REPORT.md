# QA Report — Maritime Fleet Context-Aware AI FDE Rebuild

## Final status

**PASS** — repository is structurally consistent, workshop-self-contained, and validated against the deterministic maritime evidence set.

## Architecture coverage

The participant workflow explicitly covers:

1. Enterprise Source Layer
2. Semantic Foundation
3. Connected Knowledge / Entity Resolution / Knowledge Graph
4. Graph Data Platform
5. Hybrid Retrieval
6. Runtime Context Graph
7. AI / Agent + Controlled Execution
8. Evidence + Feedback
9. PRD generation
10. Google AI Build
11. Golden-scenario verification

## Automated repository validation

- `python -m py_compile scripts/*.py`: PASS
- `python scripts/profile_baseline.py`: PASS; stored 140-row fixture profile exactly matches recomputation
- `python scripts/build_app_fixture.py`: PASS; consolidated fixture bundle regenerated
- `python scripts/sanity_check.py`: **107/107 checks passed; 0 failures; 0 warnings**
- Independent cross-data integrity pass: **355 checks; 0 issues**
- JSON / JSONL / YAML / CSV parse and referential-integrity checks: PASS
- 15 live cases map 1:1 to 15 deterministic golden scenarios: PASS
- 15 participant templates present: PASS

## Data sanity

The original case operating benchmark and supplied 140-row workshop fixture are intentionally kept as different populations.

### Source-case benchmark retained

- Median disruption-to-recovery-plan time: 94 minutes (n=384)
- P90 recovery-plan time: 286 minutes (n=384)
- Manual duplicate reconciliation: 14.8% (event incidents n=1,920)
- Plan revision after late port/cargo constraint: 22.1% (n=384)
- Satellite blackout >60 min: 9.6% (n=384)
- Incomplete vessel-to-shore rationale trace: 18.4% (audit n=250)
- Average external API retries: 37 (sample n=120)

### Supplied 140-row workshop fixture recomputation

- Rows: 140
- Unique vessels: 31
- Median plan time: 70.0 minutes
- P90 plan time: 141 minutes
- Duplicate reconciliation: 14.286%
- Late-constraint revision: 23.571%
- Blackout >60 min: 31.429%
- Missing rationale trace: 19.286%
- Average API retries: 35.35
- Navigation restricted: 8.571%
- Shore link unavailable: 8.571%

No claim is made that the 140-row workshop fixture reproduces the larger source-case benchmark.

## Safety / governance hard-gate validation

Validated deterministic requirements include:

- no autonomous AI navigation command/control;
- Master retains navigational/command authority;
- critical CMMS maintenance holds cannot be bypassed by AI;
- safety/regulatory/maintenance/cargo/crew constraints override commercial optimization;
- stale/unavailable evidence is visible and never fabricated;
- duplicate/replayed events cannot create duplicate operational actions;
- external messages/documents cannot override policy or system instructions;
- only ACTIVE policy versions may control current decision support;
- AI/cloud outage preserves deterministic vessel-side/manual continuity;
- tenant/purpose/access restrictions are applied before retrieval/context assembly;
- feedback cannot automatically rewrite policy, semantics, ontology or model behavior;
- decision traces capture observable evidence, versions, controls, concise rationale and human/technical action—not hidden chain-of-thought.

## Deterministic scenario coverage

The 15 golden scenarios cover nominal recovery, severe weather/Master authority, critical maintenance hold, identity ambiguity, stale port evidence, unavailable weather, replay/idempotency, unauthorized commit, prompt injection, AI outage, conflicting berth evidence, superseded policy retrieval, clock drift, prolonged satellite blackout, and reconnect reconciliation/governed feedback.

## DOCX quality validation

- Participant DOCX pages rendered: **12**
- All 12 rendered pages visually inspected after the final accessibility/XML change: PASS
- Accessibility audit: **0 high / 0 medium / 0 low findings**
- Image alternative text: present and meaningful
- Table header markings: present
- No observed clipping, overflow or broken glyphs in the final render

## Packaging controls

`MANIFEST.csv` records relative path, size and SHA-256 for every repository file except the manifest itself. The final ZIP is separately reopened, CRC-tested, extracted, manifest-verified and sanity-tested before delivery.
