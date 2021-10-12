frase = "Curso em video Python"
print (frase[:4])
quant= frase.count('o')
print ('a letra o aparece :', quant)

Tamanho = (len(frase))
print ("O tamanho da frase é :", Tamanho)

TamanhoSemEspaco = (len(frase.strip()))
print ("O tamanho da frase sem espeacos é : ", TamanhoSemEspaco)

trocaString = (frase.replace('Python','Android'))
print("Trocando palavras na frase : ", trocaString)

ProcuraTexto = (frase.lower().find('em'))
print (ProcuraTexto)


dividido = frase.split()
print ("a frase dividida ficou: ", dividido)
print (dividido[2])
print (dividido[2][4])


print ("""teste
testeste""")