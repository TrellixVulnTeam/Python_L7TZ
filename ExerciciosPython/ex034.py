import time

print ('olá...')
time.sleep(1)
sal = float(input('Digite seu salario : '))
if (sal > 1250):
    saln = (sal * 10)/100
    sal = sal + saln
    print ('seu salario sera de R${:.2f}'.format(sal))
else:
    saln = (sal *15)/100
    sal = saln +sal
    print ('Seu salario sera  de R${:.2f}'.format(sal))