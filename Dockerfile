# FROM ubuntu:18.04
FROM python:3.8

RUN apt-get update && apt-get install python3 && python -m pip install --upgrade pip

COPY . /app
# RUN pip install -r /app/requirements.txt
RUN apt-get install pkg-config libxml2-dev libxmlsec1-dev libxmlsec1-openssl -y
RUN pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
RUN pip install rasa[spacy]
RUN chmod u+r+x ./app/start_service.sh
CMD ["./app/start_service.sh"]