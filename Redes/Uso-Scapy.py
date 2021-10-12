scapy = 
ls()
lsc()

pacotes = sniff()
pacotes.show()

>>> pacotes = sr(IP(dst="www.youtube.com.br")/TCP(dport=[(443)]))

packet = Ether()/IP(dst="www.google.com.br")/ICMP()/"*ABCD*"
packet.show()
sendp(packet) ###enviar pacotes para o destino
sendp(packet, loop=1, inter=1)
srp1(packet)
_.show()
_.summary()



pkts = sniff(iface="wlo1", count=3)
pkts[0]
pkts[1]
pkts[2]
wrpcap('teste.pcap', pkts)
readed = rdpcap('teste.pcap')
readed[0]
readed[1]
readed[2]
icmpPkts = sniff(iface="wlo1", filter="icmp", count=10)
icmpPkts[2]
icmpPkts = sniff(iface="wlo1", filter="icmp", count=10, prn=lambda x: x.summary())
icmpPkts[2]


conf
conf.route.addnet()



traceroute(["www.yahoo.com.br","www.google.com.br","www.dca.com.br"],maxttl=25)

sniff(filter="tcp and host 192.168.2.11 and port 80", count=20

sr1(IP(dst="192.168.2.11")/UDP()/DNS(rd=1,qd=DNSQR(qname="www.terra.com.br")))
