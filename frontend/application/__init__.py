from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)



app.config['SECRET_KEY'] = getenv("SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{getenv("DATABASE_PASSWORD")}@database:3306/flask-db'

db = SQLAlchemy(app)

from application import routes