from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='Market Management', template_mode='bootstrap3')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config["SECRET_KEY"] = "fa3453722a1cefec27f0472e"

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from market import routes


