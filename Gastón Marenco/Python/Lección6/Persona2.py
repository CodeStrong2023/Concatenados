class Persona2:
    def __init__(self, nombre, apellido, edad):  # Está encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    # Getters
    @property  # Decorador
    def nombre(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    # Setters
    @nombre.setter
    def nombre(self, nombre):  # Método Setter
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')


if __name__ == '__main__':
    persona1 = Persona2('Gastón', 'Marenco', 20)
    print(persona1.nombre)  # Llamamos al método getter

    persona1.nombre = 'Juan Pedro'  # Llamamos al método setter
    print(persona1.nombre)  # Otra vez con el método getter
    print(persona1.mostar_detalles())  # Llamamos al método mostrar detalles

    # Atributo read-only(solo lectura) sería la edad porque no tiene el método set
    print(persona1.edad)

    # Tarea: Crear tres objetos más, utilizando los métodos getter and setter
    # para modificar, y mostrar los cambios con el método mostrar_detalles

    # Objeto número uno de la tarea
    persona2 = Persona2('Lio', 'Mesi', 35)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Lionel'
    persona2.apellido = 'Messi'
    persona2.edad = 36
    persona2.mostar_detalles()

    # Objeto número dos de la tarea
    persona3 = Persona2('Cristian', 'Ronald', 37)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Cristiano'
    persona3.apellido = 'Ronaldo'
    persona3.edad = 38
    persona3.mostar_detalles()

    # Objeto número tres de la tarea
    persona4 = Persona2('Pep', 'Arg', 45)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Pepe'
    persona4.apellido = 'Argento'
    persona4.edad = 46
    persona4.mostar_detalles()

    print(__name__)
