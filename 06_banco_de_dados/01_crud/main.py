from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker # sqlalchemy.orm = Tecnologia usada para o próprio programa criar o banco
from entidade import criar_tb_pessoa

def main():
    engine = create_engine("sqlite:///01_crud/database/crud.db")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(engine, Base)
    Session = sessionmaker(bind=engine) # Cria uma sessão para manipularmos o banco de dados.
    session = Session() # Inicializa uma sessão

    session.close()






if __name__ == "__main__":
    main()
