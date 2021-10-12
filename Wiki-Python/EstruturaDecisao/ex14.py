n1 = float(input("Digite a nota 1 : "))
n2 = float(input("Digite a nota 1 : "))
media = ((n1+n2)/2)
print ("a primeira nota :", n1)
print ("A segunda nota  :", n2)
print ("Media : ", media)
if media >= 9 and media <=10:
    print("Conceito A ")
    print ("Aprovado")
    exit()
elif media >= 7.5 and media < 9:
    print("Conceito B ")
    print ("Aprovado")
    exit()
elif media >= 6 and media < 7.5:
    print("Conceito C ")
    print ("Aprovado")
    exit()
elif media >= 4 and media < 6:
    print("Conceito D ")
    print ("Reprovado")
    exit()
elif media >= 0 and media < 4:
    print("Conceito E ")
    print ("Reprovado")
    exit()
else :
    print ("Opção invalida")
