from Questao3.Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, endereco, telefone, codigoSetor, salarioBase, imposto):
        super(Funcionario, self).__init__(nome, endereco, telefone)
        self.codigoSetor = codigoSetor
        self.salarioBase = salarioBase
        self.imposto = imposto

    def calcularSalarioTotal(self):
        total = self.salarioBase * (self.imposto/100)
        return total

