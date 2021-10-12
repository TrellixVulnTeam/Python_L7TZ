nome = input("Digite seu nome inteiro : ").strip()
maiuscula = nome.upper()
print ("O nome em maiusculo ficara : ", maiuscula)
minuscula = nome.lower()
print ("O nome em minusculo ficara :", minuscula)
quantidade = (len(nome) - nome.count(' '))
print ("A quantidade de caracteres do nome  digitidado é :", quantidade)
dividido = (nome.split())
print ("frase dividida : ", dividido)
print ("A quantidade de letras do primeiro nome é : ",len(dividido[0]))
primeiroNome = (nome.find(' '))
print ("A quantidade de letras do primeiro nome é : ", primeiroNome)

######
