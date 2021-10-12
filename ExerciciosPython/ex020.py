import random
a1 = str(input('Digite um nome : '))
a2 = str(input('Digite um nome : '))
a3 = str(input('Digite um nome : '))
a4 = str(input('Digite um nome : '))
Embaralhar = [a1,a2,a3,a4]
random.shuffle(Embaralhar)
print ('A ordem de apresentação sera : ')
print (Embaralhar)