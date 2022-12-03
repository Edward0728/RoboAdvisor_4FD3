import json
import pandas as pd
import os
dirname = os.path.dirname(__file__)
# Change the CSV file address to your CSV file path
#mutualFund_CSV = pd.read_csv (r'/Users/qinyang/PycharmProjects/RoboAdvisor/Investment_Data/all_funds_data.csv')
date = '2022-12-01'

allFundName = os.path.join(dirname, '../Investment_Data/funds_{}.csv'.format(date))

mutualFund_CSV = pd.read_csv (allFundName)
#risk_levels = ['None','Low','Low to Medium','Medium','Medium to High','High']

# symbol = 'TDB3491.CF'
# risk = 'low to medium'
# size = 'medium'
# percentile = '30%'
# volatility = '0.2'

def fundinfo_request(symbol):
    fund = symbol
    fund_info = mutualFund_CSV.loc[mutualFund_CSV['Symbol'] == fund]
    data = fund_info.to_json()
    #return fund_info
    return data

#print(fundinfo_request(symbol))

def riskfund_request(risk):
    print('get risk as: ', risk)
    print(type(risk))
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['Risk'] == risk.strip(), 'Symbol'].tolist()
    #data = json.dumps(fund_list)
    return fund_list
    #return data

def fundsize_request(size):
    print('get size as: ', size)
    print(type(size))
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['Size'] == size.strip(), 'Symbol'].tolist()
    #data = json.dumps(fund_list)
    return fund_list
    #return data

def fundrank_request(percentile):
    print('get percetile as: ', percentile)
    print(type(percentile))
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['Percentile'] == percentile.strip(), 'Symbol'].tolist()
    #data = json.dumps(fund_list)
    return fund_list
    #return data

def fundvolatility_request(volatility):
    print('get volatility as: ', volatility)
    print(type(volatility))
    mutualFund_CSV['Volatility'] = pd.to_numeric(mutualFund_CSV['Volatility'])
    #print(mutualFund_CSV['Volatility'])
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['Volatility'] <= float(volatility), 'Symbol'].tolist()
    #print(fund_list)
    #data = json.dumps(fund_list)
    return fund_list
    #return data

def fund_solution(risk_fund,size_fund,rank_fund,volatility_fund):
    solution = []
    for i in risk_fund:
        #print(i)
        if i in size_fund and i in rank_fund and i in volatility_fund:
            solution.append(i)
    print('fund solution: ', solution)
    if len(solution) >= 10:
        return solution[0:10]
    elif len(solution) > 0 and len(solution) < 10:
        return solution
    else:
        return(['no', 'fund', 'found'])    

# risk_fund = riskfund_request(risk)
# size_fund = fundsize_request(size)
# rank_fund = fundrank_request(percentile)
# volatility_fund = fundvolatility_request(volatility)

#print('risk', risk_fund, end = '\n')
# print('size', size_fund, end = '\n')
# print('rank', rank_fund, end = '\n')
# print('vola', volatility_fund,end = '\n')

#solution = final_solution(riskfund_request(risk),fundsize_request(size),fundrank_request(percentile),fundvolatility_request(volatility))
#print(final_solution(risk_fund,size_fund,rank_fund,volatility_fund))

