import time

n = int(input('Digite um numero : '))
print('Processando ...')
time.sleep(2)
if n % 2 == 0:
    print('Numero par')
else:
    print('Numero impar')