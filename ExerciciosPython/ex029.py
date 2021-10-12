import time

velocidade = float(input('Velocidade do carro : '))
print ("Processando ...")
time.sleep(2)
vm = (velocidade-80) * 7
if velocidade > 80:
    print ('O Carro foi multado : ')
    print ('a valor da multa foi de R${:.2f}'.format(vm))
else:
    print ('Boa viagem, dirija com segurança')