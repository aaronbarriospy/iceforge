from abc import ABC, abstractmethod
# explicacion: importo abc y abstractmethod de la libreria nativa 'abc'.
# por que?: el reto me exige crear una clase base que funcione como "contrato" y que no se pueda instanciar directamente. con esto lo logro.

class Pinguino(ABC):
    # explicacion: defino mi clase pinguino y le paso (abc) entre parentesis.
    # por que?: al hacer que herede de abc, convierto a pinguino en una clase abstracta pura. asi cumplo el primer requisito obligatorio del challenge.

    def __init__(self, nombre, energia):
        # explicacion: este es mi metodo constructor (__init__). se va a ejecutar automaticamente cada vez que instancie un pinguino hijo.
        # por que?: necesitaba un lugar centralizado para definir los atributos que todos mis pinguinos van a compartir, evitando repetir codigo en cada clase hija.

        self.__nombre = nombre
        # explicacion: guardo el nombre del pinguino usando un doble guion bajo (__).
        # por que?: aca aplico el pilar del encapsulamiento. hago que el atributo sea privado para evitar que lo modifiquen desde afuera de la clase (el "pecado capital" del que hablaba el reto).

        self.__energia = energia
        # explicacion: guardo la energia inicial, tambien de forma privada.
        # por que?: la energia es un dato critico de mi juego. solo esta misma clase debe tener el control y la logica de como sube o baja ese numero.

        self.__esta_vivo = True
        # explicacion: creo un estado interno que arranca en verdadero.
        # por que?: el motor de mi juego (la clase game) va a necesitar saber si mi pinguino sigue vivo para continuar o terminar la partida.

    def get_nombre(self):
        # explicacion: creo un metodo "getter".
        # por que?: como mi atributo nombre es privado y no se puede tocar, decidi hacer esta puerta de acceso autorizada para poder leer y mostrar el nombre en pantalla cuando lo necesite.
        return self.__nombre

    def get_energia(self):
        # explicacion: otro metodo "getter", esta vez para la energia.
        # por que?: lo necesito para imprimir el estado de salud de mi colonia en la interfaz, sin romper el encapsulamiento que arme antes.
        return self.__energia

    def recibir_dano(self, cantidad):
        # explicacion: este metodo recibe un numero (el dano de la tormenta) y procesa la resta.
        # por que?: es la forma segura que cree para alterar la energia. la logica de perder vida vive aqui adentro de mi clase, no flotando suelta en mi main.
        self.__energia -= cantidad
        
        if self.__energia <= 0:
            # explicacion: evaluo si la energia cayo a cero o a numeros negativos.
            # por que?: quiero evitar bugs en mi juego. si la energia se agota, me aseguro de clavarla en 0 y disparo la consecuencia logica: la muerte de mi pinguino.
            self.__energia = 0
            self.__esta_vivo = False

    @abstractmethod
    def ejecutar_accion(self):
        # explicacion: uso la etiqueta @abstractmethod sobre esta funcion vacia.
        # por que?: este es el contrato de mi sistema. obligo a cualquier clase hija que yo cree a programar su propia version de esta accion. aca aplico el pilar de la abstraccion.
        pass