from dominio.pinguino import Pinguino

class PinguinoIngeniero(Pinguino):
    # explicacion: al poner (pinguino) al lado del nombre, estoy aplicando la herencia.
    # por que?: mi ingeniero automaticamente ya tiene nombre, energia, y la logica de recibir dano sin que yo tenga que programar eso de vuelta.

    def __init__(self, nombre, energia, poder_reparacion):
        # explicacion: creo el constructor de mi ingeniero. pido los datos base y sumo uno nuevo: el poder de reparacion.
        # por que?: ademas de lo basico, mi ingeniero necesita saber que tan bueno es arreglando la estructura metalica.

        super().__init__(nombre, energia)
        # explicacion: uso la funcion super() para enviarle el nombre y la energia al constructor de mi clase padre.
        # por que?: le delego al padre la responsabilidad de guardar esos datos de forma privada. es la mejor practica para reutilizar codigo.

        self.__poder_reparacion = poder_reparacion
        # explicacion: guardo el poder de reparacion como un atributo privado nuevo y exclusivo de esta clase.
        # por que?: aplico encapsulamiento otra vez. este numero solo le pertenece al ingeniero y nadie desde afuera debe alterarlo.

    def ejecutar_accion(self):
        # explicacion: aca aplico el pilar del polimorfismo. estoy escribiendo mi propia version del metodo abstracto que me obligaba el contrato.
        # por que?: el ingeniero no ataca, su trabajo es arreglar. por eso, su accion devuelve los puntos de reparacion para el sistema.
        
        print(f"[{self.get_nombre()}] saca su soldador y repara {self.__poder_reparacion} puntos de la estructura.")
        return self.__poder_reparacion