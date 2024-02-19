FROM gitpod/workspace-python

RUN pyenv install 3.10 \
    && pyenv global 3.10

RUN pip install poetry sqlite-web

RUN npm install -y -g npm@8.11.0 \
    && npm install -y -g generator-pyhipster