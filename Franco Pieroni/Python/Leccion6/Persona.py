class Persona: # Creamos una clase

    def __init__(self,nombre, apellido, dni, edad, *args, **kwargs): # Se llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo está encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): # self es igual a la palabra this en Java
        print(f' La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')

print(Persona)

# En Python el constructor está oculto, para llamarlo usamos el método init

persona1 = Persona('Franco','Pieroni',38351239,29) # Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

print(f'El objeto1  de la clase persona es: {persona1.nombre} {persona1.apellido} Su edad es : {persona1.edad}')


persona2 = Persona('Guido','Pieroni',38351239,29)

print(f'El objeto2 de la clase persona es: {persona2.nombre} {persona2.apellido} Su edad es : {persona2.edad}')

persona1.nombre = 'Greta'
persona1.apellido = 'Pieroni'
persona1.edad = 28

print(f'El objeto1 modificado de la clase persona es: {persona1.nombre} {persona1.apellido} Su edad es : {persona1.edad}')

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle() # Aquí la referencia se pasa de manera automática
persona2.mostrar_detalle()

Persona.mostrar_detalle(persona1)

# Si llamamos al método desde la clase debemos pasar la referencia de un objeto
persona1.telefono = '08005554466' # Creamos un atributo superficial desde el objeto
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}')

persona3 =  Persona('Carlos','Juarez','35','Teléfono','123456789','Calle Falsa ','123','Manzana',77,'Casa',18,Altura=1.68, Peso=89, CFavorito='Bordó',Auto= 'Fiat', modelo= '2019')
persona3.mostrar_detalle()

persona4 =  Persona('Juan','Lopez','66','Teléfono','9988771122','Calle Siempreviva ','123','Manzana',60,'Casa',15,Altura=1.78, Peso=78, CFavorito='Rojo',Auto= 'Ford', modelo= '1989')
persona4.mostrar_detalle()

# print(persona1._dni) esto o se debe utilizar en python (está en capsulado)

# persona1.__nombre # Está totalmente encapsulado