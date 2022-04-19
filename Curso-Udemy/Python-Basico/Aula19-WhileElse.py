contador =0
acumulador =0

while contador <=10:
    print(contador,acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador +=1
else:
    print("aqui é o else")
print('fora do else, executado')
