FROM python:3.7.3-slim

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app