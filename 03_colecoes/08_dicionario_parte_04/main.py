# Declaração de coleções
# É convencional utilizar aspas simples para declaração de variável e aspas duplas para delacaração de valor.
usuarios = [
    {
        'nome': "Fulano", 
        'idade': 20,
        'email': "fulano@hotmail.com"
    },
    {
        'nome': "Cicrano",
        'idade': 25,
        'email': "cicrano@hotmail.com"
    },
    {
        'nome': "Beltrano",
        'idade': 30,
        'email': "beltrano@hotmail.com"
    }
]

print("\nDados dos usúarios\n")
for usuario in usuarios:
    print(f"\n{"-"*40}") # Mostrar o "-" 40 vezes para separar um dicionário do outro.
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario[chave]}")