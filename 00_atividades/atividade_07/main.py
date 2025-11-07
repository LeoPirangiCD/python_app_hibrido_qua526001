# TODO: atividade 07
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
#Bibliotecas
import os
import math
from classes import * # Importa as classes, funções e metodos.

def main():
    usuario = Conta(titular_conta = "",
                    cpf = "",
                    numero_agencia = 0,
                    numero_conta = 0,
                    saldo = 0.0) # 0.0 por ser float
    
    print("Digite os dados do usuario: ")
    usuario.titular_conta = input("Digite o nome do titular da conta: ").strip().title()
    usuario.cpf = input("Digite o CPF do titular: ").strip().replace(",",".")
    usuario.numero_agencia = 2000
    usuario.numero_conta = 9000

    limpar()
    while True:
        print(f"Bem-vindo {usuario.titular}")






    
        

   
    

    # Menu



   










if __name__ == "__main__":