FROM docker.io/ubuntu:14.04

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install git-core git wget unzip vim && \
    apt-get -y install python python-pip python-setuptools && \
    apt-get -y install python-numpy python-scipy python-matplotlib ipython

RUN pip install --upgrade pip

RUN pip install twisted[tls]
RUN pip install kademlia

RUN git clone https://github.com/h3dema/kademlia.git
RUN rm -fr /kademlia/kademlia
RUN apt-get install -y grep openssh-server
RUN files=`ls -p /kademlia | grep -v /` && \
    cd /kademlia && \
    rm -fr "$files" Makefile README* *.py LICENCE

EXPOSE 22
RUN mkdir -p /root/.ssh
COPY id_rsa /root/.ssh/id_rsa
COPY id_rsa.pub /root/.ssh/id_rsa.pub
COPY config /root/.ssh/config
RUN cd /root/.ssh/ && \
    cp id_rsa.pub authorized_keys && \
    chmod 600 *

EXPOSE 8468
CMD /etc/init.d/ssh start && /bin/bash

#
# docker build -t /kademlia github.com/h3dema/kademlia.docker
# docker run -w /kademlia -it kademlia
