import unittest
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
from io import StringIO
from csv import reader 
import builtins

from application import app
from application.routes import get_prediction1
import pandas as pd

class TestBase(TestCase):
    def create_app(self):
        return app



class TestResponse(TestBase):
    def test_get_pred(self):
        
        url = "https://alpha-vantage.p.rapidapi.com/query"
        ticker = "FB"
        querystring = {"function":"TIME_SERIES_DAILY","symbol":ticker,"outputsize":"compact","datatype":"csv"}
        headers = {
            'x-rapidapi-key': "12226b39a9mshfa23fe1cdb616ccp10fb0bjsnd8f20f98485c",
            'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
            }
        #response = requests.request("GET", url, headers=headers, params=querystring)

        
        csv = StringIO("""\
        date,open,close
        1,1,1
        1,1,1
        1,1,1""")
        
        
        
        with patch('requests.request') as m:
            m("GET", url, headers=headers, params=querystring).return_value.csv = 'test.csv'
            
            response = self.client.get(url_for('get_prediction1'))    
            self.assertIn(b'1', response.data)

                
                
            