FROM registry.access.redhat.com/ubi8/python-39:1-168
LABEL maintainer="maximiliano.pizarro.5@gmail.com"

USER root

WORKDIR /opt/app-root/src

ADD app/. /opt/app-root/src
ADD pyhipster.sh /opt/app-root/src

RUN chmod 777 /opt/app-root/src/pyhipster.sh

RUN pip install poetry
RUN npm install
RUN poetry install

EXPOSE 9000 5000 9060 8080

ENTRYPOINT [ "/opt/app-root/src/pyhipster.sh" ]

USER 1001
