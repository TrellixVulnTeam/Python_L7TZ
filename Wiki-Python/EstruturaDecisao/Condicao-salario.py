sal = float(input('Digite o salario do colaborado : '))
if sal <= 280:
    aumento = (sal * 20)/100
    nsal = sal + aumento
    print ('O salario antigo era de {} '.format(sal))
    print ('O percentual de aumento foi de 20%')
    print ('O valor do aumento foi de {} reais'.format(aumento))
    print ('o novo salario sera de {}'.format(nsal))
if sal > 280 and sal <= 700:
    aumento = (sal * 15)/100
    print ('o salario antigo era de {}'.format(sal))
    print ('o percentual de aumento foi de 15%')
    print('O valor do aumento foi de {} reais'.format(aumento))
    print('o novo salario sera de {}'.format(nsal))
if sal > 700 and sal <= 1500:
    aumento = (sal * 10)/100
    print ('o salario antigo era de {}'.format(sal))
    print ('o percentual de aumento foi de 10%')
    print('O valor do aumento foi de {} reais'.format(aumento))
    print('o novo salario sera de {}'.format(nsal))
if sal > 1500:
    aumento = (sal * 5)/100
    print ('o salario antigo era de {}'.format(sal))
    print ('o percentual de aumento foi de 5%')
    print('O valor do aumento foi de {} reais'.format(aumento))
    print('o novo salario sera de {}'.format(nsal))