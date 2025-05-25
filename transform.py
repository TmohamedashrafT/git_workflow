import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

def transform_data(raw_data):
    logging.info("Transforming API data...")
    date = raw_data.get("date")
    rate = raw_data.get("rates", {}).get("USD")
    if rate is None:
        raise ValueError("USD rate not found in API response")
    df = pd.DataFrame([{
        "date": date or datetime.utcnow().date().isoformat(),
        "egp_to_usd": rate
    }])
    logging.info(f"Exchange rate on {date}: 1 EGP = {rate} USD")
    return df

