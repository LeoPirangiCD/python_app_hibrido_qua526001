# Tema da aula: abstração
# biblioteca
from abc import ABC, abstractmethod # ABC = Tranforma uma classe em abstrata

class IParque(ABC):
    @abstractmethod
    def entrada_infantil(self):
        pass

    @abstractmethod
    def entrada_juvenil(self):
        pass

    @abstractmethod
    def entrada_adulto(self):
        pass

# Classe
class Parque(IParque):
# Construtor
    def __init__(self, nome, idade, peso):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso):
        self.__peso = peso
# Métodos de acesso
    def entrada_infantil(self):
        if self.__idade <= 15 and self.__peso < 70:
            return f"Ingresso liberado para {self.__nome}"
        else:
            return f"Entrada proibida para {self.__nome}"
        
    def entrada_juvenil(self):
        if self.__idade >= 12 and self.__idade < 18:
            return f"Ingresso liberado para {self.__nome}"
        else:
            return f"Entrada proibida para {self.__nome}"
        
    def entrada_adulto(self):
        if self.__idade >= 18:
            return f"Ingresso liberado para {self.__nome}"
        else:
            return f"Entrada proibida para {self.__nome}"
        
    