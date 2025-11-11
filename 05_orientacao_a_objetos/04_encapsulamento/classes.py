# Encapulamento (__)
class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome # Para encapsular acrescente dois _ antes do atributo
        self.__cpf = cpf # Para encapsular acrescente dois _ antes do atributo

# Método get
        @property # Usado apenas para o get
        def nome(self):
            return self.__nome
# Método set
        @nome.setter # nome_atributo.setter
        def nome(self, nome):
            self.__nome = nome
# Método get
        @property # Usado apenas para o get
        def cpf(self):
            return self.__cpf
# Método set
        @cpf.setter # nome_atributo.setter
        def cpf(self, cpf):
            return self.__cpf
