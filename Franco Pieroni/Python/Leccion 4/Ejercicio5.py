# Ejercicio 5: factorial de un número positivo

# Solicita un número positivo la usuario
num = int(input("Ingrese un número positivo: "))
# Con este ciclo while se aseguro que el número sea positivo
while num < 1:
    num = int(input("Debe ingresar un número positivo: "))
factorial = 1
index = 1
# Recorre cada indice del número, empezando por uno y agregando + 1 a (num) para incluirlo
for index in range(index, num + 1):
    factorial *= index

print(f"El factorial de {num} es: {factorial}")
