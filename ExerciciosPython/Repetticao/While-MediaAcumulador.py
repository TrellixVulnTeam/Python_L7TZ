n = 1
soma = 0
while n <= 5:
    x = int(input('Digite o %d nnumero :' % n))
    soma = soma + x
    n = n + 1
print('Media : %5.2f' % (soma/5))