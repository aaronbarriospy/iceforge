class InterfazUsuario:
    # explicacion: creo mi clase de interfaz para manejar todo lo que el usuario lee en la consola.
    # por que?: el challenge me exige una tercera zona logica solo para la ui. aca centralizo todos los prints.

    def mostrar_mensaje(self, mensaje):
        # explicacion: encapsulo la funcion print nativa de python dentro de mi propio metodo.
        # por que?: el motor me va a pasar textos y yo me encargo de dibujarlos en la pantalla. asi mantengo las responsabilidades separadas.
        print(mensaje)

    def mostrar_separador(self):
        # explicacion: creo un metodo de diseno simple.
        # por que?: para mantener la consola ordenada y que el jugador entienda cuando empieza y termina un turno.
        print("\n" + "="*40 + "\n")