# Biblioteca
import os

# Função
def boas_vindas(nome):
    os.system("cls")
    print(f"\nSeja bem-vindo, {nome} 😃\n")

# Algoritmo principal
os.system("cls")
nome = input("\nInforme seu nome: ").strip().title()
boas_vindas(nome)