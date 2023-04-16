FROM python:3.9-slim-buster

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ENV PYTHONPATH=$PYTHONPATH:/usr/src/app/

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt

COPY src /usr/src/app

CMD bash
