prA=input("Digite um produto : ")
prB=input("Digite um produto : ")
prC=input("Digite um produto : ")
menor=prA
if prB < menor:
    menor = prB;
if prC < menor:
    menor = prC;
print("O menor produto para comprar : ", menor)

