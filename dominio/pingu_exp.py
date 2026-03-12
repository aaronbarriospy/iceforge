from dominio.pinguino import Pinguino

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