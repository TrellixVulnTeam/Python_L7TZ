from scapy.all import *
host = input("Alvo : ")
portas = [21,22,25,80,113,443,8080]
pacote_ip_alvo = IP(dst = host)
pacote_tcp = TCP(dport=portas, flags="S")
pacote = pacote_ip_alvo/pacote_tcp
ans, unans = sr(pacote, inter=0.1, timeout=1)
print("Portas\tEstado")
for pacote_recebido in ans:
    print (pacote_recebido[1][IP].sport, \
    "\t", pacote_recebido[1][IP].sprintf("%flags%"))

'''
from scapy.all import *
host = input("Alvo : ")
portas = []
for cont in portas:
    portas.append(cont)
    print (portas[cont})
pacote_ip_alvo = IP(dst = host)
pacote_tcp = TCP(dport=portas, flags="S")
pacote = pacote_ip_alvo/pacote_tcp
ans, unans = sr(pacote, inter=0.1, timeout=1)
print("Portas\tEstado")
for pacote_recebido in ans:
    print (pacote_recebido[1][IP].sport, \
    "\t", pacote_recebido[1][IP].sprintf("%flags%"))
'''