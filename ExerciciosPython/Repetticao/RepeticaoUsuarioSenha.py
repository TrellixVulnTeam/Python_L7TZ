nome = str(input('Digite o nome : ')).strip().upper()
senha = str(input('Digite sua senha : ')).strip().upper()
while senha == nome :
    print ('nome e senha não podem ser iguais ')
    nome = str(input('Digite o nome : ')).strip().upper()
    senha = str(input('Digite sua senha : ')).strip().upper()