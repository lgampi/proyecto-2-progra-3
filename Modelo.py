# Mode: Clases que almacenan datos y logica del programa


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

    def escribir_a_archivo(self):
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
        with open(ruta, "r") as file:
            for line in file:
                return line

    def escribir_a_archivo(self):
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
        ruta = ManejadorArchivosTiquete.RUTA_TIQUETES
        with open(ruta, "r") as file:
            for line in file:
                return line

    def escribir_a_archivo(self):
        ruta = ManejadorArchivosTiquete.RUTA_TIQUETES
        with open(ruta, "w") as file:
            file.write("Prueba tiquetes")


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

