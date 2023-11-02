# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# númericos, utilizando argumentos variables *args como parametro de la
# función y agregar como resultado la suma de todos los valore pasados
# como argumentos.

def sumar(*nums):
    resultado = 0
    for valor in nums:
        resultado += valor
    return resultado

# Llamamos a la función
print(sumar(3, 5, 9))