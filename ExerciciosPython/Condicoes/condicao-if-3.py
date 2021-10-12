n1 = int(input ('Digite um numero : '))
n2 = int(input ('Digite um numero : '))
n3 = int(input ('Digite um numero : '))
if n1 > n2 and n1 > n3:
    print ('o numero {} e maior '.format(n1))
if n2 > n1 and n2 > n3:
    print ('o numero {} e maior '.format(n2))
if n3 > n1 and n3 > n2 :
    print ('o numero {} é maior '.format(n3))
if n1 == n2 ==n3:
    print ('os numeros {} {} {} são iguais'.format(n1,n2,n3))
if n1 == n2 :
    print ('os numero {} {} sao iguais'.format(n1,n2))
if n1 == n3 :
    print('os numero {} {} sao iguais'.format(n1, n3))
if n2 == n3 :
    print('os numero {} {} sao iguais'.format(n2, n3))