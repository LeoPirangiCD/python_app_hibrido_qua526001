import flet as ft


def main(page: ft.Page):
    page.title = "App Flex Fuel"
    page.scroll = "adaptative"
    page.theme_mode = ft.ThemeMode. LIGHT

# Variáveis
    gasolina = ft.TextField(
        label = "Valor da gasolina",
        prefix_text="R$",
        keyboard_type=ft.KeyboardType.NUMBER # Abrir o teclado numérico no celular
    )
    etanol = ft.TextField(
        label = "Valor do etanol",
        prefix_text="R$",
        keyboard_type=ft.KeyboardType.NUMBER
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
                )
            #expand=True,
        ),
        ft.ResponsiveRow( # Mantém os mesmo parametros da tela original para as outras telas
            [
                ft.Container(gasolina, col={"sm": 6, "md":4, "xl":2}),
                ft.Container(etanol, col={"sm": 6, "md":4, "xl":2})

            ]
        )
    )


ft.app(main)
