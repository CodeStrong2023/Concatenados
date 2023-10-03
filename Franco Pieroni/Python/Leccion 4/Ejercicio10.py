# Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego
# meter los caracteres en una lista sin repetir caracteres

cadena = input("Ingrese una cadena: ")
lista = []
for char in cadena:
    if char not in lista:
        lista.append(char)

print(f'\nLista de caracteres sin repetir ninguno: \n {lista}')