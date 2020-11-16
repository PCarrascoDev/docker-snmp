import pyshark
import numpy, scipy.io

#pyshark.packet.layer.Layer.get_field_by_showname()

capture = pyshark.FileCapture('netemtest.pcap', display_filter='snmp')

requests = {}
responses = {}

packet_sizes = []

paquets_per_sec = {}

bytes_per_sec = {}

t_0 = float(capture[0].sniff_timestamp)
#last_req_time = 0
for index, packet in enumerate(capture):

    pkt_time = int(float(packet.sniff_timestamp) - t_0)
    if pkt_time in paquets_per_sec:
        paquets_per_sec[pkt_time] = paquets_per_sec[pkt_time] + 1
    else:
        paquets_per_sec[pkt_time] = 1 
        
    
    if pkt_time in bytes_per_sec:
        bytes_per_sec[pkt_time] = bytes_per_sec[pkt_time] + int(packet.length)
    else:
        bytes_per_sec[pkt_time] = int(packet.length)

    packet_sizes.append(int(packet.length))
    if 'UDP' in packet and 'SNMP' in packet and packet['UDP'].get_field_by_showname('Destination Port') == '161':
        #last_req_time = float(packet.sniff_timestamp)
        #print(last_req_time)
        requests[packet['SNMP'].get_field_by_showname('request-id')] = packet
    elif 'SNMP' in packet:
        responses[packet['SNMP'].get_field_by_showname('request-id')] = packet


lostpackets = []
delays = []
for key in requests:
    #print(requests[key]['SNMP'])
    if key in responses:
        delta_time = float(responses[key].sniff_timestamp) - float(requests[key].sniff_timestamp)
        delays.append(delta_time)
        lostpackets.append(True)
    else:
        lostpackets.append(False)


timestamps = list(paquets_per_sec.keys())
pkts = list(paquets_per_sec.values())

byte_count = list(bytes_per_sec.values())

scipy.io.savemat('result.mat', mdict={'delays': delays, 'sizes': packet_sizes, 'lostpackets': lostpackets, 'timestamps': timestamps, 'pkts': pkts, 'byte_count': byte_count})
#print(result)
capture.close()