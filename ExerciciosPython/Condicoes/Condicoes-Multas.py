tp = str(input('Digite F:FEMININO ou M:MASCULINO : ')).upper().strip()
if tp == "F":
    print ("Sexo : FEMININO")
if tp == "M":
    print ("Sexo : MASCULINO")
if tp != "M" and tp != 'F':
    print ("Invalido")
