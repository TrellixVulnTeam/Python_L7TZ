
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def print_nome_completo(self):
        return (self.nome + " " + self.sobrenome)

info_pessoa = Pessoa("kelsey", "Magalhaes")
print (info_pessoa.print_nome_completo)
print (info_pessoa.nome + " " + info_pessoa.sobrenome)





class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

x = Point(1, 2)
print(x.x)