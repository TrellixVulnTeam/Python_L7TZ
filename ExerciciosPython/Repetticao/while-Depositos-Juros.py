di = float(input ('Déposito inicial : '))
tj = float(input ('Digite a taxa de juros : '))
mes = 1
saldo = di
while mes <= 24:
    saldo = saldo + (saldo *(tj/100))
    print ("o saldo do mes %d é de R$%5.2f." % (mes, saldo))
    mes = mes + 1
print ("o ganho obtido com o juros foi de R$%8.2f." % (saldo - di))