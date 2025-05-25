import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)

def load_data(df, output_path="exchange_rate.csv"): 
    df.to_csv(output_path, index=False)
    logging.info(f"Data written to {output_path}")

