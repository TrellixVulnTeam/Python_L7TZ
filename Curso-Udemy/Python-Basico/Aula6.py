'''
variavéis
'''

nome = str(input("Insira seu nome : "))
idade = int(input("Insira sua idade : "))
peso = float(input("Digite seu peso : "))
altura = float(input("Digite sua altura"))


imc = peso/altura**2

print(nome , 'tem ' , idade , ' anos de idade. Seu IMC é ', float(imc))



