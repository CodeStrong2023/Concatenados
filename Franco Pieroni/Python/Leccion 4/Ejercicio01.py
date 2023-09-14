# Ejercicio 1: llenar una lista
# Llenar una lista con los númros del 1 al 50
# Mostrar la lista con un bucle for de la siguiente manera
# 1-2-3-4-5-6-7-8-9...-50

lista = []
i = 1
while i <= 50:
    lista.append(i)
    i += 1
for i in lista:
    print(i, end='-')

# El profesor lo hace en una sola linea:
lista = list(range(1,51)) # Algoritmo eficás
for i in lista:
    print(i, end='-')

