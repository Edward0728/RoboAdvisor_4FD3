from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement

import sys
sys.path.append("../..")
from backend.API import mutualFund
symbol = 'TDB3491.CF'
risk = 'low to medium'
size = 'medium'
percentile = '30%'
volatility = '0.2'

class MutualFundLogicAdapter(LogicAdapter):
  def __init__(self, chatbot, **kwargs):
    super().__init__(chatbot, **kwargs)
  
  def can_process(self, statement):
    print(statement.text)
    with open('cx_input.txt', 'a') as output_file:
      #print(str(row))
      output_file.write(str(statement)+'\n')
    if statement.text == 'mutual fund':
      return True
    elif statement.text == 'stock':
      return True
    else:
      return False

  def process(self, input_statement,risk,size,percentile,volatility):
    data = mutualFund.get_solution(risk,size,percentile,volatility)
    print(data)
    selected_statement = Statement(text='getting %s \n ..... %s' %(input_statement.text, data))
    return selected_statement
  