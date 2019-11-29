FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-dev build-essential libxml2-dev libxslt1-dev libffi-dev graphviz libpq-dev libssl-dev redis-server zlib1g-dev

ADD . /opt/netbox

WORKDIR /opt/netbox

RUN pip3 install -r requirements.txt

RUN pip3 install napalm

WORKDIR /opt/netbox/netbox

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--insecure"]