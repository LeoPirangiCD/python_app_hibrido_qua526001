# Biblioteca
import math

#Entrada de dados
r = float(input("Informe o valor do raio de um círculo: ").strip().replace(",","."))

# Cálculos
a = math.pi*(r**2)
c = 2*math.pi*r


# Saída de dados


print(f"Número do pi: {math.pi}")
print(f"Área da cincunferência: {a:.2f}")
print(f"Tamanho da cincunferência: {c:.2f}")


