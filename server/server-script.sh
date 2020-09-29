#!/bin/sh

# echo Your container args are: "$@"
# echo "$1"
# echo "$2"

if [ $# -ne 0 ] 
then
    echo "Starting Admin SNMP daemon for agent on $1"
    echo "System description: " && snmpget -v2c -c public $1 sysDescr.0;
    while true; do 
        sleep 300 ;
        echo "System description: " && snmpget -v2c -c public $1 sysDescr.0; 
    done &

    while true; do
        sleep 60 ;
        echo "System status: " && snmpstatus -v2c -c public $1;
    done &

    while true; do
        sleep 3600 ;
        echo "SNMP Walk " && snmpwalk -v2c -c public $1 > snmpwalkout.txt ;
    done &

    while true; do
        sleep  10 ;
        echo "Network status " && snmpnetstat -v2c -c public $1 ;
    done &
else
    echo "Please specify IP Address of agent machine"
fi
