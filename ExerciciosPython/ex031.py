import time
km = float(input('Digite a quilometragem que irá percorrer : '))
print ('processando !!!')
time.sleep(2)
if km <= 200:
    v = (km * 0.50)
    print ('O valor da passagem será de R${:.2f}'.format(v))
    print ('Boa viagem ')
else:
    if km > 200:
        v = (km * 0.45)
        print ('O valor da passagem será de R${:.2f}'.format(v))
print ('Boa viagem')