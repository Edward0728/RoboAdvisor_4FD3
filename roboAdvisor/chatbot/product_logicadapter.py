from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
#import json
from userinput import parse_chat
# from userinput import Risk
# from userinput import Size
# from userinput import Percentile
# from userinput import Vola
#from userinput import conversation

import sys
sys.path.append("../..")
from backend.API import mutualFund
from backend.API import Stock
# symbol = 'TDB3491.CF'
# risk = 'low to medium'
# size = 'medium'
# percentile = '30%'
# volatility = '0.2'

# conversation = open(f'./conversations/chat.txt', 'r')
# lines = conversation.readlines() 
# Risk, Size, Percentile, Vola = parse_chat(lines)
# p = open('./conversations/parameters.txt', 'r')
# parameters = p.readlines()
# if len(parameters) != 0:
#   Risk = parameters[0]
#   Size = parameters[1]
#   Percentile = parameters[2]
#   Vola = float(parameters[3])

class MutualFundLogicAdapter(LogicAdapter):
  def __init__(self, chatbot, **kwargs):
    super().__init__(chatbot, **kwargs)
  
  def can_process(self, statement):
    print(statement.text)
    if statement.text == 'Go Money Go':
      return True
    # elif statement.text == 'Edward GO':
    #   return True
    else:
      return False

  def process(self, input_statement,additional_response_selection_parameters=None):
    #data = mutualFund.getSolution(risk,size,percentile,volatility)
    conversation = open(f'./conversations/chat.txt', 'r')
    lines = conversation.readlines() 
    Risk, Size, Percentile, Vola, Rating= parse_chat(lines)
    #funds = ", "
    if input_statement.text == 'Go Money Go': #or 'Edward GO':
      fund_data = mutualFund.getSolution(Risk,Size,Percentile,Vola)
      stock_data = Stock.getSolution(Rating)
      funds = ", "
      funds = funds.join(fund_data)
      stocks = "/ "
      stocks = stocks.join(stock_data)
      print(funds)
      open('./conversations/chat.txt', 'w').close()

    selected_statement = Statement(text='************{}************ <br > Funds: {} <br > Stocks: {}'.format(input_statement, funds,stocks))
    selected_statement.confidence = 0.9
    return selected_statement
  
  
# class StockLogicAdapter(LogicAdapter):
#   def __init__(self, chatbot, **kwargs):
#     super().__init__(chatbot, **kwargs)
  
#   def can_process(self, statement):
#     print(statement.text)
#     if statement.text == 'Go Money Go':
#       return True
#     # elif statement.text == 'Edward GO':
#     #   return True
#     else:
#       return False

#   def process(self, input_statement,additional_response_selection_parameters=None):
#     #data = mutualFund.getSolution(risk,size,percentile,volatility)
#     if input_statement.text == 'stock':
#       data = stock.get_info('AMZN')
#     #funds = json.dumps(data)
#     # print(type(input_statement.text))
#     # print(type(data))
#     #print(data)
#     #selected_statement = Statement(text=data)
#     selected_statement = Statement(text='getting {} <br > {}'.format(input_statement, data))
#     selected_statement.confidence = 0.9
#     return selected_statement