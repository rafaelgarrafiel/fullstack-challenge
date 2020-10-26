FROM python:3.8 AS build-env

COPY . /src
WORKDIR /src
USER root

RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt


ENV FLASK_ENV=development
ENV FLASK_APP=app.app:create_app

EXPOSE 5000

CMD flask run -h 0.0.0.0 -p 5000