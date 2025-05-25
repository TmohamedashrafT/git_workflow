import logging
from extract import extract_data
from transform import transform_data

logging.basicConfig(level=logging.INFO)

def test_api_response():
    logging.info("Running API response test...")
    data = extract_data("EGP", "USD")
    assert isinstance(data, dict)
    assert "rates" in data and "USD" in data["rates"]
    logging.info("API test passed.")

def test_transformation():
    logging.info("Running transformation test...")
    sample = {
        "date": "2024-01-01",
        "rates": {"USD": 0.032},
        "base": "EGP"
    }
    df = transform_data(sample)
    assert "date" in df.columns and "egp_to_usd" in df.columns
    assert df.shape[0] == 1
    logging.info("Transformation test passed.")

def run_validations():
    test_api_response()
    test_transformation()
if __name__ == "__main__":
    run_validations() 
