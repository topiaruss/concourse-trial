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
RUN pipenv install . && pipenv graph
COPY * ./
ENV PYTHONUNBUFFERED=0
CMD ["./entrypoint.sh"]