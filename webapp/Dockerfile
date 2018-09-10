FROM python:3.5

ARG DJANGO_ENV

ENV PYTHONUNBUFFERED=1
ENV WEBAPP_DIR=/webapp

RUN mkdir $WEBAPP_DIR

WORKDIR $WEBAPP_DIR

ADD requirements/base.txt $WEBAPP_DIR/ 
ADD requirements/$DJANGO_ENV.txt $WEBAPP_DIR/

RUN pip install -r $DJANGO_ENV.txt
RUN apt-get update
RUN apt-get install -y vim-tiny
ADD . $WEBAPP_DIR/