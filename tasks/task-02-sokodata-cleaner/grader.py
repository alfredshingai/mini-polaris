"""Deterministic grader for Task 02 — 100 pts."""
import importlib.util, pathlib, sys
import pandas as pd
HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("cl", str(HERE/"starter"/"cleaner_starter.py"))
cl = importlib.util.module_from_spec(spec); spec.loader.exec_module(cl)
score = 0
def check(n,c,p):
    global score
    if c: score += p
    print(f"[{'PASS' if c else 'FAIL'}] {n} (+{p if c else 0}/{p})")

def base_df():
    return pd.DataFrame([{
        "date":"2024-06-01","admin1":"Harare","admin2":"Harare","market":"Mbare ","market_id":1,
        "latitude":-17.8,"longitude":31.0,"category":"cereals","commodity":"maize","commodity_id":1,
        "unit":"kg","priceflag":"actual","pricetype":"retail","currency":"USD","price":0.8,"usdprice":0.8},
        {"date":"2024-06-01","admin1":"Harare","admin2":"Harare","market":"Mbare","market_id":1,
        "latitude":-17.8,"longitude":31.0,"category":"cereals","commodity":"maize","commodity_id":1,
        "unit":"kg","priceflag":"actual","pricetype":"retail","currency":"USD","price":0.9,"usdprice":0.9},
        {"date":"2022-01-01","admin1":"Harare","admin2":"Harare","market":"Mbare","market_id":1,
        "latitude":-17.8,"longitude":31.0,"category":"cereals","commodity":"rice","commodity_id":2,
        "unit":"kg","priceflag":"actual","pricetype":"retail","currency":"ZWL","price":5000,"usdprice":0.0017},
        {"date":"2024-06-01","admin1":"Harare","admin2":"Harare","market":"Mbare","market_id":1,
        "latitude":-17.8,"longitude":31.0,"category":"cereals","commodity":"rice","commodity_id":2,
        "unit":"kg","priceflag":"actual","pricetype":"retail","currency":"USD","price":1.5,"usdprice":1.5}])

try:
    bad = base_df().drop(columns=["price"])
    try:
        cl.clean_prices(bad); check("schema-drift raises", False, 20)
    except Exception as e:
        check("schema-drift raises", type(e).__name__=="SchemaDrift", 20)
    out = cl.clean_prices(base_df())
    check("dedupe natural key keep=last (3 rows)", len(out)==3, 20)
    check("kept last price 0.9", float(out[(out.commodity_id==1)].iloc[0]["price"])==0.9, 10)
    check("text stripped", str(out.iloc[0]["market"])=="Mbare", 10)
    rice_old = out[(out.commodity_id==2)&(out.date<pd.Timestamp("2024-01-01"))]
    check("implausible ZWL usd nulled, price kept", pd.isna(rice_old.iloc[0]["usdprice"]) and rice_old.iloc[0]["price"]==5000, 30)
    check("sorted by natural key", list(out["date"])==sorted(list(out["date"])), 10)
except Exception as e:
    print(f"[FAIL] exception: {e}"); import traceback; traceback.print_exc()
print(f"\nSCORE: {score}/100 — {'SOLVED (>=85)' if score>=85 else 'NOT SOLVED'}")
sys.exit(0 if score>=85 else 1)
