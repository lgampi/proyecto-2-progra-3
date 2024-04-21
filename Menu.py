import tkinter as tk
from Modelo import GestorDeEstacion


class VentanaVentaTiquete(tk.Toplevel):  # tk.TopLevel permite crear una ventana separada a la principal
    ANCHO_DROPDOWN = 20

    def __init__(self, master):
        super().__init__(master)

        # Inicializacion de widgets

        self.dicc_opciones_tiquetes = None
        self.valor_segun_criterio = None
        self.valores_segun_criterio = None
        self.dropdown_valor_criterio = None
        self.etiqueta_valor_criterio = None
        self.dropdown_valor_criterio_var = None
        self.opciones_valor_criterio = None
        self.criterio_seleccionado = None
        self.etiqueta_tiquete = None
        self.opciones_tiquetes = None
        self.opciones_criterios_seleccion = None

        self.etiqueta_titulo = None
        self.titulo = None

        self.dropdown_criterio_seleccion_var = None
        self.dropdown_tiquetes_var = None

        self.boton_cerrar = None
        self.boton_guardar = None

        self.etiqueta_criterio_seleccion = None
        self.dropdown_criterio_seleccion = None
        self.etiqueta_tiquetes = None
        self.dropdown_tiquetes = None

        self.title("Venta de Tiquetes - Trenes S.A")
        self.mostrar_ventana()

    def mostrar_ventana(self):
        self.geometry(Menu.CONFIG_MENU["TAMANO_INICIAL"])

        self.titulo = "Seleccione las opciones correspondientes y de click en el botón de 'Guardar cambios'"
        self.etiqueta_titulo = tk.Label(self, text=self.titulo)
        self.etiqueta_titulo.pack(padx=Menu.CONFIG_MENU["PAD_X_BOTON"], pady=Menu.CONFIG_MENU["PAD_Y_BOTON"])
        self.geometry(Menu.CONFIG_MENU["TAMANO_INICIAL"])

        # Criterio de seleccion

        self.opciones_criterios_seleccion = Menu.GESTOR_ESTACION.get_criterios_seleccion()
        # Variables para almacenar las selecciones de los dropdowns
        self.dropdown_criterio_seleccion_var = tk.StringVar(self)
        self.dropdown_criterio_seleccion_var.set(self.opciones_criterios_seleccion[0])  # Valor por defecto
        self.criterio_seleccionado = self.opciones_criterios_seleccion[0]

        self.etiqueta_criterio_seleccion = tk.Label(self, text="Seleccione el criterio de filtrado:")
        self.etiqueta_criterio_seleccion.pack()

        self.dropdown_criterio_seleccion = tk.OptionMenu(self, self.dropdown_criterio_seleccion_var,
                                                         *self.opciones_criterios_seleccion)
        self.dropdown_criterio_seleccion.pack()
        self.dropdown_criterio_seleccion.config(width=VentanaVentaTiquete.ANCHO_DROPDOWN)

        # Le da segumiento al objeto del dropdown que selecciona los valores, para saber si cambiaron.
        self.dropdown_criterio_seleccion_var.trace("w", self.cambio_de_valor_de_dropdown_criterio)

        # Dropdown de valores, segun el criterio de seleccion.

        # Este metodo determina cual debe ser el valor default a seleccionar el segundo dropdown, y sus respectivos valores si el primer dropdown cambia
        self.valor_segun_criterio = None
        self.valores_segun_criterio = None
        if self.criterio_seleccionado == "Tren":
            self.valores_segun_criterio = Menu.GESTOR_ESTACION.obtener_matriculas_trenes()
            self.valor_segun_criterio = self.valores_segun_criterio[0]
        elif self.criterio_seleccionado == "Destino":
            self.valores_segun_criterio = Menu.GESTOR_ESTACION.get_destinos()
            self.valor_segun_criterio = self.valores_segun_criterio[0]
        elif self.criterio_seleccionado == "Horario":
            self.valores_segun_criterio = Menu.GESTOR_ESTACION.get_horarios()
            self.valor_segun_criterio = self.valores_segun_criterio[0]

        self.dropdown_valor_criterio_var = tk.StringVar(self)
        self.dropdown_valor_criterio_var.set(self.valor_segun_criterio)  # Valor por defecto
        self.etiqueta_valor_criterio = tk.Label(self, text="Seleccione el valor:")
        self.etiqueta_valor_criterio.pack()
        self.dropdown_valor_criterio = tk.OptionMenu(self, self.dropdown_valor_criterio_var,
                                                     *self.valores_segun_criterio)
        self.dropdown_valor_criterio.pack()
        self.dropdown_valor_criterio.config(width=VentanaVentaTiquete.ANCHO_DROPDOWN)
        # Le da segumiento al objeto del dropdown que selecciona los valores, para saber si cambiaron.
        self.dropdown_valor_criterio_var.trace("w", self.cambio_de_valor_de_dropdown_valores_crit)


        # Falta la parte de tiquetes



        # Botones
        self.boton_guardar = tk.Button(self, text="Guardar cambios", command=self.vender_tiquete)
        self.boton_guardar.pack()
        self.boton_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        self.boton_cerrar.pack()

    def actualizar_valores_dropdown_valores_crit(self):

        # Este metodo determina cual debe ser el valor default a seleccionar el segundo dropdown, y sus respectivos valores si el primer dropdown cambia
        self.valor_segun_criterio = None
        self.valores_segun_criterio = None
        if self.criterio_seleccionado == "Tren":
            self.valores_segun_criterio = Menu.GESTOR_ESTACION.obtener_matriculas_trenes()
            self.valor_segun_criterio = self.valores_segun_criterio[0]
        elif self.criterio_seleccionado == "Destino":
            self.valores_segun_criterio = Menu.GESTOR_ESTACION.get_destinos()
            self.valor_segun_criterio = self.valores_segun_criterio[0]
        elif self.criterio_seleccionado == "Horario":
            self.valores_segun_criterio = Menu.GESTOR_ESTACION.get_horarios()
            self.valor_segun_criterio = self.valores_segun_criterio[0]

        # Clear the existing menu
        self.dropdown_valor_criterio['menu'].delete(0, 'end')
        # Add new options
        for valores_criterio in self.valores_segun_criterio:
            self.dropdown_valor_criterio['menu'].add_command(label=valores_criterio,
                                                             command=tk._setit(self.dropdown_valor_criterio_var,
                                                                               valores_criterio))

        self.dropdown_valor_criterio_var.set(self.valor_segun_criterio)  # Valor por defecto

    def cambio_de_valor_de_dropdown_criterio(self, *args):  # *args se pone para evitar errores
        self.criterio_seleccionado = self.dropdown_criterio_seleccion_var.get()
        self.actualizar_valores_dropdown_valores_crit()

    def cambio_de_valor_de_dropdown_valores_crit(self, *args):  # *args se pone para evitar errores
        self.valor_segun_criterio = self.dropdown_valor_criterio_var.get()

    def vender_tiquete(self):
        print("Tamos vendiendo tiquetes")


class VentanaInsertarTiquetes(tk.Toplevel):  # tk.TopLevel permite crear una ventana separada a la principal
    ANCHO_DROPDOWN = 20

    def __init__(self, master):
        super().__init__(master)
        self.title("Insertar Tiquetes - Trenes S.A")

        # Inicializacion de widgets
        self.dropdown_can_tiquetes_var = None
        self.dropdown_horario_var = None
        self.dropdown_trenes_var = None
        self.dropdown_destino_var = None
        self.boton_cerrar = None
        self.boton_guardar = None
        self.dropdown_can_tiquetes = None
        self.etiqueta_can_tiquetes = None
        self.dropdown_horario = None
        self.etiqueta_horario = None
        self.dropdown_destino = None
        self.etiqueta_destino = None
        self.dropdown_trenes = None
        self.etiqueta_tren = None
        self.opciones_can_tiquetes = None
        self.opciones_horario = None
        self.opciones_destino = None
        self.opciones_trenes = None
        self.label = None
        self.mensaje = None

        self.mostrar_ventana()

    def mostrar_ventana(self):
        self.mensaje = "Seleccione las opciones correspondientes y de click en el botón de 'Guardar cambios'"
        self.label = tk.Label(self, text=self.mensaje)
        self.label.pack(padx=Menu.CONFIG_MENU["PAD_X_BOTON"], pady=Menu.CONFIG_MENU["PAD_Y_BOTON"])
        self.geometry(Menu.CONFIG_MENU["TAMANO_INICIAL"])

        # Dropdowns y etiquetas para insertar nuevos tiquetes.

        # Define los valores por defecto para los dropdowns

        self.opciones_trenes = Menu.GESTOR_ESTACION.obtener_matriculas_trenes()
        self.opciones_destino = Menu.GESTOR_ESTACION.get_destinos()
        self.opciones_horario = Menu.GESTOR_ESTACION.get_horarios()
        self.opciones_can_tiquetes = Menu.GESTOR_ESTACION.get_can_tiquetes()
        # Variables para almacenar las selecciones de los dropdowns
        self.dropdown_trenes_var = tk.StringVar(self)
        self.dropdown_trenes_var.set(self.opciones_trenes[0])  # Valor por defecto

        self.dropdown_destino_var = tk.StringVar(self)
        self.dropdown_destino_var.set(self.opciones_destino[0])  # Valor por defecto

        self.dropdown_horario_var = tk.StringVar(self)
        self.dropdown_horario_var.set(self.opciones_horario[0])  # Valor por defecto

        self.dropdown_can_tiquetes_var = tk.StringVar(self)
        self.dropdown_can_tiquetes_var.set(self.opciones_can_tiquetes[0])  # Valor por defecto

        self.etiqueta_tren = tk.Label(self, text="Matricula del tren:")
        self.etiqueta_tren.pack()

        self.dropdown_trenes = tk.OptionMenu(self, self.dropdown_trenes_var, *self.opciones_trenes)
        self.dropdown_trenes.pack()
        self.dropdown_trenes.config(width=VentanaInsertarTiquetes.ANCHO_DROPDOWN)

        self.etiqueta_destino = tk.Label(self, text="Destino:")
        self.etiqueta_destino.pack()

        self.dropdown_destino = tk.OptionMenu(self, self.dropdown_destino_var, *self.opciones_destino)
        self.dropdown_destino.pack()
        self.dropdown_destino.config(width=VentanaInsertarTiquetes.ANCHO_DROPDOWN)

        self.etiqueta_horario = tk.Label(self, text="Horario:")
        self.etiqueta_horario.pack()

        self.dropdown_horario = tk.OptionMenu(self, self.dropdown_horario_var, *self.opciones_horario)
        self.dropdown_horario.pack()
        self.dropdown_horario.config(width=VentanaInsertarTiquetes.ANCHO_DROPDOWN)

        self.etiqueta_can_tiquetes = tk.Label(self, text="Cantidad de tiquetes:")
        self.etiqueta_can_tiquetes.pack()

        self.dropdown_can_tiquetes = tk.OptionMenu(self, self.dropdown_can_tiquetes_var, *self.opciones_can_tiquetes)
        self.dropdown_can_tiquetes.pack()
        self.dropdown_can_tiquetes.config(width=VentanaInsertarTiquetes.ANCHO_DROPDOWN)

        # Botones
        self.boton_guardar = tk.Button(self, text="Guardar cambios", command=self.guardar_cambios)
        self.boton_guardar.pack()
        self.boton_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        self.boton_cerrar.pack()

    def guardar_cambios(self):
        # Obtiene los valores seleccionados de los dropdowns gracias al metodo .get()
        matricula_tren = self.dropdown_trenes_var.get()
        destino = self.dropdown_destino_var.get()
        horario = self.dropdown_horario_var.get()
        can_tiquetes = self.dropdown_can_tiquetes_var.get()
        Menu.GESTOR_ESTACION.insertar_tiquetes(int(can_tiquetes), matricula_tren, destino, horario)


class Menu(tk.Tk):  # La clase menu es heredada de la clase tk.Tk

    # atributos de clase (también son constantes), para la interfaz visual (almacenados en un diccionario cons)
    CONFIG_MENU = {
        "TAM_TITULO_PRINCIPAL": 18,
        "TAM_SUBTITULO": 14,
        "TAM_TEXTO_1": 12,
        "PAD_Y_BOTON": 15,
        "PAD_X_BOTON": 20,
        "TAMANO_INICIAL": "1200x450"
    }

    GESTOR_ESTACION = GestorDeEstacion()

    def __init__(self, nombre_ventana=None):  # Constructor
        super().__init__()  # LLamando al constructor de la clase padre
        self.__ventana_venta_tiquetes_visible = False
        self.__ventana_venta_tiquetes = None
        self.__ventana_insertar_tiquetes_visible = False
        self.__ventana_insertar_tiquetes = None
        self.dibujar_ventana_principal(nombre_ventana)

    def dibujar_ventana_principal(self, nombre_ventana):
        self.title(nombre_ventana)  # metodo de la clase padre
        self.geometry(Menu.CONFIG_MENU["TAMANO_INICIAL"])  # Establece el tamañno inicial
        texto_titulo_mp = "Bienvenido a Trenes S.A"
        titulo_menu_principal = tk.Label(self, text=texto_titulo_mp,
                                         font=("Arial", Menu.CONFIG_MENU["TAM_TITULO_PRINCIPAL"]))
        titulo_menu_principal.pack()

        texto_subtitulo_mp = "Seleccione una opción:"
        subtitulo_menu_principal = tk.Label(self, text=texto_subtitulo_mp,
                                            font=("Arial", Menu.CONFIG_MENU["TAM_SUBTITULO"]))
        subtitulo_menu_principal.pack()

        # Espacio entre el subtitulo y el marco de botones
        espacio_menu_principal_1 = tk.Label(self, text="")
        espacio_menu_principal_1.pack()

        marco_botones_menu_principal = tk.Frame(self)  # crea un frame independiente para montar los botones sobre este
        marco_botones_menu_principal.pack()

        # Creación de los botones
        boton_1_menu_principal_msj = "Vender tiquete(s) a usuario"
        boton_1_menu_principal = tk.Button(marco_botones_menu_principal, text=boton_1_menu_principal_msj,
                                           command=self.mostrar_ventana_venta_tiquetes)
        boton_1_menu_principal.pack(side=tk.LEFT,
                                    padx=Menu.CONFIG_MENU["PAD_X_BOTON"])  # padx -> Ajusta la distancia horizontal
        # entre los botones

        boton_2_menu_principal_msj = "Insertar tiquetes para venta"
        boton_2_menu_principal = tk.Button(marco_botones_menu_principal, text=boton_2_menu_principal_msj,
                                           command=self.mostrar_ventana_insertar_tiquetes)
        boton_2_menu_principal.pack(side=tk.LEFT, padx=Menu.CONFIG_MENU["PAD_X_BOTON"])

        boton_3_menu_principal_msj = "Consultar cantidad de tiquetes disponibles por localización"
        boton_3_menu_principal = tk.Button(marco_botones_menu_principal,
                                           text=boton_3_menu_principal_msj)
        boton_3_menu_principal.pack(side=tk.LEFT, padx=Menu.CONFIG_MENU["PAD_X_BOTON"])

        boton_4_menu_principal_msj = "Consultar horario de trenes de hoy"
        boton_4_menu_principal = tk.Button(marco_botones_menu_principal, text=boton_4_menu_principal_msj)
        boton_4_menu_principal.pack(side=tk.LEFT, padx=Menu.CONFIG_MENU["PAD_X_BOTON"])

    def mostrar_ventana_venta_tiquetes(self):
        if self.__ventana_venta_tiquetes_visible is False:
            self.__ventana_venta_tiquetes = VentanaVentaTiquete(self)
            self.__ventana_venta_tiquetes_visible = True
        else:
            self.__ventana_venta_tiquetes_visible = False
            self.__ventana_venta_tiquetes = None

    def mostrar_ventana_insertar_tiquetes(self):
        if self.__ventana_insertar_tiquetes_visible is False:
            self.__ventana_insertar_tiquetes = VentanaInsertarTiquetes(self)
            self.__ventana_insertar_tiquetes = True
        else:
            self.__ventana_insertar_tiquetes_visible = False
            self.__ventana_insertar_tiquetes = None
