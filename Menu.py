import tkinter as tk


class Menu(tk.Tk):  # La clase menu es heredada de la clase tk.Tk
    def __init__(self,nombre_ventana=None):
        super().__init__()  # LLamando al constructor de la clase padre
        self.title(nombre_ventana) # metodo de la clase padre


