#!/bin/bash

# Install apt dependencies
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv 

# Test frontend
cd frontend
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing
python3 -m pytest --cov=application  --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..

# Test backend1
cd backend1
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing
python3 -m pytest --cov=application  --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..

# Test backend2
cd backend2
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing
python3 -m pytest --cov=application  --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..



# Test backend3
cd backend3
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing
python3 -m pytest --cov=application  --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..
