# docker-snmp

<p align="center"><img height="200" src="https://raw.githubusercontent.com/PCarrascoDev/docker-snmp/master/.res/snmp.png"></p>

## About 
SNMP Agent Daemon and automated SNMP query generator Docker images based on Ubuntu.

## Overview

### SNMP
SNMP stands for "Simple Network Management Protocol". It is an application layer protocol that helps devices to communicate and send data of their status over the network. This data is in the form of variables (OID's) wich are organized in MIB's (management information bases). This variables describe the status, configuration and overall information of a device.
The usual architecture of SNMP is based on a client-server model, where the servers act like managers collecting data from the clients. In this scenario clients are called agents.

### docker-snmp Repository
This repository has the nesessary files to build the docker images for an SNMP Server (Manager) and a SNMPD Client (Agent). The client image runs an SNMP Daemon who listens for any incoming snmpget request from a server, and it responds with the requested data. On the other hand, the server image runs an automated bash script that sends various types of snmp requests over time to a desired agent ip address.

## Install:

### Prerequisites
* GIT -> https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
* Docker version 19.03.13 -> https://docs.docker.com/engine/install/
### Build
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
  $ sudo docker run -it -d -p 161:161/udp snmp-client
```
2. Start Server Daemon, pointing to the agent address. Replace AGENT_IP_ADDRESS
```bash
  $ sudo docker run -it -p 161:161/udp snmp-server AGENT_IP_ADDRESS
```
*Be sure to verify that port 161/udp is open on both devices, and not blocked by any firewall.
*As the client runs on the background, only expect visual output from the server daemon.

## Local machine usage:
1. Start Client Daemon on local docker network
```bash
  $ sudo docker run -it -d --network="host" snmp-client
```
2. Start Server Daemon on local docker network, pointing to localhost
```bash
  $ sudo docker run -it --network="host" snmp-server localhost
```
