# Ejercicio 01: Crear una función par sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parametro de la
# Función y agregar como resultado la suma de todos los valores pasados
# Como argumentos.
# Definimos una función
def sumar_valor(*args):  # Recibimos una cantida de parámetros indefinidos
    resultado = 0
    # Iteramoscada elemento
    for valor in args:
        resultado += valor
        return resultado


# LLamamos a la función
print(sumar_valor(3, 5, 9, 2, 1))

