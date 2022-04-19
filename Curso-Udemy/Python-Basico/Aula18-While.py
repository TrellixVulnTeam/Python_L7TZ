"""
while True:
    nome = input("Digite seu nome : ")
    print(f'olá {nome}!')
print("Não sera exibido")
"""
"""
x = 0
while x <= 100:
    print(x)
    x = x + 1
print('Acabou, pois depois de 101 a condição fica false')
"""
"""
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1
print('Acabou, pois depois de 101 a condição fica false')
"""
"""
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break
    print(x)
    x = x + 1
print('Acabou, pois depois de 101 a condição fica false')
"""
"""
x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'x vale {x} e y vale {y}')
        y = y + 1
    x += 1
print("Acabou...")
"""

while True:
    print()
    n1 = input("Digite um numero : ")
    n2 = input("Digite um numero : ")
    operador = input("Digite um operador : ")


    if not n1.isnumeric() or not n2.isnumeric():
        print("Digite um numero ")
        continue

    n1 = int(n1)
    n2 = int(n2)

    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '/':
        print(n1 / n2)
    elif operador == '*':
        print(n1 * n2)

    sair = input("Deseja sair ? [s]im ou [n]ão: ")
    if sair == 's':
        break