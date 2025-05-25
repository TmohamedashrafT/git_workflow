import requests
import logging

logging.basicConfig(level=logging.INFO)

def extract_data(base_currency: str, target_currency: str):

    url = f"https://api.exchangerate.host/latest?base={base_currency}&symbols={target_currency}"
    logging.info(f"Requesting exchange rate from {base_currency} to {target_currency}...")
    response = requests.get(url)
    if response.status_code != 200:
        logging.error(f"Failed to fetch API data: {response.status_code}")
        raise Exception("API request failed.")
    data = response.json()
    logging.info("API data received successfully.")
    return data


