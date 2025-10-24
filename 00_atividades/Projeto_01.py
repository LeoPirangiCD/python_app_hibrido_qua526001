# Biblioteca
import os

# Entrada de dados
nome = input("Digite seu nome: ").strip().title() # String
email = input("Digite seu email: ").strip().lower() # String
cpf = input("Digite seu CPF: ").strip() # String
telefone = input("Digite seu telefone: ").strip() # String

os.system("cls")

#Saída de dados
print(f"Nome do usuário: {nome}")
print(f"Email do usuário: {email}")
print(f"CPF do usuário: {cpf}")
print(f"Telefone do usuário: {telefone}")

