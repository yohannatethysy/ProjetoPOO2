from Questao1.Animal import Animal
from Questao1.Cachorro import Cachorro
from Questao1.Peixe import Peixe

def main():
    a1 = Animal("Cleiton Rasta", 35, "Balada")
    a1.comer()
    a1.locomover()

    a2 = Cachorro("Sabrino", 3, "Casa", "pug")
    a2.comer()
    a2.locomover()
    a2.vigiar()
    a2.brincar()

    a3 = Peixe("Etevaldo", 0.5, "Aquário", "cauda de sereia")
    a3.comer()
    a3.locomover()

    print(a1)
    print(a2)
    print(a3)

if __name__ == '__main__':
    main()

