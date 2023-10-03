# Ejercicio 2: Función con * args para multiplicar
# Crear una función para multiplicar los valores recibidos de tipo
# númerico utilizando argumentos variables *args
# como parametro de la función y regresar como resultado la multiplicación
# de todos los valores pasados como argumentos

# Definimos la función
def multiplicar_valores(*numeros): # El masutilizado es *args
    resultado = 1 # el cero no nos permite multiplicar
    for numero in numeros:
        resultado *= numero
    return resultado


# Llamamos a la función
print(multiplicar_valores(3, 5, 15))
