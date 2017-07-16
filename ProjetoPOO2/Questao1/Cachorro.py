from Questao1.Animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, peso, habitat, raca):
        super(Cachorro, self).__init__(nome, peso, habitat)
        self.raca = raca

    def brincar(self):
        print(self.nome + " brincando.")

    def vigiar(self):
        print(self.nome + " vigiando.")

    def __str__(self):
            return "Cachorro [nome: %s, peso: %.1f, habitat: %s, raça: %s]" % (self.nome, self.peso, self.habitat, self.raca)


