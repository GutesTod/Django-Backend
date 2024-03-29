FROM python:3.12-slim AS build

WORKDIR /django_backend

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

FROM build AS migrations_init

RUN python manage.py makemigrations

FROM migrations_init AS migrate_make

RUN python manage.py migrate