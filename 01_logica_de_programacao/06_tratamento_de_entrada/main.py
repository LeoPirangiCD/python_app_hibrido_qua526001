# Declaração de variáveis

nome = input("Informe seu nome: ").strip().title()
idade = int(input("Informe sua idade: ").strip())
altura = float(input("Informe sua altura: ").strip().replace(',', '.'))

# Saída de dados
print(f"Nome do usuário: {nome}. Tipo: {type(nome)}")
print(f"Idade do usuário: {idade}. Tipo: {type(idade)}")
print(f"Altura do usuário: {altura}. Tipo: {type(altura)}")
