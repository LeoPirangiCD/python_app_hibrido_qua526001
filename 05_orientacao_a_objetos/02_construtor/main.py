# classe
class Pessoa:
    # construtor
    def __init__(self, nome, cpf, email, idade):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.idade = idade
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")
        print(f"Idade: {self.idade} anos")

# algoritmo principal
if __name__ == "__main__":
    # instancia a classe
    usuario = Pessoa(nome="", cpf="", email="", idade=0)

    # entrada de dados
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.idade = int(input("Informe a idade: ").strip())

    # saída de dados
    usuario.exibir_dados()