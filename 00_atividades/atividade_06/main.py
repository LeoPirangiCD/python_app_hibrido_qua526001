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
print("Por favor, insira os seguintes dados: ")


nome = input("Digite seu nome: ").strip().lower().title()
email = input("Digite seu e-mail: ").strip().lower()
telefone = input("Digite seu telefone: ").strip()
cpf = input("Digite seu CPF: ").strip()
genero = input("Digite seu gênero: ").strip().lower()

dados_usuario = {
    "nome" : nome,
    "email" : email,
    "telefone" : telefone,
    "cpf" : cpf,
    "genero" : genero
}

print("\n Dados do Usuário:")
for chave in dados_usuario:
    print(f"{chave.title()}: {dados_usuario[chave]}")