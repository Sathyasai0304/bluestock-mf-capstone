from data_ingestion import load_data
from data_cleaning import clean_data
from data_quality_check import validate_data
from load_to_sqlite import load_to_db

def run_pipeline():
    print("PIPELINE STARTED")

    # Step 1: Load
    data = load_data()

    # Step 2: Clean
    clean_data(data)

    # Step 3: Validate
    validate_data()

    # Step 4: Load into DB
    load_to_db()

    print("PIPELINE COMPLETED SUCCESSFULLY")

if __name__ == "__main__":
    run_pipeline()