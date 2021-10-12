#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

print ("Programa que verifica se o ano pe bissexto ")
ano = int(input("Digite um ano"))
if (ano % 4 == 0 ):
    if (ano % 100 != 0):
        print ("O ano é bissexto")
if  (ano % 4 != 0):
    if (ano %  400 != 0):
        print ("O ano não será bissexto e caiu na seguna verificação")
if (ano % 400 == 0):
        print("A ano é bissexto, terceira verificação")