from application import db
from datetime import datetime


class Predictions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    final_result = db.Column(db.String(100), nullable=False)