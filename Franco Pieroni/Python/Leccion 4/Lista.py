nombres = ['Fran', 'Eze', 'Sofi', 'Dario', 'Yvette', 'Gaston']
print(nombres)  # Muestra todos los elementos de la ista
print(nombres[0])  # Muestra el primer elemento de la lista
print(nombres[-1])  # Muestra el último elemento de la lista
print(nombres[0:2])  # Muestra los elementos del 0 la 2 de la lista
print(nombres[:3])  # Muestra desde el principio de la lista al indice sin incluirlo
print(nombres[3:])  # Muestra desde el indice indicado hasta el final

# Modificar valor:
nombres[1] = 'Leandro'
print(nombres)

# Iterar una lista
for nombre in nombres:  # Nombre es singular, la lista (nombres) es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene uan lista
print(len(nombres))  # Pasamos la lista como parametro de la función len

# Agregamos un elemento a la lista
nombres.append('Roberto')
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
print(nombres)

# También podemos insertar un elemento en un indice específico
nombres.insert(1, 'Luquitas')
print(nombres)
nombres.insert(3, 'Juana')
print(nombres)

# Para eliminar un elemento de la lista:
nombres.remove('Juana')
print(nombres)

# Para eliminar el último elemento ingresado
nombres.pop()
print(nombres)

# Eliminar un índice específico
del nombres[1]
print(nombres)

# Eliminar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
