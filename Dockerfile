FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /i-dont-speak-english
WORKDIR /i-dont-speak-english

COPY ./requirements.txt ./requirements.txt
COPY . ./i-dont-speak-english

RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt


ADD . /i-dont-speak-english