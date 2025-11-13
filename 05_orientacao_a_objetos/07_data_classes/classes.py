# biblioteca
from dataclasses import dataclass

# classes
@dataclass
class Pessoa:
    # atributos
    nome: str
    idade: int
    altura: float

    # Métodos
    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {len(self)} anos\nAltura: {self.altura} m"
    
    def __len__(self):
        return self.idade
    
    def verificar_maioridade(self):
        return ("é maior de idade" if len(self) >= 18 else "é menor de idade")