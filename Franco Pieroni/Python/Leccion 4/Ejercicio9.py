# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Solicitar al usuario que ingrese una frase, devolverá la misma frase sin espacios
# y con un contador de caracteres sin contar los espacios en blanco

frase = input("Ingrese una frase: ")
fraseMod = ""
contador = 0
for char in frase:
    if char != " ":
        fraseMod += char

print(f"La frase sin espacios es: {fraseMod}")
print(f"Su frase tiene {len(fraseMod)} caracteres sin contar espacios en blanco")