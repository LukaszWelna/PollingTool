# Dockerfile
FROM python:3.10.8

ADD main.py exceptions.py utilities.py ./server tests* .env requirements.txt ./

RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/server/"

CMD [ "python", "-m", "uvicorn", "main:app", "--reload" ]



