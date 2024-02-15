FROM python:3.12

RUN mkdir /inventory_service

WORKDIR /inventory_service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /inventory

CMD gunicorn app:apppip install fastapi-admin