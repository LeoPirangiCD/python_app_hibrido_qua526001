# importação de bibliotecas
import os

# Loop
while True:
    #limpeza de console
    os.system("cls")

    #tratamento de exceção
    try:
        #entrada de dados
        nome = input("Informe o seu nome:  ").strip().title()
        email = input("Informe o seu email: ").strip().lower()
        cpf = input("Informe o seu CPF: ").strip()

        #limpeza de console
        os.system("cls")

        #saída de dodos
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"CPF: {cpf}")

        print("1 - Inserir novos dados")
        print("2 - Sair do programa")
        opcao = input("Opção desejada: ").strip()

        #verificar a opção escolhida
        match opcao:
            case "1":
                continue
            case "2":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                break
              
    except:
        print("Não foi possível receber as informaçôes.")