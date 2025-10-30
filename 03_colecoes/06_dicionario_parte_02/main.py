# Declaração de dicionário

usuario = {
    'nome': "Leonardo Pirangi",
    "nascimento": "18/01/1981",
    "email": "leonardopirangi@hotmail.com",
    "telefone": "(11) 9 9999-9999",
    "endereco": "QNE 09"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario[chave]}")
