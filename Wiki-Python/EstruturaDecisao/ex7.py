n1=float(input("Digite um número : "))
n2=float(input("Digite um numero : "))
n3=float(input("Digite um numero : "))
maior = n1
menor = n1
if n2 > maior:
    maior = n2;
# noinspection PyInterpreter
if n2 < menor:
    menor = n2;
if n3 > maior:
    maior = n3;
if n3 < menor:
    menor = n3
print("o maior é", maior)
print("o menor e ",menor)

