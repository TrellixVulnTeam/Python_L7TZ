textp = 'Python'

#for letra in textp:
#    print(letra)

for letra in range(0,10,3):
    print(letra)
print ('##################')

for letra in range(100):
    if letra %8  ==  0:
        print(letra)

print ('#################')

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra =='t':
        nova_string = nova_string + letra.upper()
    elif letra =='h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
    print(nova_string)