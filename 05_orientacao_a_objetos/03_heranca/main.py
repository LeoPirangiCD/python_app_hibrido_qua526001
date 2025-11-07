# biblioteca do Python
import os

# nossa biblioteca
from classes import PessoaFisica, PessoaJuridica

# função limpar tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# função principal
def main():
    usuario = PessoaFisica(
        nome="", 
        cpf="", 
        idade=0, 
        email="", 
        telefone=""
    )
    empresa = PessoaJuridica(
        nome_fantasia="",
        cnpj="",
        email="",
        telefone=""
    )

    limpar()
    while True:
        print("1 - Inserir dados do usuário")
        print("2 - Inserir dados da empresa")
        print("3 - Exibir dados do usuário")
        print("4 - Exibir dados da empresa")
        print("5 - Sair do programa")
        opcao = input("Opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                usuario.nome = input("Informe seu nome: ").strip().title()
                usuario.cpf = input("Informe seu CPF: ").strip()
                usuario.idade = int(input("Informe sua idade: ").strip())
                usuario.email = input("Informe seu e-mail: ").strip().lower()
                usuario.telefone = input("Informe seu telefone: ").strip()
                limpar()
                continue
            case "2":
                empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
                empresa.cnpj = input("Informe o CNPJ: ").strip()
                empresa.email = input("Informe o e-mail da empresa: ").strip().lower()
                empresa.telefone = input("Informe o telefone da empresa: ").strip()
                limpar()
                continue
            case "1":
                usuario.nome = input("Informe seu nome: ").strip().title()
                usuario.cpf = input("Informe seu CPF: ").strip()
                usuario.idade = int(input("Informe sua idade: ").strip())
                usuario.email = input("Informe seu e-mail: ").strip().lower()
                usuario.telefone = input("Informe seu telefone: ").strip()
                limpar()
                continue
            case "2":
                empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
                empresa.cnpj = input("Informe o CNPJ: ").strip()
                empresa.email = input("Informe o e-mail da empresa: ").strip().lower()
                empresa.telefone = input("Informe o telefone da empresa: ").strip()
                limpar()
                continue
            case "3":
                usuario.exibir_dados()
                continue
            case "4":
                empresa.exibir_dados()
                continue
            case "5":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue

if __name__ == "__main__":
    main()