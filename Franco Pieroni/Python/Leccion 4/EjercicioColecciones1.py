# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetidos, por último mostrar la lista.

lista1 = [1, 2, 'Juan', 2, 3, 4, 'Jose', 5, 5, 'Juan']
print(f'Lista con duplicados: {lista1}')
lista2 = []
for num in lista1:
    if num not in lista2:
        lista2.append(num)

lista1 = lista2
print(f'Lista sin duplicados: {lista1}')

# El profesor usa una forma mas simple conviertiendo la lista en set y luego volviendola lista de nuevo

print('Método del profesor: ')

lista1 = [1, 2, 'Juan', 2, 3, 4, 'Jose', 5, 5, 'Juan']
print(f'Lista con duplicados: {lista1}')
conjunto = set(lista1)
lista1 = list(conjunto)
print(f'Lista sin duplicados: {lista1}')

# También puede hacerse en una sola linea de código (eficiente)

print('Método de una sola linea: ')
lista = list(set(lista1))
print(lista)

