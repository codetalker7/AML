# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

ENV FLASK_DEBUG=1

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
RUN python3 -m textblob.download_corpora

COPY prepare_functions.py prepare_functions.py 
COPY score.py score.py
COPY app.py app.py
COPY bow_transformer.pickle bow_transformer.pickle
COPY mlruns mlruns

CMD ["python3", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0"]
