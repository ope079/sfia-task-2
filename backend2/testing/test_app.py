import unittest
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from application import app
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_prediction2(self):
        with patch('random.uniform') as m:
            price_list = [1,1]
            sd = (price_list[1])
            current_price = (price_list[0])
            m((current_price - sd),(current_price + sd)).return_value = 1
            response = self.client.get(url_for('get_prediction2'))
            self.assertIn(b"1", response.data)