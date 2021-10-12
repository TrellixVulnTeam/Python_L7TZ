import socket
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for host in range(9, 12):
    portas = open('portas.txt', 'r')
    vulnerabilidades = open('vulnerabilidades.txt', 'r')
    for port in portas:
             try:
                    socket.connect(( str(sys.argv[1]+'.'+str(host)), int(port) ))
                    print 'Conectado : '+str(sys.argv[1]+'.'+str(host))+' na porta: '+str(port)
                    socket.settimeout(2)
                    banner = socket.recv(1024)
                    for vulnbanners in vulnerabilidades.strip():
                        if banner.strip() in vulnbanners.strip():
                            print 'you have a winner' + banner
                            print 'host :'+str(sys.argv[1]+'_'+str(host))
                            print 'porta :' +str(port)
             except :
                    print 'erro na conexao : ' +str(sys.argv[1]+'.'+str(host)) + ':'+ str(port)

                    pass