import sys
nome = str(input('Digite o seu nome :')).strip()
idade = int(input('Digite a idade : '))
salario = float(input('Digite seu salario : '))
sexo = str(input('Digite o sexo : ')).strip()
EstCivil = str(input('Digite seu estado Civil : ')).strip()
while len(nome) < 3:
    nome = str(input('Digite o seu nome : ')).strip()
while idade > 150:
    idade = int(input('Digite sua idade : '))
while salario < 0:
    float(input('Digite seu salario : '))
while sexo.strip() != "f" or sexo.strip() !="m":
    sexo = str(input('Digite o sexo : '))
while EstCivil != 's' or EstCivil != 'c' or EstCivil != 'v' or EstCivil != 'd':
    EstCivil = str(input('Digite seu estado Civil : ')).strip()
