def remove_snmp_data(packet):
    try:
        if packet['UDP']['dstport'] == 161 or packet['UDP']['srcport'] == 161:
            packet['SNMP']['data'] = "0x0"
            print("Removed data from packet")
            return packet
    except:
        print("Error")
        return None

