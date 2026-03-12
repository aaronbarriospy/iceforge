from dominio.pinguino import Pinguino

class PinguinoGuerrero(Pinguino):
    # explicacion: aca creo mi segunda clase hija para sumar polimorfismo a mi sistema.
    # por que?: mi guerrero tambien es un pinguino, asi que hereda de la misma base que el ingeniero.

    def __init__(self, nombre, energia, fuerza_ataque):
        # explicacion: armo el constructor de mi guerrero. pido lo basico y le sumo su fuerza.
        # por que?: a diferencia del ingeniero, este pinguino necesita saber cuanto dano puede hacer para defender la colonia.

        super().__init__(nombre, energia)
        # explicacion: llamo a super() para que la clase padre se encargue de guardar el nombre y la energia.
        # por que?: reciclo todo el codigo seguro que ya escribi arriba. es la mejor practica para no repetir lineas.

        self.__fuerza_ataque = fuerza_ataque
        # explicacion: guardo la fuerza de ataque como un atributo privado exclusivo de esta clase.
        # por que?: sigo manteniendo mi encapsulamiento intacto. nadie puede modificar la fuerza del guerrero desde el main.

    def ejecutar_accion(self):
        # explicacion: aca escribo mi propia version de la accion obligatoria. esto es polimorfismo puro.
        # por que?: el motor de mi juego solo va a llamar a ejecutar_accion(), y como es un guerrero, el sistema ya sabe que tiene que devolver puntos de dano en lugar de reparacion.
        
        print(f"[{self.get_nombre()}] ataca la amenaza de hielo causando {self.__fuerza_ataque} de dano.")
        return self.__fuerza_ataque