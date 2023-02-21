# syntax=docker/dockerfile:1

FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3 python3-dev python3-pip
COPY requirements.txt /api/requirements.txt
WORKDIR ./listApp

RUN pip3 install -r requirements.txt
CMD ["uvicorn main:app"]