import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)

def load_data(df, output_path="exchange_rate.csv"): 
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    logging.info(f"Data written to {output_path}")

