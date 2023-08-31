# Definimos una tupla
cocina = ('Cuchara', 'Cuchillo', 'Tenedor')
print(cocina)

# Para saber el largo de una tupla
print(len(cocina))

# Para acceder a un elemento usamos corchetes
print(cocina[0])
print(cocina[-1])

# Accedera un rango
print(cocina[0:2])

# Una tupla necesita por lo menos un elemento y la coma
# De lo contrario solo sería un tipo string cadena
# Las tuplas son inmutables, no se pueden modificar, a diferencia de las listas

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=' ')  # Usamos end=' ' para evitar los saltos de linea en print

# Solo podremos modificar una tupla si la convertimos en lista, y luego de nuevo a tupla

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

# Eliminar tupla
del cocina