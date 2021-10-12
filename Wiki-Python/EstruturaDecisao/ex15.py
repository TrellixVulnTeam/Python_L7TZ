import time
l1=int(input("Digite o primeiro lado : "))
l2=int(input("Digite o segundo lado : "))
l3=int(input("Digite o terceiro lado : "))
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;
if (l1 + l2 > l3) or (l1 + l3 > l2) or (l2 + l3 > l1):
    print ("Forma um triangulo : ")
    print ("###avaliando o tipo de triangulo : ")
    if (l1 == l2) and (l1 == l3) and (l2 == l3):
        print (" Triangulo Equilátero ")
    elif (l1 == l2) or (l1 == l3) or (l2 == l3):
        print (" Triangulo Isosceles ")
    elif (l1 != l2) and (l1 != l3) and (l2 != l3):
        print (" triangulo Escaleno")
exit()
