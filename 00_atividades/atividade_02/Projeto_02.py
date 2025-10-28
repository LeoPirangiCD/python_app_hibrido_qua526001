# Biblioteca
import os
import time
try:  
# Variáveis
    tempo = int(input("Insira um número inteiro: ").strip())
# Entrada de dados
    print("Iniciando contagem regressiva: {tempo}")
# Laço de Repetição
    while tempo >= 0:
        os.system("cls")
        print(tempo)
        time.sleep(1)
        tempo -= 1
        
    
    print("Contagem regressiva finalizada!")


except:
    print("Não foi possivel executar o contador.")
