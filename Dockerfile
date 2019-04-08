FROM python:3.7-alpine
MAINTAINER Ainazar

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN rm -rf /src
COPY ./src /src
WORKDIR /src
RUN pip install django-crispy-forms



RUN adduser -D user
USER user
