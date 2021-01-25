from application import app, db
from application.forms import Form
from application.models import Predictions 
from flask import render_template, request, redirect, url_for
from os import getenv
import requests
import json


@app.route('/')
def home():
    form = Form()
    result = Predictions.query.order_by(Predictions.id.desc()).limit(1).all()
    return render_template("index.html", title="Home", form=form, result=result, app_version=getenv("APP_VERSION"))


@app.route('/', methods=['GET', 'POST'])
def post_prediction():
    form = Form()
    ticker = form.ticker.data
    price_prediction = requests.get('http://sfia-task-2_backend1:5001/get_prediction1', data=ticker).json()
    #price_prediction = json.loads(price_prediction)
    current_price = price_prediction['response'][0]
    sd = price_prediction['response'][1]
    price_list = [current_price, sd]
    prediction1 = price_prediction["response"][2]
    previous_price = price_prediction["response"][3]
    prediction2 = requests.get('http://sfia-task-2_backend2:5002/get_prediction2', json={"price":price_list})
    prediction2 = int(prediction2.json())
    final_result = requests.get('http://sfia-task-2_backend3:5003/final_result', json= {"price":[prediction1,prediction2,current_price,previous_price]})
    new_prediction = Predictions(final_result= f"{ticker} -- {final_result.text}")
    db.session.add(new_prediction)
    db.session.commit()
    return redirect(url_for("home", form = form, app_version=getenv("APP_VERSION")))



@app.route('/get_prediction', methods=['GET','POST'])
def get_prediction():
    form = Form()
    final_results = Predictions.query.order_by(Predictions.id.desc()).limit(5).all()
    return render_template("predictions.html", final_results = final_results, form = form, app_version=getenv("APP_VERSION"))
