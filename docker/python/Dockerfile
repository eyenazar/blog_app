FROM python:3.6
MAINTAINER Ainazar

ENV PYTHONUNBUFFERED=1
ENV COLUMNS=200

COPY ./django_project /django_project
WORKDIR /django_project

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]




