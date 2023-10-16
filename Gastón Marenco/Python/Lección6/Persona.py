class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, edad):  # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Gastón', 'Marenco', '20')  # Necesitamos enviar argumentos

# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
# Tarea: Hacer el print igual que el objeto 2
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es de: {persona1.edad} años')

persona2 = Persona('Lionel', 'Messi', 36)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es de: {persona2.edad} años')

persona1.nombre = 'Pepe'
persona1.apellido = 'Argento'
persona1.edad = 45
print(
    f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es de: {persona1.edad} años')

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostar_detalle()
persona2.mostar_detalle()
