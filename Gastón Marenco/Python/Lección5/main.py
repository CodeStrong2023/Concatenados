# Comenzamos con Funciones

# Definimos una función
def mi_funcion():  # Para identificar a la función utilizamos paréntesis
    print('Hello')


mi_funcion()  # Estamos llamando a la función


# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name + ' ' + lastName)


person = ['Gastón', 'Marenco']
show(person[0], person[1])  # Pasamos uno por uno los datos de la lista a la función
show(*person)  # Esto es lo mismo que lo anterior pero le pasamos todo junto

person2 = ('Lionel', 'Messi')  # Desempaquetamos a través de una tupla
show(*person2)

person3 = {'lastName': 'Ronaldo', "name": 'Cristiano'}
show(**person3)

numbers = [1, 2, 3, 4, 5]  # Aun con la lista vaciá se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break  # Esta es la unica manera para que no se ejecute el else
else:
    print('Esto se terminó')

# List comprehension, lista de comprensión
names = ['Paolo', 'Rodrigo', 'Lupe', 'Pepe']
alongP = [p for p in names if p[0] == 'P']  # Esto regresa una nueva lista
print(alongP)

bottleC = [{'name': 'Quilmes', 'country': 'Arg'},
           {'name': 'Corona', 'country': 'Mx'},
           {'name': 'Stella Artois', 'country': 'Belgium'},
           ]
Arg = [b for b in bottleC if b['country'] == 'Arg']
print(bottleC)
print(Arg)


# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print('Saludos')
    print(f'Nombre: {name}, Apellido: {lastName}')


mi_funcion2('Gastón', 'Marenco')
mi_funcion2('Lionel', 'Messi')


# La palabra return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b


# resultado = sumar(78, 22)
# print(f'El resultado de la suma es : {resultado}')
print(f'El resultado de la suma es : {sumar(55, 45)}')


def sumar2(a=0, b=0):  # Le damos un valor por default
    return a + b


resultado = sumar2()
print(f'El resultado de la suma es : {resultado}')
print(f'El resultado de la suma es : {sumar2(22, 66)}')


# Argumentos, variables en funciones
def listarNombres(*nombres):  # Normalmente se utiliza: *args
    for nombre in nombres:  # Se va a convertir en una tupla
        print(nombre)


listarNombres('Gastón', 'Lionel', 'Cristiano')
listarNombres('Julian', 'Leandro', 'Carlos', 'Emiliano')
