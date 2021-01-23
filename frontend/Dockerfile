FROM python:latest
ARG APP_VERSION
copy . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENV APP_VERSION=${APP_VERSION}
ENTRYPOINT ["python3", "app.py"]