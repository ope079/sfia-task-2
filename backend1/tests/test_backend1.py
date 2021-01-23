import unittest
from flask import url_for
from flask_testing import TestCase
import unittest.mock
from unittest.mock import patch, mock_open, MagicMock, call

import random
import numpy as np

from application import app
from application.routes import get_prediction1
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

class TestBase(TestCase):
    def create_app(self):
        return app

d1 = pd.read_csv('/home/jenkins/.jenkins/workspace/sfia-task-2/backend1/tests/csv/FB1.csv', header=0)
value = pd.read_csv('/home/jenkins/.jenkins/workspace/sfia-task-2/backend1/application/csv/.csv', header=0)

class TestResponse(TestBase):
    def test_get_pred(self):
        with patch('pandas.read_csv') as m:
            ticker = "FB1"
            m.return_value = d1
            response = self.client.get(url_for("get_prediction1"))
            self.assertIn(b'{"response":[268.69,10.967697831802086,272.114249373302,271.07]}', response.data)

class TestResponseZero(TestBase):
    def test_get_pred_zero(self):
        with patch('pandas.read_csv') as m:
            ticker = "FB2"
            m.return_value = value
            response = self.client.get(url_for("get_prediction1"))
            self.assertIn(b'{"response":[0,0,0,0]}', response.data)

