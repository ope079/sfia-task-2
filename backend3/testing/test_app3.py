import unittest
from flask import url_for
from flask import request
from flask_testing import TestCase
from unittest.mock import patch

from application import app
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app

