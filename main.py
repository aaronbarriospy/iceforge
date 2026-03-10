from motor import Game
from ui import InterfazUsuario
# explicacion: importo la clase de mi motor y la clase de mi interfaz.
# por que?: este es el punto de entrada de mi programa. aca traigo las piezas del rompecabezas para armarlo.

if __name__ == "__main__":
    # explicacion: uso esta validacion estandar de python para asegurarme de que el archivo se ejecute directamente.
    # por que?: es una buena practica profesional y evita que el juego arranque solo si alguien importa este archivo por error.

    mi_ui = InterfazUsuario()
    # explicacion: instancio mi interfaz de consola.
    
    mi_juego = Game(mi_ui)
    # explicacion: instancio el motor de mi juego y le inyecto la interfaz como parametro.
    # por que?: asi mi motor puede usar la ui para mandar mensajes sin tener que usar prints propios.

    mi_juego.iniciar()
    # explicacion: le doy la orden de arranque al motor. empieza a correr mi game loop.
    # por que?: cumplo con la regla principal: mi main no tiene logica, if sueltos, ni variables globales. solo arranca el sistema.