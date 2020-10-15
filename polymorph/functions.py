def change_snmp_ver(packet):

    # Change snmp version
    try:
        if packet['UDP']['srcport'] == 161:
            packet['SNMP']['version'] = 2

    except:
        return None