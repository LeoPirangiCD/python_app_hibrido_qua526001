# Biblioteca
import os
import math
import time

# Função
def limpar():
    os.system("cls")

# Funções de cálculo
def quadrado(l):
    return l**2
def retangulo(b,h):
    return b*h
def triangulo(b, h):
    return (b*h)/2
def hipotenusa(b, h):
    return math.sqrt((b**2) + (h**2))

# TODO: Atividade crie uma nova função para calcular a hipotenusa do triângulo-retangulho

# Algoritmo principal
limpar()
while True:
# Menu
    print("1 - Calcular quadrado")
    print("2 - Calcular retângulo")
    print("3 - Calcular triângulo")
    print("4 - Calcular a hipotenusa: ")
    print("5 - Sair do programa: ")

    opcao = input("\nInforme a opção desejada: ").strip()
    limpar()
    match opcao:
        case "1":
            l = float(input("Informe o lado do quadrado: ").strip().replace(",","."))
            resultado = quadrado(l)
            limpar()
            print(f"\nÁrea do quadrado: {resultado}\n")
            continue
        case "2":
            b = float(input("Informe a base do retângulo: ").strip().replace(",","."))
            h = float(input("Informe a altura do retângulo: ").strip().replace(",","."))
            resultado = retangulo(b, h)
            limpar()
            print(f"\nÁrea do tringulo é: {resultado}\n")
        case "3":
            b = float(input("Informe base do triângulo: ").strip().replace(",","."))
            h = float(input("Informe a altura do triângulo: ").strip().replace(",","."))
            resultado = triangulo(b, h)
            limpar()
            print(f"\nÁrea do triângulo é: {resultado}\n")
            continue
        case "4":
            b = float(input("Informe base da hipotenusa: ").strip().replace(",","."))
            h = float(input("Informe a altura da hipotenusa: ").strip().replace(",","."))
            resultado = hipotenusa(b,h)
            limpar()
            print(f"\nÁrea do triangulo-retângulo é: {resultado:.2f}\n") # round{resultado, 2}
        case "5":
            time = 0
            while time < 5:
                time += 1
                print(time)
                continue
                print("Encerrando programa.")
            break
        case _:
            print("\nOpção Inválida. Tente de novo!\n")
            continue

    

    
