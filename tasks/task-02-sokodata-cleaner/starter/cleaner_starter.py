"""Starter — Task 02. Implement clean_prices + _null_implausible_usd."""
from __future__ import annotations
import pandas as pd
PRICE_COLUMNS = ["date","admin1","admin2","market","market_id","latitude","longitude","category","commodity","commodity_id","unit","priceflag","pricetype","currency","price","usdprice"]
NATURAL_KEY = ["date","market_id","commodity_id","pricetype","priceflag"]
VALID_FLAGS = {"actual","aggregate"}
IMPLAUSIBLE_ERA_START = "2024-01-01"
IMPLAUSIBLE_FACTOR = 0.10
class SchemaDrift(Exception):
    pass
def clean_prices(df: pd.DataFrame, country: str = "ZW") -> pd.DataFrame:
    raise NotImplementedError
def _null_implausible_usd(df: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError
