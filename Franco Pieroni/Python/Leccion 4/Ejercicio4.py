# Ejercicio 4: Sumar números pares dentro de un rango

num1 = int(input("Ingrese el primer número del rango: "))
num2 = int(input("Ingrese el último número del rango: "))
suma = 0
for num in range(num1, num2 + 1):
    if num % 2 == 0:
        suma += num

print(f"\nLa suma de los números pares del {num1} al {num2} es igual a: {suma}")