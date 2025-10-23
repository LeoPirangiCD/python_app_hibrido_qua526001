# Declaração de Variáveis
x = float(input("Informe o 1° número: ").strip().replace(',', '.'))
y = float(input("Informe o 2° número: ").strip().replace(',', '.'))

# Menu

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operador = input("Escolha a operação desejada: ").strip()

#Decisão
match operador:
    case '1':
        resultado = x + y
        print(f"O resultado da soma entre {x} e {y} é: {resultado}")
    case '2':
        resultado = x - y
        print(f"O resultado da subtração entre {x} e {y} é: {resultado}")
    case '3':
        resultado = x * y
        print(f"O resultado da multiplicação entre {x} e {y} é: {resultado}")
    case '4':
        if y != 0:
            resultado = x / y
            print(f"O resultado da divisão entre {x} e {y} é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    case _:
        print("Operação inválida. Por favor, escolha uma opção válida.")        