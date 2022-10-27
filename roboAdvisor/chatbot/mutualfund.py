from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import json
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
    if statement.text == 'Edward GO':
      return True
    elif statement.text == 'mutual fund':
      return True
    else:
      return False

  def process(self, input_statement,additional_response_selection_parameters=None):
    #data = mutualFund.getSolution(risk,size,percentile,volatility)
    data = mutualFund.getRisk(risk)
    # funds = ""
    # funds = funds.join(data)
    print(data)
    #funds = json.dumps(data)
    print(type(input_statement.text))
    print(type(data))
    #print(data)
    #selected_statement = Statement(text=data)
    selected_statement = Statement(text='getting %s ' %(data))
    #selected_statement.confidence = 0.9
    return selected_statement
  