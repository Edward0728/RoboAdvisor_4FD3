from django.apps import AppConfig
from chatbot import chatbotInstance
from flask import Flask, render_template, request
from chatterbot.conversation import Statement
from datetime import datetime

class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'


app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/login")
def login():
  return render_template("login_register.html")

@app.route("/bot")
def home():
    return render_template("chatbot.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    input_statement = Statement(text=userText)
    response = str(chatbotInstance.generate_response(input_statement))
    with open(f'./conversations/chat.txt', 'a') as output_file:
      #print(str(row))
      output_file.write(str(input_statement)+'\n')
      output_file.write(response+'\n')
    return response

if __name__ == "__main__":
    app.run() 