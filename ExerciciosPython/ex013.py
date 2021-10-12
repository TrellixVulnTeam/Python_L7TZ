salario = float(input('Digite o salario : R$'))
aumento = float(input('Digite o aumento : '))
novos = salario + (salario*aumento/100)
print ('O salario de {} com aumento de {} ficara em {}'.format(salario,aumento,novos))