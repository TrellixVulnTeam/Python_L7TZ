'''
import socket
host = input("Alvo: ")
portas =[21,22,25,80,443,53,8080,9000,7001]
for porta in portas:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((host,porta))
    sock.close()
    if resultado == 0:
        print ("Portas abertas : ",porta)
'''
import socket
host = input("Alvo: ")
portas =[21,22,25,80,443,53,8080,9000,7001]
for porta in range(100):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((host,porta))
    sock.close()
    if resultado == 0:
        print ("Portas abertas : ",porta)