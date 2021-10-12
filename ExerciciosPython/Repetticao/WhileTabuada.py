import time
print ('Tabuada de multiplicacao ')
time.sleep(2)
tb = int(input('Digite um numero : '))
x = 1
if tb < 11:
    while x <= 10:
        vr = tb * x
        print('{} * {} = {} '.format(tb , x, vr ))
        x = x + 1
else:
    print ('numero invalido')
    exit()