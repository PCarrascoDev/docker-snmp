def remove_snmp_data(packet):
    try:
        if packet['UDP']['dstport'] == 161 || packet['UDP']['srcport'] == 161:
            packet['SNMP']['data'] = None
            print("Success")
            return packet
    except:
        print("Error")
        return None

