#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
valido = False
dd=int(input("Digite um dia"))
mm=int(input("Digite um mes"))
aaaa=int(input("Digite um ano"))

if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    if (dd <=31):
        valido = True
if (mm==4 or mm==6 or mm==9 or mm==11):
    if (dd <=30):
        valido = True
if (mm==2):
    if (aaaa%4==0 and aaaa%100!=0) or (aaaa%400==0):
        if (dd<=29):
            valido = True
    else:
        if (dd <=28):
            valido = True
if (mm > 12):
    valido = False

if valido == True:
    print("A data é valida")
if valido == False :
    print("A data é invalida")

