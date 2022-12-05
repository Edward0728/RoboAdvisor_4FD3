from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
import logging

#custom_logger = logging.getLogger(__name__)

# Enable info level logging
logging.basicConfig(level=logging.INFO)

# Creating ChatBot Instance
chatbotInstance = ChatBot(
  'RoboAdvisor',
  storage_adapter='chatterbot.storage.SQLStorageAdapter',
  logic_adapters=[
    'chatterbot.logic.BestMatch',
    {
      'import_path': 'product_logicadapter.FundStockLogicAdapter',
      'default_response': 'I am sorry, but I do not understand. I am still learning.',
      'maximum_similarity_threshold': 0.90
    }
    # {
    #   'import_path': 'product_logicadapter.StockLogicAdapter',
    #   'default_response': 'I am sorry, but I do not understand. I am still learning.',
    #   'maximum_similarity_threshold': 0.90
    # }
  ],
  database_uri='sqlite:///database.sqlite3',
  #database_uri='sqlite:///C:/Users/forfu/source/repos/Edward0728/RoboAdvisor_4FD3/ChatBot/coronabot-chatterbot/database.sqlite3'
  #logger = custom_logger
)

# Training With Own Questions 

training_data_quesans = open('./training_data/profile_ques.txt').read().splitlines()
training_data_personal = open('./training_data/recommendation_chat.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer = ListTrainer(chatbotInstance)
trainer.train(
  training_data
#  './training_data/greetings.yml'
)

trainer.train(
['Can you help me with some investment ideas?',
'Sure. Let us get started.',]
)

trainer.train(
['Can you recommend some stocks and mutual funds to me?',
'Sure. Let us get started.',]
)

trainer.train(
['I need some recommendation for my investment.',
'Sure. Let us get started.',]
)

trainer.train(
['OK',
'Can I have your name, please? (Please answer in complete sentence. Same as below.)',]
)

trainer.train(
['Great.',
'Can I have your name, please? (Please answer in complete sentence. Same as below.)',]
)

trainer.train(
['Okay',
'Can I have your name, please? (Please answer in complete sentence. Same as below.)',]
)

trainer.train(
['Sounds Good',
'Can I have your name, please? (Please answer in complete sentence. Same as below.)',]
)

trainer.train(
['Nice',
'Can I have your name, please? (Please answer in complete sentence. Same as below.)',]
)

trainer.train(
['Do you need my information?',
'Can I have your name, please? (Please answer in complete sentence. Same as below.)',]
)

trainer.train(
['What information do you need?',
'Can I have your name, please? (Please answer in complete sentence. Same as below.)',]
)

trainer.train(
['My name is Sesha.',
'May I ask for your age, please? ',]
)

trainer.train(
['My name is Hua.',
'May I ask for your age, please? ',]
)

trainer.train(
['My name is Edward.',
'May I ask for your age, please? ',]
)

trainer.train(
['My age is 29.',
'How much money do you want to invest this time, please?',]
)

trainer.train(
['My age is 65.',
'How much money do you want to invest this time, please?',]
)

trainer.train(
['I want to invest $5000-$10000.',
'What fund size do you prefer at this time, please? (small, medium, large)',]
)

trainer.train(
['I want to invest $1000-$3000.',
'What fund size do you prefer at this time, please? (small, medium, large)',]
)

trainer.train(
['I want to invest $2000-$6000.',
'What fund size do you prefer at this time, please? (small, medium, large)',]
)

trainer.train(
['I want some medium size funds.',
'What fund percentile do you like, please? (top 10%, 15%, 30%)',]
)

trainer.train(
['I want some small size funds.',
'What fund percentile do you like, please? (top 10%, 15%, 30%)',]
)

trainer.train(
['I want some large size funds.',
'What fund percentile do you like, please? (top 10%, 15%, 30%)',]
)

trainer.train(
['I want top 30% funds.',
'What fund volatility can you take, please? (e.g.up to 10%)',]
)

trainer.train(
['I want top 15% funds.',
'What fund volatility can you take, please? (e.g.up to 10%)',]
)

trainer.train(
['I want top 10% funds.',
'What fund volatility can you take, please? (e.g.up to 10%)',]
)

trainer.train(
['I want top 10%.',
'What fund volatility can you take, please? (e.g.up to 10%)',]
)

trainer.train(
['I want top 30%.',
'What fund volatility can you take, please? (e.g.up to 10%)',]
)

trainer.train(
['I want top 15%.',
'What fund volatility can you take, please? (e.g.up to 10%)',]
)

trainer.train(
['I can take up to 20% volatility.',
'What fund risk level do you plan to take with, please? (low, low to medium, medium, medium to high , high)',]
)

trainer.train(
['I can take up to 9% volatility.',
'What fund risk level do you plan to take with, please? (low, low to medium, medium, medium to high , high)',]
)

trainer.train(
['I can take up to 20% volatility for the fund.',
'What stock ratings do you want at least, please? (from 1 to 5, e.g. 4.3)',]
)

trainer.train(
['I can take up to 9% volatility for the fund.',
'What fund risk level do you plan to take with, please? (low, low to medium, medium, medium to high , high)',]
)

trainer.train(
['I can take low risk.',
'What stock ratings do you want at least, please? (from 1 to 5, e.g. 4.3)',]
)

trainer.train(
['I can take low to medium risk.',
'What stock ratings do you want at least, please? (from 1 to 5, e.g. 4.3)',]
)

trainer.train(
['I can take medium risk.',
'What stock ratings do you want at least, please? (from 1 to 5, e.g. 4.3)',]
)

trainer.train(
['I can take medium to high risk.',
'What stock ratings do you want at least, please? (from 1 to 5, e.g. 4.3)',]
)

trainer.train(
['I can take high risk.',
'What stock ratings do you want at least, please? (from 1 to 5, e.g. 4.3)',]
)

trainer.train(
['I can take low risk for the fund.',
'What stock ratings do you want at least, please? (from 1 to 5, e.g. 4.3)',]
)

trainer.train(
['I can take low to medium risk for the fund.',
'What stock ratings do you want at least, please? (from 1 to 5, e.g. 4.3)',]
)

trainer.train(
['I can take medium risk for the fund.',
'What stock ratings do you want at least, please? (from 1 to 5, e.g. 4.3)',]
)

trainer.train(
['I can take medium to high risk for the fund.',
'What stock ratings do you want at least, please? (from 1 to 5, e.g. 4.3)',]
)

trainer.train(
['I can take high risk for the fund.',
'What stock ratings do you want at least, please? (from 1 to 5, e.g. 4.3)',]
)

trainer.train(
['I want stocks having ratings at least 4.5.',
'All done! Reply with "Go Money Go "and wait a second to get your customized recommendations.',]
)

trainer.train(
['I want stocks with ratings at least 4.6.',
'All done! Reply with "Go Money Go "and wait a second to get your customized recommendations.',]
)

trainer.train(
['I want stocks of ratings at least 4.7.',
'All done! Reply with "Go Money Go "and wait a second to get your customized recommendations.',]
)

trainer.train(
['I want stocks having ratings at least 3.0.',
'All done! Reply with "Go Money Go" and wait a second to get your customized recommendations.',]
)

trainer.train(
['I am looking for stable income.',
'All done! Reply with "Go Money Go" and wait a second to get your customized recommendations.',]
)

trainer.train(
['I am looking for income and growth balanced.',
'All done! Reply with "Go Money Go" and wait a second to get your customized recommendations.',]
)

trainer.train(
['I am looking for active growth.',
'All done! Reply with "Go Money Go" and wait a second to get your customized recommendations.',]
)


