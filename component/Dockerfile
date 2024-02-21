FROM quay.io/devfile/universal-developer-image:ubi8-latest

USER root

ENV PYENV_ROOT=/home/user/.pyenv

ENV VENV_PATH=/projects/pyhipster-devspace/app/.venv

RUN dnf -y install openssl-devel bzip2-devel libffi-devel

ENV PATH=$PATH:$PYENV_ROOT/bin:$VENV_PATH/bin

WORKDIR /home/user

RUN curl https://pyenv.run | bash

RUN pyenv install 3.10

RUN chown 10001:0 ${PYENV_ROOT} && chgrp -R 0 ${PYENV_ROOT} && chmod -R g=u ${PYENV_ROOT}

RUN pip install poetry

RUN npm install -y -g npm@8.11.0

RUN npm install -y -g generator-pyhipster

USER 10001