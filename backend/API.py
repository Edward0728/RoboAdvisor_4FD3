# This is to build an interface between front end and back end
# from .StockData import stockinfo_request
# from .StockPlot import stockplot_request
# from .Fund_Selector import *
# from .Stock_Selector import *
#from .CSV_retriver import fundlist_request


class mutualFund():

# should return the information of looking symbol
  def get_fund_info(symbol):
    fund_information = fundinfo_request(symbol)
    return fund_information

# should return the list of mutual funds that fall in the looking risk level
  def getRisk(risk):
    fund_list = riskfund_request(risk)
    return fund_list

  def getSize(size):
    fund_list = fundsize_request(size)
    return fund_list

  def getPercentile(percentile):
    fund_list = fundrank_request(percentile)
    return fund_list
  
  def getVolatity(volatility):
    fund_list = fundvolatility_request(volatility)
    return fund_list

  def getSolution(risk,size,percentile,volatility):
    fund_list = fund_solution(riskfund_request(risk),fundsize_request(size),fundrank_request(percentile),fundvolatility_request(volatility))
    return fund_list

#Here is an example for stock information

class Stock():
  def get_stock_info(symbol):
    stock_info = stockinfo_request(symbol)
    return stock_info

  def get_graph(symbol):
    stock_graph = stockplot_request(symbol)
    return stock_graph

# should return the list of mutual funds that fall in the looking risk level
  def getRating(rating):
    stock_list = ratingstock_request(rating)
    return stock_list

  def getPercentile(percentile):
    stock_list = stockrank_request(percentile)
    return stock_list
  
  def getVolatity(volatility):
    stock_list = stockvolatility_request(volatility)
    return stock_list

  def getSolution(rating):
  #def getSolution(rating,size,percentile,volatility):
    #stock_list = final_solution(ratingstock_request(rating),stockrank_request(percentile),stockvolatility_request(volatility))
    stock_list = stock_solution(ratingstock_request(rating))
    return stock_list
#print(stock.get_info('AMZN'))
#stock.get_graph('AMZN')

# stock = 'TLSA'
# stock = 'AAPL'
# stock = 'AMZN'
# stock = 'IBM'
