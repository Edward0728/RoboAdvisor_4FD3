import json
import os
import pandas as pd

abs_path = os.path.dirname(__file__)
rel_path = "../Investment_Data/all_funds_data.csv"
full_path = os.path.join(abs_path, rel_path)
# Change the CSV file address to your CSV file path
mutualFund_CSV = pd.read_csv (full_path)


def fundinfo_request(symbol):
    fund = symbol
    fund_info = mutualFund_CSV.loc[mutualFund_CSV['Symbol'] == fund]
    data = fund_info.to_json()
    return data


def fundlist_request(symbol):
    risk_level = symbol
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['risk'] == risk_level, 'Symbol'].tolist()
    data = json.dumps(fund_list)
    return data

