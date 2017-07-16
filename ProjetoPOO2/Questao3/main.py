from Questao3.Pessoa import Pessoa
from Questao3.Fornecedor import Fornecedor

def main():
    a1 = Pessoa("Próclise", "Rua Me Perdi, 54", "(55) 55555-5555")
    a1.falar()
    print(a1)

    a2 = Fornecedor("Mesóclise", "Rua Levantar-me-ei, 564", "(22) 22222-2222", 5.400, 500)
    a2.falar()
    a2.obterSaldo()

if __name__ == '__main__':
    main()
