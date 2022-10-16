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
    return str(chatbot.generate_response(input_statement))

if __name__ == "__main__":
    app.run() 