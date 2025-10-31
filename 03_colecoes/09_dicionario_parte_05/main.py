#Bibliotecas
import os

# Declaração de lista
usuarios = [] # A lista é listada dentro de conchete []

# Limpa console
os.system("cls")

while True:
    # menu
    print("1 - Cadastrar novo usuário: ")
    print("2 - Listar usuário: ")
    print("3 - Sair do programa: ")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls")
    match opcao:
        case "1":
            usuario = {} # Dicionário é listada entre chaves {}
            usuario['nome'] = input("Informe o nome do usuário: ").strip().title()
            usuario['idade'] = int(input("Informe a idade do usuário: ").strip().title())
            usuario['email'] = input("Informe o e-mail do usuário: ").strip().lower()
            usuarios.append(usuario)
            os.system("cls")
            print("\nNovo usuario inserido com sucesso.\n")
            continue
        case "2":
            for usuario in usuarios:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario[chave]}")
                print(f"{"-"*40}")
            continue
        case "3":
            print("Programa encerrado")
            break
        case _:
            print("\nOpção inválida! Tente novamente\n")
            continue


    
