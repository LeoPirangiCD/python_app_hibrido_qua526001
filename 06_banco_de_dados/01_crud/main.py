from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker # sqlalchemy.orm = Tecnologia usada para o próprio programa criar o banco
from entidade import criar_tb_pessoa
from modulo import limpar, cadastrar

def main():
    engine = create_engine("sqlite:///01_crud/database/crud.db")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(engine, Base)
    Session = sessionmaker(bind=engine) # Cria uma sessão para manipularmos o banco de dados.
    session = Session() # Inicializa uma sessão

    limpar()
    while True:
        print(f"{'-'*20}🐍 CRUD DA COBRA 🐍 {'-'*20}\n")
        print("0 - Sair do programa")
        print("1 - Cadastrar nova pessoa")
        opcao = input("Digite a opção desejada: ").strip()
        limpar()
        match opcao:
            case "0":
                print ("Programa encerrado")
                break
            case "1":
                print(cadastrar(session, Pessoa))
                continue
            case _:
                print("Opção inválida.")
                continue

                                        

    session.close()


if __name__ == "__main__":
    main()
