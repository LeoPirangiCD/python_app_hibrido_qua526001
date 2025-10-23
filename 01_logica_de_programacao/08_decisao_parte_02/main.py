# Declaração de variáveis
nome = input("Informe seu nome: ").strip().title()
idade = int(input("Informe sua idade: ").strip())
altura = float(input("Informe sua altura em metros: ").strip().replace(',', '.'))

# verificação de condições
if idade >= 12 and altura >= 1.15:
    print(f"Entrada de {nome} foi autorizada.")
else:
    print(f"Entrada de {nome} não foi autorizada.")