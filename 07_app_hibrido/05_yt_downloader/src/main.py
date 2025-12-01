import flet as ft
from pytubefix import YouTube

import os
import threading


def main(page: ft.Page):
    page.title = "YouTube Downloader"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.icon = "assets/youtube.png"
    
    # Crias as pastas caso não existam
    caminho_videos = "videos"
    caminho_audios = "audios"
    os.makedirs(caminho_videos, exist_ok=True)
    os.makedirs(caminho_audios, exist_ok=True)

    # Componentes da interface gráfica
    titulo = ft.Text("Use uma URL", color=ft.Colors.BLACK, size=20, weight=ft.FontWeight.BOLD)
    url = ft.TextField(
        label="Cole a URL do vídeo do YouTube aqui: ",
        widh=400,
        border_radius=10
        )
    
    base_path = os.path.dirname(__file__)
    logo_path = os.path.join(base_path, "assets", "youtube.png")
    logo_cabecalho = ft.Image(src=logo_path, width=300, height=200)

    # Componente para mostrar informações do vídeo
    video_info = ft.Container(
        content=ft.Column([]),
        visible=False,
        padding=10,
        bgcolor=ft.Colors.BLUE_GREY_50,
        border_radius=10,
        width=400,
    )
    # Barra de progresso
    progress_bar = ft.ProgressBar(
        visible=False,
        width=400,
        color=ft.Colors.BLUE,
        bgcolor=ft.Colors.BLUE_GREY_100
    )

    # Texto de status
    status_text = ft.Text(
        "",
        color=ft.Colors. BLACK,
        size=14,
        text_align=ft.TextAlign.CENTER
    )

    # Mostra as informações de vídeo na interfase
    def mostrar_info_videos(yt):
        try:
            # Limpar container
            video_info.content.controls.clear()
            # Adiciona informações do vídeo
            video_info.content.controls.extend(
                [
                    ft.Text(f"Título: {yt.title}", size=14, weigth=ft.FontWeight.BOLD),
                    ft.Text(f"Canal: {yt.author}", size=12),
                    ft.Text(f"Duração: {yt.length/60}:{yt.length%60:02d}", size=12),
                    ft.Text(f"Visualizações:  {yt.views:,}", size=12),
                ]
            )
            video_info.visible = True
            page.update()
            
        except Exception as e:
            status_text.values = f"Erro ao obter informações: {str(e)}."
            status_text.color = ft.Colors.RED
            page.update()

    # Função para baixar o vídeo
    def baixar_video(e):
        if not url.values.strip():
            status_text.value = "Por favor, insira uma URl válida."
            status_text.value = ft.Colors.ORANGE
            page.update()

        def download_thread():
            try:
                # Mostra o progresso
                progress_bar.visible = True
                status_text.value = "Analisando vídeo..."
                status_text.color = ft.Colors.RED
                page.update()

            # Cria o objeto do Youtube
                yt = YouTube(url.value.strip())
            # Mostrar informações do vídeo
                mostrar_info_videos(yt)
            # Inicia o Donwload
                status_text.value = f"Baixando vídeo: {yt.title}..."
                page.update()
            # Pega a maior resolução possível
                stream = yt.streams.get_highest_resolution()

            except Exception as e:
                progress_bar.visible = False
                status_text.value = f"Erro {str(e)}."
                status_text.value = ft.Colors.RED
                page.update()

            threading.Thread(tardet=download_thread, daemon=True).start()

    page.add(
        ft.SafeArea(
            ft.Container(

                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
