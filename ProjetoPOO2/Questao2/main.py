from Questao2.Pessoa import Pessoa
from Questao2.Funcionario import Funcionario
from Questao2.Cliente import Cliente
from Questao2.Gerente import Gerente
from Questao2.Vendedor import Vendedor
from Questao2.Produto import Produto

def main():
    a1 = Pessoa("Creuza", 28, 2)
    a1.andar()
    a1.falar()

    a2 = Funcionario("Glebis", 32, "Masculino", 3.500, "5433-9")
    a2.andar()
    a2.falar()

    a3 = Cliente("Clóvis", 59, "Masculino", "19/02/1958")
    a3.andar()
    a3.falar()

    a4 = Gerente("Brevelyn", 43, "Feminino", 2.000, "1232-5", "RH")
    a4.andar()
    a4.falar()

    a5 = Vendedor("RuPaul", 56, "Masculino", 2.150, "5983-6", 850.500, [
        Produto("Pasta de elefante", 500),
        Produto("Manta de linho de ouro", 850.000)
    ])
    a5.andar()
    a5.falar()

if __name__ == '__main__':
    main()

