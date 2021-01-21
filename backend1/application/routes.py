from application import app
from flask import request, Response, jsonify
from json import dumps
import requests
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX



@app.route('/get_prediction1', methods=['GET', 'POST'])
def get_prediction1():
    url = "https://alpha-vantage.p.rapidapi.com/query"
    ticker =request.data.decode("utf-8")
    #ticker = "FB"
    querystring = {"function":"TIME_SERIES_DAILY","symbol":f'{ticker}',"outputsize":"compact","datatype":"csv"}
    headers = {
            'x-rapidapi-key': "12226b39a9mshfa23fe1cdb616ccp10fb0bjsnd8f20f98485c",
            'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
            }
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    

    f = open(f'{ticker}.csv', "w")
    f.write(response.text)
    f.close()
    
    
    df = pd.read_csv(f'{ticker}.csv', index_col=0, parse_dates=True)
    x = df['open']
    
    sd = x.std() 

    previous_price = x[-3:-2]
    current_price = x[-2:-1]

    model = ARIMA(x[ :-2], order=(5,1,2))
    model_fit = model.fit()

    prediction = model_fit.forecast()

    current_price = float(current_price)
    sd = float(sd)
    prediction = float(prediction)
    previous_price = float(previous_price)

    information = {'response' : [current_price, sd, prediction, previous_price]}

    return jsonify(information)
    