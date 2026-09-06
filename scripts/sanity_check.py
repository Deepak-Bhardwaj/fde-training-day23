#!/usr/bin/env python3
from pathlib import Path
import csv,json,sys,statistics,zipfile
import yaml
ROOT=Path(__file__).resolve().parents[1]
checks=[]; errors=[]; warnings=[]
def ok(name,cond,detail=''):
    checks.append((name,bool(cond),detail))
    if not cond: errors.append(f'{name}: {detail}')
def csvrows(p):
    with p.open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
def jsonl(p): return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]
required=['README.md','START_HERE.md','Participant_Case_Study_Context_Aware_AI_FDE.md','Participant_Case_Study_Context_Aware_AI_FDE.docx','Participant_Runbook.md','Learning_Objectives_and_Expected_Deliverables.md','google_ai_build/01_PRD_GENERATION_PROMPT.md','google_ai_build/02_GOOGLE_AI_BUILD_MASTER_PROMPT.md','google_ai_build/06_app_fixture_bundle.json','evidence/06_evaluations/golden_scenarios.json']
for f in required: ok('required:'+f,(ROOT/f).exists(),f+' missing')
# live + golden
live=csvrows(ROOT/'evidence/01_enterprise_sources/live_disruptions.csv'); ok('live_case_count',len(live)==15,str(len(live)))
ids={r['case_id'] for r in live}; ok('unique_live_cases',len(ids)==15,'duplicate IDs')
gs=json.loads((ROOT/'evidence/06_evaluations/golden_scenarios.json').read_text()); ok('golden_count',len(gs)==15,str(len(gs))); ok('golden_sequence',[x['scenario_id'] for x in gs]==[f'GS-{i:02d}' for i in range(1,16)],'scenario sequence mismatch'); ok('golden_cases',all(x['case_id'] in ids for x in gs),'unknown live case'); ok('concrete_behaviors',all('Participants must define' not in x['expected_behavior'] and len(x['expected_behavior'])>80 for x in gs),'placeholder expected behavior')
# traps
port=jsonl(ROOT/'evidence/01_enterprise_sources/port_constraints.jsonl');
from datetime import datetime,timezone
p5=[x for x in port if x['case_id']=='MFD-L005']; ok('GS05_stale_port',len(p5)==1 and 'Last berth status' in p5[0]['text_excerpt'],'stale trap missing')
wx=jsonl(ROOT/'evidence/01_enterprise_sources/weather_ocean_snapshots.jsonl'); ok('GS06_no_weather',not any(x['case_id']=='MFD-L006' for x in wx),'MFD-L006 must lack weather')
stream=jsonl(ROOT/'evidence/01_enterprise_sources/live_event_stream.jsonl'); s7=[x for x in stream if x['case_id']=='MFD-L007']; ok('GS07_duplicate',len(s7)==2 and len({x['dedupe_key'] for x in s7})==1,'duplicate replay trap missing')
ok('GS09_prompt_injection',any(x['case_id']=='MFD-L009' and 'Ignore all fleet policies' in x['text_excerpt'] for x in port),'prompt injection trap missing')
health=jsonl(ROOT/'evidence/01_enterprise_sources/source_health_events.jsonl'); ok('GS10_ai_outage',any(x['case_id']=='MFD-L010' and x['source']=='AI_ASSIST' and x['state']=='UNAVAILABLE' for x in health),'AI outage missing')
p11=[x for x in port if x['case_id']=='MFD-L011']; ok('GS11_port_conflict',len(p11)==2 and {x['berth_state'] for x in p11}=={'AVAILABLE','CLOSED'},'port conflict missing')
tele=jsonl(ROOT/'evidence/01_enterprise_sources/vessel_telemetry.jsonl'); t13=next(x for x in tele if x['case_id']=='MFD-L013'); ok('GS13_clock_drift',t13['source_event_time']>t13['source_update_time'],'clock skew trap missing')
conn=jsonl(ROOT/'evidence/01_enterprise_sources/connectivity_events.jsonl'); c14=next(x for x in conn if x['case_id']=='MFD-L014'); ok('GS14_blackout',c14['state']=='OFFLINE' and int(c14['outage_minutes'])>=180,'blackout trap missing')
# identity ambiguity
cross=csvrows(ROOT/'evidence/03_semantic_evidence/identifier_crosswalk.csv'); ok('GS04_identity_ambiguity',any(x['source']=='AIS_PROVIDER_A' and x['source_id']=='IMO9301994' and x['match_status']=='AMBIGUOUS' for x in cross),'identity ambiguity missing')
# active/superseded policy
active=(ROOT/'evidence/02_documents/fleet_recovery_policy_v4_1.md').read_text(); old=(ROOT/'evidence/02_documents/superseded_fleet_recovery_policy_v3_7_REFERENCE_ONLY.md').read_text(); ok('active_policy','**Status:** ACTIVE' in active,'active policy status missing'); ok('superseded_policy','**Status:** SUPERSEDED' in old,'superseded status missing')
# policy invariants
cons=yaml.safe_load((ROOT/'evidence/04_policy_authority/decision_constraints.yaml').read_text()); rules=' '.join(x['rule'] for x in cons['constraints']).lower()
for phrase,key in [('autonomously authorize a navigation command','navigation authority'),('critical cmms maintenance hold','maintenance hold'),('stale or unavailable','freshness'),('duplicate or replayed events','idempotency'),('untrusted document or external-message','prompt injection'),('manual and deterministic vessel-side continuity','ai fallback'),('only active policy versions','policy version'),('must not automatically rewrite','feedback')]: ok('constraint:'+key,phrase in rules,'missing '+phrase)
roles=csvrows(ROOT/'evidence/04_policy_authority/role_authorization_matrix.csv'); ai=next(x for x in roles if x['role']=='AI_AGENT'); ok('AI_no_nav',ai['authorize_navigation_change']=='NO','AI navigation authority must be NO'); ok('AI_no_commit',ai['commit_operational_action']=='NO','AI commit authority must be NO')
# source historical fixture exact metrics
hist=csvrows(ROOT/'evidence/01_enterprise_sources/historical_disruptions.csv'); stored=json.loads((ROOT/'evidence/01_enterprise_sources/workshop_fixture_profile.json').read_text());
def iv(k): return [int(r[k]) for r in hist]
sv=sorted(iv('plan_time_minutes')); n=len(hist)
computed={'rows':n,'unique_vessels':len({r['vessel_id'] for r in hist}),'median_plan_time_minutes':statistics.median(iv('plan_time_minutes')),'p90_plan_time_minutes':sv[int(0.9*(n-1))],'duplicate_reconciliation_pct':round(100*sum(int(r['duplicate_reconciliation'])==1 for r in hist)/n,3),'late_constraint_revision_pct':round(100*sum(int(r['late_constraint_revision'])==1 for r in hist)/n,3),'blackout_gt60_pct':round(100*sum(int(r['blackout_minutes'])>60 for r in hist)/n,3),'rationale_trace_missing_pct':round(100*sum(int(r['rationale_trace_missing'])==1 for r in hist)/n,3),'average_api_retries':round(statistics.mean(iv('api_retries')),3),'navigation_restricted_pct':round(100*sum(int(r['navigation_restricted'])==1 for r in hist)/n,3),'shore_link_unavailable_pct':round(100*sum(int(r['shore_link_available'])==0 for r in hist)/n,3)}
for k,v in computed.items(): ok('fixture_profile:'+k,stored[k]==v,f'stored={stored[k]} computed={v}')
bench=json.loads((ROOT/'evidence/01_enterprise_sources/source_case_baseline.json').read_text()); ok('benchmark_median_94',bench['median_disruption_to_recovery_plan_minutes']==94,'wrong benchmark'); ok('benchmark_p90_286',bench['p90_recovery_plan_minutes']==286,'wrong benchmark p90')
# no qwen in core
for f in ['README.md','START_HERE.md','Participant_Runbook.md','Participant_Case_Study_Context_Aware_AI_FDE.md','google_ai_build/01_PRD_GENERATION_PROMPT.md']:
    ok('no_qwen:'+f,'qwen' not in (ROOT/f).read_text(encoding='utf-8').lower(),'Qwen remains in core workflow')
# templates 1-15
for i in range(1,16): ok(f'template_{i:02d}',any((ROOT/'participant_templates').glob(f'{i:02d}_*')),f'template {i} missing')
# bundle
bundle=json.loads((ROOT/'google_ai_build/06_app_fixture_bundle.json').read_text()); ok('bundle_live',len(bundle['enterprise_sources']['live_disruptions'])==15,'bundle live mismatch'); ok('bundle_golden',len(bundle['evaluation']['golden_scenarios'])==15,'bundle golden mismatch')
# trace schema
trace=json.loads((ROOT/'participant_templates/10_decision_trace_template.json').read_text());
for fld in ['trace_id','task','case_id','voyage_id','actor','context_snapshot','retrievals','source_evidence','policy_checks','versions','recommendation','concise_rationale','human_or_technical_decision','outcome']: ok('trace:'+fld,fld in trace,'missing '+fld)
# case tokens
case=(ROOT/'Participant_Case_Study_Context_Aware_AI_FDE.md').read_text()
for tok in ['94-minute','286-minute','14.8%','22.1%','9.6%','18.4%','37 average','MFD-L011','MFD-L009','MFD-L014','The LLM is not the architecture']:
    ok('case_token:'+tok,tok in case,'missing '+tok)
# JSON/YAML parse scan
for p in ROOT.rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8')); ok('json:'+str(p.relative_to(ROOT)),True)
    except Exception as e: ok('json:'+str(p.relative_to(ROOT)),False,str(e))
for p in ROOT.rglob('*.yaml'):
    try: yaml.safe_load(p.read_text(encoding='utf-8')); ok('yaml:'+str(p.relative_to(ROOT)),True)
    except Exception as e: ok('yaml:'+str(p.relative_to(ROOT)),False,str(e))
print(f'Checks: {len(checks)} | Passed: {sum(v for _,v,_ in checks)} | Failed: {len(errors)} | Warnings: {len(warnings)}')
for n,s,d in checks:
    if not s: print('FAIL',n,d)
for x in warnings: print('WARN',x)
if errors:
    print('ERRORS:'); [print('-',e) for e in errors]; sys.exit(1)
print('SANITY CHECK PASSED')
