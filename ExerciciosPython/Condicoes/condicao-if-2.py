salario = float(input('Digite o salario :' ))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print ('salario : {} Imposto a pagar : {}'.format(salario,imposto))