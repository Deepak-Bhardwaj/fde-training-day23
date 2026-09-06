#!/usr/bin/env python3
import csv,json
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]; E=ROOT/'evidence'; OUT=ROOT/'google_ai_build/06_app_fixture_bundle.json'
def csvrows(p):
    with p.open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
def jsonl(p): return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]
def js(p): return json.loads(p.read_text(encoding='utf-8'))
def y(p): return yaml.safe_load(p.read_text(encoding='utf-8'))
docs=[{'filename':p.name,'content':p.read_text(encoding='utf-8')} for p in sorted((E/'02_documents').glob('*.md'))]
bundle={'bundle_version':'2.0','organization':{'name':'MeridianBlue Shipping','fictional':True,'operating_day':'2026-09-15'},
 'architecture_storyline':['enterprise_sources','semantic_foundation','connected_knowledge','graph_platform','hybrid_retrieval','runtime_context_graph','ai_agent','governance_gate','evidence_feedback'],
 'enterprise_sources':{
  'live_disruptions':csvrows(E/'01_enterprise_sources/live_disruptions.csv'),'vessel_registry':csvrows(E/'01_enterprise_sources/vessel_registry.csv'),'voyage_schedule':csvrows(E/'01_enterprise_sources/voyage_schedule.csv'),
  'ais_positions':jsonl(E/'01_enterprise_sources/ais_positions.jsonl'),'vessel_telemetry':jsonl(E/'01_enterprise_sources/vessel_telemetry.jsonl'),'weather_ocean_snapshots':jsonl(E/'01_enterprise_sources/weather_ocean_snapshots.jsonl'),'port_constraints':jsonl(E/'01_enterprise_sources/port_constraints.jsonl'),
  'cargo_constraints':jsonl(E/'01_enterprise_sources/cargo_constraints.jsonl'),'crew_constraints':jsonl(E/'01_enterprise_sources/crew_constraints.jsonl'),'cmms_constraints':jsonl(E/'01_enterprise_sources/cmms_constraints.jsonl'),'connectivity_events':jsonl(E/'01_enterprise_sources/connectivity_events.jsonl'),'source_health_events':jsonl(E/'01_enterprise_sources/source_health_events.jsonl'),'live_event_stream':jsonl(E/'01_enterprise_sources/live_event_stream.jsonl'),
  'source_inventory':csvrows(E/'01_enterprise_sources/source_inventory.csv'),'source_case_baseline':js(E/'01_enterprise_sources/source_case_baseline.json'),'workshop_fixture_profile':js(E/'01_enterprise_sources/workshop_fixture_profile.json')},
 'documents':docs,
 'semantic_evidence':{'source_schema_dictionary':csvrows(E/'03_semantic_evidence/source_schema_dictionary.csv'),'conflicting_terms':csvrows(E/'03_semantic_evidence/conflicting_terms.csv'),'identifier_crosswalk':csvrows(E/'03_semantic_evidence/identifier_crosswalk.csv'),'kpi_definition_candidates':csvrows(E/'03_semantic_evidence/kpi_definition_candidates.csv'),'relationship_clues':csvrows(E/'03_semantic_evidence/relationship_clues.csv')},
 'policy_authority':{'role_authorization_matrix':csvrows(E/'04_policy_authority/role_authorization_matrix.csv'),'decision_constraints':y(E/'04_policy_authority/decision_constraints.yaml'),'data_access_rules':y(E/'04_policy_authority/data_access_rules.yaml'),'source_authority':y(E/'04_policy_authority/source_authority.yaml')},
 'history_feedback':{'historical_decisions':jsonl(E/'05_history_feedback/historical_decisions.jsonl'),'operator_interactions':jsonl(E/'05_history_feedback/operator_interactions.jsonl'),'authorized_overrides':csvrows(E/'05_history_feedback/authorized_overrides.csv'),'voyage_outcomes':csvrows(E/'05_history_feedback/voyage_outcomes.csv'),'historical_incident_narratives':jsonl(E/'05_history_feedback/historical_incident_narratives.jsonl')},
 'evaluation':{'golden_scenarios':js(E/'06_evaluations/golden_scenarios.json'),'expected_behaviors':js(E/'06_evaluations/expected_behaviors.json'),'acceptance_thresholds':y(E/'06_evaluations/acceptance_thresholds.yaml'),'evaluation_matrix':csvrows(E/'06_evaluations/evaluation_matrix.csv')}}
OUT.write_text(json.dumps(bundle,indent=2,ensure_ascii=False),encoding='utf-8'); print(f'Wrote {OUT} ({OUT.stat().st_size:,} bytes)')
