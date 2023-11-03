class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni  # Este atributo está encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostar_detalle(self):  # self es igual a this
        print(f'la clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')


persona1 = Persona('Gastón', 'Marenco', 32423423, 20)  # Necesitamos enviar argumentos

# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
# Tarea: Hacer el print igual que el objeto 2
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es de: {persona1.edad} años')

persona2 = Persona('Lionel', 'Messi', 23423443, 36)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es de: {persona2.edad} años')

persona1.nombre = 'Pepe'
persona1.apellido = 'Argento'
persona1.edad = 45
print(
    f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es de: {persona1.edad} años')

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostar_detalle()  # La referencia en este caso se pasa de manera automatica
persona2.mostar_detalle()

# Persona.mostar_detalle(persona1)  # Debemos pasarle una referencia para el self o dara error
persona1.telefono = '1122334455'
print(f'Este es el teléfono de: {persona1.nombre} {persona1.telefono}')  # Hemos creado un atributo de un objeto

# print(persona2.telefono)  # El objeto persona2 no tiene el atributo, da error

persona3 = Persona('Rogelio', 'Romero', 324238744, 22, 'Teléfono', '2601122333', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostar_detalle()
# print(persona3._dni)  # Esto no se debe utilizar (está encapsulado), esto dice que lo desconocemos python
# persona3.__nombre # Está totalmente encapsulado
