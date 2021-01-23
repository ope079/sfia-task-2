FROM python:latest
copy . .
RUN pip install -r requirements.txt
EXPOSE 5002
ENTRYPOINT ["python3", "app.py"]