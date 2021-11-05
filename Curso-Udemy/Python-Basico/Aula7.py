"""
Formatação de strings
"""

nome = str(input("Insira seu nome : "))
idade = int(input("Insira sua idade : "))
peso = float(input("Digite seu peso : "))
altura = float(input("Digite sua altura"))


imc = peso/altura**2

print(nome , 'tem ' , idade , ' anos de idade. Seu IMC é ', float(imc))
print(f'{nome} tem {idade} anos de idade e seu imc : {imc}')
print('{} tem {} anos e seu imc : {}'.format(nome,idade,imc))
print('{0} tem {1} anos e seu imc : {2}'.format(nome,idade,imc))
print('{n} tem {i} anos e seu imc : {im}'.format(n=nome,i=idade,im=imc))