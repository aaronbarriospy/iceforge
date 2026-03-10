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

class PinguinoExplorador(Pinguino):
    # explicacion: defino mi tercera y ultima clase hija para completar el requisito del challenge.
    # por que?: un buen sistema necesita variedad. el explorador hereda de pinguino para tener la misma base segura que los demas.

    def __init__(self, nombre, energia, destreza):
        # explicacion: armo el constructor de mi explorador. pido los datos base y le sumo su destreza.
        # por que?: la destreza va a definir que tan bueno es mi pinguino encontrando recursos entre el hielo de la tormenta.

        super().__init__(nombre, energia)
        # explicacion: llamo a super() para pasarle el nombre y la energia a mi clase padre.
        # por que?: dejo que el padre haga el trabajo de guardar los datos de forma segura para no repetir lineas de codigo.

        self.__destreza = destreza
        # explicacion: guardo la destreza como un atributo privado y unico de mi explorador.
        # por que?: mantengo mi encapsulamiento intacto. este valor no se puede modificar accidentalmente desde el motor del juego.

    def ejecutar_accion(self):
        # explicacion: escribo mi ultima version de la accion obligatoria. cierro mi ciclo de polimorfismo.
        # por que?: a diferencia de atacar o reparar, mi explorador busca recursos. el motor del juego solo va a pedirle que actue, y el objeto sabe que tiene que devolver sus puntos de destreza.
        
        print(f"[{self.get_nombre()}] explora la tormenta y recolecta {self.__destreza} recursos vitales para la colonia.")
        return self.__destreza