# This is to build an interface between front end and back end
from .StockData import stockinfo_request
from .StockPlot import stockplot_request
import Fund_Selector as F
#from .CSV_retriver import fundlist_request


class mutualFund():

# should return the information of looking symbol
  def get(symbol):
    fund_information = F.fundinfo_request(symbol)
    return fund_information

# should return the list of mutual funds that fall in the looking risk level
  def getRisk(risk):
    fund_list = F.riskfund_request(risk)
    return fund_list

  def getSize(size):
    fund_list = F.fundsize_request(size)
    return fund_list

  def getPercentile(percentile):
    fund_list = F.fundrank_request(percentile)
    return fund_list
  
  def getVolatity(volatility):
    fund_list = F.fundvolatility_request(volatility)
    return fund_list

  def getSolution(risk,size,percentile,volatility):
    fund_list = F.final_solution(F.riskfund_request(risk),F.fundsize_request(size),F.fundrank_request(percentile),F.fundvolatility_request(volatility))
    return fund_list
  

# print(mutualFund.get('RBF460.CF'))
# print(mutualFund.getRisk('Low'))


# How the frond end consumes the functions, e.g.
# import mutualFund
# mutualFund.get('RBF460.CF')
# mutualFund.getRisk('Low')
# print(mutualFund.get('RBF460.CF'))
# print(mutualFund.getRisk('Low'))


# Here is an example for stock information

class stock():
  def get_info(symbol):
    stock_info = stockinfo_request(symbol)
    return stock_info

  def get_graph(symbol):
    stock_graph = stockplot_request(symbol)
    return stock_graph

# print(stock.get_info('AMZN'))
# stock.get_graph('AMZN')

# stock = 'TLSA'
# stock = 'AAPL'
# stock = 'AMZN'
# stock = 'IBM'
