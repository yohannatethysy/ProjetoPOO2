from Questao1.Animal import Animal
from Questao1.Cauda import Cauda

class Peixe(Animal):
    def __init__(self, nome, peso, habitat, tipoCauda):
        super(Peixe, self).__init__(nome, peso, habitat)
        self.tipoCauda = Cauda(tipoCauda)

    def __str__(self):
        return "Peixe [nome: %s, peso: %.1f, habitat: %s, Tipo de Cauda: %s]" % (self.nome, self.peso, self.habitat, self.tipoCauda)

    
