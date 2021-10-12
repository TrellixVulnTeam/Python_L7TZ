import socket
usuarios=["kelsey@cooxupe.com.br","admin@cooxupe.com.br","ti@cooxupe.com.br"]
alvo =input("Alvo :")
for usuario in usuarios:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((alvo,25))
    sock.recv(1024)
    sock.send("VRFY" + usuario + "\n")
    smtp_resultado = sock.recv(1024)
    sock.close()
    if "252" in smtp_resultado:
        print(usuario + "-> Valido")
    elif "550" in smtp_resultado:
        print(usuario + "-> usuario invalido")
    elif "503" in smtp_resultado:
        print("Servidor requer autenticacao")
        break
    elif "500" in smtp_resultado:
        print ("Comando VRFY nao suportado pelo servidor")
        break
    else:
        print ("Resposta do servidor : ", smtp_resultado)