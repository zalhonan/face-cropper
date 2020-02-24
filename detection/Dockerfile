FROM python:3.7.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

ADD . /app/

EXPOSE 5000

# CMD flask run --host=0.0.0.0