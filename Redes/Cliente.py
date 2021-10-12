import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM) ###Defini a classe socket para receber endereços ipv4 e usar TCP
host = ''  ###127.0.0.1
porta = 8291 ###poderá ser qualquer porta

s.connect((host,porta))###aqui fazemos a conexão no servidor e no host
dados = s.recv(1024)###a variavel dados vai receber no máximo 1024 bytes
print(dados.decode('ascii'))###traduz a mensagem binária utlizando os caracteres ascii