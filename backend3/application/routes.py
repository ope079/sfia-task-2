from application import app
from flask import request, jsonify
import requests




@app.route('/final_result', methods=['GET', 'POST'])
def get_final_result():
    predict_data = request.json["price"]
    prediction1 = float(predict_data[0])
    prediction2 = float(predict_data[1])
    current_price = float(predict_data[2])
    previous_price = float(predict_data[3])

    if (current_price > previous_price):
            real_state = "buy" 
    else:
            real_state = "sell"
    
    if (prediction1 > previous_price):
            time_series_state = "buy" 
    else:
            time_series_state = "sell"

    if (prediction2 > previous_price):
            random_state = "buy" 
    else:
            random_state = "sell"
    final_result = {"Current price movement" : f"{real_state} at actual price {current_price}", 
    "Time series advice" : f"{time_series_state} at price {prediction1}", 
    "Random advice" : f"{random_state} at price {prediction2}", 
    "Previous price" : f"{previous_price}"}

    return jsonify(final_result)