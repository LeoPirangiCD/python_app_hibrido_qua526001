import flet as ft

# Cria Evento
def main(page: ft.Page): 
    def calcular_combustivel(e):
        if not gasolina.value:
            gasolina.error_text = "Valor da gasolina não pode ficar vazio."
            page.update()
        else:
            gasolina.error_text = ""
            page.update()

        if not etanol.value:
            etanol.error_text = "Valor do etanol não pode ficar vazio."
            page.update()
        else:
            etanol.error_text = ""

            gasolina.value = float(gasolina.value.replace(",","."))
            etanol.value = float(etanol.value.replace(",","."))
            resultado = "Gasolina" if etanol.value >= gasolina.value*0.7 else "Etanol"
            dlg_modal.content.value = resultado
            gasolina.value = ""
            etanol.value = ""

            page.open(dlg_modal) # Aciona o Enter para mudar de TexField
            
            page.update()

    page.title = "App Flex Fuel"
    page.scroll = "adaptative"
    page.theme_mode = ft.ThemeMode.LIGHT # Deixar a tela da página na cor branca # DARK na cor preta
    page.window.min_width=100

# Variáveis
    gasolina = ft.TextField(
        label = "Valor da gasolina",
        prefix_text="R$",
        keyboard_type=ft.KeyboardType.NUMBER # Abrir o teclado numérico no celular
    )
    etanol = ft.TextField(
        label = "Valor do etanol",
        prefix_text="R$",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_submit=calcular_combustivel
    )
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Melhor abastecer com: "),
        content=ft.Text(size=35, weight="bold"),
        actions=[ft.TextButton("OK", on_click=lambda e:page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("FLEX FUEL", size=35, weight="bold"),
                alignment=ft.alignment.center,
                padding=10
                ),
            ),
        
            #expand=True,
            ft.Container(
                ft.Image(
                    src="Tanque.jpg", 
                    #width=100000,
                    #height=100000,
                    fit=ft.ImageFit.CONTAIN,
                    #border_radius=ft.border_radius.horizontal(10000000, 10000000),
                    error_content=ft.Text("Não foi possível carregar a imagem"),
                    
                                       
            ),
                alignment=ft.alignment.center,
                #expand=True # Centralizador
        ),
        ft.ResponsiveRow( # Mantém os mesmo parametros da tela original para as outras telas
            [
                ft.Container(gasolina, col={"sm": 6, "md":4, "xl":2}),
                ft.Container(etanol, col={"sm": 6, "md":4, "xl":2})
            ],
            alignment=ft.MainAxisAlignment.CENTER # Centraliza as TexField independente do formato da tela # Isso que é comando Híbrido
        ),
        ft.Row(
            [
                ft.Container(
                    ft.ElevatedButton("Calcular", on_click=calcular_combustivel),
                    padding=30, # Margem interna de 30
                        
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    )


ft.app(main)
