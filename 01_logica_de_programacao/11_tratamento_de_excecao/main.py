# Tratamento de Exceção
try:
    # Entrada de dados
    nome = input("informe seu nome: ").strip().title()
    idade = int(input("informe sua idade: ").strip())
    altura = float(input("Informe sua altura ").strip().replace(",", ",."))

    #Saida de dados

    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Altura: {altura}")

except:
    print("Infelizmente o programa não pode ser executado")


   