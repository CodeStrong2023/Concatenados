class Persona: # Creamos una clase

    def __init__(self,nombre, apellido, edad): # Se llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

print(Persona)

# En Python el constructor está oculto, para llamarlo usamos el método init

persona1 = Persona('Franco','Pieroni',29) # Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

print(f'El objeto1  de la clase persona es: {persona1.nombre} {persona1.apellido} Su edad es : {persona1.edad}')


persona2 = Persona('Guido','Pieroni',29)

print(f'El objeto2 de la clase persona es: {persona2.nombre} {persona2.apellido} Su edad es : {persona2.edad}')

persona1.nombre = 'Greta'
persona1.apellido = 'Pieroni'
persona1.edad = 28

print(f'El objeto1 modificado de la clase persona es: {persona1.nombre} {persona1.apellido} Su edad es : {persona1.edad}')

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle()
persona2.mostrar_detalle()


