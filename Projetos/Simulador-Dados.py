import random
print ("JOGUE :  ")
dado1=(random.randrange(1, 6))
print(dado1)
print ("JOGUE 2: ")
dado2=(random.randrange(1, 6))
print (dado2)
aux=dado1
if aux > dado2:
    print ("jogador 1 jogou o maior numero, Jogue outra vez ")
if dado2 > aux:
    print ("jogador 2 jogou o maior numero, jogue outra vez" )
if dado2 == aux:
    print ("iguais")