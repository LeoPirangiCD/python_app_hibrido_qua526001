# Classes
class Conta:
    # Construtor
    def __init__(self, titular, cpf, agencia, n_conta, saldo):
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.n_conta = n_conta
        self.saldo = saldo
    # Métodos
    def consultar_dados(self):
        print(f"Nome do titular da conta: {self.titular}")
        print(f"CPF: {self.cpf}")
        print(f"Agência da conta: {self.agencia}")
        print(f"Número da conta: {self.n_conta}")
        print(f"{self.titular} o saldo da sua conta é de: {self.saldo:.2f}")

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return self.saldo
        else:
            return "Saldo insuficiente. Saque não permitido."
       


        pass