n = str(input('Digite uma frase : ')).strip()###aqui o strip retira os espaços
nome = n.split() ###aqui o split divide as frases colocando em forma de cadeias separadas por listas
print ('seu primeiro nome é {}'.format(nome[0]))
print ('Seu ultimo sobrenome é {}'.format(nome[len(nome)-1]))