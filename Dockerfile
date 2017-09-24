FROM python:alpine

ADD . /src

WORKDIR /src

RUN pip install -r requirements.txt

CMD FLASK_APP=app/server.py python -m flask run

