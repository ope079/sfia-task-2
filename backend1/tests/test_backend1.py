import unittest
from flask import url_for
from flask_testing import TestCase
import unittest.mock
from unittest.mock import patch, mock_open, MagicMock, call
import io
import csv 
import builtins
import mock
import random
import numpy as np

from application import app
from application.routes import get_prediction1
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

d1 = pd.read_csv('/home/o_ore/sfia-task-2/backend1/tests/FB1.csv', header=0)
value = open('/home/o_ore/sfia-task-2/backend1/tests/FB1.csv', 'rb')

class TestResponse(TestBase):
    def test_get_pred(self):
        with patch('pandas.read_csv') as m:
            m.return_value = d1
            response = self.client.get(url_for("get_prediction1"))
            self.assertIn(b'{"response":[268.69,10.967697831802086,272.114249373302,271.07]}', response.data)

