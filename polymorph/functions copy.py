#sudo docker run -it --privileged polymorph

def change_snmp_ver(packet):

    # Change snmp version
    try:
        if packet['UDP']['srcport'] == 161:
            packet['SNMP']['version'] = 3
            print("Success")
            return packet
    except:
        print("Error")
        return None

def change_snmp_community(packet):
    try:
        pass
    except:
        return None

