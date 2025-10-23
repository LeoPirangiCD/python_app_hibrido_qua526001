# Declaração de variavéis
nome = input("Informe seu nome: ").strip().title()
idade = int(input("Informe sua idade: ").strip())

# decisão
if idade >= 18:
    print(f"{nome}, você é maior de idade.")
else:
    print(f"{nome}, você é menor de idade.")