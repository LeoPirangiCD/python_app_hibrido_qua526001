import os
from classes import Pessoa

def limpar():
    os.system("cls" if os.nome == "nt" else "clear")

def main():
    pessoa = Pessoa(nome="", idade=0, genero="", telefone="")

    pessoa.nome = input("Informe o nome: ").strip().title()
    pessoa.idade = int(input("Informe a idade: ").strip())
    pessoa.genero = input("Informe o gênero: ").strip()
    pessoa.telefone = input("Informe o telefone: ").strip().lower()

    # Saída de dados
    print(pessoa)
    print(f"Idade: {len(pessoa)} anos")

if __name__ == "__main__":
    main()