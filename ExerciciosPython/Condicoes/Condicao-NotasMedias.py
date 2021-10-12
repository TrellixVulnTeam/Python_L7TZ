n1 = float(input('Digite a primeira nota : '))
n2 = float(input('Digite a segunda nota : '))
m = (n1 + n2 )/2
if m <= 4 :
    print ('Média     : {}  '.format(m))
    print ('Conceito  : E')
if m > 4 and m <= 6 :
    print ('Media     : {}  '.format(m))
    print ('Conceito  : D')
if m > 6 and m <= 7.5 :
    print ('Media     : {}  '.format(m))
    print ('Conceito  : C')
if m > 7.5 and m <= 9 :
    print ('Media     : {}  '.format(m))
    print ('Conceito  : B')
if m > 9 and m <= 10 :
    print ('Media     : {}  '.format(m))
    print ('Conceito  : A')