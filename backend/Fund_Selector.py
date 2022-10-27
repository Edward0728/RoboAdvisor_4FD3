import json
import pandas as pd
# Change the CSV file address to your CSV file path
#mutualFund_CSV = pd.read_csv (r'/Users/qinyang/PycharmProjects/RoboAdvisor/Investment_Data/all_funds_data.csv')
date = '2022-10-25'
mutualFund_CSV = pd.read_csv (f'C:/Users/forfu/source/repos/Edward0728/RoboAdvisor_4FD3/Investment_Data/all_funds_all_data_{date}.csv')
risk_levels = ['None','Low','Low to Medium','Medium','Medium to High','High']

symbol = 'TDB3491.CF'
risk = risk_levels[2]
size = 'Medium'
percentile = '30%'
volatility = '0.2'

def fundinfo_request(symbol):
    fund = symbol
    fund_info = mutualFund_CSV.loc[mutualFund_CSV['Symbol'] == fund]
    #data = fund_info.to_json()
    return fund_info

#print(fundinfo_request(symbol))

def riskfund_request(risk):
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['Risk'] == risk, 'Symbol'].tolist()
    #data = json.dumps(fund_list)
    return fund_list

def fundsize_request(size):
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['Size'] == size, 'Symbol'].tolist()
    #data = json.dumps(fund_list)
    return fund_list

def fundrank_request(percentile):
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['Percentile'] == percentile, 'Symbol'].tolist()
    #data = json.dumps(fund_list)
    return fund_list

def fundvolatility_request(volatility):
    mutualFund_CSV['Volatility'] = pd.to_numeric(mutualFund_CSV['Volatility'])
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['Volatility'] <= float(volatility), 'Symbol'].tolist()
    #data = json.dumps(fund_list)
    return fund_list

def final_solution(risk_fund,size_fund,rank_fund,volatility_fund):
    solution = []
    for i in risk_fund:
        print(i)
        if i in size_fund and i in rank_fund and i in volatility_fund:
            solution.append(i)
    if len(solution) != 0:
        return solution
    else:
        return("no fund found")    

# risk_fund = riskfund_request(risk)
# size_fund = fundsize_request(size)
# rank_fund = fundrank_request(percentile)
# volatility_fund = fundvolatility_request(volatility)

#print('risk', risk_fund, end = '\n')
# print('size', size_fund, end = '\n')
# print('rank', rank_fund, end = '\n')
# print('vola', volatility_fund,end = '\n')

solution = final_solution(riskfund_request(risk),fundsize_request(size),fundrank_request(percentile),fundvolatility_request(volatility))
print(solution)

