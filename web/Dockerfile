FROM python:3.10-slim

WORKDIR /usr/src/app

# Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY ./core ./core
COPY ./diplomado ./diplomado
COPY ./facultades ./facultades
COPY ./programas ./programas
COPY ./static ./static
COPY ./templates ./templates
COPY ./usuarios ./usuarios
COPY manage.py .