FROM alpine:3.13
LABEL maintainer = "Jean-François Giraud"

RUN apk update
RUN apk add --no-cache bash
RUN apk add --no-cache make
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
RUN apk add --no-cache pytest
RUN apk add --no-cache py3-beautifulsoup4
RUN apk add --no-cache py3-lxml
