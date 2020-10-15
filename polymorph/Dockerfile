FROM ubuntu:latest
LABEL maintainer="pedro.carrascoc@mail.udp.cl"

ENV TZ=America/Santiago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    build-essential \
    python-dev \
    libnetfilter-queue-dev \
    tcpdump \
    python3-pip \
    git

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    tshark \
    wireshark

RUN pip3 install git+https://github.com/kti/python-netfilterqueue
RUN pip3 install polymorph

RUN apt-get install -y nano iptables
CMD [ "polymorph" ]