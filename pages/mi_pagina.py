from playwright.sync_api import Page, expect


class MiPagina:
    """
    Page Object para la página web de Robedo.
    Contiene localizadores y acciones de la página.
    """
    
    # ============================================================
    # 1. URL de la página
    # ============================================================
    URL = "https://robedo111-create.github.io/mi-primera-pagina-web/"
    
    # ============================================================
    # 2. Localizadores (Selectores)
    # ============================================================
    
    # Título principal
    TITULO = "h1"
    
    # Perrito
    PERRITO_IMG = "img.perrito-img"
    
    # Tabla de horario
    TABLA = "table"
    FILAS_TABLA = "table tr"
    ENCABEZADOS_TABLA = "table th"
    CELDAS_TABLA = "table td"
    
    # Lista de juegos (Top 3) - buscamos por el <ol> que está después del h2
    LISTA_JUEGOS = "h2:has-text('Top 3 de juegos que quiero jugar') + ol"
    ITEMS_JUEGOS = "h2:has-text('Top 3 de juegos que quiero jugar') + ol li"
    
    # Lista de favoritos
    LISTA_FAVORITOS = "h2:has-text('Mis cosas favoritas') + ul"
    ITEMS_FAVORITOS = "h2:has-text('Mis cosas favoritas') + ul li"
    
    # Enlace a TikTok
    ENLACE_TIKTOK = "a[href*='tiktok.com']"
    
    # Formulario
    CAMPO_NOMBRE = "#nombre"
    CAMPO_JUEGO = "#juego"
    SELECCION_GENERO = "#genero"
    RADIO_JUGADO_SI = 'input[name="jugado"][value="Sí"]'
    RADIO_JUGADO_NO = 'input[name="jugado"][value="No"]'
    AREA_COMENTARIO = "#comentario"
    BOTON_ENVIAR = "button[type='submit']"
    MENSAJE_GRACIAS = "#mensajeGracias"
    
    # ============================================================
    # 3. Constructor
    # ============================================================
    
    def __init__(self, page: Page):
        self.page = page
    
    # ============================================================
    # 4. Acciones (Métodos)
    # ============================================================
    
    def abrir(self):
        """Abre la página web"""
        self.page.goto(self.URL)
    
    # --- Título ---
    def obtener_titulo(self):
        """Devuelve el elemento del título principal"""
        return self.page.locator(self.TITULO)
    
    def verificar_titulo(self, texto_esperado: str):
        """Verifica que el título tenga el texto esperado"""
        expect(self.obtener_titulo()).to_have_text(texto_esperado)
    
    # --- Perrito ---
    def obtener_perrito(self):
        """Devuelve el elemento de la imagen del perrito"""
        return self.page.locator(self.PERRITO_IMG)
    
    def verificar_perrito_visible(self):
        """Verifica que la imagen del perrito sea visible y tenga src"""
        perrito = self.obtener_perrito()
        expect(perrito).to_be_visible()
        src = perrito.get_attribute("src")
        assert src is not None and src != "", "La imagen no tiene fuente"
    
    # --- Tabla ---
    def obtener_tabla(self):
        """Devuelve el elemento de la tabla"""
        return self.page.locator(self.TABLA)
    
    def obtener_filas_tabla(self):
        """Devuelve todas las filas de la tabla"""
        return self.page.locator(self.FILAS_TABLA)
    
    def obtener_encabezados_tabla(self):
        """Devuelve los encabezados de la tabla"""
        return self.page.locator(self.ENCABEZADOS_TABLA)
    
    def obtener_celda(self, fila: int, columna: int):
        """Devuelve una celda específica de la tabla"""
        return self.page.locator(self.FILAS_TABLA).nth(fila).locator(self.CELDAS_TABLA).nth(columna)
    
    def verificar_tabla(self):
        """Verifica que la tabla tenga los datos correctos"""
        tabla = self.obtener_tabla()
        expect(tabla).to_be_visible()
        
        # Verificar cantidad de filas (1 encabezado + 3 datos)
        filas = self.obtener_filas_tabla()
        expect(filas).to_have_count(4)
        
        # Verificar encabezados
        encabezados = self.obtener_encabezados_tabla()
        expect(encabezados.nth(0)).to_have_text("Hora")
        expect(encabezados.nth(1)).to_have_text("Jueves")
        expect(encabezados.nth(2)).to_have_text("Viernes")
        
        # --- ARREGLO: Usar la primera fila de la tabla (índice 1) ---
        # Primera fila de datos (tr[1])
        primera_fila = filas.nth(1)
        celdas = primera_fila.locator("td")
        
        expect(celdas.nth(0)).to_have_text("9:00 AM")
        expect(celdas.nth(1)).to_have_text("Hacer ejercicio")
        expect(celdas.nth(2)).to_have_text("Tomar el transporte")
    
    # --- Lista de juegos ---
    def obtener_lista_juegos(self):
        """Devuelve la lista ordenada de juegos"""
        return self.page.locator(self.LISTA_JUEGOS)
    
    def obtener_items_juegos(self):
        """Devuelve todos los items de la lista de juegos"""
        return self.page.locator(self.ITEMS_JUEGOS)
    
    def verificar_lista_juegos(self):
        """Verifica que la lista de juegos tenga los datos correctos"""
        lista = self.obtener_lista_juegos()
        expect(lista).to_be_visible()
        
        items = self.obtener_items_juegos()
        expect(items).to_have_count(3)
        
        expect(items.nth(0)).to_have_text("Elden Ring")
        expect(items.nth(1)).to_have_text("The Legend of Zelda")
        expect(items.nth(2)).to_have_text("Cyberpunk 2077")
    
    # --- Lista de favoritos ---
    def obtener_lista_favoritos(self):
        """Devuelve la lista desordenada de favoritos"""
        return self.page.locator(self.LISTA_FAVORITOS)
    
    def obtener_items_favoritos(self):
        """Devuelve todos los items de la lista de favoritos"""
        return self.page.locator(self.ITEMS_FAVORITOS)
    
    def verificar_lista_favoritos(self):
        """Verifica que la lista de favoritos tenga los datos correctos"""
        lista = self.obtener_lista_favoritos()
        expect(lista).to_be_visible()
        
        items = self.obtener_items_favoritos()
        expect(items).to_have_count(5)
        
        favoritos_esperados = [
            "🎮 Videojuegos",
            "🎵 Música",
            "🎉 Fiestas",
            "☕ Café",
            "🍕 Pizza"
        ]
        
        for i, texto in enumerate(favoritos_esperados):
            expect(items.nth(i)).to_contain_text(texto)
    
    # --- Enlace a TikTok ---
    def obtener_enlace_tiktok(self):
        """Devuelve el enlace a TikTok"""
        return self.page.locator(self.ENLACE_TIKTOK)
    
    def verificar_enlace_tiktok(self):
        """Verifica que el enlace a TikTok exista y sea correcto"""
        enlace = self.obtener_enlace_tiktok()
        expect(enlace).to_be_visible()
        expect(enlace).to_have_text("TikTok")
        
        target = enlace.get_attribute("target")
        assert target == "_blank", "El enlace debería abrir en una nueva pestaña"
    
    # --- Formulario ---
    def llenar_formulario(self, nombre: str, juego: str, genero: str, jugado_si: bool, comentario: str):
        """Llena el formulario de recomendación con los datos proporcionados"""
        self.page.fill(self.CAMPO_NOMBRE, nombre)
        self.page.fill(self.CAMPO_JUEGO, juego)
        self.page.select_option(self.SELECCION_GENERO, genero)
        
        if jugado_si:
            self.page.check(self.RADIO_JUGADO_SI)
        else:
            self.page.check(self.RADIO_JUGADO_NO)
        
        self.page.fill(self.AREA_COMENTARIO, comentario)
    
    def enviar_formulario(self):
        """Hace clic en el botón de enviar"""
        self.page.click(self.BOTON_ENVIAR)
    
    def verificar_mensaje_agradecimiento(self, nombre_esperado: str):
        """Verifica que el mensaje de agradecimiento sea visible y contenga el nombre"""
        mensaje = self.page.locator(self.MENSAJE_GRACIAS)
        expect(mensaje).to_be_visible()
        expect(mensaje).to_contain_text(nombre_esperado)
    
    def enviar_recomendacion(self, nombre: str, juego: str, genero: str, jugado_si: bool, comentario: str):
        """
        Acción completa: llena el formulario, lo envía y verifica el mensaje.
        """
        self.llenar_formulario(nombre, juego, genero, jugado_si, comentario)
        self.enviar_formulario()
        self.verificar_mensaje_agradecimiento(nombre)