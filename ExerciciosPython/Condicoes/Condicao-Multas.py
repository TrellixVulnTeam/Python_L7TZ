v = int(input('Qual a velocidade do carro : '))
vm = (v - 80) *5
if v > 80 :
    print('voce foi multado')
    print('voce foi multado em ',vm)
else:
    print ('não existe multa')