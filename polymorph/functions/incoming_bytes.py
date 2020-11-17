def test(packet):
    import time
    ts = int(time.time())
    # your code here
    if not(hasattr(packet, 'last_time')):
        packet.global_var('last_time', ts)
    if not(hasattr(packet, 'byte_count')):
        packet.global_var('byte_count', 0)
    
    #print(packet['IP']['len'])
    delta_time = ts - packet.last_time
    if delta_time == 0 and packet['UDP']['dstport'] != 161:
        packet.byte_count = packet.byte_count + packet['IP']['len']
    else:
        print(str(packet.byte_count) + " bytes/sec")
        packet.byte_count = 0
    packet.last_time = int(time.time())
    # If the condition is meet
    return packet
