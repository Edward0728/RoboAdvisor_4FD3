from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement

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
    selected_statement = Statement(text='getting %s .....' % input_statement.text)
    return selected_statement
  