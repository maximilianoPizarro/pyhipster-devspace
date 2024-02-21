FROM python:3.10
LABEL maintainer="maximiliano.pizarro.5@gmail.com"

RUN apt update && apt -y install nodejs && apt -y install npm

RUN mkdir /opt/app-root/src
ADD app/. /opt/app-root/src
ADD pyhipster.sh /opt/app-root/src
WORKDIR /opt/app-root/src

RUN chmod 777 /opt/app-root/src/pyhipster.sh

ENV PATH=${PATH}:/opt/app-root/src

RUN pip install poetry
RUN npm install
RUN poetry install

EXPOSE 9000 5000 9060 8080

ENTRYPOINT [ "/opt/app-root/src/pyhipster.sh" ]
