import tkinter as tk
from Modelo import FabricaManejadorArchivos


class VentanaVentaTiquete(tk.Toplevel):  # tk.TopLevel permite crear una ventana separada a la principal
    def __init__(self, master):
        super().__init__(master)
        self.title("Venta de Tiquetes - Trenes S.A")
        self.mostrar_ventana()

    def mostrar_ventana(self):
        self.mensaje = Menu.MANEJADOR_TIQUETES.leer_de_archivo()
        self.label = tk.Label(self, text=self.mensaje)
        self.label.pack(padx=Menu.PAD_X_BOTON, pady=Menu.PAD_Y_BOTON)
        self.geometry(Menu.TAMANO_INICIAL)
        self.close_button = tk.Button(self, text="Close", command=self.destroy)
        self.close_button.pack()


class Menu(tk.Tk):  # La clase menu es heredada de la clase tk.Tk

    # atributos de clase (también son constantes), para la interfaz visual
    TAM_TITULO_PRINCIPAL = 18
    TAM_SUBTITULO = 14
    TAM_TEXTO_1 = 12
    PAD_Y_BOTON = 15
    PAD_X_BOTON = 20
    TAMANO_INICIAL = "1200x450"

    # atributos de clase constantes para manejo de archivos

    FABRICA_MANEJADORES = FabricaManejadorArchivos()
    MANEJADOR_TIQUETES = FABRICA_MANEJADORES.fabricar_manejador_de_archivos(1)
    MANEJADOR_TRENES = FABRICA_MANEJADORES.fabricar_manejador_de_archivos(2)

    def __init__(self, nombre_ventana=None):  # Constructor
        super().__init__()  # LLamando al constructor de la clase padre
        self.__ventana_venta_tiquetes_visible = False
        self.__ventana_venta_tiquetes = None
        self.dibujar_ventana_principal(nombre_ventana)

    def dibujar_ventana_principal(self, nombre_ventana):
        self.title(nombre_ventana)  # metodo de la clase padre
        self.geometry(Menu.TAMANO_INICIAL)  # Establece el tamañno inicial
        texto_titulo_mp = "Bienvenido a Trenes S.A"
        titulo_menu_principal = tk.Label(self, text=texto_titulo_mp, font=("Arial", Menu.TAM_TITULO_PRINCIPAL))
        titulo_menu_principal.pack()

        texto_subtitulo_mp = "Seleccione una opción:"
        subtitulo_menu_principal = tk.Label(self, text=texto_subtitulo_mp, font=("Arial", Menu.TAM_SUBTITULO))
        subtitulo_menu_principal.pack()

        # Espacio entre el subtitulo y el marco de botones
        espacio_menu_principal_1 = tk.Label(self, text="")
        espacio_menu_principal_1.pack()

        marco_botones_menu_principal = tk.Frame(self)  # crea un frame independiente para montar los botones sobre este
        marco_botones_menu_principal.pack()

        # Creación de los botones
        boton_1_menu_principal = tk.Button(marco_botones_menu_principal, text="Vender tiquete a usuario",
                                           command=self.mostrar_ventana_venta_tiquetes)
        boton_1_menu_principal.pack(side=tk.LEFT,
                                    padx=Menu.PAD_X_BOTON, )  # padx -> Ajusta la distancia horizontal entre los botones

        boton_2_menu_principal = tk.Button(marco_botones_menu_principal,
                                           text="Consultar cantidad de tiquetes disponibles por localización")
        boton_2_menu_principal.pack(side=tk.LEFT, padx=Menu.PAD_X_BOTON)

        boton_3_menu_principal = tk.Button(marco_botones_menu_principal, text="Consultar horario de trenes de hoy")
        boton_3_menu_principal.pack(side=tk.LEFT, padx=Menu.PAD_X_BOTON)

        boton_4_menu_principal = tk.Button(marco_botones_menu_principal, text="Reportar atraso o problema de tren")
        boton_4_menu_principal.pack(side=tk.LEFT, padx=Menu.PAD_X_BOTON)

    def mostrar_ventana_venta_tiquetes(self):
        if self.__ventana_venta_tiquetes_visible is False:
            self.__ventana_venta_tiquetes = VentanaVentaTiquete(self)
            self.__ventana_venta_tiquetes_visible = True
        else:
            self.__ventana_venta_tiquetes_visible = False
            self.__ventana_venta_tiquetes = None
