FROM python:3.9-alpine3.15

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN \
    apk add --no-cache python3 postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev libffi-dev

WORKDIR /app

# Python dependencies
COPY pyproject.toml pyproject.toml
USER root
RUN pip install poetry
RUN poetry config virtualenvs.create false
ADD . /app
RUN poetry install --no-dev

COPY . .

RUN export DJANGO_SETTINGS_MODULE=xepelin.settings

EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000
