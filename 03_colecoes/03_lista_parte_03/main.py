# declaração de lista
import os
nomes = []

# Limpa console
os.system("cls")

# Loop
while True:
    #menu
    print("1 - Inserir novo nome")
    print("2 - Exibir lista de nome")
    print("3 - Excluir nome na lista")
    print("4 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()

    os.system ("cls") # Limpa console

    match opcao:
        case "1":
                os.system ("cls") # Limpa console
                novo_nome = input("Informe o novo nome: ").strip().title()
                nomes.append(novo_nome)
                os.system ("cls") # Limpa console          
                print(f"{novo_nome} cadastrado com sucesso.")
                continue
        case "2":
                os.system ("cls") #Limpa console
                print("\nLista de nomes:\n")
                for i in range(len(nomes)): # Fazendo um contador com lastro de repetição. 
                      print(f"{i} - {nomes[i]}") # Mostra ao usúario a possição do nome.
                print(f"\n{'-'*40}\n") # 
                continue
        case "3":
                os.system ("cls") # Limpa console
                try:
                       posicao = int(input("Informe a possição a ser excluída: ").strip())
                       if posicao >= 0 and posicao < len(nomes):
                              del(nomes[posicao])
                              print("Nome excluído com sucesso.")
                       else:
                              print("Número inexistente.")
                        
                except Exception as e:
                       print(f"Posição inválida. {e}")
                       continue
        case "4":
                print("Programa encerrado.")
                break
        case _:
                print("Opção Inválida.")
                continue
                pass