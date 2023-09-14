# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incluya los números menores a 5 e imprimir por consola

lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

