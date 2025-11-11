# bibliotecas
import os
from classes import Conta

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()
    cc = Conta(titular="", cpf="", agencia="12345", n_conta="54321", saldo=0)
    cc.titular = input("Informe o nome do titular: ").strip().title()
    cc.cpf = input("Informe o CPF do titular: ").strip()
    limpar()

    while True: # Laço de repetição
        # menu
        print("1 - Consultar dados")
        print("2 - Depositar valor")
        print("3 - Sacar valor")
        print("4 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        match opcao:
            case "1":
                cc.consultar_dados()
                continue
            case "2":
                valor = float(input("Informe o valor do depósito: R$ ").strip().replace(",","."))
                print(f"Depósito efetuado com sucesso. Saldo atual: R$ {cc.depositar(valor):.2f}")
                continue
            case "3":
                valor = float(input("Informe o valor a ser sacado: ").strip().replace(",","."))
                print(f"Saque efetuado com sucesso! Seu saldo atual: R$ {cc.sacar(valor):.2f}")
                continue
            case "4":
                print("Programa encerrado com sucesso.")
                break
            case _:
                print("Opção inválida.")
                continue

if __name__ == "__main__":
    main()

#  TODO: atividade 07
""""
crie um app de banco. O programa deverá ter a classe Conta, com os atributos:
Titular da conta (Nome)
CPF do titular
Número da agência
Número da conta
Saldo
Os usuário irá inserir os dados "Titular da conta" e "CPF", e poderá escolher entre as seguintes opções:
Consultar dados da conta
Depositar valor
Sacar valor
Sair do programa
"""

