# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a fahrenheit y viseversa.
# Investigar las formulas

# Función:
def celcius_fahrenheit(celcius):
    return celsius * 9 / 5 + 32

celsius = float(input('Digite el valor de celsius: '))
resultado = celcius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado: .2f}')

# Función:
def fahrenheit_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

fahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado = fahrenheit_celcius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado: .2f}')


