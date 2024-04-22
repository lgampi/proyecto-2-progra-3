import tkinter as tk
from Modelo import GestorDeEstacion


class VentanaVentaTiquete(tk.Toplevel):  # tk.TopLevel permite crear una ventana separada a la principal
    ANCHO_DROPDOWN = 20

    def __init__(self, master):
        try:
            super().__init__(master)
            # Inicializacion de widgets

            self.tiquete_a_vender = None
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
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def mostrar_ventana(self):
        try:
            self.geometry(Menu.CONFIG_MENU["TAMANO_INICIAL"])

            # Criterio de seleccion

            self.opciones_criterios_seleccion = Menu.GESTOR_ESTACION.get_criterios_seleccion()
            # Variables para almacenar las selecciones de los dropdowns
            self.dropdown_criterio_seleccion_var = tk.StringVar(self)
            self.dropdown_criterio_seleccion_var.set(self.opciones_criterios_seleccion[0])  # Valor por defecto
            self.criterio_seleccionado = self.opciones_criterios_seleccion[0]

            self.etiqueta_criterio_seleccion = tk.Label(self, text="Seleccione el criterio de filtrado:")

            self.dropdown_criterio_seleccion = tk.OptionMenu(self, self.dropdown_criterio_seleccion_var,
                                                             *self.opciones_criterios_seleccion)

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

            self.dropdown_valor_criterio = tk.OptionMenu(self, self.dropdown_valor_criterio_var,
                                                         *self.valores_segun_criterio)

            self.dropdown_valor_criterio.config(width=VentanaVentaTiquete.ANCHO_DROPDOWN)
            # Le da segumiento al objeto del dropdown que selecciona los valores, para saber si cambiaron.
            self.dropdown_valor_criterio_var.trace("w", self.cambio_de_valor_de_dropdown_valores_crit)

            # Tiquetes

            # Se retorna un diccionario de la forma:
            """
            {
                "llave_1": [tiquete_1,tiquete_2,tiquete_3...],
                "llave_2": [tiquete_10,tiquete_11,tiquete_12...],
            }
            Donde las llaves pueden ser: Numero de placa de tren ó lugar de destino ó hora de salida.
            """
            self.dicc_opciones_tiquetes = Menu.GESTOR_ESTACION.obtener_tiquetes_no_vendidos(self.criterio_seleccionado)

            llave_opciones_tiquetes = self.valor_segun_criterio
            # Se espera que los valores segun el criterio, sean las mismas llaves que agrupan al diccionario de tiquetes.
            # Ejemplo: Si los trenes son [5001,5002], se espera que las llaves igualmente sean 5001 y 5002.

            # List comprehension para componer una lista de numeros de tiquetes basados en la lista de tiquetes
            self.opciones_tiquetes = [tiquete.__str__() for tiquete in
                                      self.dicc_opciones_tiquetes[llave_opciones_tiquetes]]
            primer_elemento_lista = None
            mostrar = True
            if len(self.opciones_tiquetes) > 0:  # Debe haber al menos un tiquete registrado
                primer_elemento_lista = self.opciones_tiquetes[
                    0]  # El primer elemento de la lista accedida por medio de la llave del diccionario.
            else:
                mostrar = False

            if mostrar:  # Si no hay ni un solo tiquete leido del archivo, no se deben mostrar las opciones.
                self.titulo = "Seleccione las opciones correspondientes y de click en el botón de 'Crear tiquetes'"
                self.etiqueta_titulo = tk.Label(self, text=self.titulo)
                self.etiqueta_titulo.pack(padx=Menu.CONFIG_MENU["PAD_X_BOTON"], pady=Menu.CONFIG_MENU["PAD_Y_BOTON"])
                self.geometry(Menu.CONFIG_MENU["TAMANO_INICIAL"])

                self.tiquete_a_vender = primer_elemento_lista
                self.dropdown_tiquetes_var = tk.StringVar(self)

                self.dropdown_tiquetes_var.set(primer_elemento_lista)  # Valor por defecto
                self.etiqueta_tiquete = tk.Label(self, text="Seleccione el tiquete a vender:")

                self.dropdown_tiquetes = tk.OptionMenu(self, self.dropdown_tiquetes_var, *self.opciones_tiquetes)

                self.dropdown_tiquetes.config(width=VentanaVentaTiquete.ANCHO_DROPDOWN)
                self.dropdown_tiquetes_var.trace("w", self.cambio_de_valor_de_tiquete)

                # Botones
                self.boton_guardar = tk.Button(self, text="Vender tiquete seleccionado", command=self.vender_tiquete)

                self.etiqueta_criterio_seleccion.pack()
                self.dropdown_criterio_seleccion.pack()
                self.etiqueta_valor_criterio.pack()
                self.dropdown_valor_criterio.pack()
                self.etiqueta_tiquete.pack()
                self.dropdown_tiquetes.pack()
                self.boton_guardar.pack()
                self.boton_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
                self.boton_cerrar.pack()
            else:
                self.titulo = "Debe haber al menos un tiquete registrado para la venta!"
                self.etiqueta_titulo = tk.Label(self, text=self.titulo)
                self.etiqueta_titulo.pack(padx=Menu.CONFIG_MENU["PAD_X_BOTON"], pady=Menu.CONFIG_MENU["PAD_Y_BOTON"])
                self.geometry(Menu.CONFIG_MENU["TAMANO_INICIAL"])
                self.boton_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
                self.boton_cerrar.pack()

                raise Exception("Debe haber al menos un tiquete registrado para usar esta opcion")


        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def actualizar_valores_dropdown_valores_crit(self):
        try:
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
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def cambio_de_valor_de_dropdown_criterio(self, *args):  # *args se pone para evitar errores
        try:
            self.criterio_seleccionado = self.dropdown_criterio_seleccion_var.get()
            self.actualizar_valores_dropdown_valores_crit()
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def cambio_de_valor_de_dropdown_valores_crit(self, *args):  # *args se pone para evitar errores

        try:
            self.valor_segun_criterio = self.dropdown_valor_criterio_var.get()
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def cambio_de_valor_de_tiquete(self, *args):

        try:
            self.tiquete_a_vender = self.dropdown_tiquetes_var.get()
            print(f"Tiquete seleccionado: {self.tiquete_a_vender}")
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def vender_tiquete(self):
        try:
            num_tiquete_a_vender = None
            if self.tiquete_a_vender is not None:
                num_tiquete_a_vender = self.tiquete_a_vender.split(",")[
                    0]  # Un ejemplo del string esperado es el siguiente: 1,5001,Heredia,6:00AM
                # donde 1 es el num de tiquete, 5001 la matricula del tren, Heredia el destino y 6:00AM la hora de salida.
            if num_tiquete_a_vender is not None:
                print(f"Se ha registrado el tiquete con el numero {num_tiquete_a_vender} para venta")
                Menu.GESTOR_ESTACION.vender_tiquete(num_tiquete_a_vender)

            print(f"Tiquete: {self.tiquete_a_vender} vendido!")
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")


class VentanaInsertarTiquetes(tk.Toplevel):  # tk.TopLevel permite crear una ventana separada a la principal
    ANCHO_DROPDOWN = 20

    def __init__(self, master):
        try:
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
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def mostrar_ventana(self):
        try:
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
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def guardar_cambios(self):
        try:
            # Obtiene los valores seleccionados de los dropdowns gracias al metodo .get()
            matricula_tren = self.dropdown_trenes_var.get()
            destino = self.dropdown_destino_var.get()
            horario = self.dropdown_horario_var.get()
            can_tiquetes = self.dropdown_can_tiquetes_var.get()
            Menu.GESTOR_ESTACION.insertar_tiquetes(int(can_tiquetes), matricula_tren, destino, horario)
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")


class TablaConsultas(tk.Frame):
    def __init__(self, padre, datos):  # datos es una matriz
        try:
            tk.Frame.__init__(self, padre)
            can_filas = len(datos)
            can_columnas = len(datos[0])
            # Primero crea la matriz con las entradas tk.Entry, para posteriormente agregar los datos
            self.celdas = [[tk.Entry(self) for j in range(can_filas)] for i in range(can_columnas)]

            # En este ciclo se agregan los datos como un label
            for i in range(can_filas):
                for j in range(can_columnas):
                    dato_celda = datos[i][j]
                    celda = tk.Label(self, text=dato_celda, borderwidth=1, relief="solid", width=10)
                    celda.grid(row=i, column=j)  # Posicion de los objetos celda con una disposicicion (layout) de tipo grid
                    self.celdas[i][j] = celda
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")


class VentanaConsulta(tk.Toplevel):  # tk.TopLevel permite crear una ventana separada a la principal
    ANCHO_DROPDOWN = 20

    def __init__(self, master):
        try:
            super().__init__(master)
            self.tabla_consultas = None
            self.boton_cerrar = None
            self.label = None
            self.mensaje = None
            self.title("Consulta de Tiquetes Por Localización - Trenes S.A")
            self.mostrar_ventana()
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def mostrar_ventana(self):
        try:
            self.mensaje = "Detalle de tiquetes disponibles según localización:"
            self.label = tk.Label(self, text=self.mensaje)
            self.label.pack(padx=Menu.CONFIG_MENU["PAD_X_BOTON"], pady=Menu.CONFIG_MENU["PAD_Y_BOTON"])
            self.geometry(Menu.CONFIG_MENU["TAMANO_INICIAL"])

            datos = Menu.GESTOR_ESTACION.obtener_can_tiquetes_no_vendidos_formato_matriz()

            self.tabla_consultas = TablaConsultas(self, datos)
            # Inicializacion de widgets
            self.tabla_consultas.pack()

            self.boton_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
            self.boton_cerrar.pack()
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")


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
        try:
            super().__init__()  # LLamando al constructor de la clase padre
            self.__ventana_venta_tiquetes_visible = False
            self.__ventana_venta_tiquetes = None
            self.__ventana_insertar_tiquetes_visible = False
            self.__ventana_insertar_tiquetes = None
            self.__ventana_consultas_visible = False
            self.__ventana_consultas = None
            self.dibujar_ventana_principal(nombre_ventana)
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def dibujar_ventana_principal(self, nombre_ventana):
        try:
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
                                               text=boton_3_menu_principal_msj,
                                               command=self.mostrar_ventana_consulta_can_tiquetes)
            boton_3_menu_principal.pack(side=tk.LEFT, padx=Menu.CONFIG_MENU["PAD_X_BOTON"])

            boton_4_menu_principal_msj = "Consultar horario de trenes de hoy"
            boton_4_menu_principal = tk.Button(marco_botones_menu_principal, text=boton_4_menu_principal_msj,
                                               command=self.mostrar_ventana_horarios)
            boton_4_menu_principal.pack(side=tk.LEFT, padx=Menu.CONFIG_MENU["PAD_X_BOTON"])

            marco_espaciador = tk.Frame(self,height=50)  # crea un frame para hacer espacio
            marco_espaciador.pack()

            boton_cerrar = tk.Button(self, text="Cerrar Programa", command=self.destroy)
            boton_cerrar.pack()
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def mostrar_ventana_venta_tiquetes(self):
        try:
            if self.__ventana_venta_tiquetes_visible is False:
                self.__ventana_venta_tiquetes = VentanaVentaTiquete(self)
                self.__ventana_venta_tiquetes_visible = True
            else:
                self.__ventana_venta_tiquetes_visible = False
                self.__ventana_venta_tiquetes = None
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def mostrar_ventana_insertar_tiquetes(self):
        try:
            if self.__ventana_insertar_tiquetes_visible is False:
                self.__ventana_insertar_tiquetes = VentanaInsertarTiquetes(self)
                self.__ventana_insertar_tiquetes_visible = True
            else:
                self.__ventana_insertar_tiquetes_visible = False
                self.__ventana_insertar_tiquetes = None
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def mostrar_ventana_consulta_can_tiquetes(self):
        try:
            if self.__ventana_consultas_visible is False:
                self.__ventana_consultas = VentanaConsulta(self)
                self.__ventana_consultas_visible = True
            else:
                self.__ventana_consultas_visible = False
                self.__ventana_consultas = None
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def mostrar_ventana_horarios(self):
        try:
            raise Exception("Funcionalidad no disponible aun!")
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")