from django.apps import AppConfig
from chatbot import chatbotInstance
from flask import Flask, render_template, request
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin
from chatterbot.conversation import Statement
from datetime import datetime


class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'



class FlaskConfig(object):
  SECRET_KEY = 'SECRET KEY'
  # Flask-SQLAlchemy settings
  SQLALCHEMY_DATABASE_URI = 'sqlite:///basic_app.sqlite3'    # File-based SQL database
  SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning
  # Flask user setting
  USER_APP_NAME = "RoboAdvisor"      # Shown in and email templates and page footers
  USER_CORPORATION_NAME = "RoboAdvisor"
  USER_COPYRIGHT_YEAR = "2022"
  USER_ENABLE_EMAIL = False        # Disable email authentication
  USER_ENABLE_USERNAME = True    # Enable username authentication
  # USER_EMAIL_SENDER_NAME = USER_APP_NAME
  # USER_EMAIL_SENDER_EMAIL = "noreply@example.com"
  # USER_LOGIN_TEMPLATE = 'login_register.html'
  # USER_LOGIN_TEMPLATE                     = 'flask_user/login_or_register.html'
  # USER_REGISTER_TEMPLATE                  = 'flask_user/login_or_register.html'

app = Flask(__name__)
app.config.from_object(__name__+'.FlaskConfig')
app.static_folder = 'static'

# initialize flask-babelex
babel = Babel(app)

# initialize flask-sqlalchemy
db = SQLAlchemy(app)

# define the User data-model
class User(db.Model, UserMixin):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

  # User authentication information. The collation='NOCASE' is required
  # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
  username = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)
  username_confirmed_at = db.Column(db.DateTime())
  # email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)
  # email_confirmed_at = db.Column(db.DateTime())
  password = db.Column(db.String(255), nullable=False, server_default='')

  # User information
  # first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
  # last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')

  # Define the relationship to Role via UserRoles
  roles = db.relationship('Role', secondary='user_roles')
# Define the role data-model
class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(50), unique=True)

# Define the UserRoles association table
class UserRoles(db.Model):
  __tablename__ = 'user_roles'
  id = db.Column(db.Integer(), primary_key=True)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
  role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

# Setup Flask-User and specify the User data-model
user_manager = UserManager(app, db, User)

# Create all database tables
db.create_all()

# Create 'hl' user with no roles
if not User.query.filter(User.username == 'hl').first():
    user = User(
        username='hl',
        username_confirmed_at=datetime.utcnow(),
        password=user_manager.hash_password('Password1'),
    )
    db.session.add(user)
    db.session.commit()

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

# @app.route("/login")
# def login():
#   return render_template("login_register.html")

@app.route("/bot")
@login_required
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