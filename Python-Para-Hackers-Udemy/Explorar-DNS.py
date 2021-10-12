import socket
dominio = input("Alvo : ")
brute = ["ns", "ns1", "ns2", "ns3", "ns4", "www", "ftp", "intranet", "mail"]

for nome in brute:
    DNS = nome+ "."+dominio
    try:
        print (DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass