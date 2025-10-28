#TODO
# Crie uma lista com os nomes de todos os estados brasileiros e mostre na tela os estados em ordem alfabética

# Declaração da lista
Estados = ["Espírito Santo",
"Mato Grosso",
"Rio de Janeiro",
"Ceará",
"Goiás",
"Pará",
"Maranhão",
"Bahia",
"Amapá",
"Mato Grosso do Sul",
"Rio Grande do Norte",
"Minas Gerais",
"Paraíba",
"Acre", 
"Pernambuco",
"Tocantins",
"Paraná",
"Piauí",
"Santa Catarina",
"São Paulo",
"Amazonas",
"Rio Grande do Sul",
"Rondônia",
"Alagoas", 
"Roraima",
"Sergipe",
"Distrito Federal"]

# Imprime todos os itens listado
print(Estados)

# Organiza os itens um abaixo do outro
for Estado in Estados:
    print(Estado)

# Organiza os itens em ordem alfabética
Estados.sort()
print("\nEstados em ordem alfabética:\n")
for Estado in Estados:
    print(Estado)

# Organiza os itens em ordem alfabética reversa
Estados.sort(reverse=True)
print("\nEstados em ordem alfabética reversa\n")
for Estado in Estados:
    print(Estado)