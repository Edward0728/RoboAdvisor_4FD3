from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from API.mutualFund import get
import sys

sys.path.insert(0, '/Users/hw/digital-garage/RoboAdvisor_4FD3/backend')

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
    
    selected_statement = Statement(text='getting %s ..... %s' % input_statement.text % get('RBF460.CF'))
    return selected_statement
  