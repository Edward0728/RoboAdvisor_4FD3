# This is to build an interface between front end and back end
from StockData import stockinfo_request
from StockPlot import stockplot_request

class mutualFund():

  # should return the information of looking symbol
  def get(symbol):
    fund_information = {1,2,3}
    return fund_information

  # should return the list of mutual funds that fall in the looking risk level
  def getRisk(level):
    fund_list = {4,5,6}
    return fund_list


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

  def get_graph(graph):
    stock_graph = stockplot_request(graph)
    return stock_graph


stock.get_info('AAPL')
stock.get_graph('AAPL')


