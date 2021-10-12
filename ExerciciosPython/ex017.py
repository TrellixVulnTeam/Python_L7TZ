



'''co = float(input('Qual o comprimento do cateto oposto : '))
ca = float(input('Qual o comprimento do cateto adjacente : '))
h1 = (co**2 + ca**2)**(1/2)
print('a hipotenusa vai medir {:.2f}'.format(h1))'''

import math
co = float(input('Qual o comprimento do cateto oposto'))
ca = float(input('Qual o comprimento do cateto adjacente'))
h1 = math.hypot(co,ca)
print ('a hipotenusa vai medir {:.2f}'.format(h1))