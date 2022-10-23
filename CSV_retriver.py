import json

import pandas as pd
# Change the CSV file address to your CSV file path
#mutualFund_CSV = pd.read_csv (r'/Users/qinyang/PycharmProjects/RoboAdvisor/Investment_Data/all_funds_data.csv')
mutualFund_CSV = pd.read_csv (r'C:/Users/forfu/source/repos/Edward0728/RoboAdvisor_4FD3/Investment_Data/all_funds_data.csv')
risk_levels = ['None','Low','Low to Medium','Medium','Medium to High','High']

symbol = 'TDB3491.CF'
risk = risk_levels[2]

def fundinfo_request(symbol):
    fund = symbol
    fund_info = mutualFund_CSV.loc[mutualFund_CSV['Symbol'] == fund]
    data = fund_info.to_json()
    return data

#print(fundinfo_request(symbol))

def riskfund_request(risk):
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['risk'] == risk, 'Symbol'].tolist()
    data = json.dumps(fund_list)
    return data

#print(riskfund_request(risk))

