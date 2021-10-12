#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

n = input("Digite um numero : ")
n_str = str(n)
qt_n = len(n)
if (qt_n >=4):
    print ("Numero invalido ...")
    exit()
else:
    if qt_n == 3:
        centena = n_str[0:1]
        dezena = n_str[1:2]
        unidade = n_str[2:8]
        print (n_str+" = "+centena+" centenas, " +dezena+" dezenas e "+unidade+" unidades ")
    if qt_n == 2:
        dezena = n_str[0:1]
        unidade = n_str[1:2]
        print( n_str+" = "+dezena+" dezenas e " +unidade+" unidades")
    if qt_n == 1:
        unidade = n_str[0:1]
        print( n_str+ " = "+unidade+" unidades")
