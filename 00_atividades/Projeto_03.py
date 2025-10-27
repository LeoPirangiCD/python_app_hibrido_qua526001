# Indíce de Massa Corporal (IMC)
import os
import time
import math

try:
    pass
    # Entrada de dados
    nome = (input("Informe o nome do usúario ").strip().title())
    peso = float(input("Informe o seu peso em kg: ").strip().replace(",","."))
    altura = float(input("Informe a sua altura em metros: ").strip().replace(",","."))
    
    # Cálculo do IMC
    imc = peso / (altura ** 2)
    
    # Limpa o console
    #os.system("cls")
    
    # Saída de dados
    print(f"{nome} seu IMC é: {imc:.2f}")
    
    # Classificação do IMC
    if imc < 18.5:
        print("Classificação: Abaixo do peso.")
    elif imc < 25:
        print("Classificação: Peso ideal.")
    elif imc < 30:
        print("Classificação: Acima do peso.")
    elif imc < 35:
        print("Classificação: Obesidade grau 1.")
    elif imc < 40:
        print("Classificação: Obesidade grau 2.")
    else:
        print("Classificação: Obesidade mórbita.")
except:
    print("Não foi possível calcular o IMC. Dados errados.")