# biblioteca dataclass
from dataclasses import dataclass

@dataclass # O @ para o dataclass funcionar
class Pessoa:
    email: str
    telefone: str
    endereco: str

    def __str__(self):
        return f"Email: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"
    
@dataclass # Para cada uma nova classe, um novo @dataclass
class PessoaFisica(Pessoa):
    nome: str
    idade: int
    cpf: str
    profissao: str

    def __str__(self):
        return f"\nDADOS DO USUÁRIO:\nNome:{self.nome}\nIdade: {len(self)}\nCPF: {self.cpf}\nProfissão: {self.profissao}\n{super().__str__()}"
    def __len__(self):
        return self.idade
    
@dataclass
class PessoaJuridica(Pessoa):
    nome_fantasia: str
    cnpj: str
    website: str
    
    def __str__(self):
        return f"\nDADOS DA EMPRESA:\nNome fantasia: {self.nome_fantasia}\nCNPJ: {self.cnpj}\nWebsite: {self.website}{super().__str__()}"


