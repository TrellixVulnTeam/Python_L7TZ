import time
ladoa = float(input('Digite o primeiro lado : '))
ladob = float(input('Digite o segundo lado : '))
ladoc = float(input('Digite o terceiro lado : '))
print ('verificando se forma um triangulo ...')
time.sleep(2)
if (ladoa + ladob) > ladoc:
    print ('Formam um triangulo')
elif (ladob + ladoc) > ladoa:
    print ('Formam um triangulo')
elif (ladoa + ladoc) > ladob:
    print ('Formam um triangulo')
print ('verificando o tipo do triangulo ...')
time.sleep(2)
if ladoa == ladob == ladoc:
    print ('tipo : Triangulo equilátero ')
elif ladoa == ladob or ladob == ladoc or ladoa == ladoc:
    print ('tipo : Triangulo isósceles ')
elif ladoa != ladob and ladob != ladoc and ladoa != ladoc:
    print ('tipo : Triangulo Escaleno')