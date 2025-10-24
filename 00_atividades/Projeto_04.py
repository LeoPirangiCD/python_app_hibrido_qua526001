# Cinema
while True:
    try:
        # Variáveis
        nome = input("Informe seu nome: ").strip().title()
        idade = int(input("Informe sua idade: ").strip())

# Lista de filmes
        print("Cinema Pirangi")

        print("Sala 1 - A Roda Quadrada - Livre")
        print("Sala 2 - A Volta dos Que Não Foram - 12 anos")
        print("Sala 3 - Poeira em Alto Mar - 14 anos")
        print("Sala 4 - As Tranças do Rei Careca - 16 anos")
        print("Sala 5 - A Vingança do Frango Assado - 18 anos")

        sala = (int(input("Informe o número da sala desejada: ").strip()))
        if sala == 1 and 2 and 3 and 4 and 5:
         match sala:
            case 1:
                if sala == 5 and idade >= 18:
                    print(f"{nome}, seu ingresso será impresso.")
                else:
                    print(f"{nome}, você não tem idade suficiente para assistir a este filme.")
                    continue
            case 2:
                if sala == 4 and idade >= 16:
                    print(f"{nome}, seu ingresso será impresso.")
                else:
                    print(f"{nome}, você não tem idade suficiente para assistir a este filme.")
                    continue
            case 3:
                if sala == 3 and idade >= 14:
                    print(f"{nome}, seu ingresso será impresso.")
                else:
                    print(f"{nome}, você não tem idade suficiente para assistir a este filme.")
                    continue
            case 4:
                if sala == 2 and idade >= 12:
                    print(f"{nome}, seu ingresso será impresso.")
                else:
                    print(f"{nome}, você não tem idade suficiente para assistir a este filme.")
                    continue
            case 5:
                if sala == 1:
                    print(f"{nome}, seu ingresso será impresso.")
                    continue
        else:
            print("Sala inválida. Por favor, escolha uma sala entre 1 e 5")
            
    except:
        print("Não foi possível processar as informações.")