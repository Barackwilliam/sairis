FROM python:3.12.7-slim-bullseye
WORKDIR /app

#install system dependences
RUN apt-get update

#install dependences
RUN pip install --upgrade pip
COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app


ENTRYPOINT ["gunicorn", "ecommerce.wsgi", "-b", "0.0.0.0:8000"]

