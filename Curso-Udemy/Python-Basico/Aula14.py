hr = int(input("por favor, digite um horario : "))
if (hr >=0 and hr <=11):
    print ("Bom dia")
if (hr >=12 and hr <= 17):
    print ("Boa tarde")
if (hr <= 18 and hr >= 24):
    print ("Boa noite")