# Declaração de dicionário
veiculo = {
    "Fabricante": "Chevrolet",
    "Modelo": "Chevette",
    "Ano": 1973,
    "Cor": "Branco",
    "Placa": "DF-1973"

}

# Exibe os dados
for chave in veiculo:
    print(f"{chave.capitalize()}: {veiculo[chave]}")

# Usuário escolhe o campo que deseja mudar
while True:
    campo = input("Informe o nome do campo que deseja alterar ou digite 'sair' para encerrar o programa: ").strip().lower()

    match campo:
        case "fabricante":
            veiculo["Fabricante"] = input("Informe o novo fabricante: ").strip()
            
        case "modelo":
            veiculo["Modelo"] = input("Informe o novo modelo: ").strip()
            
        case "ano":
            veiculo["Ano"] = int(input("Informe o novo ano: ").strip())
            
        case "cor":
            veiculo["Cor"] = input("Informe o nova cor: ").strip()
            
        case "placa":
            veiculo["Placa"] = input("Informe a nova placa: ").strip()
            
        case "sair":
            print("Programa encerrado.")
            break
        case _:
            print("Campo inválido. Tente novamente.")
            continue
# Exibe os dados atualizados
    for chave in veiculo:
        print(f"{chave.capitalize()}: {veiculo[chave]}")