from application import app, db
from application.forms import Form
from application.models import Predictions 
from flask import render_template, request, redirect, url_for
import requests
import json

'''
@app.route('/')
def home():
    form = Form()
    #final_results = Predictions.query.limit(5).all
    return render_template("index.html", title="Home", form=form)
'''

@app.route('/', methods=['GET', 'POST'])
def post_prediction():
    form = Form()
    ticker = form.ticker.data
    price_prediction = requests.get('http://backend1:5001/get_prediction1', data=ticker).json()
    #price_prediction = json.loads(price_prediction)
    current_price = price_prediction['response'][0]
    sd = price_prediction['response'][1]
    price_list = [current_price, sd]
    prediction1 = price_prediction["response"][2]
    previous_price = price_prediction["response"][3]
    prediction2 = requests.get('http://backend2:5002/get_prediction2', json={"price":price_list})
    prediction2 = float(prediction2.json())
    final_result = requests.get('http://backend3:5003/final_result', json= {"price":[prediction1,prediction2,current_price,previous_price]})
    new_prediction = Predictions(final_result=str(final_result.json()))
    db.session.add(new_prediction)
    db.session.commit()
    return redirect(url_for("home", final_results = final_results, form = Form()))



@app.route('/get_prediction', methods=['GET','POST'])
def get_prediction():
    form = Form()
    final_results = Predictions.query.limit(5).all()
    return render_template("predictions.html", final_results = final_results, form = Form())
