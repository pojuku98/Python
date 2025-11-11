from datetime import datetime

def calculate_claim(row):
    # How much needs to be paid to the customer
    payout = row['claim_amount']

    # rule_1： 'age' over 65 → 0.5 * payout
    if row['age'] > 65:
        payout *= 0.5

    # rule_2：car_insurance + drunk_driving → Deny
    if row['insurance_type'] == 'car' and row['accident_type'] == 'drunk_driving':
        return 0, "Deny: Drunk driving"

    # rule_3： Insurance less one year → Deny
    start_date = datetime.strptime(row['policy_start_date'], "%Y-%m-%d")
    days_since_start = (datetime.now() - start_date).days
    if days_since_start < 365:
        return 0, "Deny: Insurance less than one year"

    # rule_4： Health insurance + hospital_days < 3 → Deny
    if row['insurance_type'] == 'health' and row['hospital_days'] < 3:
        return 0, "Deny: Hospital days not fulfill"

    return payout, "Claim successful"
