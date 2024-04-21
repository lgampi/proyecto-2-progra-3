# Modelo: Clases que almacenan datos y logica del programa
import os


class Tren:
    def __init__(self, matricula, estado):
        self.__matricula = matricula
        self.__estado = estado  # Si el tren está usable o no.

    def get_matricula(self):
        return self.__matricula

    def get_estado(self):
        return self.__estado


class Tiquete:
    def __init__(self, tren, num_tiquete, destino, hora_salida):
        self.__tren = tren
        self.__num_tiquete = num_tiquete
        self.__destino = destino
        self.__hora_salida = hora_salida

    def get_destino(self):
        return self.__destino

    def get_hora_salida(self):
        return self.__hora_salida

    def get_num_tiquete(self):
        return self.__num_tiquete

    def get_tren(self):
        return self.__tren


class ManejadorArchivos:  # Clase padre que sirve como "molde", sirve como una interfaz.
    def __init__(self):
        raise Exception("No se puede instanciar esta clase")

    @staticmethod  # Los métodos estáticos, son métodos de la clase, no de un objeto.
    def obtener_singleton():
        pass

    def leer_de_archivo(self):
        pass

    def escribir_a_archivo(self, o):
        pass


class ManejadorArchivosTren(ManejadorArchivos):
    # Acá se usa el patrón singleton
    # Esta clase sólo permite instanciar un único objeto de ella.
    instancia_singleton = None
    RUTA_TRENES = "archivos/trenes.txt"

    def __init__(self):
        if ManejadorArchivosTren.instancia_singleton is None:
            ManejadorArchivosTren.instancia_singleton = self
        else:
            raise Exception("No debe crear más objetos")

    @staticmethod  # Los métodos estáticos, son métodos de la clase, no de un objeto.
    def obtener_singleton():
        if ManejadorArchivosTren.instancia_singleton is None:
            ManejadorArchivosTren()
        return ManejadorArchivosTren.instancia_singleton

    def leer_de_archivo(self):
        ruta = ManejadorArchivosTren.RUTA_TRENES
        trenes = []
        with open(ruta, "r") as file:
            for line in file:
                linea = line.split(",")
                matricula = linea[0]
                estado = linea[1]
                tren = Tren(matricula, estado)
                trenes.append(tren)
        return trenes

    def escribir_a_archivo(self, o):
        ruta = ManejadorArchivosTren.RUTA_TRENES
        with open(ruta, "w") as file:
            file.write("Prueba trenes")


class ManejadorArchivosTiquete(ManejadorArchivos):
    # Acá se usa el patrón singleton
    # Esta clase sólo permite instanciar un único objeto de ella.
    instancia_singleton = None
    RUTA_TIQUETES = "archivos/tiquetes.txt"

    def __init__(self):
        if ManejadorArchivosTiquete.instancia_singleton is None:
            ManejadorArchivosTiquete.instancia_singleton = self
        else:
            raise Exception("No debe crear más objetos")

    @staticmethod  # Los métodos estáticos, son métodos de la clase, no de un objeto.
    def obtener_singleton():
        if ManejadorArchivosTiquete.instancia_singleton is None:
            ManejadorArchivosTiquete()
        return ManejadorArchivosTiquete.instancia_singleton

    def leer_de_archivo(self):
        tiquetes = []
        ruta = ManejadorArchivosTiquete.RUTA_TIQUETES
        with open(ruta, "r") as file:
            for line in file:
                dato_tiquete = line.split(",")  # Separar el string por "," en una lista.
                matricula = dato_tiquete[0]
                num_tiquete = dato_tiquete[1]
                destino = dato_tiquete[2]
                hora_salida = dato_tiquete[3]
                tiquete = Tiquete(matricula, num_tiquete, destino, hora_salida)
                tiquetes.append(tiquete)
        return tiquetes

    def escribir_a_archivo(self, o):
        ruta = ManejadorArchivosTiquete.RUTA_TIQUETES
        try:
            with open(ruta, "a") as file:
                file.write(f"{o.get_tren()},{o.get_num_tiquete()},{o.get_destino()},{o.get_hora_salida()}\n")
        except FileNotFoundError:
            print(f"Excepcion, el archivo {ruta} no existe")


class FabricaManejadorArchivos:
    def __init__(self):  # El constructor no requiere de otros atributos.
        pass

    @staticmethod
    def fabricar_manejador_de_archivos(tipo):
        if tipo == 1:
            return ManejadorArchivosTiquete.obtener_singleton()
        elif tipo == 2:
            return ManejadorArchivosTren.obtener_singleton()
        else:
            raise Exception("No existe este tipo de objeto a fabricar")


class GestorDeEstacion:
    # Esta clase maneja la cantidad de tiquetes y los trenes, es la clase principal del modelo.

    # Atributos de clase constantes para manejo de archivos

    FABRICA_MANEJADORES = FabricaManejadorArchivos()
    MANEJADOR_TIQUETES = FABRICA_MANEJADORES.fabricar_manejador_de_archivos(1)
    MANEJADOR_TRENES = FABRICA_MANEJADORES.fabricar_manejador_de_archivos(2)
    secuencia_tiquetes = 1  # Se inicializa como 1, se actualiza al leer tiquetes. Esta es la proxima secuencia esperable, no la ultima.

    def __init__(self):
        self.__tiquetes = []
        self.__trenes = []

    def obtener_tiquetes(self):
        # Cada vez que la vista pide la lista de tiquetes, esta se actualiza.
        self.__tiquetes = GestorDeEstacion.MANEJADOR_TIQUETES.leer_de_archivo()

        # Actualizar la ultima secuencia de tiquetes

        if len(self.__tiquetes) > 0:  # Se valida si hay al menos un tiquete en el archivo
            ultimo_tiquete = self.__tiquetes[-1]
            GestorDeEstacion.secuencia_tiquetes = int(
                ultimo_tiquete.get_num_tiquete()) + 1  # Ej: si estamos en el 400, ahora el ultimo es el 401
        else:
            pass  # Como la secuencia se inicializa en 1, no hace falta reasignar su valor.
        return self.__tiquetes

    def insertar_tiquetes(self, can_tiquetes, tren, destino, hora_de_salida):
        # Mejorar despues
        self.obtener_tiquetes()  # Se actualiza la lista de tiquetes, y se obtiene el último tiquete generado.

        for i in range(0, can_tiquetes):  # Para cada tiquete se quiere insertar
            nuevo_tiquete = Tiquete(tren, GestorDeEstacion.secuencia_tiquetes, destino, hora_de_salida)
            GestorDeEstacion.MANEJADOR_TIQUETES.escribir_a_archivo(nuevo_tiquete)
            # Como ya actualizamos los tiquetes, con la lista que ya tenemos, basta con agregarlo a dicha lista
            self.__tiquetes.append(nuevo_tiquete)
            GestorDeEstacion.secuencia_tiquetes += 1

    def obtener_matriculas_trenes(self):
        self.__trenes = GestorDeEstacion.MANEJADOR_TRENES.leer_de_archivo()
        # List comprehension, genera una lista de matriculas apartir de la lista de objetos de trenes self.__trenes .
        return [tren.get_matricula() for tren in self.__trenes]
