# Modelo: Clases que almacenan datos y logica del programa

class Tren:
    def __init__(self, matricula, estado):
        self.__matricula = matricula
        self.__estado = estado  # Si el tren está usable o no.

    def get_matricula(self):
        return self.__matricula

    def get_estado(self):
        return self.__estado


class Tiquete:
    def __init__(self, tren, num_tiquete, destino, hora_salida, vendido):
        self.__tren = tren
        self.__num_tiquete = num_tiquete
        self.__destino = destino
        self.__hora_salida = hora_salida
        self.__vendido = vendido  # En el archivo a guardar, se refleja como 0 o 1 y se convierte a booleano.

    def get_destino(self):
        return self.__destino

    def get_hora_salida(self):
        return self.__hora_salida

    def get_num_tiquete(self):
        return self.__num_tiquete

    def get_tren(self):
        return self.__tren

    def get_vendido(self):
        return self.__vendido

    def set_vendido(self, vendido):
        self.__vendido = vendido

    # Sobreescribiendo el metodo __str__ para representar el objeto como string de la siguiente manera:
    def __str__(self):
        return f"{self.__num_tiquete},{self.__tren},{self.__destino},{self.__hora_salida}"


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
        try:
            if ManejadorArchivosTren.instancia_singleton is None:
                ManejadorArchivosTren.instancia_singleton = self
            else:
                raise Exception("No debe crear más objetos")
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    @staticmethod  # Los métodos estáticos, son métodos de la clase, no de un objeto.
    def obtener_singleton():
        try:
            if ManejadorArchivosTren.instancia_singleton is None:
                ManejadorArchivosTren()
            return ManejadorArchivosTren.instancia_singleton
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def leer_de_archivo(self):
        trenes = []
        try:
            ruta = ManejadorArchivosTren.RUTA_TRENES
            with open(ruta, "r") as file:
                for line in file:
                    linea = line.split(",")
                    matricula = linea[0]
                    estado = linea[1]
                    tren = Tren(matricula, estado)
                    trenes.append(tren)
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")
        return trenes

    def escribir_a_archivo(self, o):
        try:
            ruta = ManejadorArchivosTren.RUTA_TRENES
            with open(ruta, "w") as file:
                file.write("Prueba trenes")
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")


class ManejadorArchivosTiquete(ManejadorArchivos):
    # Acá se usa el patrón singleton
    # Esta clase sólo permite instanciar un único objeto de ella.
    instancia_singleton = None
    RUTA_TIQUETES = "archivos/tiquetes.txt"

    def __init__(self):
        try:
            if ManejadorArchivosTiquete.instancia_singleton is None:
                ManejadorArchivosTiquete.instancia_singleton = self
            else:
                raise Exception("No debe crear más objetos")
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    @staticmethod  # Los métodos estáticos, son métodos de la clase, no de un objeto.
    def obtener_singleton():
        try:
            if ManejadorArchivosTiquete.instancia_singleton is None:
                ManejadorArchivosTiquete()
            return ManejadorArchivosTiquete.instancia_singleton
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def leer_de_archivo(self):
        tiquetes = []
        try:
            ruta = ManejadorArchivosTiquete.RUTA_TIQUETES
            with open(ruta, "r") as file:
                for line in file:
                    dato_tiquete = line.split(",")  # Separar el string por "," en una lista.
                    matricula = dato_tiquete[0]
                    num_tiquete = dato_tiquete[1]
                    destino = dato_tiquete[2]
                    hora_salida = dato_tiquete[3]
                    vendido = False  # Por default en True, a menos de que se encuentre lo contrario en el archivo
                    if int(dato_tiquete[4]) == 1:
                        vendido = True
                    tiquete = Tiquete(matricula, num_tiquete, destino, hora_salida, vendido)
                    tiquetes.append(tiquete)
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")
        return tiquetes

    def escribir_a_archivo(self, o):
        ruta = ManejadorArchivosTiquete.RUTA_TIQUETES
        try:
            with open(ruta, "a") as file:
                vendido = 0
                if o.get_vendido() is True:
                    vendido = 1
                file.write(f"{o.get_tren()},{o.get_num_tiquete()},{o.get_destino()},{o.get_hora_salida()},{vendido}\n")
        except FileNotFoundError:
            print(f"Excepcion, el archivo {ruta} no existe")
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def vender_tiquete(self, num_tiquete):
        ruta = ManejadorArchivosTiquete.RUTA_TIQUETES
        try:
            tiquetes = self.leer_de_archivo()  # Obtiene la lista de tiquetes.
            linea = 1
            for tiquete in tiquetes:
                if tiquete.get_num_tiquete() == num_tiquete:
                    tiquete.set_vendido(True)
            # Uso del operador ternario
            lineas_por_escribir = [
                f"{o.get_tren()},{o.get_num_tiquete()},{o.get_destino()},{o.get_hora_salida()},{1 if o.get_vendido() is True else 0}\n"
                for o in tiquetes]
            with open(ruta,
                      "w+") as file:  # El modo w+ trunca (vacia) el archivo y luego escribe sobre el, el nuevo contenido.
                file.writelines(lineas_por_escribir)
        except FileNotFoundError:
            print(f"Excepcion, el archivo {ruta} no existe")
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")


class FabricaManejadorArchivos:
    def __init__(self):  # El constructor no requiere de otros atributos.
        pass

    @staticmethod
    def fabricar_manejador_de_archivos(tipo):
        try:
            if tipo == 1:
                return ManejadorArchivosTiquete.obtener_singleton()
            elif tipo == 2:
                return ManejadorArchivosTren.obtener_singleton()
            else:
                raise Exception("No existe este tipo de objeto a fabricar")
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")


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
        self.__destinos = ["Heredia", "Cartago"]
        self.__horarios = ["6:00AM", "7:00AM", "8:00AM", "3:00PM", "4:00PM", "5:00PM"]
        self.__can_tiquetes = ["25", "50", "100"]
        self.__criterios_seleccion = ["Tren", "Destino", "Horario"]

    def get_criterios_seleccion(self):
        return self.__criterios_seleccion

    def get_destinos(self):
        return self.__destinos

    def get_horarios(self):
        return self.__horarios

    def get_can_tiquetes(self):
        return self.__can_tiquetes

    def obtener_tiquetes(self):
        # Cada vez que la vista pide la lista de tiquetes, esta se actualiza.
        try:
            self.__tiquetes = GestorDeEstacion.MANEJADOR_TIQUETES.leer_de_archivo()

            # Actualizar la ultima secuencia de tiquetes

            if len(self.__tiquetes) > 0:  # Se valida si hay al menos un tiquete en el archivo
                ultimo_tiquete = self.__tiquetes[-1]  # Con -1 se accede al ultimo elemento de la lista
                GestorDeEstacion.secuencia_tiquetes = int(
                    ultimo_tiquete.get_num_tiquete()) + 1  # Ej: si estamos en el 400, ahora el ultimo es el 401
            else:
                pass  # Como la secuencia se inicializa en 1, no hace falta reasignar su valor.
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")
        return self.__tiquetes

    def insertar_tiquetes(self, can_tiquetes, tren, destino, hora_de_salida):
        try:
            self.obtener_tiquetes()  # Se actualiza la lista de tiquetes, y se obtiene el último tiquete generado.

            for i in range(0, can_tiquetes):  # Para cada tiquete se quiere insertar
                nuevo_tiquete = Tiquete(tren, GestorDeEstacion.secuencia_tiquetes, destino, hora_de_salida, False)
                GestorDeEstacion.MANEJADOR_TIQUETES.escribir_a_archivo(nuevo_tiquete)
                # Como ya actualizamos los tiquetes, con la lista que ya tenemos, basta con agregarlo a dicha lista
                self.__tiquetes.append(nuevo_tiquete)
                GestorDeEstacion.secuencia_tiquetes += 1
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def obtener_tiquetes_no_vendidos(self, criterio):
        tiquetes_resultantes = dict()  # Vamos a usar un diccionario para agrupar a los tiquetes
        try:
            # Con el parametro criterio, vamos a agrupar por horario, destino o matricula.
            if criterio not in self.__criterios_seleccion:  # Si criterio no es ninguno de estos tres
                raise Exception("Parametro 'criterio' invalido")

            self.obtener_tiquetes()  # Con esto actualizamos la lista de tiquetes (self.__tiquetes)

            # Con esto vamos actualizamos la lista de trenes y obtenemos sus matriculas.
            matriculas_trenes = self.obtener_matriculas_trenes()
            grupos = []

            if criterio == "Tren":
                for matricula_tren in matriculas_trenes:  # Para cada matricula del tren
                    # Acá, a cada matricula del tren, le damos una lista vacia para agrupar, usando la matricula como llave.
                    tiquetes_resultantes[matricula_tren] = []
                for tiquete in self.__tiquetes:
                    if tiquete.get_vendido() is False:
                        tiquetes_resultantes[tiquete.get_tren()].append(tiquete)
            elif criterio == "Destino":
                for destino in self.__destinos:  # Para cada destino
                    # A cada destino se le da una lista vacia para agrupar, usando el destino como llave,
                    tiquetes_resultantes[destino] = []
                for tiquete in self.__tiquetes:
                    if tiquete.get_vendido() is False:
                        tiquetes_resultantes[tiquete.get_destino()].append(tiquete)
            elif criterio == "Horario":
                for horario in self.__horarios:  # Para cada horario
                    # A cada horario se le da una lista vacia para agrupar, usando lah ora como llave.
                    tiquetes_resultantes[horario] = []
                for tiquete in self.__tiquetes:
                    if tiquete.get_vendido() is False:
                        tiquetes_resultantes[tiquete.get_hora_salida()].append(tiquete)
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")
        return tiquetes_resultantes

    def obtener_can_tiquetes_no_vendidos_formato_matriz(self):
        matriz_resultado = []
        try:
            tiquetes_no_vendidos = self.obtener_tiquetes_no_vendidos(self.__criterios_seleccion[1])
            for llave, valor in tiquetes_no_vendidos.items():
                matriz_resultado.append([llave, len(tiquetes_no_vendidos[llave])])
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")
        return matriz_resultado

    def obtener_matriculas_trenes(self):
        try:
            self.__trenes = GestorDeEstacion.MANEJADOR_TRENES.leer_de_archivo()
            # List comprehension, genera una lista de matriculas apartir de la lista de objetos de trenes self.__trenes .
            return [tren.get_matricula() for tren in self.__trenes]
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")

    def vender_tiquete(self, num_tiquete_a_vender):
        try:
            GestorDeEstacion.MANEJADOR_TIQUETES.vender_tiquete(num_tiquete_a_vender)
        except Exception as e:
            print(f"Ha ocurrido la excepcion: {e}")