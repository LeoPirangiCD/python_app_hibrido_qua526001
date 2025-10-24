# Indíce de Massa Corporal (IMC)
import os
import time
import math

try:
    pass
    # Entrada de dados
    peso = float(input("Informe o seu peso em kg: ").strip().replace(",","."))
    altura = float(input("Informe a sua altura em metros: ").strip().replace(",","."))
    
    # Cálculo do IMC
    imc = peso / (altura ** 2)
    
    # Limpa o console
    #os.system("cls")
    
    # Saída de dados
    print(f"Seu IMC é: {imc:.2f}")
    
    # Classificação do IMC
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("Classificação: Peso normal")
    elif 25 <= imc < 29.9:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obesidade")
    
except:
    print("Não foi possível calcular o IMC. Dados errados.")