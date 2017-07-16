from Questao2.Funcionario import Funcionario
class Vendedor(Funcionario):
    def __init__(self, nome, idade, genero, salario, matricula, valorVendas, vendas):
        super(Vendedor, self).__init__(nome, idade, genero, salario, matricula)
        self.valorVendas = valorVendas
        self.vendas = vendas

    def __str__(self):
        return "Vendedor [valor de vendas: %s, vendas: %s]" % str(self.valorVendas), str(self.vendas)


