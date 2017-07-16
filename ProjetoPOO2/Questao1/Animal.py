class Animal():
    def __init__(self, nome, peso, habitat):
        self.nome = nome
        self.peso = peso
        self.habitat = habitat

    def comer(self):
        print(self.nome + " comendo de forma genérica.")

    def locomover(self):
        print(self.nome + " movendo-se de forma genérica.")

    def __str__(self):
        return "Animal [nome: %s, peso: %.1f, habitat: %s]" % (self.nome, self.peso, self.habitat)

