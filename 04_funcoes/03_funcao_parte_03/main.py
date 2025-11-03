# biblioteca
import os

# Função
def boas_vindas(nome):
    os.system("cls")
    return f"\nSeja bem_vindo, {nome} 😎\n " # O return não fica entre parentese por chama uma função.

# Algoritmo principal
os.system("cls")
nome = input("Informe seu nome: ").strip().title()
resultado = boas_vindas(nome)
print(resultado)

