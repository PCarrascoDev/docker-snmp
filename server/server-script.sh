#!/bin/sh

#Test for arguments
if [ $# -ne 0 ] 
then
    echo "Starting Admin SNMP daemon for agent on $1"
    echo "System description: " && snmpget -v2c -c public $1 sysDescr.0;

    #Request sysDescription every 5min
    while true; do 
        sleep 300 ;
        echo "System description: " && snmpget -v2c -c public $1 sysDescr.0; 
    done &

    #Request sysStatus every minute
    while true; do
        sleep 60 ;
        echo "System status: " && snmpstatus -v2c -c public $1;
    done &

    #Do a full snmp walk every hour
    while true; do
        sleep 3600 ;
        echo "SNMP Walk " && snmpwalk -v2c -c public $1 > snmpwalkout.txt ;
    done &

    #Request device network status every 10sec
    while true; do
        sleep  10 ;
        echo "Network status " && snmpnetstat -v2c -c public $1 ;
    done &

    #Update MIB's every 2 hours
    while true; do
        sleep  7200 ;
        echo "Updating MIB's... " && download-mibs ;
    done
else
    echo "Please specify IP Address of agent machine"
fi
