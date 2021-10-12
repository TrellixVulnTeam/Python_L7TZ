#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

n = int(input("Digite um valor  : "))
if n > 10 and n < 600:
    print ("pode sacar")
    cem = int(n /100)
    n = n -(cem*100)

    cinquenta = int(n/50)
    n = n -(cinquenta*50)

    dez = int(n/10)
    n = n -(dez*10)

    cinco = int(n/5)
    n = n-(cinco*5)

    um = n

    print("notas de cem : ", cem)
    print("Notas de cinquenta :", cinquenta)
    print("Notas de dez :", dez)
    print("Notas de cinco :", cinco)
    print("Notas de um :", um)

elif n > 600:
    print ("Saque indisponivel para este valor para comprar gangibrina")