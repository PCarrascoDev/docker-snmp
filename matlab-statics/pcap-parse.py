import pyshark
import numpy, scipy.io

#Abrir la captura
capture = pyshark.FileCapture('netemtest.pcap', display_filter='snmp')


#Almacenamiento metricas
requests = {}
responses = {}

packet_sizes = []

packets_per_sec = {}

bytes_per_sec = {}

#Tiempo primer packet
t_0 = float(capture[0].sniff_timestamp)

for index, packet in enumerate(capture):

    
    pkt_time = int(float(packet.sniff_timestamp) - t_0)

    #Contar packets por cada segundo
    if pkt_time in packets_per_sec:
        packets_per_sec[pkt_time] = packets_per_sec[pkt_time] + 1
    else:
        packets_per_sec[pkt_time] = 1 
        
    #Sumar bytes de cada packet por cada segundo
    if pkt_time in bytes_per_sec:
        bytes_per_sec[pkt_time] = bytes_per_sec[pkt_time] + int(packet.length)
    else:
        bytes_per_sec[pkt_time] = int(packet.length)

    #Guardar el tamaño de cada packet
    packet_sizes.append(int(packet.length))

    #Almacenar cada request y response SNMP
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

    #Si la request tiene una response asociada, el packet no se perdió
    if key in responses:
        delta_time = float(responses[key].sniff_timestamp) - float(requests[key].sniff_timestamp)
        delays.append(delta_time)
        lostpackets.append(True)
    else:
        #Sino el packet se considera como perdido
        lostpackets.append(False)


#Ordenar datos en listas
timestamps = list(packets_per_sec.keys())
pkts = list(packets_per_sec.values())
byte_count = list(bytes_per_sec.values())

#Almacenar métricas en .mat para usar en matlab
scipy.io.savemat('result.mat', mdict={'delays': delays, 'sizes': packet_sizes, 'lostpackets': lostpackets, 'timestamps': timestamps, 'pkts': pkts, 'byte_count': byte_count})

capture.close()