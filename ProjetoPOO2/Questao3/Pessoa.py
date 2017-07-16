class Pessoa():
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def falar(self):
        print(self.nome + " falando.")

    def __str__(self):
        return "[nome: %s, endereco: %s, telefone: %s]" % (self.nome, self.endereco, self.telefone)

