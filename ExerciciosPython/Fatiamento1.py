frase = str(input("digite uma cidade")).split()
a= (frase[0:8] == 'GUAXUPE')
if (a == frase):
    print ("A cidade esta correta")
else:
    print ("Por favor , digite novamente")
