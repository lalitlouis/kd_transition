FROM tensorflow/tensorflow:latest

RUN apt-get update && apt-get install -y vim

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

COPY train_kserve.py /opt/

WORKDIR /app