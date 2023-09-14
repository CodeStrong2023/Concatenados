# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga dos listas y que a continuación
# cree las siguientes listas (en las que no debe haber repetición)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primer lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas

lista = ['Franco', 'Gaston', 'Leandro', 'Yvet', 'Sofia', 'Dario']
print(f'Lista 1: {lista}')
lista0 = ['Franco', 'Leandro', 'Dario', 'Natalia', 'Ariel', 'Osvaldo']
print(f'Lista 2: {lista0}')
print()
lista1 = []
lista2 = []
lista3 = []
lista4 = []

for str in lista:
    if str not in lista1:
        lista1.append(str)
for str in lista0:
    if str not in lista1:
        lista1.append(str)

print(f'Lista de palabras que aparecen en las listas: {lista1}')

for str in lista:
    if str not in lista0:
        lista2.append(str)

print(f'Lista de palabras que aparecen en la primer lista y no en la segunda: {lista2}')

for str in lista0:
    if str not in lista:
        lista3.append(str)

print(f'Lista de palabras que aparecen en la segunda lista y no en la primera: {lista3}')

for str1 in lista:
    for str2 in lista0:
        if str1 == str2:
            lista4.append(str1)

print(f'Lista de palabras que aparecen en ambas listas: {lista4}')

# Método del profesor:
print('Metodo del profesor: ')

conjunto1 = set(lista)
conjunto2 = set(lista0)

lista1 = list(conjunto1 | conjunto2) # Union de conjuntos
lista2 = list(conjunto1 - conjunto2) # Solo muestra el conjunto1
lista3 = list(conjunto2 - conjunto1 ) # Solo muestra el conjunto2
lista4 = list(conjunto1 & conjunto2) # Muestra ambas listas

print(f'Lista de palabras que aparecen en las listas: {lista1}')
print(f'Lista de palabras que aparecen en la primer lista y no en la segunda: {lista2}')
print(f'Lista de palabras que aparecen en la segunda lista y no en la primera: {lista3}')
print(f'Lista de palabras que aparecen en ambas listas: {lista4}')