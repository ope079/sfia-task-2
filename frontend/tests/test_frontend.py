import unittest
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from application import app, db
from application.models import Predictions
from application.routes import post_prediction, get_prediction
from os import getenv
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI= "sqlite:///",
            WTF_CSRF_ENABLED=False,
            DEBUG=True
        )
        return app
    
    def setUp(self):
        """
        Will be called before every test
        """
        db.create_all()

        final_result1 = Predictions(final_result="Current price movement: sell at actual price 1, Previous price: 2")
        final_result2 = Predictions(final_result="Current price movement: sell at actual price 3, Previous price: 4")
        final_result3 = Predictions(final_result="Current price movement: sell at actual price 5, Previous price: 6")
        final_result4 = Predictions(final_result="Current price movement: sell at actual price 7, Previous price: 8")
        final_result5 = Predictions(final_result="Current price movement: sell at actual price 9, Previous price: 10")

        db.session.add(final_result1)
        db.session.add(final_result2)
        db.session.add(final_result3)
        db.session.add(final_result4)
        db.session.add(final_result5)
        db.session.commit()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)

    def test_post_prediction(self):
        response = self.client.get(url_for('post_prediction'))
        self.assertEqual(response.status_code,200)
    
    def test_get_prediction(self):
        response = self.client.get(url_for('get_prediction'))
        self.assertEqual(response.status_code,200)   


class TestPost2(TestBase):
    def test_post_prediction1(self):
        with requests_mock.mock() as n:
            n.get('http://sfia-task-2_backend1:5001/get_prediction1', json={'response' : [7,7,7,7]})
            n.get('http://sfia-task-2_backend2:5002/get_prediction2', text="1")
            n.get('http://sfia-task-2_backend3:5003/final_result', json= {'Current price movement' : 'sell at actual price 7', 
    'Time series advice' : 'sell at price 7', 
    'Random advice' : 'sell at price 7', 
    'Previous price' : '7'})
            response = self.client.post(url_for('post_prediction'),follow_redirects=True)
            self.assertIn('{&#34;Current price movement&#34;: &#34;sell at actual price 7&#34;, &#34;Time series advice&#34;: &#34;sell at price 7&#34;, &#34;Random advice&#34;: &#34;sell at price 7&#34;, &#34;Previous price&#34;: &#34;7&#34;}', response.data.decode("utf-8"))


class TestGet(TestBase):    
    def test_get_predictions(self):
        response = self.client.get(url_for('get_prediction'))
        self.assertIn( b"Current price movement: sell at actual price 9, Previous price: 10", response.data)
        self.assertIn( b"Current price movement: sell at actual price 1, Previous price: 2", response.data)