#!/bin/sh

while true; do sleep 15 ; snmpget -v2c -c public 192.168.0.8 sysDescr.0; done