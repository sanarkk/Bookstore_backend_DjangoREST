FROM python:3.10
MAINTAINER sanarkk

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend-bookstore-drf

COPY ./requirements.txt .

ENV SECRET_KEY=django-insecure-d3v_^&h1x6v-%#ab!(s**sw4k6j^@@mb%6dk$iszc(ms^1%ymc
ENV DEBUG=True
ENV HOST=db
ENV NAME=bookstore_db
ENV USERNAME=bookstore_user
ENV PASSWORD=bookstore_user_/1


RUN pip install -r requirements.txt

COPY . .