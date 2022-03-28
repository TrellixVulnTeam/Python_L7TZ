"""
:s - Texto (strings)
:d - inteiros
:f - float
:.(número)f - Quantidade de cadas decimais
:(caractere)(> ou < ou ^) (Quantidade)(Tipo -s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""



n1 = 10
n2 = 3
div = n1/n2
print ('{:.3f}'.format(div))
print ( f'{div:.2f}')

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')

nome = 'kelsey'
n_formatado = '{n:0<20}'.format(n=nome)
print(n_formatado)