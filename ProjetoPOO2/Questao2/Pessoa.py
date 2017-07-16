class Pessoa():
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def andar(self):
        print(self.nome + " andando.")

    def falar(self):
        print(self.nome + " falando.")