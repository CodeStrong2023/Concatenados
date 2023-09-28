# Lista = Ariel , Liliana, Natalia, Osvaldo
# Colecciones en Python

# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0:2]) #Solo muestra el indice 0, 1 pero no el indice 2
# ir del inicio de la lista  al indice (sin incluirlo)
print(nombres[ :3]) # Indice a mostrar 0, 1, 2
#Desde el indice indicado hasta  el final
print(nombres[1: ])
# Modificamos el valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
# Iterar una lista
for nombre in nombres: # nombre es singular, la lista es prural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene
print(len(nombres)) #le pasamos como parametro la lista

# Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el último elemento
nombres.pop()
print(nombres)

# Eliminar un indice en especifico
del nombres[2] # del significa delete (eleminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres) #Aqui nos mostrara un error

# Definimos una Tupla
cocina =  ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# Mostrar manera inversa
print(cocina[-1])

# Acceder  a un rango
print(cocina[0:2])

# Ejemplo
verduras = ('papa',) # Una tupla necesita aunque sea de un elemento: la coma
# de lo contrario solo seria un tipo string cadena

# Recoremos los elementos de la tupla
for cocinar in cocina: # Print esta usando \n  para saltos de linea
    print(cocinar, end=' ') # Usamos end= para eliminar los saltos de lineas

cocinalista = list(cocina)
cocinalista[0] = 'Plato'
cocina = tuple(cocinalista)
print('\n', cocina)

# del cocina # Esto es para eliminar una tupla

# Tipo set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas)) # Usamos la función len = length significa largo

#Revisar si un elemento existe dentro de set
print('Júpiter' not in planetas)

# Agregar un elemento
planetas.add('Tierra') # add es una función
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter') # Esta función ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard('Tierra') # Esta función no nos presenta ningun error
print(planetas)

# Limpiar set o conjunto
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
# print(planetas) # Al eliminar nos muetra un error

# 'Maradona':10 Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dick(key,value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificar los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos solo mostrando llaves
    print(termino)

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): # Estamos usando una función
    print(termino) # Muestra solo las llaves

for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario) # devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario # el diccionario se borro
# print(diccionario)

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 =lista1+lista2 # Concatenamos
print(lista3)

lista3.extend([7, 8, 9, 1]) # Función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Función para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) esto daría un error por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = lista3 * 2
print(lista)

# Métodos de ordenamiento, en Python es un función
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) # Ordena descendentemente
print(lista3)

# Repaso de Tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Acción booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# Repaso de set o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el número 3 NO esta en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Nos devuelve como respuesta un booleano

# Operacicones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elemento tiene en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aqui preguntamos si un conjuto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto estan dentro del 3
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, estos es si comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eleminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Lo diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},
    27: {'Nombre': 'Julián Álvarez', 'Edad': 23, 'Altura': 1.70, 'Precio': '51 Millones', 'Posicion': 'Delantero'},
    23: {'Nombre': 'Damián Emiliano Martínez', 'Edad': 31, 'Altura': 1.95, 'Precio': '19 Millones', 'Posicion': 'Arquero'},
    5: {'Nombre': 'Leandro Paredes', 'Edad': 29, 'Altura': 1.82, 'Precio': '27 Millones', 'Posicion': 'Centrocampista'},
    }

for llave, valoe in seleccionArgentina.items():
    print(llave, valor)

# Como tarea agragar por lo menos 4 Jugadores mas al directorio: seleccionArgentina
print('Tenemos cargados en el diccionario la cantida de jugadores: ', end=' ')
print(len(seleccionArgentina))

# Pilas usando lista
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # Quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo así: {pila}')

# Cola con listas
# Estructura de datos de tipos fifo( first input/ first ouput)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

# Seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')