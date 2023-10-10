# Ejercicio 1: Eliminar duplicados de una lista
# Escribir un programa donde tenga una lista y que a continuación
# Elimine los elementos repetidos, por último mostrar la lista

# Creamos la lista
lista = [1, 2, 3, "Gastón", 7, 7, 3, "Lionel", 1, "Gastón", 2, "Lionel"]
# conjunto = set(lista)  # Convertimos la lista a un conjunto de tipo set
# lista = list(conjunto)  # Convertimos el conjunto a una lista
lista = list(set(lista))  # La conversion hecha en una sola línea de código (eficiente)
print(lista)
