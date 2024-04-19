import tkinter as tk


class Menu(tk.Tk):  # La clase menu es heredada de la clase tk.Tk
    # atributos de clase (también son constantes)
    TAM_TITULO_PRINCIPAL = 18
    TAM_SUBTITULO = 14
    TAM_TEXTO_1 = 12
    PAD_Y_BOTON = 15
    PAD_X_BOTON = 20

    def __init__(self, nombre_ventana=None):  # Constructor
        super().__init__()  # LLamando al constructor de la clase padre
        self.title(nombre_ventana)  # metodo de la clase padre

        texto_titulo_mp = "Bienvenido a Trenes S.A"
        titulo_menu_principal = tk.Label(self, text=texto_titulo_mp, font=("Arial", Menu.TAM_TITULO_PRINCIPAL))
        titulo_menu_principal.pack()

        texto_subtitulo_mp = "Seleccione una opción:"
        subtitulo_menu_principal = tk.Label(self, text=texto_subtitulo_mp, font=("Arial", Menu.TAM_SUBTITULO))
        subtitulo_menu_principal.pack()

        # Espacio entre el subtitulo y el marco de botones
        espacio_menu_principal_1 = tk.Label(self, text="")
        espacio_menu_principal_1.pack()

        marco_botones_menu_principal = tk.Frame(self) # crea un frame independiente para montar los botones sobre este
        marco_botones_menu_principal.pack()

        # Creación de los botones
        boton_1_menu_principal = tk.Button(marco_botones_menu_principal, text="Vender tiquete a usuario")
        boton_1_menu_principal.pack(side=tk.LEFT,
                                    padx=Menu.PAD_X_BOTON)  # padx -> Ajusta la distancia horizontal entre los botones

        boton_2_menu_principal = tk.Button(marco_botones_menu_principal,
                            text="Consultar cantidad de tiquetes disponibles por localización")
        boton_2_menu_principal.pack(side=tk.LEFT, padx=Menu.PAD_X_BOTON)

        boton_3_menu_principal = tk.Button(marco_botones_menu_principal, text="Consultar horario de trenes de hoy")
        boton_3_menu_principal.pack(side=tk.LEFT, padx=Menu.PAD_X_BOTON)

        boton_4_menu_principal = tk.Button(marco_botones_menu_principal, text="Reportar atraso o problema de tren")
        boton_4_menu_principal.pack(side=tk.LEFT, padx=Menu.PAD_X_BOTON)
