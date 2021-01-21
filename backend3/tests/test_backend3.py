import unittest
from flask import url_for
from flask import request, jsonify
from flask_testing import TestCase
from unittest.mock import patch

from application import app
from application.routes import get_final_result
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app


class TestFinalResult(TestBase):
     def test_final_result(self):
        predict_data = [4,4,4,4]
        prediction1 = 4
        prediction2 = 4
        current_price = 4
        previous_price = 4
        response = self.client.post(url_for('get_final_result'), json = {"price" : [prediction1,prediction2,current_price,previous_price]})
        self.assertIn(b'4' ,response.data)