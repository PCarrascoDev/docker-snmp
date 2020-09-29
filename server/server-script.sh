#!/bin/sh

while true; do 
    sleep 300 ;
    echo "System description: " && snmpget -v2c -c public 192.168.0.8 sysDescr.0; 
done &

while true; do
    sleep 60 ;
    echo "System status: " && snmpstatus -v2c -c public 192.168.0.8;
done &

while true; do
    sleep 3600 ;
    echo "SNMP Walk " && snmpwalk -v2c -c public 192.168.0.8 > snmpwalkout.txt ;
done 