# Ejercicio 6: Tabla de multiplicar
# Pedir al usuario que ingrese un número y guarde en unalista su tabla de multiplicar hasta el 10

num = int(input("Ingrese un número para ver su tabla de multiplicar:  "))

lista = []

for index in range(1, 11):
    lista.append(num * index)

print(f"La tabla de multiplicar del {num} es: {lista}")


