from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired

class Form(FlaskForm):
    ticker = StringField('Enter stock ticker', validators=[DataRequired()])
    submit = SubmitField('Get the price')
