FROM gitpod/workspace-python

RUN pyenv install 3.10 \
    && pyenv global 3.10

RUN pip install poetry sqlite-web

