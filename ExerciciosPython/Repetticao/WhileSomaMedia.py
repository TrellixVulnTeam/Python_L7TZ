x = 1
soma = 0
while x < 5:
    n = int(input("Digite o numero {}".format(x)))
    soma = soma + n
    print ("o valor da soma é {}".format(soma))
    x = x +1
print ("A media da soma é : ".format(soma/x))