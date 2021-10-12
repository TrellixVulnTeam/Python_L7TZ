import ssl, socket
host = "www.google.com.br"
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockssl=ssl.wrap_socket(sock)
sockssl.connect((host,443))
sockssl.send("HEAD / HTTP/1.1\r\nHost:%s\r\n\r\n" %host)
print (sockssl.recv(1024))