FROM python:3.6-slim

COPY . /root

#RUN mkdir -p /data/files/
WORKDIR /root

#RUN pip install flask gunicorn
#RUN apt-get update && apt-get install -y libgtk2.0-dev
RUN pip install -r requirements.txt
RUN pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz

