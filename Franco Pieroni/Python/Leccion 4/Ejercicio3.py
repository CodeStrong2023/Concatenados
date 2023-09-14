# Ejercicio 3: Inserta elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario
# introduzca un número 0, el programa dejaría de insertar.
# Por último, mostrar los números ordeandos de menor a mayor


lista = []
salir = False
while not salir:
    numero = int(input('Digite un número: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() # La lista está ordenada con esta función
print(f'\nLista ordenada: \n{lista}')
