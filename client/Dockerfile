FROM ubuntu:latest
LABEL maintainer="pedro.carrascoc@mail.udp.cl"

RUN apt-get update && apt-get install -y \
    git \
    gcc \
    libtool \
    make \
    libperl-dev \
    snmp

RUN git clone https://github.com/net-snmp/net-snmp

RUN cd net-snmp && \
    ./configure -q --with-defaults && \
    make && \
    make install

COPY snmpd.conf /etc/snmp
COPY snmp.conf /etc/snmp

RUN cp -R /usr/local/lib /usr

EXPOSE 161/UDP

CMD ["snmpd", "-f", "-c", "/etc/snmp/snmpd.conf"]
