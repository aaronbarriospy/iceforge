# archivo: dominio.py

# explicacion: traigo las herramientas nativas para poder crear clases abstractas.
importar modulo para abstraccion

# explicacion: defino mi molde principal asegurandome de que sea abstracto.
clase Pinguino (debe ser abstracta):

    # explicacion: creo mi constructor para recibir los datos iniciales.
    metodo constructor(nombre, energia):
        # explicacion: guardo el nombre aplicando encapsulamiento.
        atributo privado nombre = nombre
        
        # explicacion: guardo la energia aplicando encapsulamiento.
        atributo privado energia = energia
        
        # explicacion: creo mi estado vital por defecto.
        atributo privado esta_vivo = verdadero

    # explicacion: armo mi primer getter.
    metodo obtener_nombre():
        devolver atributo privado nombre

    # explicacion: armo mi segundo getter.
    metodo obtener_energia():
        devolver atributo privado energia

    # explicacion: creo el metodo para alterar la salud internamente.
    metodo recibir_dano(cantidad):
        restarle la cantidad al atributo privado energia
        
        si el atributo privado energia es menor o igual a 0:
            fijar atributo privado energia en 0
            cambiar atributo privado esta_vivo a falso

    # explicacion: armo mi contrato obligatorio para las clases hijas.
    etiqueta para obligar abstraccion
    metodo ejecutar_accion():
        no hace nada (pasar)

from abc import ABC, abstractmethod

class Pinguino(ABC):
    def __init__(self, nombre, energia):
        self.__nombre = nombre
        self.__energia = energia
        self.__esta_vivo = True

    def get_nombre(self):
        return self.__nombre

    def get_energia(self):
        return self.__energia

    def recibir_dano(self, cantidad):
        self.__energia -= cantidad

        if self.__energia <= 0:
            self.__energia = 0
            self.__esta_vivo = False

    @abstractmethod
    def ejecutar_accion(self):
        pass


# archivo: dominio.py (continuacion)

clase PinguinoIngeniero (hereda de Pinguino):
    metodo constructor(nombre, energia, poder_reparacion):
        llamar al constructor del padre(nombre, energia)
        atributo privado poder_reparacion = poder_reparacion

    metodo ejecutar_accion():
        imprimir(f"[{obtener_nombre()}] repara {poder_reparacion} puntos.")
        devolver atributo privado poder_reparacion

clase PinguinoGuerrero (hereda de Pinguino):
    metodo constructor(nombre, energia, fuerza_ataque):
        llamar al constructor del padre(nombre, energia)
        atributo privado fuerza_ataque = fuerza_ataque

    metodo ejecutar_accion():
        imprimir(f"[{obtener_nombre()}] ataca causando {fuerza_ataque} de dano.")
        devolver atributo privado fuerza_ataque

class PinguinoIngeniero(Pinguino):
    def __init__(self, nombre, energia, poder_reparacion):
        super().__init__(nombre, energia)
        self.__poder_reparacion = poder_reparacion

    def ejecutar_accion(self):
        print(f"[{self.get_nombre()}] repara {self.__poder_reparacion} puntos")
        return self.__poder_reparacion
class PinguinoGuerrero(Pinguino):
    def __init__(self, nombre, energia, fuerza_ataque):
        super().__init__(nombre, energia)
        self.__fuerza_ataque = fuerza_ataque
    def ejecutar_accion(self):
        print(f"[{self.get_nombre()}] ataca causando {self.__fuerza_ataque} de dano")
        return self.__fuerza_ataque
