divida = float(input('Digite o valor inicial da divida : '))
taxa = float(input('Digite o valor inicial do juro : '))
pagamento = float(input('Digite o valor que sera mensalmente : '))
mes = 1
if (divida * (taxa/100) > pagamento):
    print("os Juros são maiores do que o pagamento atual    ")
else :
    saldo = divida
    juros_pagos = 0
    while saldo > pagamento:
        juros = saldo * taxa/100
        saldo = saldo + juros - pagamento
        juros_pagos = juros_pagos + juros
        print ("Saldo da divida no mes %d é de R$%6.2f" % (mes,saldo))
        mes = mes + 1
    print("Para pagar uma dívida de R$%8.2f, a %5.2f %% de juros," % (divida, taxa))
    print("você precisará de %d meses, pagando um total de R$%8.2f de juros." % (mes - 1, juros_pagos))
    print("No último mês, você teria um saldo residual de R$%8.2f a pagar." % (saldo))