from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
db = SQLAlchemy(app)


app.config['SECRET_KEY'] = getenv("SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{getenv("DATABASE_PASSWORD")}@10.116.0.3:3306/flaskdb'



from application import routes