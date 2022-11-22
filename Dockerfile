# Dockerfile
FROM python:3.10.8

ADD main.py exceptions.py utilities.py tests* .env requirements.txt ./

COPY ./server ./server

RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]



