class Produto():
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return "Produto [nome: %s, valor: %s]" % str(self.nome) + str(self.valor)


