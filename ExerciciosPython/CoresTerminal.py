print ('\033[31;m cor vermelha')
print ('\033[7;30;m o caracter 7 inverte tudo')
print ('\033[0;33;44;m fundo padrao com letra amarela com fundo azul')
print ('\033[7;33;44;m fundo padrao com letra amarela com fundo azul invertido')
print ('\033[4;31;46;m letras sublinhadas com cor vermelha com fundo ciano')
print ('\033[4;31;46;m letras sublinhadas com cor vermelha com fundo ciano com limite na contra-barra \033[m')
print ('\033[4;30;45;m texto sublinhado com letra branca com fundo lilás com limite de barra \033[m')
a = 3
b = 4
print ('Os valores são \033[1;35;m{} e {} \033[m'.format(a,b))

nome = str(input('Digite o nome : '))
print('Seu nome é \033[7;30;47;m {} \033[m; : '.format(nome))

nome = str(input('Digite um nome : '))
print ('Seu nome  {}{}{}: '.format('\033[33m',nome,'\033[m'),)

