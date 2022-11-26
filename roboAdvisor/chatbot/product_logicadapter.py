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

class FundStockLogicAdapter(LogicAdapter):
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
    Risk, Size, Percentile, Vola, Rating, Goal= parse_chat(lines)

    
    #funds = ", "
    if input_statement.text == 'Go Money Go': #or 'Edward GO':
      fund_data = mutualFund.getSolution(Risk,Size,Percentile,Vola)
      stock_data = Stock.getSolution(Rating)
      if 'no' not in fund_data:
        print('fund length: ', len(fund_data))
        if Goal==1:
          fund_percentage= 0.8/len(fund_data)
        if Goal==2:
          fund_percentage= 0.6/len(fund_data)
        if Goal==3:
          fund_percentage= 0.4/len(fund_data)
        fund_perc_str = ' ' + str(round(fund_percentage,4)*100)+'%'
      else:
        stock_perc_str = ''

      if 'no' not in stock_data:
        print(' stock length: ', len(stock_data))        
        if Goal==1:
          stock_percentage = 0.2/len(stock_data)
        if Goal==2:
          stock_percentage = 0.4/len(stock_data)     
        if Goal==3:
          stock_percentage = 0.6/len(stock_data)
        stock_perc_str =' ' + str(round(stock_percentage,4)*100)+'%'                
      else:
        stock_perc_str = ''
      print('fund%', fund_perc_str, 'stock%', stock_perc_str)

      funds = fund_perc_str + ",<br /> "
      funds = funds.join(fund_data) + fund_perc_str
      stocks = stock_perc_str + ",<br />"
      stocks = stocks.join(stock_data) + stock_perc_str
      open('./conversations/chat.txt', 'w').close()

    selected_statement = Statement(text='****************{}**************** <br > Funds: <br \> {} <br > <br \> Stocks: <br \> {}'.format(input_statement, funds,stocks))
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