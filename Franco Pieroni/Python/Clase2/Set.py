# Tipo Set
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
