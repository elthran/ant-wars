FROM python:3.7-alpine
WORKDIR /ant-wars
ENV PYTHONBREAKPOINT ipdb.set_trace
ENV FLASK_ENV=development
ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
# https://nickjanetakis.com/blog/docker-tip-9-installing-popular-packages-on-alpine
# mariadb-dev == default-libmysqlclient-dev
# build-base == build-essentials
RUN apk add  --no-cache --virtual build-dependencies \
    mariadb-dev \
    build-base \
    bc
RUN apk add --no-cache bash
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apk del build-dependencies
COPY . .
CMD ["flask", "run"]
# CMD ["exec", "$@"]
