import flet as ft


def main(page: ft.Page): 
    
    page.add( # Conteúdo da página
        ft.SafeArea( # Guarda os elementos do safeArea
            ft.Container( # Caixa onde se guarda os elementos
                ft.Text("Minha primeira aplicação.", size=40, weight="bold"), # ft.text() é o print do flex # Size=40 (Aumenta o tamanho da fonte do texto) # weight="bold" (Coloca o texto em negrito)
                alignment=ft.alignment.center, # Centralizar o texto na tela
            )
        ),
            ft.Container(
                ft.Image(
                    src="Anjo.jpg", 
                    fit=ft.ImageFit.CONTAIN,
                    error_content=ft.Text("Não foi ppssível carregar a imagem")
            ),
            alignment=ft.alignment.center,
            expand=True # Centralizador
        )
    )


ft.app(main) # Executa a aplicação
