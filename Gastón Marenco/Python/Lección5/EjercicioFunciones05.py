# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a fahrenheit y viseversa.
# Investigar las fórmulas

# Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32  # La precedencia: multiplicación, división y suma


# Función que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9  # Respetar la precedencia utilizando parentesis


gCelsius = float(input('Digite el valor de celsius: '))
resultado = celsius_fahrenheit(gCelsius)
print(f'{gCelsius} C a F -> {resultado:.2f}')

gFahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado = fahrenheit_celsius(gFahrenheit)
print(f'{gFahrenheit} F a C -> {resultado:.2f}')
