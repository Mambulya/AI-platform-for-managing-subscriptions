FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 

WORKDIR /code

ENV PYTHONPATH=/code/src

COPY ./data /code/data
COPY ./src /code/src
COPY ./requirements.txt /code/requirements.txt
COPY ./.env /code/.env

RUN pip install --no-cache-dir -r /code/requirements.txt

CMD ["python3", "src/app/main.py"]