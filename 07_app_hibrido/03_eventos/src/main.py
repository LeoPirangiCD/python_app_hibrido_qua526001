# Programação voltada a eventos
import flet as ft

def main(page: ft.Page):
    # função evento
    def exibir_nome(e):
        nome_saida.value = nome.value
        nome_saida.update()
    # Propriedades da página
    page.title = "App de manipulação de eventos"
    page.scroll = "adaptive" # page.scroll = Alterar a barra de rolagem # adaptative = Deixá-la adaptável
    page.theme_mode = ft.ThemeMode.LIGHT # page.theme_mode = Alterar a cor da página para branco, se fosse preto, seria DARK

    # Declaração de variáveis
    nome = ft.TextField(label="Informe seu nome", on_submit=exibir_nome) # label = não apaga o comando "Informe seu nome" # on_submit = ativa o botao enter
    nome_saida=ft.Text("")
    
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Trabalhando com Eventos", size=50, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        ft.Container(
            ft.Text("Leonardo Pirangi", size=45, weight="bold"),
            alignment=ft.alignment.center,
            ),
        nome,
        ft.ElevatedButton("Enviar", on_click=exibir_nome), 
        nome_saida
    ),  
            


ft.app(main)
