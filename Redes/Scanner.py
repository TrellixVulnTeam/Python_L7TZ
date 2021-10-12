import nmap
import sys

N = nmap.PortScanner() ###variavel N recebe a classe PortScanner do nmap
 
###alvo = input("Alvo: ")####pega o que foi digitado na variavel alvo
###porta = input("Porta: ")####pega o que foi digitado na variavel porta
 
#######N.scan(alvo, porta) ### passa os parametro de alvo e porta para a classe scan
N.scan(sys.argv[1], sys.argv[2])###chama o modulo sys, passando os argumentos
print(N.scaninfo())###mostra informacoes de como o scan é feito
print(N.command_line())###mostra o comando utilizado para o escaneamento
for host in N.all_hosts():### o alvo fica nessa lista, no momento de execucao
    print("########################")
    print('[+]Host : %s (%s)' % (host, N[host].hostname()))###vai printar a variavel host concatenado com o hostname
    print('[+]State : %s' % N[host].state())###pega o estado de conexao do host, verifica se esta ativo ou nao
    for proto in N[host].all_protocols():###Verifica os protocolos das portas abertas
        print('########################')
        print('[+]Protocolo : %s' % proto)###aqui exibe os protocolos
        lport = N[host][proto].keys()###Crio uma variavel protocolo, dentro do laco for, passando pra essa variavel as portas abertas, sendo estas as portas abertas a chave do dicionario
        lport = list(lport)###Converte de dicionario para lista
        lport.sort()###ordena a lista
        for port in lport:###para cada porta que tiver dentro da variavel lport
            print ('[+]porta : %s\testado : %s' % (port, N[host][proto][port]['state']))###vai printar na tela o estada da porta(open ou closed)
 
 
'''
Podemos utilizar os seguinte comandos abaixo : 
N.command_line()
N.scaninfo()
N.all_hosts()
N[host].hostname()
N[host].state()
N[host].all_protocols()
N[host][proto].keys()
N[host].has_tcp(port)
N[host].has_tcp(port)
N[host][proto][port]
N[host][proto][port]['state']
 
'''
