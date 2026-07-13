import pytest
from playwright.sync_api import Page
from pages.mi_pagina import MiPagina


# ============================================================
# PRUEBA 1: Título principal
# ============================================================
def test_titulo_principal(page: Page):
    """Prueba que el título de la página sea correcto"""
    mi_pagina = MiPagina(page)
    mi_pagina.abrir()
    mi_pagina.verificar_titulo("🎉 ¡Hola, Robedo!")


# ============================================================
# PRUEBA 2: Perrito visible
# ============================================================
def test_perrito_visible(page: Page):
    """Prueba que la imagen del perrito se cargue"""
    mi_pagina = MiPagina(page)
    mi_pagina.abrir()
    mi_pagina.verificar_perrito_visible()


# ============================================================
# PRUEBA 3: Formulario de recomendación
# ============================================================
def test_formulario_envio(page: Page):
    """Prueba que el formulario se pueda enviar y muestre el mensaje de agradecimiento"""
    mi_pagina = MiPagina(page)
    mi_pagina.abrir()
    
    mi_pagina.enviar_recomendacion(
        nombre="Robedo",
        juego="Elden Ring",
        genero="RPG",
        jugado_si=True,
        comentario="¡Es un juegazo!"
    )


# ============================================================
# PRUEBA 4: Verificar la tabla de horario
# ============================================================
def test_tabla_horario(page: Page):
    """Prueba que la tabla del horario exista y tenga los datos correctos"""
    mi_pagina = MiPagina(page)
    mi_pagina.abrir()
    mi_pagina.verificar_tabla()


# ============================================================
# PRUEBA 5: Verificar la lista de juegos (Top 3)
# ============================================================
def test_lista_juegos(page: Page):
    """Prueba que la lista de juegos exista y tenga los elementos correctos"""
    mi_pagina = MiPagina(page)
    mi_pagina.abrir()
    mi_pagina.verificar_lista_juegos()


# ============================================================
# PRUEBA 6: Verificar la lista de cosas favoritas
# ============================================================
def test_lista_favoritos(page: Page):
    """Prueba que la lista de cosas favoritas exista y tenga los elementos correctos"""
    mi_pagina = MiPagina(page)
    mi_pagina.abrir()
    mi_pagina.verificar_lista_favoritos()


# ============================================================
# PRUEBA 7: Verificar el enlace a TikTok
# ============================================================
def test_enlace_tiktok(page: Page):
    """Prueba que el enlace a TikTok exista y tenga el texto correcto"""
    mi_pagina = MiPagina(page)
    mi_pagina.abrir()