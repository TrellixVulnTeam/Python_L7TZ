"""
Operadores logicos =
and,not,or
in e not in
"""

a = 2
b = 3
nome = 'dfsaffd'

if not b > a:
    print("B é maior que A")
else:
    print("A é maior que B")


if 'k' in nome:
    print("Existe a letra k no seu nome")
"""
Operadores logicos =
and,not,or
in e not in
"""

a = 2
b = 3
nome = 'dfsaffd'
if not b > a:
    print("B é maior que A")
else:
    print("A é maior que B")



usuario = input("Digite : ")
qtd_carateres = len(usuario)

if qtd_carateres < 6:
    print("Não digitar pelo menos 6")
    print("Saindo...")
    exit();
else:
    print("cadastrado")
print(usuario, qtd_carateres, type(qtd_carateres))