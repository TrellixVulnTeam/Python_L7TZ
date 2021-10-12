n1 = float(input('Digite a primeira media'))
n2 = float (input('Digite a segunda media'))
m = (n1 + n2)/2
print ('media {:.2f}'.format(m))
if m >= 6.0:
    print ('aprovado')
else:
    print ('Volte para fazer uma nova prova')