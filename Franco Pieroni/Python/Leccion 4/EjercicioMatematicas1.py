import math

numero = int(input('Ingrese un número positivo: '))
while (numero < 1):
    numero = int(input('Debe ingresar un número positivo: '))
raizCuadrada = math.sqrt(numero)
print(f'La raiz cuadrada de {numero} es {raizCuadrada:.2f}')