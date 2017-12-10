FROM quay.io/russf/docker-py-base-image

RUN mkdir app
WORKDIR app
COPY Pipfile* ./
RUN pipenv install . && pipenv graph
COPY * ./
ENV PYTHONUNBUFFERED=0
CMD ["./entrypoint.sh"]