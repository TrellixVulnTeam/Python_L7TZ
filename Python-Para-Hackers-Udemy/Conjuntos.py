#Conjunto e basicamente uma lista que não pode ter valores iguais

conjunto = {"alho", "sal", "cenoura", "sal", "banana", "sal", "alface"}
conjunto.add("xarope")
conjunto.add("1212")
print (conjunto)
conjunto.pop()
print (conjunto)
copia_conjuntto = conjunto.copy();
print (copia_conjuntto)
dif =conjunto.difference(copia_conjuntto)
print(dif)
#conjunto .pop()
#print conjunto

#copia_de_conjunto = conjunto.copy()
#print (conjunto)
#print (copia_de_conjunto)

#comparar_conjunto = ("alho", "sal", "conjunto")
#print (conjunto.difference(comparar_conjunto)