import unittest
from flask import url_for, request, Response
from flask_testing import TestCase
from unittest.mock import patch, Mock

from application import app
from application.routes import get_prediction2
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_prediction2(self):
        with patch('random.randint') as m:
            m.return_value = 1000
            response = self.client.post(url_for("get_prediction2"), json={"price" : [7,7,7,7]})
            self.assertIn(b"1000", response.data)