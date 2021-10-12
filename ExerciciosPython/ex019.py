import random
a1 = str(input('Digite um nome : '))
a2 = str(input('Digite um nome : '))
a3 = str(input('Digite um nome : '))
a4 = str(input('Digite um nome : '))
lista =[a1, a2, a3, a4]
escolhido = random.choice(lista)
print ('O escolhido foi {}'.format(escolhido))