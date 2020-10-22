def change_snmp_community(packet):

    try:
        if packet['UDP']['srcport'] == 161:
            packet['SNMP']['community'] = None
            print("Success")
            return packet
    except:
        print("Error")
        return None
