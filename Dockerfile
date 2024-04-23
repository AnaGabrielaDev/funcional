FROM python:3.8-slim-buster

RUN apt-get update && apt-get upgrade -y && apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip3 install pydevd-pycharm~=203.7148.72
RUN pip3 install mysql-connector-python
RUN pip3 install watchdog[watchmedo]

WORKDIR /app

COPY . /app

CMD watchmedo auto-restart -d /app -p '*.py' -- python3 src/index.py
