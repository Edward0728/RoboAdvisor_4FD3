  # This is to build an interface between front end and back end
from StockData import stockinfo_request
from StockPlot import stockplot_request
from Fund_Selector import *
from Stock_Selector import *
  
def getSolution(rating):
    #def getSolution(rating,size,percentile,volatility):
    #stock_list = final_solution(ratingstock_request(rating),stockrank_request(percentile),stockvolatility_request(volatility))
    stock_list = stock_solution(ratingstock_request(rating))
    return stock_list

stock_list = getSolution('4.5')