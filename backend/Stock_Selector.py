import json
import pandas as pd
import os
dirname = os.path.dirname(__file__)
# Change the CSV file address to your CSV file path
#mutualStock_CSV = pd.read_csv (r'/Users/qinyang/PycharmProjects/RoboAdvisor/Investment_Data/all_stocks_data.csv')
date = '2022-11-12'

allStockName = os.path.join(dirname, '../Investment_Data/stocks_{}.csv'.format(date))

Stock_CSV = pd.read_csv (allStockName)
#rating_levels = ['None','Low','Low to Medium','Medium','Medium to High','High']

# symbol = 'TDB3491.CF'
# rating = 'low to medium'
# size = 'medium'
# percentile = '30%'
# volatility = '0.2'

def stockinfo_request(symbol):
    stock = symbol
    stock_info = Stock_CSV.loc[Stock_CSV['Symbol'] == stock]
    data = stock_info.to_json()
    #return stock_info
    return data

#print(stockinfo_request(symbol))

def ratingstock_request(rating):
    print('get rating as: ', rating)
    print(type(rating))
    stock_list = Stock_CSV.loc[Stock_CSV['Rating'] >= rating.strip(), 'Symbol'].tolist()
    #data = json.dumps(stock_list)
    return stock_list
    #return data

def stockrank_request(percentile):
    print('get percetile as: ', percentile)
    print(type(percentile))
    stock_list = Stock_CSV.loc[Stock_CSV['Percentile'] == percentile.strip(), 'Symbol'].tolist()
    #data = json.dumps(stock_list)
    return stock_list
    #return data

def stockvolatility_request(volatility):
    print('get volatility as: ', volatility)
    print(type(volatility))
    Stock_CSV['Volatility'] = pd.to_numeric(Stock_CSV['Volatility'])
    #print(mutualStock_CSV['Volatility'])
    stock_list = Stock_CSV.loc[Stock_CSV['Volatility'] <= float(volatility), 'Symbol'].tolist()
    #print(stock_list)
    #data = json.dumps(stock_list)
    return stock_list
    #return data

def final_solution(rating_stock):
#def final_solution(rating_stock,size_stock,rank_stock,volatility_stock):
    solution = []
    for i in rating_stock:
        solution.append(i)
    if len(solution) != 0:
        return solution
    else:
        return(['no', 'stock', 'found'])    

# rating_stock = ratingstock_request(rating)
# size_stock = stocksize_request(size)
# rank_stock = stockrank_request(percentile)
# volatility_stock = stockvolatility_request(volatility)

#print('rating', rating_stock, end = '\n')
# print('size', size_stock, end = '\n')
# print('rank', rank_stock, end = '\n')
# print('vola', volatility_stock,end = '\n')

#solution = final_solution(ratingstock_request(rating),stocksize_request(size),stockrank_request(percentile),stockvolatility_request(volatility))
#print(final_solution(rating_stock,size_stock,rank_stock,volatility_stock))

