n1 = float(input("digite a primeira nota : "))
n2 = float(input("Digite a segunda nota : "))
m = (n1 + n1) / 2
print("sua media é :" ,m )
if m >= 7:
    print ("Aprovado")
    exit()
elif m < 7 :
    print ("Reprovado")
elif m == 7:
    print("Aprovado com distincao")