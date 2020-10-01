#!/bin/sh

#Test for arguments
if [ $# -ne 0 ] 
then
    if expr "$1" : '[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*$' >/dev/null || [ "$1" = "localhost" ]; then

        echo "Starting Admin SNMP daemon for agent on $1"
        echo "System description: " && snmpget -v2c -c public $1 sysDescr.0;

        #Request sysDescription
        while true; do 
            sleep 30 ;
            echo "System description: " && snmpget -v2c -c public $1 sysDescr.0; 
        done &

        #Request sysStatus
        while true; do
            sleep 20 ;
            echo "System status: " && snmpstatus -v2c -c public $1;
        done &

        #Do a full snmp
        while true; do
            sleep 50 ;
            echo "SNMP Walk " && snmpwalk -v2c -c public $1 > snmpwalkout.txt ;
        done &

        #Request device network status
        while true; do
            sleep  10 ;
            echo "Network status " && snmpnetstat -v2c -c public $1 ;
        done &

        #Update MIB's
        while true; do
            sleep  90 ;
            echo "Updating MIB's... " && download-mibs ;
        done &

        #Uptime
        while true; do
            sleep  40 ;
            echo "Uptime: " && snmpget -v2c -c public $1 hrSystemNumUsers.0 ;
        done  &

        #CPU Load
        while true; do
            sleep  60 ;
            echo "CPU Load: " && snmpwalk -v2c -c public $1 hrProcessorLoad.* ;
        done 

    else
    echo "Wrong agent address"

    fi

else
    echo "Please specify IP Address of agent machine"
fi
