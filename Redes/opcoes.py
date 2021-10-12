import optparse

parser = optparse.OptionParser()###Criamos o objeto de opcoes

parser.add_option("-?", action="help", help="Mostra a ajuda") ###cria a opcao help
parser.add_option("-F", "--kelsey", help="Mostra o site",dest="NOME", metavar="NOME SITE",action="append")

(options, args ) = parser.parse_args() ###recebe o argumento que o usuario esta passando nessas variaveis
###print(options)###mostra o que tem dentro dos argumentos
####print(args)###mostra o que tem dentro dos argumentos

if options.NOME :
   print("Esse é o nome do site",options.NOME)
else:
   print("Esse nao é o nome do site",options.NOME)
print (options.NOME)
print (args)
