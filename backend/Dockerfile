FROM python:3.11.4


RUN mkdir /app
WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt
CMD [ "python", "." ]