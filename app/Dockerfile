FROM python:3.8-slim-buster

SHELL ["/bin/bash", "-c"]

ENV APP_DIR=/opt/app

COPY requirements.txt $APP_DIR/requirements.txt
COPY setup.cfg $APP_DIR/setup.cfg
COPY setup.py $APP_DIR/setup.py

WORKDIR $APP_DIR

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m pip install -e .

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "-c"]
