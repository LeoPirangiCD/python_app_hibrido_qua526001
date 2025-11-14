import os
from classes import PessoaFisica, PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()
    usuario = PessoaFisica(nome="",idade=0, cpf="", profissao="", email="", telefone="", endereco="")
    empresa = PessoaJuridica(nome_fantasia="", cnpj="", website="",email="", telefone="", endereco="")

    print("INFORME OS DADOS DO USUARIO:\n")

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a idade: ").strip())
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.profissao = input("Informe a profissão: ").strip()
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.telefone = input("Informe o telefone: ").strip()
    usuario.endereco = input("Informe o endereço: ").strip().title()

    limpar()
    print("INFORME OS DADOS DA EMPRESA\n")

    empresa.nome_fantasia = input("Informe o nome fantasia: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.website = input("Informe o website: ").strip().lower()
    empresa.email = input("Informe o e-mail: ").strip().lower()
    empresa.telefone = input("Informe o telefone: ").strip()
    empresa.endereco = input("Informe o endereço: ").strip().title()

    limpar()
    print(usuario)
    print(empresa)



if __name__ == "__main__":
    main()