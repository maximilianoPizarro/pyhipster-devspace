FROM quay.io/devfile/universal-developer-image:ubi8-latest

USER root

ENV PATH=$PATH/usr/bin

RUN pip install poetry

RUN npm install -y -g npm@8.11.0

RUN npm install -y -g generator-pyhipster

USER 1001