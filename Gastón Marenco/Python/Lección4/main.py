# Colecciones en Python

# lista = Gaston(0), Ezequiel(1), Lionel(2), Pepe(3)
nombres = ['Gastón', 'Ezequiel', 'Lionel', 'Pepe']

print(nombres)  # Muestra la lista completa
print(nombres[0])  # Muestra el PRIMER valor de la lista
print(nombres[1])  # Muestra el SEGUNDO valor de la lista
print(nombres[-1])  # Muestra el ULTIMMO valor de la lista
print(nombres[-2])  # Muestra el PENULTIMO valor de la lista

print(nombres[0:2])  # Muestra el indice 0, 1 pero no el 2

print(nombres[:3])  # Va desde el inicio de la lista hasta al incice (sin incluirlo)
print(nombres[1:])  # Va desde el índice indicado hasta el final

nombres[3] = 'Willy'  # Modifica la posicion 3 en la lista
print(nombres)

# Iterar una lista
for nombre in nombres:  # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene
print(len(nombres))  # Le pasamos como parametro la lista

# Agregamos un elemento
nombres.append('Vegetta')
# nombres.append([1, 2, 3])
# nombres.append(True)
# nombres.append(10.45)
# nombres.append([4, 5])
# nombres.append(7)
print(nombres)

# Insertamos un elemento en un índice específico
nombres.insert(1, 'Koco')
print(nombres)

# Eliminamos un elemento
nombres.remove('Koco')
print(nombres)

# Eliminamos el untimo elemento
nombres.pop()
print(nombres)

# Eliminar un índice en específico
del nombres[2]  # "del" significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres)  # Aquí mostrara un error, ya que la lista "nombres" ya no existe

# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)
print(len(cocina))

# Acceder a un elemnto, utilizamos corchetes en vez de parentesis
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:1])

# Ejemplo
verduras = ('papa',)  # Una tupla necesita aunque sea de un elemento: la coma, sino solo seria un tipo string cadena

# Recorremos los elementos de la tupla
for cocinar in cocina:  # Print esta utilizando \n para los saltos de línea
    print(cocinar, end=' ')  # Usamos end= para eliminar los saltos de línea

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

del cocina  # Esto es para eliminar una tupla

# Tipo set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas))  # Usamos la función len = lenght segnifica largo

# Revisar si un elemento existe dentro de set
print('Marte' in planetas)
print('marte' not in planetas)

# Añadir un elemento
planetas.add('Tierra')  # add es una función
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter')  # Esta función ante un mal ingreso u inexistencia del elmento da error
print(planetas)
planetas.discard('Tierra')  # Esta función no nos presenta ningun error
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set
del planetas
# print(planetas)  # Al eliminar nos muestra fun error

# 'Maradona':10 Un diccionario está compuesto por dos elementos, una Llave(Key) y un Valor(Value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:  # Recorremos mostrando solo las llaves
    print(termino)

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)  # Muestra solo las llaves

for valor in diccionario.values():  # Usamos una función para acceder al valor
    print(valor)

# Comprobar la existencia de algún elemento
print('IDE' in diccionario)  # Devuelve un booleano
print('IDE' not in diccionario)

# Agregamos un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario
# print(diccionario)  # El diccionario se borro

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2  # Concatenamos
print(lista3)

lista3.extend([7, 8, 9, 1])  # Función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5))  # Función para ubicar en qué índice está el valor ingresado
# print(lista3.index(0))  # Esto daria un error por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay de una lista
print(lista3.count(1))  # Cuenta cuantos valores iguales hay dentro de una lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento, en Python es una función
lista3.sort()  # Ordena los elementos de manera ascendente
print(lista3)
lista3.sort(reverse=True)  # Ordena los elementos de manera descendente
print(lista3)

# Repaso de Tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')
print(tupla)

print(4 in tupla)  # Accion booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# Repaso de set o conjunto
# Para definir un conjunto
conjunto1 = {'bye', }
conjunto2 = set()

conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1)  # Preguntamos si el número 3 NO está en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)  # Nos devuelve como respuesta un booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2  # La línea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2  # Qué elemento tienen en común
print(conjunto3)

conjunto3 = conjunto1 - conjunto2  # Asigna el valor que está en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2  # Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3))  # Aquí preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1))  # Preguntamos si los elementos del conjunto1 están dentro del 3
print(conjunto3.issuperset(conjunto2))  # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))  # No hay cosas en comun

# Convertir un conjunto en completamente inmutable
conjunto1 = frozenset  # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Gastón': {'Edad': 20, 'Altura': 1.80}, 'Lionel': [36, 1.70], 'Ronaldo': (38, 1.87)}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 36, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Ángel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Def. Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print('Tenemos cargados en el diccionario la cantidad de: ', end='')
print(len(seleccionArgentina), 'Jugadores')

# Como tarea agregar por lo menos 4 Jugadores más al diccionario: seleccionArgentina

seleccionArgentina[23] = {'Nombre': 'Emiliano Martínez', 'Edad': 31, 'Altura': 1.95, 'Precio': '28 Millones', 'Posicion': 'Arquero'}
seleccionArgentina[24] = {'Nombre': 'Enzo Fernández', 'Edad': 22, 'Altura': 1.78, 'Precio': '18 Millones', 'Posicion': 'Centrocampista'}
seleccionArgentina[27] = {'Nombre': 'Julián Álvarez', 'Edad': 23, 'Altura': 1.7, 'Precio': '60 Millones', 'Posicion': 'Delantero'}
seleccionArgentina[22] = {'Nombre': 'Lautaro Martínez', 'Edad': 26, 'Altura': 1.74, 'Precio': '80 Millones', 'Posicion': 'Delantero'}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print('Tenemos cargados en el diccionario la cantidad de: ', end='')
print(len(seleccionArgentina), 'Jugadores')

# Pilas usando listas
pila = [1, 2, 3]

# Agregamos elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop()  # Quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')

# Colas con listas
# Estructura de datos de tipo fifo(first input / first output)
cola = ['Gastón', 'Lionel', 'Ronaldo', 'Pepe']

# Agregamos elementos al final de la cola
cola.append('Coqui')
cola.append('Paola')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

# Seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')
