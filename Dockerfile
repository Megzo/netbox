ARG FROM=python:3.8.1-alpine3.11
ARG NETBOX_PATH=.
FROM ${FROM} as builder

RUN apk add --no-cache \
      bash \
      build-base \
      ca-certificates \
      cyrus-sasl-dev \
      graphviz \
      jpeg-dev \
      libevent-dev \
      libffi-dev \
      libxslt-dev \
      openldap-dev \
      postgresql-dev

WORKDIR /install

RUN pip install --prefix="/install" --no-warn-script-location \
# gunicorn is used for launching netbox
      gunicorn \
      greenlet \
      eventlet \
# napalm is used for gathering information from network devices
      napalm \
# napalm-ce is used for communicating with Huawei CE devices
      napalm-ce \
# ruamel is used in startup_scripts
      'ruamel.yaml>=0.15,<0.16' \
# django_auth_ldap is required for ldap
      django_auth_ldap \
# django-storages was introduced in 2.7 and is optional
      django-storages \
# required for CI tests	  
	  pycodestyle \
	  coverage
	  

COPY ${NETBOX_PATH}/requirements.txt /
RUN pip install --prefix="/install" --no-warn-script-location -r /requirements.txt

###
# Main stage
###

ARG FROM
FROM ${FROM} as main

RUN apk add --no-cache \
      bash \
      ca-certificates \
      graphviz \
      libevent \
      libffi \
      libjpeg-turbo \
      libressl \
      libxslt \
      postgresql-libs \
      ttf-ubuntu-font-family

WORKDIR /opt

COPY --from=builder /install /usr/local

ARG NETBOX_PATH
COPY ${NETBOX_PATH} /opt/netbox

COPY docker/configuration.docker.py /opt/netbox/netbox/netbox/configuration.py
COPY docker/gunicorn_config.py /etc/netbox/config/
COPY docker/nginx.conf /etc/netbox-nginx/nginx.conf
COPY docker/docker-entrypoint.sh /opt/netbox/docker-entrypoint.sh
COPY docker/startup_scripts/ /opt/netbox/startup_scripts/
COPY docker/initializers/ /opt/netbox/initializers/
COPY docker/configuration.py /etc/netbox/config/configuration.py

WORKDIR /opt/netbox/netbox

# Must set permissions for '/opt/netbox/netbox/static' directory
# to g+w so that `./manage.py collectstatic` can be executed during
# container startup.
# Must set permissions for '/opt/netbox/netbox/media' directory
# to g+w so that pictures can be uploaded to netbox.
RUN mkdir static && chmod g+w static media

ENTRYPOINT [ "/opt/netbox/docker-entrypoint.sh" ]

CMD ["gunicorn", "-c /etc/netbox/config/gunicorn_config.py", "netbox.wsgi"]

