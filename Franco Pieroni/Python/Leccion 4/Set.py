# Tipo Set
from typing import Dict, Any

planetas = {'Marte','Venus','Jupiter'}
print(len(planetas)) # Usamos la función len = largo

# Revisar si un elemento existe dentro del set
print('Marte' in planetas)

# Agregar un elemento
planetas.add('Tierra') # add es una función
print(planetas)

# Eliminar elementos puede generar errores
planetas.remove('Jupiter')
print(planetas)

# Discard cumple la misma función pero no da errores
planetas.discard('Tierra')
print(planetas)

# Limpiar Set
planetas.clear()
print(planetas)

# Eliminar Set o Conjunto
del planetas

# Repaso de set o conjunto
conjunto2 = set()
conjunto1 = {'bye','Hola'}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el número 3 está en el conjunto 1

# Como hacer la igualdad de dos conjuntos
print(conjunto2 == conjunto1) # Nos devuelve como respuesta un booleano

# Operaciones con conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea une los dos conjuntos
print(conjunto3)

# Intersección
conjunto3 = conjunto1 & conjunto2 # Que elemento tienen en común
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que está en el conjunto 1 y no en el conjunto 2
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)

# Subconjuntos
conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto 1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdaderoquiere decir que el conjunto es un subconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos no comparten elementos (disconexos)
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en comun

# Convertir un conjunto en totalmente inmutable
conjunto1 = frozenset # No se puede agrega, modificar, ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {'Azul' : 'Blue', 'Rojo' : 'Red','Verde' : 'Green', 'Amarillo' : 'Yellow'}

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel' : {'Edad' : 40, 'Altura' : 1.83}, 'Osvaldo' : [45, 1.85], 'Natalia' : [35, 1.67]}
print(diccionario2)

seleccionArgentina: dict[int | Any, dict[str, str | float | int] | dict[str, str | float | int] | dict[str, str | float | int] | dict[str, str | float | int] | dict[str, str | float | int] | Any] = {
    10: {'Nombre' : 'Lionel Messi', 'Edad' : 35, 'Altura' : 1.70, 'Precio' : '50 Millones', 'Posicion' : 'Toda la cancha'},
    11: {'Nombre' : 'Ángel Di María', 'Edad' : 34, 'Altura' : 1.80, 'Precio' : '12 Millones', 'Posicion' : 'Extremo Izquierdo'},
    21: {'Nombre' : 'Paulo Dybala', 'Edad' : 28, 'Altura' : 1.77, 'Precio' : '35 Millones', 'Posicion' : 'Mediapunta'},
    1:  {'Nombre' : 'Emiliano Martinez', 'Edad' : 30, 'Altura' : 1.88, 'Precio' : '10 Millones', 'Posicion' : 'Arquero'},
    20: {'Nombre' : 'Alexis Mac Allister', 'Edad' : 24, 'Altura' : 1.76, 'Precio' : '70 Millones', 'Posicion' : 'Mediocmapista Ofensivo'}
}

print(seleccionArgentina[10])

for llave, valor in seleccionArgentina.items():
     print(llave, valor)

seleccionArgentina[5] =  {
    5: {'Nombre' : 'Leandro Paredes', 'Edad' : 29, 'Altura' : 1.82, 'Precio' : '15 Millones', 'Posicion' : 'Centrocampista'}
}
seleccionArgentina[6] =  {
    26: {'Nombre' : 'Nahuel Molina', 'Edad' : 25, 'Altura' : 1.75, 'Precio' : '35 Millones', 'Posicion' : 'Lateral Derecho'}
}
seleccionArgentina[7] =  {
    13: {'Nombre' : 'Cristian Romero', 'Edad' : 25, 'Altura' : 1.85, 'Precio' : '60 Millones', 'Posicion' : 'Defensa Central'}
}
seleccionArgentina[8] =  {
    22: {'Nombre' : 'Lautaro Martinez', 'Edad' : 26, 'Altura' : 1.74, 'Precio' : '85 Millones', 'Posicion' : 'Centrodelantero'}
}
seleccionArgentina[9] =  {
    9: {'Nombre' : 'Julian Albarez', 'Edad' : 23, 'Altura' : 1.70, 'Precio' : '60 Millones', 'Posicion' : 'Centrodelantero'}
}

print(seleccionArgentina)
print('Tenemos cargados en el diccionario la cantidad de jugadores: ', end=' ')
print(len(seleccionArgentina))

# Usando Pilas
pila = [1,2,3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos por el final
elementoBorrado = pila.pop() # Quita el último elemento y lo guarda en una variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo así: {pila}')

# Colas con listas
# Estructura de datos de tipo fifo(first input / first output)
cola = ['Ariel','Osvaldo','Natalia','Liliana','Pilar']

# Agregamos elementos al final de la cola
cola.append('Jose')
cola.append('Rober')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(cola)

# Seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')







