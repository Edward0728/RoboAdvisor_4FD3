from django.apps import AppConfig
from chatbot import chatbot
from flask import Flask, render_template, request
from chatterbot.conversation import Statement


class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'


app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    input_statement = Statement(text=userText)
    response= str(chatbot.generate_response(input_statement))
    with open('conversation.txt', 'a') as output_file:
      #print(str(row))
      output_file.write(str(input_statement)+'\n')
      output_file.write(response+'\n')
    return response

if __name__ == "__main__":
    app.run() 