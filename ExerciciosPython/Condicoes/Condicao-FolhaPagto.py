hr = float(input ('Digite a quantidade de horas trabalhadas durante o mês : '))
vh = float(input('Digite o valor da hora : '))
sal = hr * vh
print (sal)
if sal <= 900:
    print ('Salário Bruto        : {} '.format(sal))
    IR = 0
    print ('(-) IR (0%)          : Esta isento de IR')
    INSS = (sal * 8)/100
    print ('(-) INSS (8%)        : Desconto INSS {} :'.format(INSS))
    FGTS = (sal * 11)/100
    print ('FGTS (11%)           : Valor depositado pelo empresa {}'.format(FGTS))
    ds = (IR + INSS)
    print ('descontos          {}:  '.format(ds))
    sall = (sal - ds)
    print ('salario Liquido    {}:  '.format(sall))
if sal <= 1500:
    print('Salário Bruto        : {} '.format(sal))
    IR = (sal * 5)/100
    print('(-) IR (0%)          : Esta isento de IR')
    INSS = (sal * 9) / 100
    print('(-) INSS (9%)        : Desconto INSS {} :'.format(INSS))
    FGTS = (sal * 11) / 100
    print('FGTS (11%)           : Valor depositado pelo empresa {}'.format(FGTS))
    ds = (IR + INSS)
    print('descontos          {}:  '.format(ds))
    sall = (sal - ds)
    print('salario Liquido    {}:  '.format(sall))
if sal <=2500:
    print('Salário Bruto        : {} '.format(sal))
    IR = (sal * 10)/100
    print('(-) IR (10%)          : Esta isento de IR')
    INSS = (sal * 11) / 100
    print('(-) INSS (11%)        : Desconto INSS {} :'.format(INSS))
    FGTS = (sal * 11) / 100
    print('FGTS (11%)           : Valor depositado pelo empresa {}'.format(FGTS))
    ds = (IR + INSS)
    print('descontos          {}:  '.format(ds))
    sall = (sal - ds)
    print('salario Liquido    {}:  '.format(sall))