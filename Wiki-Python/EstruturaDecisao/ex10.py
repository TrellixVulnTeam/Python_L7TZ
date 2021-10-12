print ("Digite o turno de estudo : ")
print ("digite : ")
print ("M - matutino")
print ("V - Vespertino")
print ("N - Noturno")
turno = input("Digite : ")
if turno == 'M' or turno == 'm':
    print ("O periodo é matutino")
    exit()
if turno == 'V' or turno =='v':
    print ("O periodo é vespertino")
    exit()
if turno == 'N' or turno == 'n':
    print ("o periodo é Noturno")
    exit()
else:
    print ("entrada invalida")