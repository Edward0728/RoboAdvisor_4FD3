import json
import pandas as pd
import os
from .Stock_Prediction import *

dirname = os.path.dirname(__file__)
# Change the CSV file address to your CSV file path
#mutualStock_CSV = pd.read_csv (r'/Users/qinyang/PycharmProjects/RoboAdvisor/Investment_Data/all_stocks_data.csv')
date = '2022-12-02'

allStockName = os.path.join(dirname, '../Investment_Data/stocks_{}.csv'.format(date))
Stock_CSV = pd.read_csv (allStockName)
n_future = 60
#rating_levels = ['None','Low','Low to Medium','Medium','Medium to High','High']

# symbol = 'TDB3491.CF'
# rating = 'low to medium'
# size = 'medium'
# percentile = '30%'
# volatility = '0.2'

#rating = 4.5

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
    Stock_CSV['Rating'] = pd.to_numeric(Stock_CSV['Rating'])
    stock_list = Stock_CSV.loc[Stock_CSV['Rating'] >= float(rating.strip()), 'Symbol'].tolist()
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

def stock_solution(rating_stock):
#def final_solution(rating_stock,size_stock,rank_stock,volatility_stock):
    solution_rate = []
    print(rating_stock)
    for i in rating_stock:
        stock_ticker = i[:-2]+'.TO'
        print(stock_ticker)
        x = multi_step_forecasts(stock_ticker.strip(),0, n_future)
        solution_rate.append((i,x))
        def rate(stock):
            return stock[1]      
        solution_rate.sort(key = rate, reverse=True)
    solution = (i[1] for i in solution_rate)
    #print('stock solution: ', solution)
    if len(solution) >= 10:
        return solution[0:10]
    elif len(solution) > 0 and len(solution) < 10:
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

