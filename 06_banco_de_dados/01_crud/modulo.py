import os
from datetime import datetime

def limpar():
    os.system("cls" if os.name == "nt" else "clear")



def cadastrar(session, Pessoa):
    try:
        nome = input("Informe o nome: ").strip().title()
        genero = input("Informe o genero: ").strip()
        nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
        nascimento = datetime.strptime(nascimento, "%d/%m/%Y").date()
        email = input("Informe o e-mail: ").strip().lower()

        # Filtrando atributo email das pessoas que posssuem o email informado
        pessoas = session.query(Pessoa).filter(Pessoa.email.like(email)).all()

        if email in [pessoa.email for pessoa in pessoas]:
            return "E-mail já cadastrado."
        else:
            nova_pessoa = Pessoa(nome=nome, nascimento = nascimento, email = email, genero = genero)
            
        session.add(nova_pessoa) # Insert (Insere nova pessoa ao banco)
        session.commit()
        return f"{nova_pessoa.nome} cadastrada com sucesso."


    except Exception as e:
        print(f"Não foi possivel cadastrar. {e}")

# read
def listar(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()
        
        print("\nPESSOAS CADASTRADOS\n")
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            print(f"Gênero: {pessoa.genero}")
            print(f"Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}") # strftime("%d/%m/%Y") (Converte a data para o modo brasileiro de dia/mês/ano)
            print(f"\n{'-'*40}\n")

    except Exception as e:
        print(f"Não foi possivel listar. {e}.")
# update
def atualizar(session, Pessoa):
    id_pessoa = ""
    novo_nome = ""
    novo_email = ""
    novo_nascimento = ""
    novo_genero = ""
    try:
        print("\nEscolha o campo que deseja pesquisar: \n")
        print("1 - ID")
        print("2 - email")
        print("3 - Sair")
        opcao = input("Opção desejada: ").strip
        limpar()
        match opcao:
            case "1":
                id_pessoa = input("Informe o ID: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                email = input("Informe o e-mail").strip().lower()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case "3":
                return ""
            case _:
                print("Pesquisa inválida. Tente novamente.")
        if pessoa:
            limpar()
            while True:
                print(f"ID {pessoa.id_pessoa}")
                print("Qual campo deseja alterar: \n")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"2 - E-mail: {pessoa.email}")
                print(f"3 - Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}")
                print(f"4 - Gênero {pessoa.genero}")
                print("5 - Finalizar")
                campo = input("Campo desejado: ").strip()
                limpar()
                match campo:
                    case "1":
                        novo_nome = input("Informe o novo nome: ").strip().title()
                        continue
                    case "2":
                        novo_email = input("Informe o novo e-mail: ").strip().lower()
                        pessoas = session.query(Pessoa),filter(Pessoa.email == novo_email).all()
                        if email in {pessoa.email for pessoa in pessoas}:
                            print("E-mail já cadastrado.")
                        continue
                    case "3":
                        novo_nascimento = input("Informe a nova data de nascimento dd/mm/yyyy: ").strip()
                        pessoa = session.query(Pessoa),filter(Pessoa.nascimento == novo_nascimento)
                    case "4":
                        novo_genero = input("Informe o novo gênero: ").strip().lower()
                        continue
                    case "5":
                        novo_nome = novo_nome if novo_nome != "" else pessoa.nome
                        novo_email = novo_email if novo_email != "" else pessoa.email
                        novo_nascimento = datetime.strftime(novo_nascimento,("%d/%m/%Y")).date() if novo_nascimento != "" else pessoa.nascimento
                        novo_genero = novo_genero if novo_genero != "" else pessoa.genero
                        break
                    case _:
                        print("Campo invalido")
                        continue
            pessoa.nome = novo_nome
            pessoa.email = novo_email
            pessoa.nascimento = novo_nascimento
            pessoa.genero = novo_genero

            session.commit()
            return "Dados atualizados com sucesso."
        else:
            return "Pessoa não encontrada."


            





    except Exception as e:
        print(f"Não foi possivel alterar os dados. {e}.")