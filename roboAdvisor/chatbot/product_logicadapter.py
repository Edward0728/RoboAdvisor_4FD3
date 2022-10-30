from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
#import json
from userinput import Risk
from userinput import Size
from userinput import Percentile
from userinput import Volatility
#from userinput import conversation

import sys
sys.path.append("../..")
from backend.API import mutualFund
from backend.API import stock
# symbol = 'TDB3491.CF'
# risk = 'low to medium'
# size = 'medium'
# percentile = '30%'
# volatility = '0.2'

class MutualFundLogicAdapter(LogicAdapter):
  def __init__(self, chatbot, **kwargs):
    super().__init__(chatbot, **kwargs)
  
  def can_process(self, statement):
    print(statement.text)
    if statement.text == 'mutual fund':
      return True
    elif statement.text == 'Edward GO':
      return True
    else:
      return False

  def process(self, input_statement,additional_response_selection_parameters=None):
    #data = mutualFund.getSolution(risk,size,percentile,volatility)
    if input_statement.text == 'mutual fund' or 'Edward GO':
      data = mutualFund.getSolution(Risk,Size,Percentile,Volatility)
      funds = ", "
      funds = funds.join(data)
      print(funds)
    #funds = json.dumps(data)
    # print(type(input_statement.text))
    # print(type(data))
    #print(data)
    #selected_statement = Statement(text=data)
    selected_statement = Statement(text='getting {} <br > {}'.format(input_statement, funds))
    selected_statement.confidence = 0.9
    return selected_statement
  
  
# class StockLogicAdapter(LogicAdapter):
#   def __init__(self, chatbot, **kwargs):
#     super().__init__(chatbot, **kwargs)
  
#   def can_process(self, statement):
#     print(statement.text)
#     if statement.text == 'stock':
#       return True
#     elif statement.text == 'Edward GO':
#       return True
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