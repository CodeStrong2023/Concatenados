# Ejercicio 7: Juego adivina el número
# Se debe generar un número aleatorio entre 1 y 100 y luego pedir al usuario que
# ingrese números, indicando si es mayor o menor, hasta que el usurio acierte
# Luego se deberá indicar el número de intentos

import random

random = random.randint(1, 100)
intentos = 0

while True:
    num = int(input("¿En qué número entre 1 y 100 estoy pensando?: "))
    while num < 1 or num > 100:
        print("Debe ser un número entre 1 y 100")
        num = int(input("¿En qué número entre 1 y 100 estoy pensando?: "))

    if num > random:
        print(f"El número que estoy pensando es menor a {num}")
        intentos += 1
    elif num < random:
        print(f"El número que estoy pensando es mayor a {num}")
        intentos += 1
    else:
        print(f"¡Acertaste! el número que pensaba era {num}, ¡te felicito! (:")
        intentos += 1
        print(f"¡Lo lograste luego de {intentos} intentos!")
        break
