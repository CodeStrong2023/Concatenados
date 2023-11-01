# Comenzamos con Funciones:

# Definimos una función con snake case
# Siempre debemos definir primero y llamar a la función después
def mi_funcion():
    print("Saludos a todos los compañeros de la Tecnicatura")


# Llamamos a la función
mi_funcion()
mi_funcion()
mi_funcion()


# Si queremos utilizar una función de otro módulo debemos importar

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name + ' ' + lastName)


person = ["Ariel", "Betancud"]
show(person[0], person[1])  # Pasamos uno por uno los datos de la lisa a la función
show(*person)  # Es lo mismo resumido
person2 = ("Osvaldo", "Giordanini")  # Desempaquetamos a través de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}  # Desempaquetamos diccionarios
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
else:
    print("Esto se termino")

# List comprehension, Lista de comprensión
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P']  # Regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           {"name": "Skol", "country": "Brazil"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de argumentos
def mi_funcion2(name, lastName):
        print("Saludos a todos los que nos ven a través del canal de YouTube")
        print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2("Jorge", "Lucero")

# Palabra return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a +b
resultado = sumar(78, 22)
print(f'El resultado de la suma es: {resultado}')

def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma es: {resultado}')
print(f'Resultado de la suma es: {sumar2(22, 66)}')

# Argumentos, variables en funciones
def listarNombres(*nombres):
    for nombre in nombres: # Se convierte en tupla
        print(nombre)
listarNombres("Lucas", "Jose", "Claudia", "Rosa", "Maria")
listarNombres("Marcos", "Daniel", "Romina", "Pepe", "Marcela", "Carlos")

def listarTerminos(**terminos): # Lo mas utilizado es **kwargs para recibir argumentos
    for llave, valor in terminos.items():
        print(f'{llave} : {valor}')

listarTerminos()
listarTerminos(IDE = 'Integrated Develoment Enviroment', PK = 'Primary Key')