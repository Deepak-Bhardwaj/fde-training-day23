#!/usr/bin/env python3
from pathlib import Path
import csv,json,statistics
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'evidence/01_enterprise_sources/historical_disruptions.csv'
with p.open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
def iv(k): return [int(r[k]) for r in rows]
sv=sorted(iv('plan_time_minutes')); n=len(rows)
calc={
 'rows':n,'unique_vessels':len({r['vessel_id'] for r in rows}),'median_plan_time_minutes':statistics.median(iv('plan_time_minutes')),'p90_plan_time_minutes':sv[int(0.9*(n-1))],
 'duplicate_reconciliation_pct':round(100*sum(int(r['duplicate_reconciliation'])==1 for r in rows)/n,3),
 'late_constraint_revision_pct':round(100*sum(int(r['late_constraint_revision'])==1 for r in rows)/n,3),
 'blackout_gt60_pct':round(100*sum(int(r['blackout_minutes'])>60 for r in rows)/n,3),
 'rationale_trace_missing_pct':round(100*sum(int(r['rationale_trace_missing'])==1 for r in rows)/n,3),
 'average_api_retries':round(statistics.mean(iv('api_retries')),3),
 'navigation_restricted_pct':round(100*sum(int(r['navigation_restricted'])==1 for r in rows)/n,3),
 'shore_link_unavailable_pct':round(100*sum(int(r['shore_link_available'])==0 for r in rows)/n,3)}
stored=json.loads((ROOT/'evidence/01_enterprise_sources/workshop_fixture_profile.json').read_text())
bench=json.loads((ROOT/'evidence/01_enterprise_sources/source_case_baseline.json').read_text())
print('Source-case benchmark (different population):')
print(json.dumps(bench,indent=2))
print()
print('140-row workshop fixture profile:')
print(json.dumps(calc,indent=2))
print()
print('Stored profile matches computed:',stored==calc)
