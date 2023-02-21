# syntax=docker/dockerfile:1

FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3 python3-dev python3-pip
COPY requirements.txt /listApp/requirements.txt
COPY . /listApp/
WORKDIR ./listApp

RUN pip3 install -r requirements.txt
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
