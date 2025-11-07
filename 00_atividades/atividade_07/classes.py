import os
import math

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# Classes
class Conta:
    def __init__ (self, titular_conta, cpf, numero_agencia, numero_conta, saldo):
        self.titular_conta = titular_conta
        self.cpf = cpf
        self.numero_agencia = numero_agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

   # Saída de dados
    def exibir_dados(self):
        print(f"Nome: {self.titular_conta}")
        print(f"CPF: {self.cpf}")
        print(f"Número da agência: {self.numero_agencia}")
        print(f"Número da conta: {self.numero_conta}")
        print(f"Saldo disponível: {self.saldo}")

    def depositar_saldo(self):
        limpar()
        valor = float(input("Valor a ser adicionado a conta: {}"))
        if self.saldo == 0:
            self.saldo = valor
        else:
            self.saldo = self.saldo + valor

    def sacar(self):
        limpar()
        sacar = float(input("Digite o valor de saque: ").strip().replace(",","."))
        self.saldo = self.saldo - sacar
        print(f"Seu saldo atual é: {self.saldo}")

