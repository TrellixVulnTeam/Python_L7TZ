import time
print ('Tabuada de multiplicacao ')
time.sleep(2)
tb1 = int(input('Digite o primeiro numero : '))
tb2 = int(input('Digite o segundo numero : '))
tb = 1
if tb1 < 11 and tb2 > 0:
    while tb2 <= 10:
        vr = tb1 * tb2
        print('{} * {} = {} '.format(tb1 , tb2, vr ))
        tb2 = tb2 + 1
else:
    print ('numero invalido')
    exit()