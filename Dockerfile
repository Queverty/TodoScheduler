FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY backend /backend
WORKDIR /backend
EXPOSE 8000
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install -r /temp/requirements.txt
#FROM nginx:latest
#COPY nginx.conf /etc/nginx/conf.d/default.conf
RUN adduser --disabled-password service-user
USER service-user

