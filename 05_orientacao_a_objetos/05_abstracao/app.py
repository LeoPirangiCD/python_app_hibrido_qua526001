import os
from classes import Parque

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    ingresso = Parque(nome="", idade=0, peso=0.0)

    ingresso.nome = input("Informe o nome: ").strip().title()
    ingresso.idade = int(input("Informe o idade: ").strip())
    ingresso.peso = float(input("Informe o peso em kg: ").strip().replace(",","."))
    limpar()

# Menu
    while True:
        print("1 - Categoria Infantil")
        print("2 - Categoria Juvenil")
        print("3 - Categoria Adulto")
        print("4 - Sair do programa.")
        opcao = input("Escolha a sua opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                print(ingresso.entrada_infantil())
                continue
            case "2":
                print(ingresso.entrada_juvenil())
                continue
            case "3":
                print(ingresso.entrada_adulto())
                continue
            case "4":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida, tente novamente.")
                continue


if __name__ == "__main__":
    main()