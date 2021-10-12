#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
n1 = float(input("Digite um numero : "))
if (n1 == round(n1)):
    print(f'{int(n1)} é um numero inteiro ')
else:
    print(f'{n1} é um numero decimal ')