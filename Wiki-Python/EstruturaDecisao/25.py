"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
 O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
 Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
 entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
print("######################################################")
print("Responda as perguntas : ")
print("1/Sim  0/Nao")
r1 = int(input("Telefonou para a vítima?"))
r2 = int(input("Esteve no local do crime?"))
r3 = int(input("Mora perto da vítima?"))
r4 = int(input("Devia para a vítima?"))
r5 = int(input("Já trabalhou com a vítima?"))

sr=r1 + r2 + r3 + r4 + r5
if sr == 2:
    print ("Suspeito")
if sr >=3 and sr <=4:
    print ("Cumplice")
if sr ==5 :
    print ("inocente")
else:
    print ("inocente ...")
