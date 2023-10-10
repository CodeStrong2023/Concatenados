import math  # Importamos la clase math para hacer uso de la función sqrt(raíz cuadrada)

# Ejercicio: Dada la siguiente tupla crear una lista y mostar los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)

lista = []  # Definimos una lista

# Filtramos los números menores a 5 de la tupla
for i in tupla:
    if i < 5:
        lista.append(i)

print(lista)  # Mostramos la lista

# Ejercicio de matematicas
# Para sacar la raíz cuadrada de un número positivo
numero = int(input('Digite un número positivo: '))
while numero < 0:
    print('Error -> Debería ser un numero positivo')
    numero = int(input('Digite un número positivo: '))
print(f'\nSu raíz cuadrada es: {math.sqrt(numero):.2f}')
