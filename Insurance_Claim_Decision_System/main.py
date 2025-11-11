import pandas as pd
from logic.claim_processor import ClaimProcessor

def main():
    print("=== Insurance Claim Decision System ===")

    FILE_PATH = "data/claims.csv"
    processor = ClaimProcessor(FILE_PATH)

    # Read file
    processor.load_data()

    # Finish program if read file fail
    if processor.df is None:
        return

    # Claim decision
    processor.claim_decision()

    # Output to CSV file
    processor.save_file()

if __name__ == "__main__":
    main()