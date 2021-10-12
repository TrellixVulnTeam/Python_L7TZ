#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal

n1 = float(input("Digite um numero : "))
n2 = float(input("Digite um numero : "))

print ("1 - soma")
print ("2 - divisao")
print ("3 - subtração")
print ("4 - multiplicação")
op = int(input("Digite a opcao : "))

if (op == 1):
    r=n1+n2
    print ("O resultado é ",r)
    if (r%2 ==0 ):
        print("par")
    else:
        print("impar")
    if (r >= 1):
        print("positivo")
    else:
        print("negativo")
    if (r == round(r)):
        print(f'{int(r)} inteiro ')
    else:
        print(f'{r} decimal ')
    exit()


if (op == 2):
    r=n1/n2
    print ("O resultado é ",r)
    if (r%2 ==0 ):
        print("par")
    else:
        print("impar")
    if (r >= 1):
        print("positivo")
    else:
        print("negativo")
    if (r == round(r)):
        print(f'{int(r)} inteiro ')
    else:
        print(f'{r} decimal ')
    exit()

if (op == 3):
    r=n1-n2
    print ("O resultado é ",r)
    if (r % 2 == 0):
        print("par")
    else:
        print("impar")
    if (r >= 1):
        print("positivo")
    else:
        print("negativo")
    if (r == round(r)):
        print(f'{int(r)} inteiro ')
    else:
        print(f'{r} decimal ')
    exit()

if (op == 4):
    r=n1*n2
    print ("O resultado é ",r)
    if (r % 2 == 0):
        print("par")
    else:
        print("impar")
    if (r >= 1):
        print("positivo")
    else:
        print("negativo")
    if (r == round(r)):
        print(f'{int(r)} inteiro ')
    else:
        print(f'{r} decimal ')
    exit()
