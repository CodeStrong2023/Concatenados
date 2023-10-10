# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parametro de la
# función y agregar como resultados la suma de todos los valores pasados
# como argumentos

# Definimos una función
def sumar_valor(*args):  # Recibimos una cantidad de parametros indefinidos
    resultado = 0
    # Iteramos elemento
    for valor in args:
        resultado += valor
    return resultado


# Llamamos a la función
print(sumar_valor(3, 5, 9, 2, 1))
