# Função
def main():
    # Entrada de dados
    nome = input("Informe seu nome: ").strip().title()
    idade = int(input("Informe sua idade: ").strip())

    # Operador Ternário
    resultado = "é maior de idade." if idade >= 18 else "É menor de idade."

    # Saída de dados
    print(f"{nome} {resultado}")

# Protege algoritmo principal (Impede que outros programadores acessem a determinada função.)
if __name__ == "__main__":
    main()