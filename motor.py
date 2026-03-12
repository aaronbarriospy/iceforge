from dominio.pingu_inge import PinguinoIngeniero
from dominio.pingu_guerr import PinguinoGuerrero
from dominio.pingu_exp import PinguinoExplorador

class Game:
    # explicacion: esta es la clase game, el motor que coordina todo mi sistema.
    # por que?: asi separo la logica de control de las reglas de los pinguinos y cumplo con el requisito principal del motor.

    def __init__(self, ui):
        # explicacion: en mi constructor, ahora pido un objeto ui (interfaz de usuario) como parametro obligatorio.
        # por que?: aca aplico inyeccion de dependencias. mi motor no imprime nada por su cuenta, le delega esa tarea a la interfaz.

        self.__ui = ui
        # explicacion: guardo la interfaz que recibi como un atributo privado de mi motor.

        self.__estructura_metalica = 50
        # explicacion: defino la salud inicial de mi estructura central.

        self.__juego_activo = True
        # explicacion: creo la bandera booleana que mantendra vivo mi game loop.

        self.__equipo = [
            PinguinoIngeniero("kowalski", 100, 20),
            PinguinoGuerrero("rico", 100, 30),
            PinguinoExplorador("cabo", 100, 15)
        ]
        # explicacion: instancio a mis pinguinos y los agrupo en una lista privada aplicando polimorfismo.

    def jugar_turno(self):
        # explicacion: defino lo que ocurre paso a paso en cada ronda de mi juego.

        self.__ui.mostrar_separador()
        self.__ui.mostrar_mensaje("--- inicia un nuevo turno en la colonia ---")
        # explicacion: en lugar de usar print(), llamo a mi objeto ui para que muestre los textos en la consola.
        # por que?: cumplo con la separacion de zonas. mi motor solo da la orden de mostrar, pero no le importa como se dibuja en la pantalla.
        
        for pinguino in self.__equipo:
            if pinguino.get_energia() > 0:
                resultado = pinguino.ejecutar_accion()
                # explicacion: le ordeno a cada pinguino que actue sin importarme de que tipo es.

                if isinstance(pinguino, PinguinoIngeniero):
                    self.__estructura_metalica += resultado
                    self.__ui.mostrar_mensaje(f"la estructura recupero puntos. estado actual: {self.__estructura_metalica}/100")

        self.__ui.mostrar_mensaje("la tormenta de hielo golpea la colonia...")
        self.__estructura_metalica -= 10
        
        for pinguino in self.__equipo:
             pinguino.recibir_dano(10)
             # explicacion: todos mis pinguinos vivos sufren el dano de la tormenta usando su metodo interno seguro.

    def verificar_estado(self):
        # explicacion: evaluo mis condiciones de victoria o derrota al final de cada turno.

        if self.__estructura_metalica >= 100:
            self.__ui.mostrar_mensaje("¡victoria! la estructura alcanzo el 100%. la colonia sobrevive a la tormenta.")
            self.__juego_activo = False
            # explicacion: apago mi game loop porque ganamos.
            
        elif self.__estructura_metalica <= 0:
            self.__ui.mostrar_mensaje("derrota... la estructura colapso y la colonia se congelo.")
            self.__juego_activo = False
            # explicacion: apago mi game loop porque perdimos.

    def iniciar(self):
        # explicacion: este es mi game loop principal, el corazon de mi sistema.

        self.__ui.mostrar_mensaje("iniciando sistema de simulacion penguin academy...")
        while self.__juego_activo:
            self.jugar_turno()
            self.verificar_estado()