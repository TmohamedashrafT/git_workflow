from extract import extract_data
from transform import transform_data
from load import load_data
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    data = extract_data()
    transformed = transform_data(data)
    load_data(transformed)
    logging.info("ETL completed successfully.")