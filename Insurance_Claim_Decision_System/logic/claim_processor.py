import pandas as pd
from logic.claim_rules import calculate_claim

from datetime import datetime


class ClaimProcessor:
    def __init__(self, file_path):
        """ Construct the object """
        self.path = file_path
        self.df = None
        self.results = []

    def load_data(self):
        """ Read CSV file and do exception handling """
        try:
            self.df = pd.read_csv(self.path)
            print("Successfully access the CSV file.")
        except FileNotFoundError:
            print("Can not find the file, please check the path")

    def claim_decision(self):
        """ Do claim decision """
        for _, row in self.df.iterrows():
            payout, reason = calculate_claim(row)
            self.results.append({
                                    "customer_id": row['customer_id'],
                                    "payout": payout,
                                    "reason": reason
            })
        print("Claim decision finish.")

    def save_file(self):
        """ Save the results to CSV file """
        results_df = pd.DataFrame(self.results)
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = f"output/results_{current_time}.csv"
        results_df.to_csv(save_path, index=False)
        print(f"Results already save to {save_path}")
        print(results_df)