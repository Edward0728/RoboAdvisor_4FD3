from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
#import logging

#custom_logger = logging.getLogger(__name__)


# Creating ChatBot Instance
chatbot = ChatBot(
  'RoboBot',
  storage_adapter='chatterbot.storage.SQLStorageAdapter',
  logic_adapters=[
    'chatterbot.logic.BestMatch',
    {
      'import_path': 'product_logicadapter.MutualFundLogicAdapter',
      'default_response': 'I am sorry, but I do not understand. I am still learning.',
      'maximum_similarity_threshold': 0.90
    },
    {
      'import_path': 'product_logicadapter.StockLogicAdapter',
      'default_response': 'I am sorry, but I do not understand. I am still learning.',
      'maximum_similarity_threshold': 0.90
    }
  ],
  database_uri='sqlite:///database.sqlite3',
  #database_uri='sqlite:///C:/Users/forfu/source/repos/Edward0728/RoboAdvisor_4FD3/ChatBot/coronabot-chatterbot/database.sqlite3'
  #logger = custom_logger
)

# Training With Own Questions 

training_data_quesans = open('./training_data/profile_ques.txt').read().splitlines()
training_data_personal = open('./training_data/recommendation_chat.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data)



# # Training With Corpus
# trainer_corpus = ChatterBotCorpusTrainer(chatbot)

# trainer_corpus.train(
#     'chatterbot.corpus.english'
# )


#  # Training with Personal Ques & Ans 
# conversation = [
#     "Hello",
#     "Hi there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is good to hear",
#     "Thank you.",
#     "You're welcome."
# ]

# trainer = ListTrainer(chatbot)
# trainer.train(conversation)

# Training with English Corpus Data 
# trainer_corpus = ChatterBotCorpusTrainer(chatbot)
# trainer_corpus.train(
#     'chatterbot.corpus.english'
# ) 
