# Loop
while True:
    try:
        # menu
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Sair do programa")
        opcao = input("Informa a opção desejada: ").strip()
        
        if opcao != "5":
            n1 = int(input("Informe o 1° número: ").strip())
            n2 = int(input("Informe o 2° número: ").strip())

            match opcao:
                case "1":
                    result = n1 + n2
                    print(f"A soma é: {result}")
                    continue
                case "2":
                    result = n1 - n2
                    print(f"A subtração é: {result}")
                    continue

                case "3":
                    result = n1 * n2
                    print(f"A multiplicação é: {result}")
                    continue

                case "4":
                    result = n1 / n2
                    print(f"A divisão é: {result}")
                    continue

                case _:
                    print("Opção inválida.")                
                
        else:
            print("Programa encerrado.")
            break
           
    except:
        print("Valores inválidos.")

