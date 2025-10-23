# Entrada de dados
aluno = input("Informe o nome do aluno: ").strip().title()
nota = float(input("Informe a nota: ").strip().replace(',', '.'))

# verificar a nota do aluno
if nota >= 0 and nota <= 10:
    if nota >= 7:
         print(f"Parabéns {aluno}! Você foi aprovado com a nota {nota:.1f}.")
    elif nota >= 5:
         print(f"{aluno}, você está de recuperação com a nota {nota:.1f}.")
    else:
         print(f"{aluno}, você foi reprovado com a nota {nota:.1f}.")
else:
    print("Nota inválida! A nota deve estar entre 0 e 10.")