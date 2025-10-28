
import time
import os

# Declaração de lista
nomes = ["Fulano", "Cicrano", "Beltrano", "João", "Maria", "José"]

# Exiba todos os nomes da lista
print(nomes)

# Exiba o primeiro nome
print(nomes[0])
print(f"{nomes[0]} e {(nomes[3])}")

# Exibe toda a lista
for nome in nomes:
    print(nome)

# Ordena a lista em ordem alfabética
nomes.sort()

# Re-exibir a lita em ordem alfabética (\n = Quebra de linha)
print("\nOrdem alfabética:\n")
for nome in nomes:
    print(nome)

# Ordem Alfabética Reversa
nomes.sort(reverse=True)
print("\nOrdem alfabética reversa:\n")
for nome in nomes:
    print(nome)