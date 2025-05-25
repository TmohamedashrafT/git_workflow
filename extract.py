import requests
import logging

logging.basicConfig(level=logging.INFO)

def extract_data(base_currency: str, target_currency: str):

    url = f"https://openexchangerates.org/api/latest.json?app_id=a92f8bad8e044bc79949a676886da2c8"
    logging.info(f"Requesting exchange rate from {base_currency} to {target_currency}...")
    response = requests.get(url)
    if response.status_code != 200:
        logging.error(f"Failed to fetch API data: {response.status_code}")
        raise Exception("API request failed.")
    data = response.json()
    logging.info("API data received successfully.")
    return data


