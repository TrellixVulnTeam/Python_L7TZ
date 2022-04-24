
frase = "exercicios de python"
qt = len(frase)
contador = 0
nova_string = ''
#print(frase[3])
#print(frase,qt)
input=input("Digite a letra  uue desehva substituir : ")
while contador < qt:
    letra = frase[contador]
    if letra == input:
        nova_string += 'P'

    else:
        nova_string += letra
    contador +=1
print(nova_string)