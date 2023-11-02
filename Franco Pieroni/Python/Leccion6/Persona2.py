class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._nombre

    @nombre.setter  # decorador
    def nombre(self, nombre):  # Método Setter
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @property  # decorador
    def apellido(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._apellido

    @apellido.setter  # decorador
    def apellido(self, apellido):  # Método Setter
        print('Estamos utilizando el método set')
        self._apellido = apellido

    @property  # decorador
    def edad(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._edad

    @edad.setter  # decorador
    def edad(self, edad):  # Método Setter
        print('Estamos utilizando el método set')
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')



if __name__ == '__main__':
    persona1 = Persona2('Franco', 'Pieroni', 29)
    print(persona1.nombre)  # Llamamos al método getter
    print(persona1.apellido)
    print(persona1.edad)

    persona1.nombre = 'Guido'  # Llamamos al método setter
    print(persona1.nombre)
    print(persona1.mostrar_detalles())  # Llamamos al método mostrar detalles
    # Atributo read-only o solo lectura (sería la edad porque no tiene un método set)
    print(persona1.edad)

    # Tarea: Crear tres objetos mas utilizando los métodos getter and setter
    # para modificar y mostrar los cambios con el método mostrar_detalles

    # Objeto 1 tarea
    persona2 = Persona2('Leo', 'Messirve', 35)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Lionel'
    persona2.apellido = 'Messi'
    persona2.edad = 36
    print(persona2.mostrar_detalles())

    # Objeto 2 tarea
    persona3 = Persona2('Miguel', 'Merentiel', 27)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Edinson'
    persona3.apellido = 'Cavani'
    persona3.edad = 36

    print(persona3.mostrar_detalles())

    # Objeto 3 tarea
    persona4 = Persona2('Luca', 'Langoni', 21)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Valentin'
    persona4.apellido = 'Barco'
    persona4.edad = 18

    print(persona4.mostrar_detalles())

    print(__name__)
