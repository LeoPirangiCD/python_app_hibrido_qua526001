#TODO: Atividade
""""
Crie um programa que receba do usuário os seguintes dados:

Nome
E-mail
Telefone
CPF
Gênero

Após isso, o programa deve armazenar esses dados em um dicionário e exibir os dados desse dicionário.

"""
# Declaração de dicionário
dados_usuario = {}

print("\nPor favor, insira os seguintes dados: \n")
# Entrada de dados
dados_usuario["nome"] = input("Digite seu nome: ").strip().lower().title()
dados_usuario["email"] = input("Digite seu e-mail: ").strip().lower()
dados_usuario["telefone"] = input("Digite seu telefone: ").strip()
dados_usuario["cpf"] = input("Digite seu CPF: ").strip()
dados_usuario["genero"] = input("Digite seu gênero: ").strip()

print("\n Dados do Usuário:\n")
for chave in dados_usuario:
    print(f"{chave.capitalize()}: {dados_usuario[chave]}")