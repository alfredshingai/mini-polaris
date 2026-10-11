"""Deterministic grader for Task 03 — 100 pts (synthetic fixtures inline)."""
import importlib.util, pathlib, sys, tempfile, csv, os
HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("v", str(HERE/"starter"/"validator_starter.py"))
v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
score=0
def check(n,c,p):
    global score
    if c: score+=p
    print(f"[{'PASS' if c else 'FAIL'}] {n} (+{p if c else 0}/{p})")
vocab={"sectors":["energy","transport"],"organization_roles":["financier","builder"],"location_precision":["exact","approximate","unknown"],"evidence_strength":["strong","medium","weak"],"date_precision":["day","month","year"]}
def write(d,n,rows,fields):
    with open(os.path.join(d,n),"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
try:
    with tempfile.TemporaryDirectory() as d:
        write(d,"projects.csv",[{"id":"p1","canonical_name":"Kariba Dam","country_iso3":"ZWE","sectors":"energy","lat":"-16.5","lon":"28.8","location_precision":"exact"},{"id":"","canonical_name":"Kariba Dam","country_iso3":"zw","sectors":"magic","lat":"51.5","lon":"-0.1","location_precision":"exact"}],["id","canonical_name","country_iso3","sectors","lat","lon","location_precision"])
        write(d,"organizations.csv",[{"id":"o1","canonical_name":"Sinohydro"}],["id","canonical_name"])
        write(d,"participation_records.csv",[{"id":"r1","role":"financier","org_id":"o1"},{"id":"r2","role":"","org_id":""}],["id","role","org_id"])
        write(d,"contracts.csv",[{"id":"c1","value_original":"100","currency":""},{"id":"c2","value_original":"50","currency":"US"}],["id","value_original","currency"])
        write(d,"claims.csv",[{"id":"cl1","claim_text":"built dam","verbatim_quote":"","source_id":"s1","evidence_strength":"strong"},{"id":"cl2","claim_text":"","verbatim_quote":"q","source_id":"","evidence_strength":"nope"}],["id","claim_text","verbatim_quote","source_id","evidence_strength"])
        write(d,"dates.csv",[{"id":"d1","precision":"day"}],["id","precision"])
        errors,warns=v.validate(d,vocab)
        E="\n".join(errors); W="\n".join(warns)
        check("missing id → error", any("missing id" in e for e in errors), 15)
        check("bad iso/sector → error", any("iso3" in e for e in errors) and any("sector" in e for e in errors), 15)
        check("role/org missing → error", sum("role" in e or "org_id" in e for e in errors)>=2, 15)
        check("value w/o currency → error", any("currency" in e for e in errors), 15)
        check("claim text/source/strength → error", sum("claim" in e or "source_id" in e or "evidence" in e for e in errors)>=2, 15)
        check("verbatim missing → warn", any("verbatim" in w for w in warns), 10)
        check("coords outside Africa → warn", any("bbox" in w or "outside" in w for w in warns), 15)
        check("returns 2 lists", isinstance(errors,list) and isinstance(warns,list), 0)
except Exception as e:
    print(f"[FAIL] exception {e}"); import traceback; traceback.print_exc()
print(f"\nSCORE: {score}/100 — {'SOLVED (>=85)' if score>=85 else 'NOT SOLVED'}")
sys.exit(0 if score>=85 else 1)
