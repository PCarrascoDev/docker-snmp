results = load('result.mat');

timestamps = result.timestamps;
pkts_per_seq = result.pkts;
bytes_per_seq = result.byte_count;

figure()

histogram(results.delays, 'Normalization', 'prob');
xlabel('Delay (Sec)')
ylabel('Probability');

figure()
histogram(results.sizes, 'Normalization', 'prob');
xlabel('Packet size (Bytes)');
ylabel('Probability');

C = categorical(result.lostpackets, [1 0], {'Arrived', 'Lost'});

figure()
histogram(C, 'Normalization','probability', 'BarWidth',0.5);
ylabel('Percentage %');
yticklabels(yticks*100);

figure()
histogram(pkts_per_seq, 'Normalization', 'prob');
xlabel('Packets/sec');
ylabel('Probability');

figure()
histogram(bytes_per_seq, 15,'Normalization', 'prob');
xlabel('Bytes/sec');
ylabel('Probability');
