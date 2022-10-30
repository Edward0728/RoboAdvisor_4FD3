import json
import pandas as pd
# Change the CSV file address to your CSV file path
#mutualFund_CSV = pd.read_csv (r'/Users/qinyang/PycharmProjects/RoboAdvisor/Investment_Data/all_funds_data.csv')
date = '2022-10-25'
mutualFund_CSV = pd.read_csv (f'C:/Users/forfu/source/repos/Edward0728/RoboAdvisor_4FD3/Investment_Data/all_funds_all_data_{date}.csv')
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
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['Risk'] == risk, 'Symbol'].tolist()
    #data = json.dumps(fund_list)
    return fund_list
    #return data

def fundsize_request(size):
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['Size'] == size, 'Symbol'].tolist()
    #data = json.dumps(fund_list)
    return fund_list
    #return data

def fundrank_request(percentile):
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['Percentile'] == percentile, 'Symbol'].tolist()
    #data = json.dumps(fund_list)
    return fund_list
    #return data

def fundvolatility_request(volatility):
    mutualFund_CSV['Volatility'] = pd.to_numeric(mutualFund_CSV['Volatility'])
    print(mutualFund_CSV['Volatility'])
    fund_list = mutualFund_CSV.loc[mutualFund_CSV['Volatility'] <= float(volatility), 'Symbol'].tolist()
    #data = json.dumps(fund_list)
    print(fund_list)
    return fund_list
    #return data

def final_solution(risk_fund,size_fund,rank_fund,volatility_fund):
    solution = []
    for i in risk_fund:
        #print(i)
        if i in size_fund and i in rank_fund and i in volatility_fund:
            solution.append(i)
    if len(solution) != 0:
        return solution
    else:
        return(['No fund found'])   

data = final_solution(riskfund_request('low to medium'),fundsize_request('medium'),fundrank_request('30%'),fundvolatility_request('0.15'))
funds = ", "
funds = funds.join(data)
print(funds) 
