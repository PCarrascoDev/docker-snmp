def change_snmp_ver(packet):

    # Change snmp version
    try:
        if packet['UDP']['srcport'] == 161:
            new_ver = 3
            packet['SNMP']['version'] = new_ver
            print("Successfully changed version to " + str(new_ver))
            return packet
    except:
        print("Error")
        return None