# 'Maradona':10 Un diccionario esta compuesto por dos elementos
# Una LLAVE y un VALOR
# dict(key,value)
diccionario = {
    'IDE':'Integrated Development Enviroment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Base de Datos'
}

# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar el elemento
print(diccionario.get('POO'))
print(diccionario.get('IDE'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:
    print(termino)

# Necesitamos una función para recorrer el diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# Comprobar existencia de algún elemento
print('IDE' in diccionario) # devuelve un booleano

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar un diccionario
del diccionario
