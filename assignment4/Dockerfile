# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY prepare_functions.py prepare_functions.py 
COPY score.py score.py
COPY app.py app.py
COPY mlruns/ mlruns/

CMD ["python3", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0"]
