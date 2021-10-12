import math
a = int(input('Digite o primeiro valor : '))
if a == 0 :
    print ('A equacao não é do segundo grau :')
    exit()
b = int(input('Digite o segundo valor : '))
c = int(input('Digite o terceiro valor : '))
delta = (b*b)-(4*a*c)
if delta < 0 :
    print ('o valor do delta é {}. A equação não possui raizes reais'.format(delta))
print (delta)
if delta == 0:
    raiz = (-1 *b + math.sqrt(delta))/(2*a)
    print ('A raiz da equacao é {}'.format(raiz))
if delta > 0 :
    raiz1 = (-1 * b + math.sqrt(delta))/(2*a)
    raiz2 = (-1 * b - math.sqrt(delta))/(2*a)
    print ('as raizes da equacao são {} e {}'.format(raiz1,raiz2))