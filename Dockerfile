FROM python:3.10.5-slim

WORKDIR /code
COPY ./ ./

RUN pip install -U pip && \
     pip install -r requirements.txt

WORKDIR /code/src

EXPOSE 8000
