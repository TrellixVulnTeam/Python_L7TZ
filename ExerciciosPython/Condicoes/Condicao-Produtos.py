import time
p1 = float(input("Digite o preço do primeiro produto :"))
p2 = float(input('Digite o preço do segundo produto :'))
p3 = float(input("Digite o preço do terceiro produto :"))
print ("Verificando ........")
time.sleep(2)
if (p1 < p2) and  p3:
    print ('o primeio produto com valor de {} é mais barato'.format((p1)))
if (p2 < p1) and p3:
    print ('o segundo produto com valor de {} e mais barato'.format((p2)))
if (p3 < p2) and p1:
    print ('o terceiro produto com valor de {} é mais barato'.format(p3))