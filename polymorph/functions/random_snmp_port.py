def random_snmp_port(packet):
    import random
    try:
        if packet['UDP']['srcport'] == 161:
            rand_n = random.randint(1000, 26000)
            packet['UDP']['dstport'] = rand_n
            print("Changed destination port to: " + str(rand_n))
            return packet
    except:
        print("Error")
        return None
