from application import app
from flask import request, Response
import requests
import random



@app.route('/get_prediction2', methods=['GET', 'POST'])
def get_prediction2():
    price_list = request.json["price"]

    sd = (price_list[1]) * 100
    current_price = (price_list[0]) * 100
    random_price = random.randint((current_price - sd),(current_price + sd))
    return Response(str(random_price), mimetype='text/plain')


    




