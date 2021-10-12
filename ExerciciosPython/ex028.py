import random
import time
print ("####Processando numeros aleatorios #####")
n = random.randint(0,5)
user = int(input('Adivinhe o número ! '))
print ('Processando ... ')
time.sleep(3)
print ('#####Verificando numero ! ####')
if user == n:
    print ('Acertou, adivinhei esse numero !')
else:
    print ('Tente outra vez')
print ('o numero que eu pensei foi {}'.format(n))
if user > 6:
    print ('numero invalido')

