# docker-snmp

## Install: 
1. Download
```bash
  $ git clone https://github.com/PCarrascoDev/docker-snmp/
```
2. Build Client
```bash
  $ sudo docker build -t snmp-client ~/docker-snmp/client
```
3. Build Server
```bash
  $ sudo docker build -t snmp-server ~/docker-snmp/server
```
## Usage:
1. Start Client Daemon (SNMPD)
```bash
  $ sudo docker run -it -d -p 161:161/udp  snmp-client
```
2. Start Server Daemon, pointing to the agent address
```bash
  $ sudo docker run -it -p 161:161/udp  snmp-server AGENT_IP_ADDRESS
```

## Local machine usage:
1. Start Client Daemon on local docker network
```bash
  $ sudo docker run -it -d --network="host" snmp-client
```
2. Start Server Daemon on local docker network, pointing to localhost
```bash
  $ sudo docker run -it --network="host" snmp-server localhost
```
