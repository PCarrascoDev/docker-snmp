def random_snmp_request(packet):
    try:
        if packet['UDP']['dstport'] == 161:
            packet['SNMP']['data'] = "0xa11d02044c6534e9020100020100300f300d06092b06010201070701080500"
            print("Successfully injected new data")
            return packet
    except:
        print("Error")
        return None
