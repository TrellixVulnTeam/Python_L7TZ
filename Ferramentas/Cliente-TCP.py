import socket
import time

target="www.cafescooxupe.com.br"
port=443

##inicia um objeto do tipo socket
cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#recebe conexão porta,destino
dst = (target,port)

#conectar o cliente
cl.connect(dst)
print ("Conectado ao destino ...")
time.sleep(5)

#Enviando dados
msg="Connection done"
message=msg.encode()
cl.send (message);
#Receber alguns dados
resp = cl.recv(2048)
