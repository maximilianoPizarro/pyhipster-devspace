FROM registry.redhat.io/codeready-workspaces/plugin-java11-rhel8:latest

USER root

ENV PATH=$PATH/usr/bin

RUN yum -y module reset nodejs:10

RUN yum -y remove nodejs npm

RUN yum -y module enable nodejs:16

RUN yum install -y nodejs

WORKDIR /usr/bin

RUN dnf -y install wget yum-utils make gcc openssl-devel bzip2-devel libffi-devel zlib-devel xz-devel

RUN wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz && tar xzf Python-3.10.8.tgz

RUN cd Python-3.10.8 && ./configure --with-system-ffi --with-computed-gotos --enable-loadable-sqlite-extensions

WORKDIR /usr/bin/Python-3.10.8

RUN make -j ${nproc} && make altinstall

RUN rm /usr/bin/Python-3.10.8.tgz

RUN wget https://raw.githubusercontent.com/maximilianoPizarro/pyhipster-devspace/main/.bashrc

RUN source ~/.bashrc

RUN pip3.10 install poetry

RUN npm install -y -g npm@8.11.0

RUN npm install -y -g generator-pyhipster

WORKDIR /home/jboss

RUN chown -hR jboss "/home/jboss"
 
RUN chmod +x "/home/jboss"

USER 1001