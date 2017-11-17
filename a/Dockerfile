FROM python:alpine3.6

RUN apk update \
    && apk add --virtual build-dependencies \
        build-base \
        gcc \
        wget \
        git \
        librdkafka-dev \
    && apk add \
        bash

RUN pip install pipenv && mkdir app

WORKDIR app

COPY Pipfile* ./
RUN pipenv install .
COPY * ./
ENV PYTHONUNBUFFERED=0
ENTRYPOINT ["bash", "-c", "$(pipenv --venv)/bin/python3 component.py"]
