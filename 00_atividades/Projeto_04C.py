try:
# Variáveis
        nome = input("Informe seu nome: ").strip().title()
        idade = int(input("Informe sua idade: ").strip())
# Loop
        while True:
# Lista de Filmes
                sala_1 = "A Roda Quadrada"
                sala_2 = "A Volta do que Não Foram"
                sala_3 = "Poeira em Alto Mar"
                sala_4 = "As tranças do Rei Careca"
                sala_5 = "A Vingança do Frango Assado"

# Menu de filmes:
                print(f"Sala 1 -{sala_1} - Livre")
                print(f"Sala 2 -{sala_2} - 12 anos")
                print(f"Sala 3 -{sala_3} - 14 anos")
                print(f"Sala 4 -{sala_4} - 16 anos")
                print(f"Sala 5 -{sala_5} - 18 anos")
                sala = input("Informe a sala desejada: ").strip()

# Verifica a sala selecionada
                match sala:
                        case "1":
                                idade_minima = 0
                                filme = sala_1
                        case "2":
                                idade_minima = 12
                                filme = sala_2
                        case "3":
                                idade_minima = 14
                                filme = sala_3                                      
                        case "4":
                                idade_minima = 16
                                filme = sala_4
                        case "5":
                                idade_minima = 18
                                filme = sala_5
                        case _:
                                print("Sala inexistente.")
                if idade >= idade_minima:
                        print(f"O {nome} escolheu {filme}. Tenha um bom filme.")
                        break
                else:
                        print(f"{nome} não foi autorizado a ver {filme}")
                        continue     
except Exception as e:
        print("Erro no programa. {e}")
