def change_snmp_community(packet):

    try:
        if packet['UDP']['srcport'] == 161:
            new_comm = None
            packet['SNMP']['community'] = new_comm
            print("Changed SNMP community to: " str(new_comm))
            return packet
    except:
        print("Error")
        return None
