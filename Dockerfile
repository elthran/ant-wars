FROM python:3.7-alpine

WORKDIR /ant-wars
RUN apk add --no-cache gcc musl-dev linux-headers
# https://nickjanetakis.com/blog/docker-tip-9-installing-popular-packages-on-alpine
# mariadb-dev == default-libmysqlclient-dev
# build-base == build-essentials
RUN apk add  --no-cache --virtual build-dependencies \
    build-base \
    mariadb-dev
# RUN apk add --no-cache mariadb-connector-c-dev
RUN apk add --no-cache bash
# RUN echo "If you want pip to install faster in testing run: bin/pip-cache-downloads.sh first."
# allows docker to use requirement caching
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# RUN apk del build-dependencies
COPY . .
CMD ["flask", "run"]
# CMD ["exec", "$@"]
