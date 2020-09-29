FROM ubuntu:latest
LABEL maintainer="pedro.carrascoc@mail.udp.cl"

RUN apt-get update && apt-get install -y \
    snmp \
    snmp-mibs-downloader

COPY snmp.conf /etc/snmp