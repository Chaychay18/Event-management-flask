from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///details.db'
app.config['SECRET_KEY']='hello'
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)
bcrypt= Bcrypt(app)
login_manager=LoginManager(app)


from applications import routes
