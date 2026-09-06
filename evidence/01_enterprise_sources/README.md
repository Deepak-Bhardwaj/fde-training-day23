# Enterprise Source Layer Evidence

These files simulate the fragmented brownfield evidence available to the fleet operations center and vessel edge on **2026-09-15**.

- `historical_disruptions.csv` is copied from the original workshop pack and contains 140 synthetic historical events.
- `source_case_baseline.json` preserves the larger operating benchmark stated in the original case study. It is **not** claimed to be calculated from the 140-row fixture.
- `workshop_fixture_profile.json` is calculated from the supplied 140-row fixture so participants can compare populations honestly.
- `live_disruptions.csv` and the JSONL feeds form the deterministic 15-case operating day used by the golden scenarios.

The source files deliberately contain stale data, missing data, identity mismatch, clock skew, duplicate delivery, contradictory port evidence, an untrusted prompt-injection string, AI outage, and satellite blackout. Do not clean away these traps before architecture design.
