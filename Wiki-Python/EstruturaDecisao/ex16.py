import math
print("### calculo equacao do segundo grau : ax² + bx + c")
delta = 0;
a=float(input("Digite o valor de A : "))
if a == 0:
    print("Coeficiente A : ")
    exit();
else:
    b=float(input("Coeficiente B : "))
    c=float(input("Coeficiente C : "))
    delta = b**2 - (4 * a * c)
    print("Valor delta : {}".format(delta))
    if delta < 0 :
        print("a equação não possui raizes reais ")
        exit();
    elif delta == 0:
        print ("Possui umaa raiz real, o delta é zero : ")
        raiz = -b / (2*a)
        print("a raiz é : {}".format(raiz))
    else:
        raiz1=(-b + math.sqrt(delta)) / (2 * a)
        raiz2=(-b + math.sqrt(delta) ) / (2*a)
        print("as raizes sao {} e {}".format(raiz1, raiz2))
        exit();


