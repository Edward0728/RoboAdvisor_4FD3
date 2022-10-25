from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import sys
sys.path.append("../..")

from backend.API import mutualFund

class MutualFundLogicAdapter(LogicAdapter):
  def __init__(self, chatbot, **kwargs):
    super().__init__(chatbot, **kwargs)
  def can_process(self, statement):
    print(statement.text)
    if statement.text == 'mutual fund':
      return True
    elif statement.text == 'stock':
      return True
    else:
      return False
  def process(self, input_statement, additional_response_selection_parameters):
    data = mutualFund.getRisk('Low')
    print(data)
    selected_statement = Statement(text='getting %s \n ..... %s' %(input_statement.text, data))
    return selected_statement
  