# biblioteca
import os

# classe
class Pessoa:
    # atributos
    nome = "Alex Machado"
    idade = 40
    email = "alex@gmail.com"

    # método
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"E-mail: {self.email}")

if __name__ == "__main__":
    # instancia a classe (cria novo objeto)
    usuario = Pessoa()

    # limpa console
    os.system("cls" if os.name == "nt" else "clear")

    # saída de dados
    usuario.exibir_dados()