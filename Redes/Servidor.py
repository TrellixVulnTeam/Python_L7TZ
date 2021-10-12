import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM) ###Defini a classe socket para receber endereços ipv4 e usar TCP
host = ''  ###127.0.0.1
porta = 8291 ###poderá ser qualquer porta

msg = 'cliente conectado' ###Envia uma mensagem ap client

s.bind((host,porta)) #####colocar o servidor em escuta, pegando o host e a porta que deverão ficar ouvindo
s.listen(1) ###Quantas conexões simultaneas poderão ficar ouvindo

while True:###enquanto o servidor estiver ligado
    c, e = s.accept() ### a variaveis c (conexão) e e(endereço do cliente que vai se conectar) ficaram aceitando conexão
    print("conectado com ", e)###mostra qual ip se conectou com o servidor
    c.send(msg.encode('ascii'))####envia a mensagem para o cliente, porém temos que fazer o encoding.
    c.close()###podemos fechar o servidor