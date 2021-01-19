FROM python:latest
copy . .
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT ["python3", "app.py"]