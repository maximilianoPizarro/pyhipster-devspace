FROM python:3.10
LABEL maintainer="maximiliano.pizarro.5@gmail.com"

RUN apt update && apt -y install nodejs && apt -y install npm

RUN mkdir /home/app
ADD app/. /home/app
ADD pyhipster.sh /home/app
WORKDIR /home/app

RUN chmod 777 /home/app/pyhipster.sh

ENV PATH=${PATH}:/home/app

RUN pip install poetry
RUN npm install
RUN poetry install

EXPOSE 9000 5000 9060 8080

ENTRYPOINT [ "/home/app/pyhipster.sh" ]
